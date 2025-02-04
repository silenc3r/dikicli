import os
import tempfile
import shutil
import pytest
from dikicli.core import lookup_online
from dikicli.core import _parse_html, parse_en_pl
from dikicli.core import WordNotFound
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
class TestCompareComma:
    def test_compare_hubris(self):
        html_dump = lookup_online("hubris")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misfit(self):
        html_dump = lookup_online("misfit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wiry(self):
        html_dump = lookup_online("wiry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_until(self):
        html_dump = lookup_online("until")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scoop(self):
        html_dump = lookup_online("scoop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strain(self):
        html_dump = lookup_online("strain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_work(self):
        html_dump = lookup_online("work")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hog(self):
        html_dump = lookup_online("hog")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gangster(self):
        html_dump = lookup_online("gangster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_AC(self):
        html_dump = lookup_online("AC")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hotel(self):
        html_dump = lookup_online("hotel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pet(self):
        html_dump = lookup_online("pet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_problem(self):
        html_dump = lookup_online("problem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

@pytest.mark.vcr
class TestCompareNoPoS:
    def test_compare_guest(self):
        html_dump = lookup_online("guest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kind_of(self):
        html_dump = lookup_online("kind of")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sort_of(self):
        html_dump = lookup_online("sort of")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

@pytest.mark.vcr
class TestCompareNoExamples:
    def test_compare_potent(self):
        html_dump = lookup_online("potent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pining(self):
        html_dump = lookup_online("pining")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_encrypt(self):
        html_dump = lookup_online("encrypt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

@pytest.mark.vcr
class TestCompareVariations:
    def test_compare_tameable(self):
        html_dump = lookup_online("tameable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gold(self):
        html_dump = lookup_online("gold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gradient(self):
        html_dump = lookup_online("gradient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_GOP(self):
        html_dump = lookup_online("GOP")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glamorising(self):
        html_dump = lookup_online("glamorising")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nice(self):
        html_dump = lookup_online("nice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

@pytest.mark.vcr
class TestCompareOther:
    def test_compare_shutdown(self):
        html_dump = lookup_online("shutdown")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_injustice(self):
        html_dump = lookup_online("injustice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tint(self):
        html_dump = lookup_online("tint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deferral(self):
        html_dump = lookup_online("deferral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

@pytest.mark.vcr
class TestCompareNotFound:
    def test_compare_zzzzzz(self):
        html_dump = lookup_online("zzzzzz")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

    def test_compare_greaves(self):
        html_dump = lookup_online("greaves")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

    def test_compare_reconnoitered(self):
        html_dump = lookup_online("reconnoitered")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

    def test_compare_ayahyuasca(self):
        html_dump = lookup_online("ayahyuasca")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

@pytest.mark.vcr
class TestCompareProfanity:
    def test_compare_yam(self):
        html_dump = lookup_online("yam")
        try:
            result = parse_en_pl(html_dump)
        except WordNotFound as exn:
            result = str(exn)
        try:
            f_result = to_dict(_parse_html(html_dump))
        except WordNotFound as exn:
            f_result = str(exn)
        assert result == f_result

