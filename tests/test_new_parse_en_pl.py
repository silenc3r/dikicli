import logging
import os
import tempfile
import shutil

import pytest

from dikicli.core import _parse_html, parse_en_pl
from dikicli.core import lookup_online
from dikicli.helpers import to_dict

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


# @pytest.mark.vcr()
class TestToDict:
    def test_apple(self):
        html_dump = lookup_online("apple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_weight(self):
        html_dump = lookup_online("weight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_abandon(self):
        html_dump = lookup_online("abandon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_pet(self):
        html_dump = lookup_online("pet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_snitch(self):
        html_dump = lookup_online("snitch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_guest(self):
        html_dump = lookup_online("guest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_sad(self):
        html_dump = lookup_online("sad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
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
            html_dump = lookup_online(word)
            result = parse_en_pl(html_dump)
            f_result = to_dict(_parse_html(html_dump))
            assert result == f_result

    def test_would(self):
        html_dump = lookup_online("would")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_tumult(self):
        html_dump = lookup_online("tumult")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_subordinate(self):
        html_dump = lookup_online("subordinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result
