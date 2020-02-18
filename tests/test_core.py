import logging
import os
import shutil
import tempfile
from pathlib import Path

import pytest

from dikicli.core import Config
from dikicli.core import Meaning
from dikicli.core import PartOfSpeech
from dikicli.core import Translation
from dikicli.core import WordNotFound
from dikicli.core import _get_words
from dikicli.core import _lookup_online
from dikicli.core import _parse_cached
from dikicli.core import _parse_html
from dikicli.core import _save_to_history
from dikicli.core import translate
from dikicli.templates import CONFIG_TEMPLATE

from .context import TEST_DIR

logger = logging.getLogger(__name__)

# pylint: disable=len-as-condition


@pytest.fixture(autouse=True)
def env():
    orig_env = dict(os.environ)
    data_dir = tempfile.mkdtemp(prefix="diki_data-")
    cache_dir = tempfile.mkdtemp(prefix="diki_cache-")
    os.environ["DIKI_DATA_DIR"] = data_dir
    os.environ["DIKI_CACHE_DIR"] = cache_dir
    if "DIKI_CONFIG_FILE" in os.environ:
        del os.environ["DIKI_CONFIG_FILE"]
    os.environ["DIKI_DEBUG"] = "true"

    yield

    shutil.rmtree(data_dir)
    shutil.rmtree(cache_dir)
    os.environ.clear()
    os.environ.update(orig_env)


@pytest.fixture
def conf_dict(env):
    config = {
        "data dir": os.environ["DIKI_DATA_DIR"],
        "linewrap": "78",
        "colors": "yes",
        "web browser": "default",
    }
    return config


class ParserTester:
    def _test_translations_dict(self, html_dump, native=False, cached=False):
        if cached:
            parsed = _parse_cached(html_dump)
        else:
            parsed = _parse_html(html_dump, native)
        assert len(parsed) > 0
        assert isinstance(parsed, list)
        for translation in parsed:
            key = translation[0]
            meanings = translation[1]
            assert isinstance(translation, Translation)
            assert isinstance(key, tuple)
            assert isinstance(meanings, list)
            assert len(meanings) > 0
            for part in meanings:
                assert isinstance(part, PartOfSpeech)
                assert len(part.meanings) > 0
                for m in part.meanings:
                    assert isinstance(m, Meaning)
                    assert len(m.meaning) > 0
                    assert isinstance(m.meaning, list)
                    assert isinstance(m.examples, list)
                    for e in m.examples:
                        assert isinstance(e, list)


@pytest.mark.vcr()
class TestParsing(ParserTester):
    def test_parse_simple(self):
        html_dump = _lookup_online("juxtaposition")
        parsed = _parse_html(html_dump, native=False)
        assert len(parsed) == 1
        assert isinstance(parsed, list)
        first_translation = parsed[0]
        assert isinstance(first_translation, Translation)
        assert first_translation[0] == ("juxtaposition",)
        meanings = first_translation[1]
        assert len(meanings) == 1
        assert isinstance(meanings, list)
        parts = meanings[0]
        assert isinstance(parts, PartOfSpeech)
        assert isinstance(parts.part, str)
        mlist = parts.meanings
        assert isinstance(mlist, list)
        assert isinstance(mlist[0], Meaning)
        assert isinstance(mlist[0].examples, list)
        assert len(mlist[0].examples) == 0
        assert isinstance(mlist[0].meaning, list)
        assert len(mlist[0].meaning) == 1
        assert mlist[0].meaning[0] == "zestawienie"

    def test_parse_complex(self):
        words = ["guest", "dog", "work", "moll", "apple"]
        for word in words:
            html_dump = _lookup_online(word)
            self._test_translations_dict(html_dump)

    def test_parse_native(self):
        words = ["krowa", "moll", "wąwóz"]
        for word in words:
            html_dump = _lookup_online(word)
            self._test_translations_dict(html_dump, native=True)

    def test_parse_raises_not_found(self):
        html_dump = _lookup_online("vvvvxxxx")
        with pytest.raises(WordNotFound) as e:
            _parse_html(html_dump)
            assert str(e.value) == "Nie znaleziono tłumaczenia wpisanej frazy"

    def test_parse_raises_suggestions(self):
        html_dump = _lookup_online("colag")
        with pytest.raises(WordNotFound) as e:
            _parse_html(html_dump)
            assert "Czy chodziło ci o:" in str(e.value)


