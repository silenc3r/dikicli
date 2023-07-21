import logging
import os
import tempfile
import shutil

import pytest

from dikicli.core import _parse_html
from dikicli.helpers import flatten
from dikicli.parsers import (
    _lookup_online,
    parse_en_pl,
    Entity,
    Meaning,
    PartOfSpeech,
    Sentence,
)

DEBUG = False


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


@pytest.mark.vcr()
class TestFlatten:
    def test_apple(self):
        html_dump = _lookup_online("apple")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_weight(self):
        html_dump = _lookup_online("weight")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_abandon(self):
        html_dump = _lookup_online("abandon")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_pet(self):
        html_dump = _lookup_online("pet")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_snitch(self):
        html_dump = _lookup_online("snitch")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_guest(self):
        html_dump = _lookup_online("guest")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_sad(self):
        html_dump = _lookup_online("sad")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_alternative_wordings(self):
        for word in [
            "scathe",
            "pundit",
            "cusp",
            "palliative",
            "millipede",
            "coincidence",
            "crater",
            "rose",
            "mayhem",
        ]:
            html_dump = _lookup_online(word)
            result = parse_en_pl(html_dump)
            f_result = flatten(_parse_html(html_dump))
            assert result == f_result

    def test_would(self):
        html_dump = _lookup_online("would")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_tumult(self):
        html_dump = _lookup_online("tumult")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_subordinate(self):
        html_dump = _lookup_online("subordinate")
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result
