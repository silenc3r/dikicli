import logging
import pytest
import urllib.parse
import urllib.request

from pathlib import Path

from context import TEST_DIR

from dikicli.core import WordNotFound
from dikicli.core import Config
from dikicli.core import get_words, parse, parse_cached
from dikicli.core import save_to_history
from dikicli.core import translate
from dikicli.templates import CONFIG_TEMPLATE

logger = logging.getLogger(__name__)

URL = "https://www.diki.pl/{word}"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; "
        "Trident/7.0;  rv:11.0) like Gecko"
    )
}


def get_html(word):
    safe_url = URL.format(word=urllib.parse.quote(word))
    req = urllib.request.Request(safe_url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return response.read()


class ParserTester:
    def _test_translations_dict(self, html_dump, native=False, cached=False):
        if cached:
            parsed = parse_cached(html_dump)
        else:
            parsed = parse(html_dump, native)
        assert len(parsed) > 0
        assert isinstance(parsed, list)
        for translation in parsed:
            key = translation[0]
            meanings = translation[1]
            assert isinstance(key, tuple)
            assert isinstance(meanings, list)
            assert len(meanings) > 0
            for part in meanings:
                assert isinstance(part, dict)
                assert "part" in part
                assert "meanings_list" in part
                assert len(part["meanings_list"]) > 0
                for m in part["meanings_list"]:
                    assert "examples" in m
                    assert "meaning" in m
                    assert len(m["meaning"]) > 0
                    assert isinstance(m["meaning"], list)
                    assert isinstance(m["examples"], list)
                    for e in m["examples"]:
                        assert isinstance(e, list)


@pytest.mark.vcr()
class TestParsing(ParserTester):
    def test_parse_simple(self):
        html_dump = get_html("juxtaposition")
        parsed = parse(html_dump, native=False)
        assert len(parsed) == 1
        assert isinstance(parsed, list)
        # assert parsed == []
        first_translation = parsed[0]
        dict_entity = first_translation[0]
        assert isinstance(dict_entity, tuple)
        meanings = first_translation[1]
        assert len(meanings) == 1
        assert isinstance(meanings, list)
        parts = meanings[0]
        assert isinstance(parts, dict)
        assert "part" in parts
        assert "meanings_list" in parts
        assert isinstance(parts["part"], str)
        mlist = parts["meanings_list"]
        assert isinstance(mlist, list)
        assert isinstance(mlist[0], dict)
        assert "examples" in mlist[0]
        assert "meaning" in mlist[0]
        assert isinstance(mlist[0]["examples"], list)
        assert len(mlist[0]["examples"]) == 0
        assert isinstance(mlist[0]["meaning"], list)
        assert len(mlist[0]["meaning"]) == 1
        assert mlist[0]["meaning"][0] == "zestawienie"

    def test_parse_complex(self):
        words = ["guest", "dog", "work", "moll", "apple"]
        for word in words:
            html_dump = get_html(word)
            self._test_translations_dict(html_dump)

    def test_parse_native(self):
        words = ["krowa", "moll", "wąwóz"]
        for word in words:
            html_dump = get_html(word)
            self._test_translations_dict(html_dump, native=True)

    def test_parse_raises_not_found(self):
        html_dump = get_html("vvvvxxxx")
        with pytest.raises(WordNotFound) as e:
            parse(html_dump)
            assert str(e.value) == "Nie znaleziono tłumaczenia wpisanej frazy"

    def test_parse_raises_suggestions(self):
        html_dump = get_html("colag")
        with pytest.raises(WordNotFound) as e:
            parse(html_dump)
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
        "+dog",
        "work",
        "-moll",
        "*apple",
        "-donkey",
        "-juxtaposition",
        "grave",
        "*pen",
        "-glass",
    ]

    def test_get_words_no_prefix(self, tmpdir):
        prefix = ""
        f = tmpdir.mkdir("dikicli").join("words.txt")
        f.write("\n".join(self.words))
        path = Path(f)
        any_prefix_words = [
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
        assert get_words(path, prefix) == any_prefix_words

    def test_get_words_dash_prefix(self, tmpdir):
        prefix = "-"
        f = tmpdir.mkdir("dikicli").join("words.txt")
        f.write("\n".join(self.words))
        path = Path(f)
        dash_prefix_words = ["moll", "donkey", "juxtaposition", "glass"]
        assert get_words(path, prefix) == dash_prefix_words


class TestSaveToHistory:
    def test_save_one_word(self, tmpdir):
        prefix = "+"
        data_dir = Path(tmpdir.mkdir("dikicli"))
        word = "this"
        save_to_history(word, prefix, data_dir)
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["+this\n"]

    def test_save_several_words(self, tmpdir):
        prefix = "@"
        data_dir = Path(tmpdir.mkdir("dikicli"))
        words = ["this", "that", "and", "something", "else"]
        for w in words:
            save_to_history(w, prefix, data_dir)
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["@this\n", "@that\n", "@and\n", "@something\n", "@else\n"]

    def test_save_word_when_parent_dirs_dont_exist(self, tmpdir):
        prefix = ""
        data_dir = Path(tmpdir.mkdir("dikicli")).joinpath("some", "nested", "folders")
        word = "this"
        save_to_history(word, prefix, data_dir)
        assert data_dir.is_dir()
        assert data_dir.name == "folders"
        with open(data_dir.joinpath("words.txt")) as f:
            saved = f.readlines()
        assert saved == ["this\n"]


class TestConfig:
    t_data_dir = "/derp"
    t_prefix = "*"
    t_linewrap = "5"
    t_colors = "false"
    t_web_browser = "weasel"

    def test_config_file_overwrites_defaults(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                prefix=self.t_prefix,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["data dir"] == self.t_data_dir
        assert config["prefix"] == self.t_prefix
        assert config["linewrap"] == self.t_linewrap
        assert config["colors"] == self.t_colors
        assert config["web browser"] == self.t_web_browser

    def test_config_file_invalid_prefix(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        self.t_prefix = "$"
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                prefix=self.t_prefix,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["prefix"] == "none"

    def test_config_file_invalid_linewrap(self, tmpdir):
        f = tmpdir.mkdir("dikicli").join("config.conf")
        self.t_linewrap = "-10"
        f.write(
            CONFIG_TEMPLATE.format(
                data_dir=self.t_data_dir,
                prefix=self.t_prefix,
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
                prefix=self.t_prefix,
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
                prefix=self.t_prefix,
                linewrap=self.t_linewrap,
                colors=self.t_colors,
                browser=self.t_web_browser,
            )
        )
        config = Config()
        config.config_file = Path(f)
        config.read_config()
        assert config["colors"] == "yes"


@pytest.mark.vcr()
class TestTranslate:
    def test_translate_remarkable(self):
        assert translate("remarkable", "", use_cache=False)[0][0] == ("remarkable",)

    # TODO: need more tests
