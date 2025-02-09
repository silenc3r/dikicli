import pathlib

DIR = pathlib.Path(__file__).resolve().parent


def generate():
    with open(DIR / "test_compare_new.py", mode="w") as f:
        f.write(
            """\
import os
import tempfile
import shutil
import pytest
from dikicli.core import lookup_online
from dikicli.core import parse_en_pl
from dikicli.core import WordNotFound


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


"""
        )

        f.write(
            """\
@pytest.mark.vcr
class TestCompareComma:
"""
        )
        for w in [
            "hubris",
            "misfit",
            "wiry",
            "until",
            "scoop",
            "strain",
            "work",
            "hog",
            "gangster",
            "AC",
            "hotel",
            "pet",
            "problem",
        ]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareNoPoS:
"""
        )
        for w in ["guest", "kind of", "sort of"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareNoExamples:
"""
        )
        for w in ["potent", "pining", "encrypt"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareVariations:
"""
        )
        for w in ["tameable", "gold", "gradient", "GOP", "glamorising", "nice"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareOther:
"""
        )
        for w in ["shutdown", "injustice", "tint", "deferral"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareNotFound:
"""
        )
        for w in ["zzzzzz", "greaves", "reconnoitered", "ayahyuasca"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

"""
            )
        f.write(
            """\
@pytest.mark.vcr
class TestCompareProfanity:
"""
        )
        for w in ["yam"]:
            safe_w = w.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_compare_{safe_w}(self):
        html_dump = lookup_online("{w}")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

"""
            )


if __name__ == "__main__":
    generate()