class TestParsingCached(ParserTester):
    cache_dir = Path(TEST_DIR).joinpath("html_cache")

    def test_parse_cached(self):
        for filename in self.cache_dir.iterdir():
            with open(filename, mode="r") as f:
                html_dump = f.read()
            self._test_translations_dict(html_dump, cached=True)


class TestGetWords:
    words = [
        "guest",
        "dog",
        "work",
        "moll",
        "apple",
        "donkey",
        "juxtaposition",
        "grave",
        "pen",
        "glass",
    ]

    def test_get_words(self, tmpdir):
        data_dir = tmpdir.mkdir("dikicli")
        f = data_dir.join("words.txt")
        f.write("\n".join(self.words))
        path = Path(data_dir)
        expected_words = [
            "guest",
            "dog",
            "work",
            "moll",
            "apple",
            "donkey",
            "juxtaposition",
            "grave",
            "pen",
            "glass",
        ]
        assert _get_words(path) == expected_words


class TestSaveToHistory:
    def test_save_one_word(self, tmpdir):
        data_dir = Path(tmpdir.mkdir("dikicli"))
        word = "this"
        _save_to_history(word, data_dir)
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["this\n"]

    def test_save_several_words(self, tmpdir):
        data_dir = Path(tmpdir.mkdir("dikicli"))
        words = ["this", "that", "and", "something", "else"]
        for w in words:
            _save_to_history(w, data_dir)
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["this\n", "that\n", "and\n", "something\n", "else\n"]

    def test_save_word_when_parent_dirs_dont_exist(self, tmpdir):
        data_dir = Path(tmpdir.mkdir("dikicli")).joinpath("some", "nested", "folders")
        word = "this"
        _save_to_history(word, data_dir)
        assert data_dir.is_dir()
        assert data_dir.name == "folders"
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["this\n"]


class TestConfig:
    t_data_dir = "/derp"
    t_linewrap = "5"
    t_colors = "false"
    t_web_browser = "weasel"

    def test_config_file_overwrites_defaults(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        # DIKI_DATA_DIR takes precendence over defaults
        if "DIKI_DATA_DIR" in os.environ:
            del os.environ["DIKI_DATA_DIR"]
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["data dir"] == self.t_data_dir
        assert config["linewrap"] == self.t_linewrap
        assert config["colors"] == self.t_colors
        assert config["web browser"] == self.t_web_browser

    def test_config_file_invalid_linewrap(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        self.t_linewrap = "-10"
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["linewrap"] == "78"
        self.t_linewrap = "seventy eight"
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["linewrap"] == "78"

    def test_config_file_invalid_colors(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        self.t_colors = "maybe"
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["colors"] == "yes"

    translation = [
        Translation(
            word=("chłosta",),
            parts_of_speech=[
                PartOfSpeech(
                    part="rzeczownik",
                    meanings=[
                        Meaning(meaning=["lash"], examples=[]),
                        Meaning(meaning=["birch"], examples=[]),
                        Meaning(
                            meaning=["whipping"],
                            examples=[["chłosta, chłostanie", None]],
                        ),
                        Meaning(meaning=["flogging"], examples=[]),
                        Meaning(
                            meaning=["caning"],
                            examples=[["chłosta, kara chłosty", None]],
                        ),
                        Meaning(
                            meaning=["chastisement"],
                            examples=[["chłosta (cielesna kara)", None]],
                        ),
                    ],
                )
            ],
        ),
        Translation(
            word=("chłostać",),
            parts_of_speech=[
                PartOfSpeech(
                    part="czasownik",
                    meanings=[
                        Meaning(
                            meaning=["whip"],
                            examples=[
                                ["biczować, chłostać (za pomocą bata), smagać", None]
                            ],
                        ),
                        Meaning(
                            meaning=["lash"],
                            examples=[
                                [
                                    "chłostać, smagać , wychłostać, wysmagać, zacinać batem",
                                    None,
                                ]
                            ],
                        ),
                        Meaning(meaning=["birch"], examples=[]),
                        Meaning(
                            meaning=["scourge"],
                            examples=[["biczować, chłostać (kogoś)", None]],
                        ),
                        Meaning(
                            meaning=["flog"],
                            examples=[["chłostać (biczem, batem)", None]],
                        ),
                        Meaning(
                            meaning=["thresh"],
                            examples=[["bić (kogoś), chłostać, spuszczać łomot", None]],
                        ),
                    ],
                )
            ],
        ),
    ]


@pytest.mark.vcr()
class TestTranslate:
    def test_translate_remarkable(self, conf_dict):
        config = conf_dict
        assert translate("remarkable", config, use_cache=False)[0][0] == ("remarkable",)

    # TODO: need more tests
