import pathlib

DIR = pathlib.Path(__file__).resolve().parent

def get_words():
    from dikicli.core import _get_words
    words = _get_words(pathlib.Path("/home/dawid/.local/share/dikicli"))
    return words

def generate():
    with open(DIR / "test_compare_all.py", mode="w") as f:
        f.write("""\
import os
import tempfile
import shutil
import pytest
from dikicli.core import lookup_online
from dikicli.core import _parse_html, parse_en_pl
from dikicli.helpers import to_dict


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


@pytest.mark.vcr
class TestCompareAll:
""")
        words = get_words()
        for w in words:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

""")

if __name__ == "__main__":
    generate()
