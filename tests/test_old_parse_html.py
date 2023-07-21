import logging
import os
import tempfile
import shutil

import pytest

from dikicli.core import _parse_html
from dikicli.core import lookup_online
from dikicli.helpers import flatten
from dikicli.parsers import (
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
        html_dump = lookup_online("apple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_weight(self):
        html_dump = lookup_online("weight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_abandon(self):
        html_dump = lookup_online("abandon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_pet(self):
        html_dump = lookup_online("pet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_snitch(self):
        html_dump = lookup_online("snitch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_guest(self):
        html_dump = lookup_online("guest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_sad(self):
        html_dump = lookup_online("sad").html
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
            html_dump = lookup_online(word).html
            result = parse_en_pl(html_dump)
            f_result = flatten(_parse_html(html_dump))
            assert result == f_result

    def test_would(self):
        html_dump = lookup_online("would").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_tumult(self):
        html_dump = lookup_online("tumult").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_subordinate(self):
        html_dump = lookup_online("subordinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result
