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
    def test_compare_pawning(self):
        html_dump = lookup_online("pawning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apparently(self):
        html_dump = lookup_online("apparently")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scathe(self):
        html_dump = lookup_online("scathe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fecund(self):
        html_dump = lookup_online("fecund")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caucus(self):
        html_dump = lookup_online("caucus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pamper(self):
        html_dump = lookup_online("pamper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venerated(self):
        html_dump = lookup_online("venerated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incisive(self):
        html_dump = lookup_online("incisive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gospel(self):
        html_dump = lookup_online("gospel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suppleness(self):
        html_dump = lookup_online("suppleness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mingle(self):
        html_dump = lookup_online("mingle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blitheness(self):
        html_dump = lookup_online("blitheness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mulligan(self):
        html_dump = lookup_online("mulligan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascent(self):
        html_dump = lookup_online("ascent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nonchalant(self):
        html_dump = lookup_online("nonchalant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pundit(self):
        html_dump = lookup_online("pundit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cervical(self):
        html_dump = lookup_online("cervical")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggravate(self):
        html_dump = lookup_online("aggravate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commissioner(self):
        html_dump = lookup_online("commissioner")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oracular(self):
        html_dump = lookup_online("oracular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_giardia(self):
        html_dump = lookup_online("giardia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swathe(self):
        html_dump = lookup_online("swathe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_daub(self):
        html_dump = lookup_online("daub")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feline(self):
        html_dump = lookup_online("feline")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ayahuasca(self):
        html_dump = lookup_online("ayahuasca")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garret(self):
        html_dump = lookup_online("garret")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Solidarity(self):
        html_dump = lookup_online("Solidarity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drudgery(self):
        html_dump = lookup_online("drudgery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hosier(self):
        html_dump = lookup_online("hosier")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remarkable(self):
        html_dump = lookup_online("remarkable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snotty(self):
        html_dump = lookup_online("snotty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cusp(self):
        html_dump = lookup_online("cusp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endeavor(self):
        html_dump = lookup_online("endeavor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embellishment(self):
        html_dump = lookup_online("embellishment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commend(self):
        html_dump = lookup_online("commend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palliative(self):
        html_dump = lookup_online("palliative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parishioner(self):
        html_dump = lookup_online("parishioner")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_millipede(self):
        html_dump = lookup_online("millipede")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kludge(self):
        html_dump = lookup_online("kludge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_introspection(self):
        html_dump = lookup_online("introspection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinnacle(self):
        html_dump = lookup_online("pinnacle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ballpark(self):
        html_dump = lookup_online("ballpark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantrum(self):
        html_dump = lookup_online("tantrum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disconcerting(self):
        html_dump = lookup_online("disconcerting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_missive(self):
        html_dump = lookup_online("missive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feigned(self):
        html_dump = lookup_online("feigned")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deferral(self):
        html_dump = lookup_online("deferral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manure(self):
        html_dump = lookup_online("manure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penury(self):
        html_dump = lookup_online("penury")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fringe(self):
        html_dump = lookup_online("fringe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coincidence(self):
        html_dump = lookup_online("coincidence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_surmount(self):
        html_dump = lookup_online("surmount")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succor(self):
        html_dump = lookup_online("succor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amatory(self):
        html_dump = lookup_online("amatory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_needlessly(self):
        html_dump = lookup_online("needlessly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yearn(self):
        html_dump = lookup_online("yearn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dreary(self):
        html_dump = lookup_online("dreary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upheaval(self):
        html_dump = lookup_online("upheaval")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contented(self):
        html_dump = lookup_online("contented")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snarly(self):
        html_dump = lookup_online("snarly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transitively(self):
        html_dump = lookup_online("transitively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenable(self):
        html_dump = lookup_online("tenable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_klutz(self):
        html_dump = lookup_online("klutz")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hackney(self):
        html_dump = lookup_online("hackney")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chlamydia(self):
        html_dump = lookup_online("chlamydia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cache(self):
        html_dump = lookup_online("cache")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crude(self):
        html_dump = lookup_online("crude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bint(self):
        html_dump = lookup_online("bint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dour(self):
        html_dump = lookup_online("dour")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pillock(self):
        html_dump = lookup_online("pillock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crater(self):
        html_dump = lookup_online("crater")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_finagle(self):
        html_dump = lookup_online("finagle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veer(self):
        html_dump = lookup_online("veer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boomlet(self):
        html_dump = lookup_online("boomlet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rose(self):
        html_dump = lookup_online("rose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mayhem(self):
        html_dump = lookup_online("mayhem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renowned(self):
        html_dump = lookup_online("renowned")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ephemeral(self):
        html_dump = lookup_online("ephemeral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sickly(self):
        html_dump = lookup_online("sickly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sensible(self):
        html_dump = lookup_online("sensible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blustery(self):
        html_dump = lookup_online("blustery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virulent(self):
        html_dump = lookup_online("virulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adrift(self):
        html_dump = lookup_online("adrift")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rascal(self):
        html_dump = lookup_online("rascal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hodgepodge(self):
        html_dump = lookup_online("hodgepodge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humongous(self):
        html_dump = lookup_online("humongous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stocky(self):
        html_dump = lookup_online("stocky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reef(self):
        html_dump = lookup_online("reef")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cervix(self):
        html_dump = lookup_online("cervix")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maroon(self):
        html_dump = lookup_online("maroon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grubby(self):
        html_dump = lookup_online("grubby")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serendipitous(self):
        html_dump = lookup_online("serendipitous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_altercation(self):
        html_dump = lookup_online("altercation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bravado(self):
        html_dump = lookup_online("bravado")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eerie(self):
        html_dump = lookup_online("eerie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thaw(self):
        html_dump = lookup_online("thaw")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewildering(self):
        html_dump = lookup_online("bewildering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taint(self):
        html_dump = lookup_online("taint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vie(self):
        html_dump = lookup_online("vie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agenda(self):
        html_dump = lookup_online("agenda")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midst(self):
        html_dump = lookup_online("midst")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_churn(self):
        html_dump = lookup_online("churn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nexus(self):
        html_dump = lookup_online("nexus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oat(self):
        html_dump = lookup_online("oat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chastity(self):
        html_dump = lookup_online("chastity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poplar(self):
        html_dump = lookup_online("poplar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glazed(self):
        html_dump = lookup_online("glazed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seethe(self):
        html_dump = lookup_online("seethe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serene(self):
        html_dump = lookup_online("serene")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tempestuous(self):
        html_dump = lookup_online("tempestuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stoked(self):
        html_dump = lookup_online("stoked")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantalize(self):
        html_dump = lookup_online("tantalize")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mesmerizing(self):
        html_dump = lookup_online("mesmerizing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gull(self):
        html_dump = lookup_online("gull")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stratify(self):
        html_dump = lookup_online("stratify")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derive(self):
        html_dump = lookup_online("derive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_absentminded(self):
        html_dump = lookup_online("absentminded")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wiry(self):
        html_dump = lookup_online("wiry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoonful(self):
        html_dump = lookup_online("spoonful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_munchkin(self):
        html_dump = lookup_online("munchkin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peppy(self):
        html_dump = lookup_online("peppy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flummoxed(self):
        html_dump = lookup_online("flummoxed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurt(self):
        html_dump = lookup_online("spurt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_linger(self):
        html_dump = lookup_online("linger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crumple(self):
        html_dump = lookup_online("crumple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inundate(self):
        html_dump = lookup_online("inundate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smut(self):
        html_dump = lookup_online("smut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elicit(self):
        html_dump = lookup_online("elicit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acme(self):
        html_dump = lookup_online("acme")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neurotic(self):
        html_dump = lookup_online("neurotic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_restless(self):
        html_dump = lookup_online("restless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exaltation(self):
        html_dump = lookup_online("exaltation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tether(self):
        html_dump = lookup_online("tether")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_communion(self):
        html_dump = lookup_online("communion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fuselage(self):
        html_dump = lookup_online("fuselage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plenitude(self):
        html_dump = lookup_online("plenitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proxy(self):
        html_dump = lookup_online("proxy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucidity(self):
        html_dump = lookup_online("lucidity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_navel(self):
        html_dump = lookup_online("navel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opulent(self):
        html_dump = lookup_online("opulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bijective(self):
        html_dump = lookup_online("bijective")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skewers(self):
        html_dump = lookup_online("skewers")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_underpin(self):
        html_dump = lookup_online("underpin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pneumonia(self):
        html_dump = lookup_online("pneumonia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relentlessly(self):
        html_dump = lookup_online("relentlessly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_provost(self):
        html_dump = lookup_online("provost")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spruce(self):
        html_dump = lookup_online("spruce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nix(self):
        html_dump = lookup_online("nix")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_damsel(self):
        html_dump = lookup_online("damsel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enthrall(self):
        html_dump = lookup_online("enthrall")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glitzy(self):
        html_dump = lookup_online("glitzy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tithing(self):
        html_dump = lookup_online("tithing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jettison(self):
        html_dump = lookup_online("jettison")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bugle(self):
        html_dump = lookup_online("bugle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aspen(self):
        html_dump = lookup_online("aspen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pang(self):
        html_dump = lookup_online("pang")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limbo(self):
        html_dump = lookup_online("limbo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opportunistic(self):
        html_dump = lookup_online("opportunistic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_platitude(self):
        html_dump = lookup_online("platitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kale(self):
        html_dump = lookup_online("kale")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apricot(self):
        html_dump = lookup_online("apricot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flak(self):
        html_dump = lookup_online("flak")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowry(self):
        html_dump = lookup_online("dowry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concoct(self):
        html_dump = lookup_online("concoct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mute(self):
        html_dump = lookup_online("mute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuine(self):
        html_dump = lookup_online("genuine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impartial(self):
        html_dump = lookup_online("impartial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliers(self):
        html_dump = lookup_online("pliers")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plod(self):
        html_dump = lookup_online("plod")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestigial(self):
        html_dump = lookup_online("vestigial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vest(self):
        html_dump = lookup_online("vest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cohesion(self):
        html_dump = lookup_online("cohesion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pauper(self):
        html_dump = lookup_online("pauper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhilarating(self):
        html_dump = lookup_online("exhilarating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sumptuous(self):
        html_dump = lookup_online("sumptuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gratuitous(self):
        html_dump = lookup_online("gratuitous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meddle(self):
        html_dump = lookup_online("meddle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yam(self):
        html_dump = lookup_online("yam")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deftly(self):
        html_dump = lookup_online("deftly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fitful(self):
        html_dump = lookup_online("fitful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rancid(self):
        html_dump = lookup_online("rancid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stilted(self):
        html_dump = lookup_online("stilted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unprepossessing(self):
        html_dump = lookup_online("unprepossessing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redemption(self):
        html_dump = lookup_online("redemption")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_planer(self):
        html_dump = lookup_online("planer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wimpy(self):
        html_dump = lookup_online("wimpy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evocative(self):
        html_dump = lookup_online("evocative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_workhorse(self):
        html_dump = lookup_online("workhorse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predicate(self):
        html_dump = lookup_online("predicate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sophistry(self):
        html_dump = lookup_online("sophistry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permanence(self):
        html_dump = lookup_online("permanence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deranged(self):
        html_dump = lookup_online("deranged")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disingenuous(self):
        html_dump = lookup_online("disingenuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fizzle(self):
        html_dump = lookup_online("fizzle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dinky(self):
        html_dump = lookup_online("dinky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stranglehold(self):
        html_dump = lookup_online("stranglehold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yap(self):
        html_dump = lookup_online("yap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grogginess(self):
        html_dump = lookup_online("grogginess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exertion(self):
        html_dump = lookup_online("exertion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solicite(self):
        html_dump = lookup_online("solicite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_custard(self):
        html_dump = lookup_online("custard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irreverence(self):
        html_dump = lookup_online("irreverence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutted(self):
        html_dump = lookup_online("gutted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cashew(self):
        html_dump = lookup_online("cashew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaff(self):
        html_dump = lookup_online("gaff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seclude(self):
        html_dump = lookup_online("seclude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seditious(self):
        html_dump = lookup_online("seditious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sassy(self):
        html_dump = lookup_online("sassy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_botcher(self):
        html_dump = lookup_online("botcher")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endearing(self):
        html_dump = lookup_online("endearing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maintainer(self):
        html_dump = lookup_online("maintainer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealous(self):
        html_dump = lookup_online("zealous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kiln(self):
        html_dump = lookup_online("kiln")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chagrin(self):
        html_dump = lookup_online("chagrin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oud(self):
        html_dump = lookup_online("oud")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squalid(self):
        html_dump = lookup_online("squalid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plaster(self):
        html_dump = lookup_online("plaster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obnoxious(self):
        html_dump = lookup_online("obnoxious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_idem(self):
        html_dump = lookup_online("idem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_realtor(self):
        html_dump = lookup_online("realtor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chivalry(self):
        html_dump = lookup_online("chivalry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tussle(self):
        html_dump = lookup_online("tussle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vile(self):
        html_dump = lookup_online("vile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clumsy(self):
        html_dump = lookup_online("clumsy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derelict(self):
        html_dump = lookup_online("derelict")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trite(self):
        html_dump = lookup_online("trite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procurement(self):
        html_dump = lookup_online("procurement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cannily(self):
        html_dump = lookup_online("cannily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_femur(self):
        html_dump = lookup_online("femur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infibulate(self):
        html_dump = lookup_online("infibulate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rampage(self):
        html_dump = lookup_online("rampage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruinous(self):
        html_dump = lookup_online("ruinous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soliloquy(self):
        html_dump = lookup_online("soliloquy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wreath(self):
        html_dump = lookup_online("wreath")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deceit(self):
        html_dump = lookup_online("deceit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vermin(self):
        html_dump = lookup_online("vermin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrid(self):
        html_dump = lookup_online("acrid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foreman(self):
        html_dump = lookup_online("foreman")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pep(self):
        html_dump = lookup_online("pep")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meadowlark(self):
        html_dump = lookup_online("meadowlark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petite(self):
        html_dump = lookup_online("petite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thistle(self):
        html_dump = lookup_online("thistle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenure(self):
        html_dump = lookup_online("tenure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incense(self):
        html_dump = lookup_online("incense")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_easel(self):
        html_dump = lookup_online("easel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predicament(self):
        html_dump = lookup_online("predicament")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portly(self):
        html_dump = lookup_online("portly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exasperating(self):
        html_dump = lookup_online("exasperating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rancorous(self):
        html_dump = lookup_online("rancorous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punditry(self):
        html_dump = lookup_online("punditry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notoriety(self):
        html_dump = lookup_online("notoriety")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holster(self):
        html_dump = lookup_online("holster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pithy(self):
        html_dump = lookup_online("pithy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ableism(self):
        html_dump = lookup_online("ableism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congruence(self):
        html_dump = lookup_online("congruence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pronounced(self):
        html_dump = lookup_online("pronounced")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sequin(self):
        html_dump = lookup_online("sequin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flounder(self):
        html_dump = lookup_online("flounder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serendipity(self):
        html_dump = lookup_online("serendipity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coveted(self):
        html_dump = lookup_online("coveted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revet(self):
        html_dump = lookup_online("revet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_etch(self):
        html_dump = lookup_online("etch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleight(self):
        html_dump = lookup_online("sleight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poignant(self):
        html_dump = lookup_online("poignant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chirality(self):
        html_dump = lookup_online("chirality")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assiduously(self):
        html_dump = lookup_online("assiduously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gait(self):
        html_dump = lookup_online("gait")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blindside(self):
        html_dump = lookup_online("blindside")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_putter(self):
        html_dump = lookup_online("putter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phony(self):
        html_dump = lookup_online("phony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidelity(self):
        html_dump = lookup_online("fidelity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sore(self):
        html_dump = lookup_online("sore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splendid(self):
        html_dump = lookup_online("splendid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hamlet(self):
        html_dump = lookup_online("hamlet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoist(self):
        html_dump = lookup_online("hoist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_depress(self):
        html_dump = lookup_online("depress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_felony(self):
        html_dump = lookup_online("felony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_androgen(self):
        html_dump = lookup_online("androgen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asset(self):
        html_dump = lookup_online("asset")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auspicious(self):
        html_dump = lookup_online("auspicious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallow(self):
        html_dump = lookup_online("fallow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discord(self):
        html_dump = lookup_online("discord")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gullible(self):
        html_dump = lookup_online("gullible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enema(self):
        html_dump = lookup_online("enema")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vindicate(self):
        html_dump = lookup_online("vindicate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kelp(self):
        html_dump = lookup_online("kelp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouse(self):
        html_dump = lookup_online("grouse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lenient(self):
        html_dump = lookup_online("lenient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_esophagus(self):
        html_dump = lookup_online("esophagus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_angst(self):
        html_dump = lookup_online("angst")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fink(self):
        html_dump = lookup_online("fink")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foo(self):
        html_dump = lookup_online("foo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congruent(self):
        html_dump = lookup_online("congruent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cerebellum(self):
        html_dump = lookup_online("cerebellum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creepy(self):
        html_dump = lookup_online("creepy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobweb(self):
        html_dump = lookup_online("cobweb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_potent(self):
        html_dump = lookup_online("potent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inertia(self):
        html_dump = lookup_online("inertia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_legibility(self):
        html_dump = lookup_online("legibility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flock(self):
        html_dump = lookup_online("flock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foray(self):
        html_dump = lookup_online("foray")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tender(self):
        html_dump = lookup_online("tender")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exude(self):
        html_dump = lookup_online("exude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiefdom(self):
        html_dump = lookup_online("fiefdom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inert(self):
        html_dump = lookup_online("inert")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_devise(self):
        html_dump = lookup_online("devise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knuckle(self):
        html_dump = lookup_online("knuckle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulverize(self):
        html_dump = lookup_online("pulverize")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantamount(self):
        html_dump = lookup_online("tantamount")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dole(self):
        html_dump = lookup_online("dole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attrit(self):
        html_dump = lookup_online("attrit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_battery(self):
        html_dump = lookup_online("battery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myopic(self):
        html_dump = lookup_online("myopic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affectionate(self):
        html_dump = lookup_online("affectionate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malodorous(self):
        html_dump = lookup_online("malodorous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seaweed(self):
        html_dump = lookup_online("seaweed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resentment(self):
        html_dump = lookup_online("resentment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_causation(self):
        html_dump = lookup_online("causation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_critic(self):
        html_dump = lookup_online("critic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stiffen(self):
        html_dump = lookup_online("stiffen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minimalist(self):
        html_dump = lookup_online("minimalist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deprecate(self):
        html_dump = lookup_online("deprecate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pet(self):
        html_dump = lookup_online("pet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dye(self):
        html_dump = lookup_online("dye")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluble(self):
        html_dump = lookup_online("voluble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chisel(self):
        html_dump = lookup_online("chisel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renounce(self):
        html_dump = lookup_online("renounce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bereavement(self):
        html_dump = lookup_online("bereavement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sustain(self):
        html_dump = lookup_online("sustain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carbohydrate(self):
        html_dump = lookup_online("carbohydrate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luddite(self):
        html_dump = lookup_online("luddite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verbiage(self):
        html_dump = lookup_online("verbiage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diorama(self):
        html_dump = lookup_online("diorama")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anoint(self):
        html_dump = lookup_online("anoint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mint(self):
        html_dump = lookup_online("mint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_would(self):
        html_dump = lookup_online("would")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insinuate(self):
        html_dump = lookup_online("insinuate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malice(self):
        html_dump = lookup_online("malice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rescind(self):
        html_dump = lookup_online("rescind")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broil(self):
        html_dump = lookup_online("broil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stout(self):
        html_dump = lookup_online("stout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobbles(self):
        html_dump = lookup_online("cobbles")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parse(self):
        html_dump = lookup_online("parse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dysentery(self):
        html_dump = lookup_online("dysentery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abide(self):
        html_dump = lookup_online("abide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraught(self):
        html_dump = lookup_online("fraught")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastoral(self):
        html_dump = lookup_online("pastoral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quell(self):
        html_dump = lookup_online("quell")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awl(self):
        html_dump = lookup_online("awl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paisley(self):
        html_dump = lookup_online("paisley")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_darkly(self):
        html_dump = lookup_online("darkly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_viceroy(self):
        html_dump = lookup_online("viceroy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagrant(self):
        html_dump = lookup_online("flagrant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_could(self):
        html_dump = lookup_online("could")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trenchant(self):
        html_dump = lookup_online("trenchant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rupture(self):
        html_dump = lookup_online("rupture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcer(self):
        html_dump = lookup_online("ulcer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaguely(self):
        html_dump = lookup_online("vaguely")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumult(self):
        html_dump = lookup_online("tumult")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candor(self):
        html_dump = lookup_online("candor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conducive(self):
        html_dump = lookup_online("conducive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subordinate(self):
        html_dump = lookup_online("subordinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excoriate(self):
        html_dump = lookup_online("excoriate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merciless(self):
        html_dump = lookup_online("merciless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abominable(self):
        html_dump = lookup_online("abominable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turbulent(self):
        html_dump = lookup_online("turbulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lambast(self):
        html_dump = lookup_online("lambast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_privileges(self):
        html_dump = lookup_online("privileges")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defiance(self):
        html_dump = lookup_online("defiance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overcast(self):
        html_dump = lookup_online("overcast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salient(self):
        html_dump = lookup_online("salient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_these(self):
        html_dump = lookup_online("these")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_valiantly(self):
        html_dump = lookup_online("valiantly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucid(self):
        html_dump = lookup_online("lucid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbated(self):
        html_dump = lookup_online("exacerbated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commutative(self):
        html_dump = lookup_online("commutative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coarse(self):
        html_dump = lookup_online("coarse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superficial(self):
        html_dump = lookup_online("superficial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscientious(self):
        html_dump = lookup_online("conscientious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hillock(self):
        html_dump = lookup_online("hillock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alluvial(self):
        html_dump = lookup_online("alluvial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_viscous(self):
        html_dump = lookup_online("viscous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beguiling(self):
        html_dump = lookup_online("beguiling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manifold(self):
        html_dump = lookup_online("manifold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scallop(self):
        html_dump = lookup_online("scallop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recourse(self):
        html_dump = lookup_online("recourse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whisked(self):
        html_dump = lookup_online("whisked")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feeble(self):
        html_dump = lookup_online("feeble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swill(self):
        html_dump = lookup_online("swill")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_levy(self):
        html_dump = lookup_online("levy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corral(self):
        html_dump = lookup_online("corral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cluck(self):
        html_dump = lookup_online("cluck")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belligerence(self):
        html_dump = lookup_online("belligerence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chasm(self):
        html_dump = lookup_online("chasm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_latitude(self):
        html_dump = lookup_online("latitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incessant(self):
        html_dump = lookup_online("incessant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mar(self):
        html_dump = lookup_online("mar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mandarin(self):
        html_dump = lookup_online("mandarin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangy(self):
        html_dump = lookup_online("tangy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palatable(self):
        html_dump = lookup_online("palatable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avery(self):
        html_dump = lookup_online("avery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insidiously(self):
        html_dump = lookup_online("insidiously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouchiness(self):
        html_dump = lookup_online("grouchiness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_traduce(self):
        html_dump = lookup_online("traduce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumble(self):
        html_dump = lookup_online("rumble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_timber(self):
        html_dump = lookup_online("timber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indulgence(self):
        html_dump = lookup_online("indulgence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yttria(self):
        html_dump = lookup_online("yttria")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crest(self):
        html_dump = lookup_online("crest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apple(self):
        html_dump = lookup_online("apple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whirl(self):
        html_dump = lookup_online("whirl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrutiny(self):
        html_dump = lookup_online("scrutiny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abandon(self):
        html_dump = lookup_online("abandon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hubris(self):
        html_dump = lookup_online("hubris")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creed(self):
        html_dump = lookup_online("creed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aghast(self):
        html_dump = lookup_online("aghast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concession(self):
        html_dump = lookup_online("concession")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contest(self):
        html_dump = lookup_online("contest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unravel(self):
        html_dump = lookup_online("unravel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whimper(self):
        html_dump = lookup_online("whimper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nigh(self):
        html_dump = lookup_online("nigh")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_molasses(self):
        html_dump = lookup_online("molasses")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revered(self):
        html_dump = lookup_online("revered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_captivity(self):
        html_dump = lookup_online("captivity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unanimous(self):
        html_dump = lookup_online("unanimous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminence(self):
        html_dump = lookup_online("eminence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juggernaut(self):
        html_dump = lookup_online("juggernaut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laudanum(self):
        html_dump = lookup_online("laudanum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interdict(self):
        html_dump = lookup_online("interdict")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fulfill(self):
        html_dump = lookup_online("fulfill")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_groggy(self):
        html_dump = lookup_online("groggy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paucity(self):
        html_dump = lookup_online("paucity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morrow(self):
        html_dump = lookup_online("morrow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_porous(self):
        html_dump = lookup_online("porous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sodding(self):
        html_dump = lookup_online("sodding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beholden(self):
        html_dump = lookup_online("beholden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eyesore(self):
        html_dump = lookup_online("eyesore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vainglory(self):
        html_dump = lookup_online("vainglory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coalesce(self):
        html_dump = lookup_online("coalesce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fester(self):
        html_dump = lookup_online("fester")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petulance(self):
        html_dump = lookup_online("petulance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leniency(self):
        html_dump = lookup_online("leniency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debris(self):
        html_dump = lookup_online("debris")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vanity(self):
        html_dump = lookup_online("vanity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compel(self):
        html_dump = lookup_online("compel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solipsist(self):
        html_dump = lookup_online("solipsist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_betide(self):
        html_dump = lookup_online("betide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ludicrous(self):
        html_dump = lookup_online("ludicrous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chant(self):
        html_dump = lookup_online("chant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hound(self):
        html_dump = lookup_online("hound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ideation(self):
        html_dump = lookup_online("ideation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infamy(self):
        html_dump = lookup_online("infamy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leshy(self):
        html_dump = lookup_online("leshy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contemporary(self):
        html_dump = lookup_online("contemporary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muck(self):
        html_dump = lookup_online("muck")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abutting(self):
        html_dump = lookup_online("abutting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaunt(self):
        html_dump = lookup_online("gaunt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distaste(self):
        html_dump = lookup_online("distaste")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ecocide(self):
        html_dump = lookup_online("ecocide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjugation(self):
        html_dump = lookup_online("conjugation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicissitude(self):
        html_dump = lookup_online("vicissitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouper(self):
        html_dump = lookup_online("grouper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bespoke(self):
        html_dump = lookup_online("bespoke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protraction(self):
        html_dump = lookup_online("protraction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aphasia(self):
        html_dump = lookup_online("aphasia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sluice(self):
        html_dump = lookup_online("sluice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ivory(self):
        html_dump = lookup_online("ivory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lichen(self):
        html_dump = lookup_online("lichen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avon(self):
        html_dump = lookup_online("avon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscientiousness(self):
        html_dump = lookup_online("conscientiousness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_complex(self):
        html_dump = lookup_online("complex")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pried(self):
        html_dump = lookup_online("pried")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entail(self):
        html_dump = lookup_online("entail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unrepentant(self):
        html_dump = lookup_online("unrepentant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plateau(self):
        html_dump = lookup_online("plateau")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pus(self):
        html_dump = lookup_online("pus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_latent(self):
        html_dump = lookup_online("latent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vignette(self):
        html_dump = lookup_online("vignette")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenet(self):
        html_dump = lookup_online("tenet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedition(self):
        html_dump = lookup_online("sedition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snub(self):
        html_dump = lookup_online("snub")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_buoyant(self):
        html_dump = lookup_online("buoyant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pushy(self):
        html_dump = lookup_online("pushy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_walnut(self):
        html_dump = lookup_online("walnut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stuffy(self):
        html_dump = lookup_online("stuffy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mace(self):
        html_dump = lookup_online("mace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetual(self):
        html_dump = lookup_online("perpetual")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procurer(self):
        html_dump = lookup_online("procurer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sander(self):
        html_dump = lookup_online("sander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assertive(self):
        html_dump = lookup_online("assertive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wokeness(self):
        html_dump = lookup_online("wokeness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fluke(self):
        html_dump = lookup_online("fluke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrill(self):
        html_dump = lookup_online("shrill")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snubbed(self):
        html_dump = lookup_online("snubbed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orifice(self):
        html_dump = lookup_online("orifice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ignoramus(self):
        html_dump = lookup_online("ignoramus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remission(self):
        html_dump = lookup_online("remission")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diligence(self):
        html_dump = lookup_online("diligence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heredity(self):
        html_dump = lookup_online("heredity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vertigo(self):
        html_dump = lookup_online("vertigo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vertebrate(self):
        html_dump = lookup_online("vertebrate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pegboard(self):
        html_dump = lookup_online("pegboard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vainly(self):
        html_dump = lookup_online("vainly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infringement(self):
        html_dump = lookup_online("infringement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desolation(self):
        html_dump = lookup_online("desolation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tend(self):
        html_dump = lookup_online("tend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adjourn(self):
        html_dump = lookup_online("adjourn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permeate(self):
        html_dump = lookup_online("permeate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heft(self):
        html_dump = lookup_online("heft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utterance(self):
        html_dump = lookup_online("utterance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_careen(self):
        html_dump = lookup_online("careen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_VAT(self):
        html_dump = lookup_online("VAT")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turnip(self):
        html_dump = lookup_online("turnip")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paragon(self):
        html_dump = lookup_online("paragon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pecan(self):
        html_dump = lookup_online("pecan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peruse(self):
        html_dump = lookup_online("peruse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_putty(self):
        html_dump = lookup_online("putty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cotton(self):
        html_dump = lookup_online("cotton")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraternity(self):
        html_dump = lookup_online("fraternity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caldera(self):
        html_dump = lookup_online("caldera")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mellow(self):
        html_dump = lookup_online("mellow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emasculate(self):
        html_dump = lookup_online("emasculate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stewardship(self):
        html_dump = lookup_online("stewardship")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incontinence(self):
        html_dump = lookup_online("incontinence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gendarmerie(self):
        html_dump = lookup_online("gendarmerie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splurge(self):
        html_dump = lookup_online("splurge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ebony(self):
        html_dump = lookup_online("ebony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redeem(self):
        html_dump = lookup_online("redeem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slut(self):
        html_dump = lookup_online("slut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_invalidation(self):
        html_dump = lookup_online("invalidation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoil(self):
        html_dump = lookup_online("spoil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heinous(self):
        html_dump = lookup_online("heinous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grazing(self):
        html_dump = lookup_online("grazing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_galore(self):
        html_dump = lookup_online("galore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brine(self):
        html_dump = lookup_online("brine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mirthless(self):
        html_dump = lookup_online("mirthless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiefs(self):
        html_dump = lookup_online("fiefs")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstructive(self):
        html_dump = lookup_online("obstructive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ponderous(self):
        html_dump = lookup_online("ponderous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indispensable(self):
        html_dump = lookup_online("indispensable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sullen(self):
        html_dump = lookup_online("sullen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prance(self):
        html_dump = lookup_online("prance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_content(self):
        html_dump = lookup_online("content")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squander(self):
        html_dump = lookup_online("squander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bedridden(self):
        html_dump = lookup_online("bedridden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bore(self):
        html_dump = lookup_online("bore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pursuer(self):
        html_dump = lookup_online("pursuer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_offspring(self):
        html_dump = lookup_online("offspring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misfit(self):
        html_dump = lookup_online("misfit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manacle(self):
        html_dump = lookup_online("manacle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parochial(self):
        html_dump = lookup_online("parochial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ribald(self):
        html_dump = lookup_online("ribald")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patronize(self):
        html_dump = lookup_online("patronize")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loaf(self):
        html_dump = lookup_online("loaf")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crevice(self):
        html_dump = lookup_online("crevice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cow(self):
        html_dump = lookup_online("cow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cello(self):
        html_dump = lookup_online("cello")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cuneiform(self):
        html_dump = lookup_online("cuneiform")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contort(self):
        html_dump = lookup_online("contort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudent(self):
        html_dump = lookup_online("prudent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riveting(self):
        html_dump = lookup_online("riveting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wryly(self):
        html_dump = lookup_online("wryly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protomartyr(self):
        html_dump = lookup_online("protomartyr")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taxidermist(self):
        html_dump = lookup_online("taxidermist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_addled(self):
        html_dump = lookup_online("addled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_germinate(self):
        html_dump = lookup_online("germinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stipulate(self):
        html_dump = lookup_online("stipulate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anathema(self):
        html_dump = lookup_online("anathema")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feathered(self):
        html_dump = lookup_online("feathered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rowan(self):
        html_dump = lookup_online("rowan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rectifier(self):
        html_dump = lookup_online("rectifier")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immediacy(self):
        html_dump = lookup_online("immediacy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_batter(self):
        html_dump = lookup_online("batter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_honky(self):
        html_dump = lookup_online("honky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruthless(self):
        html_dump = lookup_online("ruthless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deliberation(self):
        html_dump = lookup_online("deliberation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squib(self):
        html_dump = lookup_online("squib")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prophecy(self):
        html_dump = lookup_online("prophecy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slew(self):
        html_dump = lookup_online("slew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravine(self):
        html_dump = lookup_online("ravine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Levi(self):
        html_dump = lookup_online("Levi")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vapidity(self):
        html_dump = lookup_online("vapidity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stunt(self):
        html_dump = lookup_online("stunt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inhibited(self):
        html_dump = lookup_online("inhibited")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effusively(self):
        html_dump = lookup_online("effusively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defer(self):
        html_dump = lookup_online("defer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coattail(self):
        html_dump = lookup_online("coattail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incriminate(self):
        html_dump = lookup_online("incriminate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feast(self):
        html_dump = lookup_online("feast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heave(self):
        html_dump = lookup_online("heave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_escalator(self):
        html_dump = lookup_online("escalator")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longshoreman(self):
        html_dump = lookup_online("longshoreman")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incinerate(self):
        html_dump = lookup_online("incinerate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glee(self):
        html_dump = lookup_online("glee")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consign(self):
        html_dump = lookup_online("consign")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coercion(self):
        html_dump = lookup_online("coercion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procure(self):
        html_dump = lookup_online("procure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_usher(self):
        html_dump = lookup_online("usher")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protagonist(self):
        html_dump = lookup_online("protagonist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discernible(self):
        html_dump = lookup_online("discernible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tropic(self):
        html_dump = lookup_online("tropic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_masonite(self):
        html_dump = lookup_online("masonite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spun(self):
        html_dump = lookup_online("spun")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penchant(self):
        html_dump = lookup_online("penchant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sombre(self):
        html_dump = lookup_online("sombre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_graze(self):
        html_dump = lookup_online("graze")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reeling(self):
        html_dump = lookup_online("reeling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plaid(self):
        html_dump = lookup_online("plaid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscience(self):
        html_dump = lookup_online("conscience")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kindred(self):
        html_dump = lookup_online("kindred")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flatulence(self):
        html_dump = lookup_online("flatulence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adherent(self):
        html_dump = lookup_online("adherent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sacrosanct(self):
        html_dump = lookup_online("sacrosanct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heartburn(self):
        html_dump = lookup_online("heartburn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arduous(self):
        html_dump = lookup_online("arduous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_specter(self):
        html_dump = lookup_online("specter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pretence(self):
        html_dump = lookup_online("pretence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vain(self):
        html_dump = lookup_online("vain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permeable(self):
        html_dump = lookup_online("permeable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rambunctious(self):
        html_dump = lookup_online("rambunctious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emaciate(self):
        html_dump = lookup_online("emaciate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impediment(self):
        html_dump = lookup_online("impediment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salience(self):
        html_dump = lookup_online("salience")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_klutzy(self):
        html_dump = lookup_online("klutzy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disclosure(self):
        html_dump = lookup_online("disclosure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arid(self):
        html_dump = lookup_online("arid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_philander(self):
        html_dump = lookup_online("philander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tidbit(self):
        html_dump = lookup_online("tidbit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jostle(self):
        html_dump = lookup_online("jostle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concord(self):
        html_dump = lookup_online("concord")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_residue(self):
        html_dump = lookup_online("residue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumultuous(self):
        html_dump = lookup_online("tumultuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_translucent(self):
        html_dump = lookup_online("translucent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cooties(self):
        html_dump = lookup_online("cooties")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_underlining(self):
        html_dump = lookup_online("underlining")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sog(self):
        html_dump = lookup_online("sog")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moose(self):
        html_dump = lookup_online("moose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eke(self):
        html_dump = lookup_online("eke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoggish(self):
        html_dump = lookup_online("hoggish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chafing(self):
        html_dump = lookup_online("chafing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admonish(self):
        html_dump = lookup_online("admonish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nitpick(self):
        html_dump = lookup_online("nitpick")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clamp(self):
        html_dump = lookup_online("clamp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_usufruct(self):
        html_dump = lookup_online("usufruct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuple(self):
        html_dump = lookup_online("tuple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_volatile(self):
        html_dump = lookup_online("volatile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrink(self):
        html_dump = lookup_online("shrink")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cleavage(self):
        html_dump = lookup_online("cleavage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dint(self):
        html_dump = lookup_online("dint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckon(self):
        html_dump = lookup_online("reckon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nausea(self):
        html_dump = lookup_online("nausea")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vixen(self):
        html_dump = lookup_online("vixen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goop(self):
        html_dump = lookup_online("goop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strident(self):
        html_dump = lookup_online("strident")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_server(self):
        html_dump = lookup_online("server")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pebble(self):
        html_dump = lookup_online("pebble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turtle(self):
        html_dump = lookup_online("turtle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shard(self):
        html_dump = lookup_online("shard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smear(self):
        html_dump = lookup_online("smear")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterministic(self):
        html_dump = lookup_online("deterministic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chump(self):
        html_dump = lookup_online("chump")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mortician(self):
        html_dump = lookup_online("mortician")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penance(self):
        html_dump = lookup_online("penance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placid(self):
        html_dump = lookup_online("placid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maven(self):
        html_dump = lookup_online("maven")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertinent(self):
        html_dump = lookup_online("pertinent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cornucopia(self):
        html_dump = lookup_online("cornucopia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_static(self):
        html_dump = lookup_online("static")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unmoored(self):
        html_dump = lookup_online("unmoored")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larch(self):
        html_dump = lookup_online("larch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blistering(self):
        html_dump = lookup_online("blistering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stride(self):
        html_dump = lookup_online("stride")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nutmeg(self):
        html_dump = lookup_online("nutmeg")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posit(self):
        html_dump = lookup_online("posit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_charter(self):
        html_dump = lookup_online("charter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oblivious(self):
        html_dump = lookup_online("oblivious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_schist(self):
        html_dump = lookup_online("schist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predilection(self):
        html_dump = lookup_online("predilection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solace(self):
        html_dump = lookup_online("solace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaunt(self):
        html_dump = lookup_online("vaunt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulchritude(self):
        html_dump = lookup_online("pulchritude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheapening(self):
        html_dump = lookup_online("cheapening")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impalpable(self):
        html_dump = lookup_online("impalpable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_severe(self):
        html_dump = lookup_online("severe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contingent(self):
        html_dump = lookup_online("contingent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_falter(self):
        html_dump = lookup_online("falter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swirl(self):
        html_dump = lookup_online("swirl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cratering(self):
        html_dump = lookup_online("cratering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_industrious(self):
        html_dump = lookup_online("industrious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crass(self):
        html_dump = lookup_online("crass")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quibble(self):
        html_dump = lookup_online("quibble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lacerate(self):
        html_dump = lookup_online("lacerate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arrear(self):
        html_dump = lookup_online("arrear")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wariness(self):
        html_dump = lookup_online("wariness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parable(self):
        html_dump = lookup_online("parable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congenial(self):
        html_dump = lookup_online("congenial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pusillanimity(self):
        html_dump = lookup_online("pusillanimity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grizzled(self):
        html_dump = lookup_online("grizzled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endorsement(self):
        html_dump = lookup_online("endorsement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upsell(self):
        html_dump = lookup_online("upsell")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blackened(self):
        html_dump = lookup_online("blackened")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sizzle(self):
        html_dump = lookup_online("sizzle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hawthorn(self):
        html_dump = lookup_online("hawthorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lotion(self):
        html_dump = lookup_online("lotion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_macaw(self):
        html_dump = lookup_online("macaw")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reprieve(self):
        html_dump = lookup_online("reprieve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gust(self):
        html_dump = lookup_online("gust")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shank(self):
        html_dump = lookup_online("shank")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bramble(self):
        html_dump = lookup_online("bramble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corvid(self):
        html_dump = lookup_online("corvid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stud(self):
        html_dump = lookup_online("stud")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ceaselessly(self):
        html_dump = lookup_online("ceaselessly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crayfish(self):
        html_dump = lookup_online("crayfish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stern(self):
        html_dump = lookup_online("stern")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sapient(self):
        html_dump = lookup_online("sapient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arresting(self):
        html_dump = lookup_online("arresting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tentatively(self):
        html_dump = lookup_online("tentatively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retain(self):
        html_dump = lookup_online("retain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posterity(self):
        html_dump = lookup_online("posterity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lacklustre(self):
        html_dump = lookup_online("lacklustre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grungy(self):
        html_dump = lookup_online("grungy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_establish(self):
        html_dump = lookup_online("establish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asinine(self):
        html_dump = lookup_online("asinine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interdiction(self):
        html_dump = lookup_online("interdiction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clemency(self):
        html_dump = lookup_online("clemency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_circumvent(self):
        html_dump = lookup_online("circumvent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lark(self):
        html_dump = lookup_online("lark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adenoids(self):
        html_dump = lookup_online("adenoids")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veracity(self):
        html_dump = lookup_online("veracity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effuse(self):
        html_dump = lookup_online("effuse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_panache(self):
        html_dump = lookup_online("panache")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_isthmus(self):
        html_dump = lookup_online("isthmus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gestation(self):
        html_dump = lookup_online("gestation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quinine(self):
        html_dump = lookup_online("quinine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jugular(self):
        html_dump = lookup_online("jugular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exuberant(self):
        html_dump = lookup_online("exuberant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastry(self):
        html_dump = lookup_online("pastry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapscallion(self):
        html_dump = lookup_online("rapscallion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exonym(self):
        html_dump = lookup_online("exonym")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ensconce(self):
        html_dump = lookup_online("ensconce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coherence(self):
        html_dump = lookup_online("coherence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poised(self):
        html_dump = lookup_online("poised")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pls(self):
        html_dump = lookup_online("pls")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quirky(self):
        html_dump = lookup_online("quirky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hopefully(self):
        html_dump = lookup_online("hopefully")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mantle(self):
        html_dump = lookup_online("mantle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tribulation(self):
        html_dump = lookup_online("tribulation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_to(self):
        html_dump = lookup_online("to")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knoll(self):
        html_dump = lookup_online("knoll")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abhor(self):
        html_dump = lookup_online("abhor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_illegitimacy(self):
        html_dump = lookup_online("illegitimacy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juxtaposition(self):
        html_dump = lookup_online("juxtaposition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shag(self):
        html_dump = lookup_online("shag")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immersion(self):
        html_dump = lookup_online("immersion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tactile(self):
        html_dump = lookup_online("tactile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haphazardly(self):
        html_dump = lookup_online("haphazardly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turf(self):
        html_dump = lookup_online("turf")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_basswood(self):
        html_dump = lookup_online("basswood")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rowdy(self):
        html_dump = lookup_online("rowdy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outwardly(self):
        html_dump = lookup_online("outwardly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_credible(self):
        html_dump = lookup_online("credible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fawning(self):
        html_dump = lookup_online("fawning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_closure(self):
        html_dump = lookup_online("closure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duplicitous(self):
        html_dump = lookup_online("duplicitous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scald(self):
        html_dump = lookup_online("scald")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparate(self):
        html_dump = lookup_online("disparate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endow(self):
        html_dump = lookup_online("endow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weasel(self):
        html_dump = lookup_online("weasel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gravitas(self):
        html_dump = lookup_online("gravitas")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_casket(self):
        html_dump = lookup_online("casket")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_omniscient(self):
        html_dump = lookup_online("omniscient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rag(self):
        html_dump = lookup_online("rag")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rod(self):
        html_dump = lookup_online("rod")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suckle(self):
        html_dump = lookup_online("suckle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oxblood(self):
        html_dump = lookup_online("oxblood")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peckish(self):
        html_dump = lookup_online("peckish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tableau(self):
        html_dump = lookup_online("tableau")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attrition(self):
        html_dump = lookup_online("attrition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawler(self):
        html_dump = lookup_online("brawler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggrieved(self):
        html_dump = lookup_online("aggrieved")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shawty(self):
        html_dump = lookup_online("shawty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foible(self):
        html_dump = lookup_online("foible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slant(self):
        html_dump = lookup_online("slant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deer(self):
        html_dump = lookup_online("deer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flamboyant(self):
        html_dump = lookup_online("flamboyant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pat(self):
        html_dump = lookup_online("pat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vine(self):
        html_dump = lookup_online("vine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_iridescent(self):
        html_dump = lookup_online("iridescent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glean(self):
        html_dump = lookup_online("glean")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dope(self):
        html_dump = lookup_online("dope")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wanton(self):
        html_dump = lookup_online("wanton")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uppity(self):
        html_dump = lookup_online("uppity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_composure(self):
        html_dump = lookup_online("composure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pabulum(self):
        html_dump = lookup_online("pabulum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unremarkable(self):
        html_dump = lookup_online("unremarkable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clark(self):
        html_dump = lookup_online("clark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bosom(self):
        html_dump = lookup_online("bosom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discrete(self):
        html_dump = lookup_online("discrete")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleet(self):
        html_dump = lookup_online("sleet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rarefaction(self):
        html_dump = lookup_online("rarefaction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hubcap(self):
        html_dump = lookup_online("hubcap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tatters(self):
        html_dump = lookup_online("tatters")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tack(self):
        html_dump = lookup_online("tack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crumpet(self):
        html_dump = lookup_online("crumpet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bawl(self):
        html_dump = lookup_online("bawl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_funnel(self):
        html_dump = lookup_online("funnel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wail(self):
        html_dump = lookup_online("wail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leisure(self):
        html_dump = lookup_online("leisure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rolodex(self):
        html_dump = lookup_online("rolodex")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cupola(self):
        html_dump = lookup_online("cupola")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eczema(self):
        html_dump = lookup_online("eczema")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_festoon(self):
        html_dump = lookup_online("festoon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drivel(self):
        html_dump = lookup_online("drivel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicinity(self):
        html_dump = lookup_online("vicinity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_starlight(self):
        html_dump = lookup_online("starlight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_decimate(self):
        html_dump = lookup_online("decimate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_astonished(self):
        html_dump = lookup_online("astonished")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impugning(self):
        html_dump = lookup_online("impugning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stew(self):
        html_dump = lookup_online("stew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sensibly(self):
        html_dump = lookup_online("sensibly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dengue(self):
        html_dump = lookup_online("dengue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convent(self):
        html_dump = lookup_online("convent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mendacious(self):
        html_dump = lookup_online("mendacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allotment(self):
        html_dump = lookup_online("allotment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bicentennial(self):
        html_dump = lookup_online("bicentennial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_astute(self):
        html_dump = lookup_online("astute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_treacly(self):
        html_dump = lookup_online("treacly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edification(self):
        html_dump = lookup_online("edification")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ail(self):
        html_dump = lookup_online("ail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tally(self):
        html_dump = lookup_online("tally")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cordial(self):
        html_dump = lookup_online("cordial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_racoon(self):
        html_dump = lookup_online("racoon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tepid(self):
        html_dump = lookup_online("tepid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detriment(self):
        html_dump = lookup_online("detriment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mercurial(self):
        html_dump = lookup_online("mercurial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_timbre(self):
        html_dump = lookup_online("timbre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appalling(self):
        html_dump = lookup_online("appalling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewilderment(self):
        html_dump = lookup_online("bewilderment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_livid(self):
        html_dump = lookup_online("livid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wailing(self):
        html_dump = lookup_online("wailing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_devious(self):
        html_dump = lookup_online("devious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_axiom(self):
        html_dump = lookup_online("axiom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tarp(self):
        html_dump = lookup_online("tarp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacitly(self):
        html_dump = lookup_online("tacitly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tug(self):
        html_dump = lookup_online("tug")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrappy(self):
        html_dump = lookup_online("scrappy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_payoff(self):
        html_dump = lookup_online("payoff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_animosity(self):
        html_dump = lookup_online("animosity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lupine(self):
        html_dump = lookup_online("lupine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asunder(self):
        html_dump = lookup_online("asunder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwitting(self):
        html_dump = lookup_online("unwitting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quisling(self):
        html_dump = lookup_online("quisling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_connoisseur(self):
        html_dump = lookup_online("connoisseur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaporous(self):
        html_dump = lookup_online("vaporous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harlot(self):
        html_dump = lookup_online("harlot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blunderbuss(self):
        html_dump = lookup_online("blunderbuss")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muddler(self):
        html_dump = lookup_online("muddler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commotion(self):
        html_dump = lookup_online("commotion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trout(self):
        html_dump = lookup_online("trout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extort(self):
        html_dump = lookup_online("extort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vernacular(self):
        html_dump = lookup_online("vernacular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_queasy(self):
        html_dump = lookup_online("queasy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pretentious(self):
        html_dump = lookup_online("pretentious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrewd(self):
        html_dump = lookup_online("shrewd")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mantel(self):
        html_dump = lookup_online("mantel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onus(self):
        html_dump = lookup_online("onus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hypodermic(self):
        html_dump = lookup_online("hypodermic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prophesying(self):
        html_dump = lookup_online("prophesying")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pry(self):
        html_dump = lookup_online("pry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inundated(self):
        html_dump = lookup_online("inundated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holistic(self):
        html_dump = lookup_online("holistic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aperture(self):
        html_dump = lookup_online("aperture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grasp(self):
        html_dump = lookup_online("grasp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_searing(self):
        html_dump = lookup_online("searing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recalcitrant(self):
        html_dump = lookup_online("recalcitrant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moribund(self):
        html_dump = lookup_online("moribund")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transitive(self):
        html_dump = lookup_online("transitive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brat(self):
        html_dump = lookup_online("brat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mush(self):
        html_dump = lookup_online("mush")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immerse(self):
        html_dump = lookup_online("immerse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imbue(self):
        html_dump = lookup_online("imbue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shutter(self):
        html_dump = lookup_online("shutter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fingertip(self):
        html_dump = lookup_online("fingertip")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurn(self):
        html_dump = lookup_online("spurn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curfew(self):
        html_dump = lookup_online("curfew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subpoena(self):
        html_dump = lookup_online("subpoena")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plunge(self):
        html_dump = lookup_online("plunge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissent(self):
        html_dump = lookup_online("dissent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contagion(self):
        html_dump = lookup_online("contagion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petty(self):
        html_dump = lookup_online("petty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preordain(self):
        html_dump = lookup_online("preordain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revery(self):
        html_dump = lookup_online("revery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amygdala(self):
        html_dump = lookup_online("amygdala")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rendition(self):
        html_dump = lookup_online("rendition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incumbent(self):
        html_dump = lookup_online("incumbent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_analgesic(self):
        html_dump = lookup_online("analgesic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prejudice(self):
        html_dump = lookup_online("prejudice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savage(self):
        html_dump = lookup_online("savage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marvellous(self):
        html_dump = lookup_online("marvellous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dulcimer(self):
        html_dump = lookup_online("dulcimer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stupor(self):
        html_dump = lookup_online("stupor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rickets(self):
        html_dump = lookup_online("rickets")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utensil(self):
        html_dump = lookup_online("utensil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mollify(self):
        html_dump = lookup_online("mollify")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dot(self):
        html_dump = lookup_online("dot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mansion(self):
        html_dump = lookup_online("mansion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corroborate(self):
        html_dump = lookup_online("corroborate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vapid(self):
        html_dump = lookup_online("vapid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quixotic(self):
        html_dump = lookup_online("quixotic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effigy(self):
        html_dump = lookup_online("effigy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bungle(self):
        html_dump = lookup_online("bungle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wane(self):
        html_dump = lookup_online("wane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mend(self):
        html_dump = lookup_online("mend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ambient(self):
        html_dump = lookup_online("ambient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gluttony(self):
        html_dump = lookup_online("gluttony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheeky(self):
        html_dump = lookup_online("cheeky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lymphoma(self):
        html_dump = lookup_online("lymphoma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affirm(self):
        html_dump = lookup_online("affirm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confide(self):
        html_dump = lookup_online("confide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preternatural(self):
        html_dump = lookup_online("preternatural")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evanescent(self):
        html_dump = lookup_online("evanescent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ineffectual(self):
        html_dump = lookup_online("ineffectual")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alacrity(self):
        html_dump = lookup_online("alacrity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marsupial(self):
        html_dump = lookup_online("marsupial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_courting(self):
        html_dump = lookup_online("courting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_balk(self):
        html_dump = lookup_online("balk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_collate(self):
        html_dump = lookup_online("collate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_denouement(self):
        html_dump = lookup_online("denouement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oaf(self):
        html_dump = lookup_online("oaf")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riverine(self):
        html_dump = lookup_online("riverine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuberculosis(self):
        html_dump = lookup_online("tuberculosis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mottle(self):
        html_dump = lookup_online("mottle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_iffy(self):
        html_dump = lookup_online("iffy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savory(self):
        html_dump = lookup_online("savory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sobriety(self):
        html_dump = lookup_online("sobriety")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Mace(self):
        html_dump = lookup_online("Mace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wrong_headed(self):
        html_dump = lookup_online("wrong-headed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reticent(self):
        html_dump = lookup_online("reticent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abruptly(self):
        html_dump = lookup_online("abruptly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eulogy(self):
        html_dump = lookup_online("eulogy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slime(self):
        html_dump = lookup_online("slime")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awning(self):
        html_dump = lookup_online("awning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bowled(self):
        html_dump = lookup_online("bowled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glum(self):
        html_dump = lookup_online("glum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calcify(self):
        html_dump = lookup_online("calcify")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forthright(self):
        html_dump = lookup_online("forthright")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mischief(self):
        html_dump = lookup_online("mischief")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_granadilla(self):
        html_dump = lookup_online("granadilla")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garish(self):
        html_dump = lookup_online("garish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compulsory(self):
        html_dump = lookup_online("compulsory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lotus(self):
        html_dump = lookup_online("lotus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quotidian(self):
        html_dump = lookup_online("quotidian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perch(self):
        html_dump = lookup_online("perch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_segues(self):
        html_dump = lookup_online("segues")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flirty(self):
        html_dump = lookup_online("flirty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smugness(self):
        html_dump = lookup_online("smugness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spic(self):
        html_dump = lookup_online("spic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mastic(self):
        html_dump = lookup_online("mastic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pompous(self):
        html_dump = lookup_online("pompous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admissible(self):
        html_dump = lookup_online("admissible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minimalistic(self):
        html_dump = lookup_online("minimalistic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hovercraft(self):
        html_dump = lookup_online("hovercraft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compound(self):
        html_dump = lookup_online("compound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crusty(self):
        html_dump = lookup_online("crusty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spite(self):
        html_dump = lookup_online("spite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_buzzard(self):
        html_dump = lookup_online("buzzard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_waver(self):
        html_dump = lookup_online("waver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravel(self):
        html_dump = lookup_online("ravel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismal(self):
        html_dump = lookup_online("dismal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impotence(self):
        html_dump = lookup_online("impotence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assuage(self):
        html_dump = lookup_online("assuage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conduct(self):
        html_dump = lookup_online("conduct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indict(self):
        html_dump = lookup_online("indict")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emaciated(self):
        html_dump = lookup_online("emaciated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solitude(self):
        html_dump = lookup_online("solitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brill(self):
        html_dump = lookup_online("brill")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_constraint(self):
        html_dump = lookup_online("constraint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derogatory(self):
        html_dump = lookup_online("derogatory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruesome(self):
        html_dump = lookup_online("gruesome")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_umpire(self):
        html_dump = lookup_online("umpire")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rout(self):
        html_dump = lookup_online("rout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_runt(self):
        html_dump = lookup_online("runt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bovine(self):
        html_dump = lookup_online("bovine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_this(self):
        html_dump = lookup_online("this")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mold(self):
        html_dump = lookup_online("mold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagaries(self):
        html_dump = lookup_online("vagaries")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epiphanic(self):
        html_dump = lookup_online("epiphanic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overhead(self):
        html_dump = lookup_online("overhead")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perennial(self):
        html_dump = lookup_online("perennial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aptly(self):
        html_dump = lookup_online("aptly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menacing(self):
        html_dump = lookup_online("menacing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loon(self):
        html_dump = lookup_online("loon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satiable(self):
        html_dump = lookup_online("satiable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_callousness(self):
        html_dump = lookup_online("callousness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_huff(self):
        html_dump = lookup_online("huff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incidentally(self):
        html_dump = lookup_online("incidentally")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brassiere(self):
        html_dump = lookup_online("brassiere")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_torpor(self):
        html_dump = lookup_online("torpor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_profane(self):
        html_dump = lookup_online("profane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calamity(self):
        html_dump = lookup_online("calamity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hard_boiled(self):
        html_dump = lookup_online("hard-boiled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burly(self):
        html_dump = lookup_online("burly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epistemology(self):
        html_dump = lookup_online("epistemology")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artisan(self):
        html_dump = lookup_online("artisan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epitomize(self):
        html_dump = lookup_online("epitomize")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpably(self):
        html_dump = lookup_online("culpably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mitten(self):
        html_dump = lookup_online("mitten")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bequeath(self):
        html_dump = lookup_online("bequeath")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endowment(self):
        html_dump = lookup_online("endowment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rebuke(self):
        html_dump = lookup_online("rebuke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refute(self):
        html_dump = lookup_online("refute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merit(self):
        html_dump = lookup_online("merit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilante(self):
        html_dump = lookup_online("vigilante")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frontier(self):
        html_dump = lookup_online("frontier")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confidant(self):
        html_dump = lookup_online("confidant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallacy(self):
        html_dump = lookup_online("fallacy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preposterous(self):
        html_dump = lookup_online("preposterous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mockery(self):
        html_dump = lookup_online("mockery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lugubrious(self):
        html_dump = lookup_online("lugubrious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hemlock(self):
        html_dump = lookup_online("hemlock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discern(self):
        html_dump = lookup_online("discern")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derisively(self):
        html_dump = lookup_online("derisively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_woe(self):
        html_dump = lookup_online("woe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conn(self):
        html_dump = lookup_online("conn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_telltale(self):
        html_dump = lookup_online("telltale")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fawn(self):
        html_dump = lookup_online("fawn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conclude(self):
        html_dump = lookup_online("conclude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flinching(self):
        html_dump = lookup_online("flinching")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subpar(self):
        html_dump = lookup_online("subpar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rosewood(self):
        html_dump = lookup_online("rosewood")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fare(self):
        html_dump = lookup_online("fare")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumple(self):
        html_dump = lookup_online("rumple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irascible(self):
        html_dump = lookup_online("irascible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weld(self):
        html_dump = lookup_online("weld")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lean(self):
        html_dump = lookup_online("lean")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hither(self):
        html_dump = lookup_online("hither")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lump(self):
        html_dump = lookup_online("lump")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compunction(self):
        html_dump = lookup_online("compunction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_measles(self):
        html_dump = lookup_online("measles")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trigger(self):
        html_dump = lookup_online("trigger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wallaby(self):
        html_dump = lookup_online("wallaby")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adamant(self):
        html_dump = lookup_online("adamant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irritable(self):
        html_dump = lookup_online("irritable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_querulous(self):
        html_dump = lookup_online("querulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocate(self):
        html_dump = lookup_online("reciprocate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_offal(self):
        html_dump = lookup_online("offal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coop(self):
        html_dump = lookup_online("coop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eerily(self):
        html_dump = lookup_online("eerily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inane(self):
        html_dump = lookup_online("inane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexorably(self):
        html_dump = lookup_online("inexorably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concave(self):
        html_dump = lookup_online("concave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retrieve(self):
        html_dump = lookup_online("retrieve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cadaver(self):
        html_dump = lookup_online("cadaver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dereliction(self):
        html_dump = lookup_online("dereliction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_licorice(self):
        html_dump = lookup_online("licorice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knapsack(self):
        html_dump = lookup_online("knapsack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overhaul(self):
        html_dump = lookup_online("overhaul")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shill(self):
        html_dump = lookup_online("shill")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hallmark(self):
        html_dump = lookup_online("hallmark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poise(self):
        html_dump = lookup_online("poise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affluent(self):
        html_dump = lookup_online("affluent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verboten(self):
        html_dump = lookup_online("verboten")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refutation(self):
        html_dump = lookup_online("refutation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fealty(self):
        html_dump = lookup_online("fealty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minted(self):
        html_dump = lookup_online("minted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_odious(self):
        html_dump = lookup_online("odious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blithely(self):
        html_dump = lookup_online("blithely")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trap(self):
        html_dump = lookup_online("trap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_felt(self):
        html_dump = lookup_online("felt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spur(self):
        html_dump = lookup_online("spur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Bedouin(self):
        html_dump = lookup_online("Bedouin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_varnish(self):
        html_dump = lookup_online("varnish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_espouse(self):
        html_dump = lookup_online("espouse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fecundity(self):
        html_dump = lookup_online("fecundity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gourd(self):
        html_dump = lookup_online("gourd")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adage(self):
        html_dump = lookup_online("adage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scotch(self):
        html_dump = lookup_online("scotch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quark(self):
        html_dump = lookup_online("quark")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruse(self):
        html_dump = lookup_online("ruse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vein(self):
        html_dump = lookup_online("vein")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_winch(self):
        html_dump = lookup_online("winch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruminate(self):
        html_dump = lookup_online("ruminate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revelry(self):
        html_dump = lookup_online("revelry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_colon(self):
        html_dump = lookup_online("colon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scooped(self):
        html_dump = lookup_online("scooped")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_itinerant(self):
        html_dump = lookup_online("itinerant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oeuvre(self):
        html_dump = lookup_online("oeuvre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scion(self):
        html_dump = lookup_online("scion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exalted(self):
        html_dump = lookup_online("exalted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_playwright(self):
        html_dump = lookup_online("playwright")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liaison(self):
        html_dump = lookup_online("liaison")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abject(self):
        html_dump = lookup_online("abject")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexpressible(self):
        html_dump = lookup_online("inexpressible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mound(self):
        html_dump = lookup_online("mound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despair(self):
        html_dump = lookup_online("despair")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pettiness(self):
        html_dump = lookup_online("pettiness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portentous(self):
        html_dump = lookup_online("portentous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stagger(self):
        html_dump = lookup_online("stagger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hopeless(self):
        html_dump = lookup_online("hopeless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_until(self):
        html_dump = lookup_online("until")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debonair(self):
        html_dump = lookup_online("debonair")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_columnist(self):
        html_dump = lookup_online("columnist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precarious(self):
        html_dump = lookup_online("precarious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candidly(self):
        html_dump = lookup_online("candidly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loom(self):
        html_dump = lookup_online("loom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bilateral(self):
        html_dump = lookup_online("bilateral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shellac(self):
        html_dump = lookup_online("shellac")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fennel(self):
        html_dump = lookup_online("fennel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slavish(self):
        html_dump = lookup_online("slavish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feckless(self):
        html_dump = lookup_online("feckless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feral(self):
        html_dump = lookup_online("feral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fortitude(self):
        html_dump = lookup_online("fortitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slantwise(self):
        html_dump = lookup_online("slantwise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convoluted(self):
        html_dump = lookup_online("convoluted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defector(self):
        html_dump = lookup_online("defector")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheekily(self):
        html_dump = lookup_online("cheekily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocity(self):
        html_dump = lookup_online("reciprocity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subliminal(self):
        html_dump = lookup_online("subliminal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furry(self):
        html_dump = lookup_online("furry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crayon(self):
        html_dump = lookup_online("crayon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blotter(self):
        html_dump = lookup_online("blotter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_callous(self):
        html_dump = lookup_online("callous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prescient(self):
        html_dump = lookup_online("prescient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinch(self):
        html_dump = lookup_online("pinch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equine(self):
        html_dump = lookup_online("equine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adamantine(self):
        html_dump = lookup_online("adamantine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigent(self):
        html_dump = lookup_online("indigent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_musk(self):
        html_dump = lookup_online("musk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impugned(self):
        html_dump = lookup_online("impugned")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumble(self):
        html_dump = lookup_online("tumble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shim(self):
        html_dump = lookup_online("shim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_billet(self):
        html_dump = lookup_online("billet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blossom(self):
        html_dump = lookup_online("blossom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thrall(self):
        html_dump = lookup_online("thrall")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conifer(self):
        html_dump = lookup_online("conifer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_milter(self):
        html_dump = lookup_online("milter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scoop(self):
        html_dump = lookup_online("scoop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scuttle(self):
        html_dump = lookup_online("scuttle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_injunction(self):
        html_dump = lookup_online("injunction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jot(self):
        html_dump = lookup_online("jot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lye(self):
        html_dump = lookup_online("lye")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petulant(self):
        html_dump = lookup_online("petulant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recriminate(self):
        html_dump = lookup_online("recriminate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inviolate(self):
        html_dump = lookup_online("inviolate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moderate(self):
        html_dump = lookup_online("moderate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merle(self):
        html_dump = lookup_online("merle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_streaked(self):
        html_dump = lookup_online("streaked")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_valiance(self):
        html_dump = lookup_online("valiance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disrobe(self):
        html_dump = lookup_online("disrobe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elm(self):
        html_dump = lookup_online("elm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_descending(self):
        html_dump = lookup_online("descending")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reverie(self):
        html_dump = lookup_online("reverie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clot(self):
        html_dump = lookup_online("clot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trough(self):
        html_dump = lookup_online("trough")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luster(self):
        html_dump = lookup_online("luster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rind(self):
        html_dump = lookup_online("rind")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reserved(self):
        html_dump = lookup_online("reserved")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drizzle(self):
        html_dump = lookup_online("drizzle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranquility(self):
        html_dump = lookup_online("tranquility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_descendant(self):
        html_dump = lookup_online("descendant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_butch(self):
        html_dump = lookup_online("butch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_court(self):
        html_dump = lookup_online("court")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duvet(self):
        html_dump = lookup_online("duvet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discreet(self):
        html_dump = lookup_online("discreet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascertain(self):
        html_dump = lookup_online("ascertain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jacob(self):
        html_dump = lookup_online("jacob")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aneurysm(self):
        html_dump = lookup_online("aneurysm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaudy(self):
        html_dump = lookup_online("gaudy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bespectacled(self):
        html_dump = lookup_online("bespectacled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placidity(self):
        html_dump = lookup_online("placidity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zeal(self):
        html_dump = lookup_online("zeal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flatter(self):
        html_dump = lookup_online("flatter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliability(self):
        html_dump = lookup_online("pliability")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flabbily(self):
        html_dump = lookup_online("flabbily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quadrilateral(self):
        html_dump = lookup_online("quadrilateral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snapshot(self):
        html_dump = lookup_online("snapshot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nephew(self):
        html_dump = lookup_online("nephew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stymie(self):
        html_dump = lookup_online("stymie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dreadnought(self):
        html_dump = lookup_online("dreadnought")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wizard(self):
        html_dump = lookup_online("wizard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tertiary(self):
        html_dump = lookup_online("tertiary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amicable(self):
        html_dump = lookup_online("amicable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unnerving(self):
        html_dump = lookup_online("unnerving")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ordeal(self):
        html_dump = lookup_online("ordeal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peritonitis(self):
        html_dump = lookup_online("peritonitis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_profligate(self):
        html_dump = lookup_online("profligate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_industry(self):
        html_dump = lookup_online("industry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kith(self):
        html_dump = lookup_online("kith")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceal(self):
        html_dump = lookup_online("conceal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antebellum(self):
        html_dump = lookup_online("antebellum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venerable(self):
        html_dump = lookup_online("venerable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clarion(self):
        html_dump = lookup_online("clarion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goldfinch(self):
        html_dump = lookup_online("goldfinch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ornery(self):
        html_dump = lookup_online("ornery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wart(self):
        html_dump = lookup_online("wart")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitously(self):
        html_dump = lookup_online("precipitously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sly(self):
        html_dump = lookup_online("sly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterred(self):
        html_dump = lookup_online("deterred")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquiesce(self):
        html_dump = lookup_online("acquiesce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deteriorate(self):
        html_dump = lookup_online("deteriorate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strayed(self):
        html_dump = lookup_online("strayed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fore(self):
        html_dump = lookup_online("fore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paulownia(self):
        html_dump = lookup_online("paulownia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apologetic(self):
        html_dump = lookup_online("apologetic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enticing(self):
        html_dump = lookup_online("enticing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ensconced(self):
        html_dump = lookup_online("ensconced")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lead(self):
        html_dump = lookup_online("lead")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jilted(self):
        html_dump = lookup_online("jilted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antecedent(self):
        html_dump = lookup_online("antecedent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meandering(self):
        html_dump = lookup_online("meandering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealot(self):
        html_dump = lookup_online("zealot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rudderless(self):
        html_dump = lookup_online("rudderless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_judicious(self):
        html_dump = lookup_online("judicious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_promiscuous(self):
        html_dump = lookup_online("promiscuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squirm(self):
        html_dump = lookup_online("squirm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gallantry(self):
        html_dump = lookup_online("gallantry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forestall(self):
        html_dump = lookup_online("forestall")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incessantly(self):
        html_dump = lookup_online("incessantly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_esoteric(self):
        html_dump = lookup_online("esoteric")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_banter(self):
        html_dump = lookup_online("banter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_injective(self):
        html_dump = lookup_online("injective")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_environment(self):
        html_dump = lookup_online("environment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tentative(self):
        html_dump = lookup_online("tentative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jarring(self):
        html_dump = lookup_online("jarring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moot(self):
        html_dump = lookup_online("moot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_faze(self):
        html_dump = lookup_online("faze")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strain(self):
        html_dump = lookup_online("strain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lath(self):
        html_dump = lookup_online("lath")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscarry(self):
        html_dump = lookup_online("miscarry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contingency(self):
        html_dump = lookup_online("contingency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceit(self):
        html_dump = lookup_online("conceit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_invalidate(self):
        html_dump = lookup_online("invalidate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malaise(self):
        html_dump = lookup_online("malaise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resolute(self):
        html_dump = lookup_online("resolute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidget(self):
        html_dump = lookup_online("fidget")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crux(self):
        html_dump = lookup_online("crux")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flip(self):
        html_dump = lookup_online("flip")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gorgeous(self):
        html_dump = lookup_online("gorgeous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lupus(self):
        html_dump = lookup_online("lupus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Mongoloid(self):
        html_dump = lookup_online("Mongoloid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serpentine(self):
        html_dump = lookup_online("serpentine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pancreas(self):
        html_dump = lookup_online("pancreas")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poultry(self):
        html_dump = lookup_online("poultry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_explicit(self):
        html_dump = lookup_online("explicit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gander(self):
        html_dump = lookup_online("gander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palliate(self):
        html_dump = lookup_online("palliate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lay(self):
        html_dump = lookup_online("lay")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deferential(self):
        html_dump = lookup_online("deferential")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interleaving(self):
        html_dump = lookup_online("interleaving")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travesty(self):
        html_dump = lookup_online("travesty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spindly(self):
        html_dump = lookup_online("spindly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quail(self):
        html_dump = lookup_online("quail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_southpaw(self):
        html_dump = lookup_online("southpaw")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trampled(self):
        html_dump = lookup_online("trampled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furlough(self):
        html_dump = lookup_online("furlough")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trifling(self):
        html_dump = lookup_online("trifling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repudiation(self):
        html_dump = lookup_online("repudiation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implicit(self):
        html_dump = lookup_online("implicit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recoil(self):
        html_dump = lookup_online("recoil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_provenance(self):
        html_dump = lookup_online("provenance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overzealous(self):
        html_dump = lookup_online("overzealous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhortation(self):
        html_dump = lookup_online("exhortation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implacable(self):
        html_dump = lookup_online("implacable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mumble(self):
        html_dump = lookup_online("mumble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rube(self):
        html_dump = lookup_online("rube")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ennui(self):
        html_dump = lookup_online("ennui")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chastised(self):
        html_dump = lookup_online("chastised")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nous(self):
        html_dump = lookup_online("nous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elope(self):
        html_dump = lookup_online("elope")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conch(self):
        html_dump = lookup_online("conch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nab(self):
        html_dump = lookup_online("nab")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untether(self):
        html_dump = lookup_online("untether")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_septum(self):
        html_dump = lookup_online("septum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redress(self):
        html_dump = lookup_online("redress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weight(self):
        html_dump = lookup_online("weight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_folly(self):
        html_dump = lookup_online("folly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hernia(self):
        html_dump = lookup_online("hernia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brained(self):
        html_dump = lookup_online("brained")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vexed(self):
        html_dump = lookup_online("vexed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riff(self):
        html_dump = lookup_online("riff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maggot(self):
        html_dump = lookup_online("maggot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serfdom(self):
        html_dump = lookup_online("serfdom")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raunchy(self):
        html_dump = lookup_online("raunchy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impressively(self):
        html_dump = lookup_online("impressively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rehearse(self):
        html_dump = lookup_online("rehearse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travail(self):
        html_dump = lookup_online("travail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_propensity(self):
        html_dump = lookup_online("propensity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influx(self):
        html_dump = lookup_online("influx")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opaque(self):
        html_dump = lookup_online("opaque")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shibboleth(self):
        html_dump = lookup_online("shibboleth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scorn(self):
        html_dump = lookup_online("scorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pilfer(self):
        html_dump = lookup_online("pilfer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asphyxiation(self):
        html_dump = lookup_online("asphyxiation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lethargy(self):
        html_dump = lookup_online("lethargy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unequivocal(self):
        html_dump = lookup_online("unequivocal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_converse(self):
        html_dump = lookup_online("converse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parlor(self):
        html_dump = lookup_online("parlor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_latch(self):
        html_dump = lookup_online("latch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expedient(self):
        html_dump = lookup_online("expedient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reimburse(self):
        html_dump = lookup_online("reimburse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bruin(self):
        html_dump = lookup_online("bruin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stepchild(self):
        html_dump = lookup_online("stepchild")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lackey(self):
        html_dump = lookup_online("lackey")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rap(self):
        html_dump = lookup_online("rap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Melanoma(self):
        html_dump = lookup_online("Melanoma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hefty(self):
        html_dump = lookup_online("hefty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_monosomy(self):
        html_dump = lookup_online("monosomy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penitence(self):
        html_dump = lookup_online("penitence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_backlash(self):
        html_dump = lookup_online("backlash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onerous(self):
        html_dump = lookup_online("onerous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ailing(self):
        html_dump = lookup_online("ailing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sternum(self):
        html_dump = lookup_online("sternum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chasten(self):
        html_dump = lookup_online("chasten")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beleaguer(self):
        html_dump = lookup_online("beleaguer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuinely(self):
        html_dump = lookup_online("genuinely")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_piteously(self):
        html_dump = lookup_online("piteously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larceny(self):
        html_dump = lookup_online("larceny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insurmountable(self):
        html_dump = lookup_online("insurmountable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extirpation(self):
        html_dump = lookup_online("extirpation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ventriloquist(self):
        html_dump = lookup_online("ventriloquist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_innocuous(self):
        html_dump = lookup_online("innocuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remedial(self):
        html_dump = lookup_online("remedial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bickering(self):
        html_dump = lookup_online("bickering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unilaterally(self):
        html_dump = lookup_online("unilaterally")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attaboy(self):
        html_dump = lookup_online("attaboy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_continuous(self):
        html_dump = lookup_online("continuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mullet(self):
        html_dump = lookup_online("mullet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimony(self):
        html_dump = lookup_online("acrimony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glib(self):
        html_dump = lookup_online("glib")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fray(self):
        html_dump = lookup_online("fray")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mundane(self):
        html_dump = lookup_online("mundane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haptic(self):
        html_dump = lookup_online("haptic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relenting(self):
        html_dump = lookup_online("relenting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grandiose(self):
        html_dump = lookup_online("grandiose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wacky(self):
        html_dump = lookup_online("wacky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_engender(self):
        html_dump = lookup_online("engender")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nowt(self):
        html_dump = lookup_online("nowt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wispy(self):
        html_dump = lookup_online("wispy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_left(self):
        html_dump = lookup_online("left")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hip(self):
        html_dump = lookup_online("hip")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transience(self):
        html_dump = lookup_online("transience")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parsnips(self):
        html_dump = lookup_online("parsnips")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_work(self):
        html_dump = lookup_online("work")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shoddy(self):
        html_dump = lookup_online("shoddy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ochre(self):
        html_dump = lookup_online("ochre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coerce(self):
        html_dump = lookup_online("coerce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_castigate(self):
        html_dump = lookup_online("castigate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loftiness(self):
        html_dump = lookup_online("loftiness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wand(self):
        html_dump = lookup_online("wand")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barren(self):
        html_dump = lookup_online("barren")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bras(self):
        html_dump = lookup_online("bras")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recondite(self):
        html_dump = lookup_online("recondite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derision(self):
        html_dump = lookup_online("derision")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pelvis(self):
        html_dump = lookup_online("pelvis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacky(self):
        html_dump = lookup_online("tacky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pail(self):
        html_dump = lookup_online("pail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pernicious(self):
        html_dump = lookup_online("pernicious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagrantly(self):
        html_dump = lookup_online("flagrantly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emphysema(self):
        html_dump = lookup_online("emphysema")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_streak(self):
        html_dump = lookup_online("streak")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yttrium(self):
        html_dump = lookup_online("yttrium")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jocular(self):
        html_dump = lookup_online("jocular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstinate(self):
        html_dump = lookup_online("obstinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protruding(self):
        html_dump = lookup_online("protruding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nudge(self):
        html_dump = lookup_online("nudge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apprehensive(self):
        html_dump = lookup_online("apprehensive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squash(self):
        html_dump = lookup_online("squash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_udder(self):
        html_dump = lookup_online("udder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prevalent(self):
        html_dump = lookup_online("prevalent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eal(self):
        html_dump = lookup_online("eal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scholarly(self):
        html_dump = lookup_online("scholarly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rye(self):
        html_dump = lookup_online("rye")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belligerent(self):
        html_dump = lookup_online("belligerent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loquacious(self):
        html_dump = lookup_online("loquacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extracurricular(self):
        html_dump = lookup_online("extracurricular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inextricably(self):
        html_dump = lookup_online("inextricably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_graceful(self):
        html_dump = lookup_online("graceful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sybaritic(self):
        html_dump = lookup_online("sybaritic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broad(self):
        html_dump = lookup_online("broad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inconvenience(self):
        html_dump = lookup_online("inconvenience")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rejoice(self):
        html_dump = lookup_online("rejoice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagrancy(self):
        html_dump = lookup_online("vagrancy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vexatious(self):
        html_dump = lookup_online("vexatious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spook(self):
        html_dump = lookup_online("spook")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glimpsing(self):
        html_dump = lookup_online("glimpsing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wallow(self):
        html_dump = lookup_online("wallow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strife(self):
        html_dump = lookup_online("strife")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tone_deaf(self):
        html_dump = lookup_online("tone-deaf")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_triage(self):
        html_dump = lookup_online("triage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heiress(self):
        html_dump = lookup_online("heiress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slither(self):
        html_dump = lookup_online("slither")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanctity(self):
        html_dump = lookup_online("sanctity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penultimate(self):
        html_dump = lookup_online("penultimate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gimpy(self):
        html_dump = lookup_online("gimpy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neural(self):
        html_dump = lookup_online("neural")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preserve(self):
        html_dump = lookup_online("preserve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prodigious(self):
        html_dump = lookup_online("prodigious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inept(self):
        html_dump = lookup_online("inept")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oedipal(self):
        html_dump = lookup_online("oedipal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coifs(self):
        html_dump = lookup_online("coifs")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_astray(self):
        html_dump = lookup_online("astray")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gawp(self):
        html_dump = lookup_online("gawp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_escarpment(self):
        html_dump = lookup_online("escarpment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimoniously(self):
        html_dump = lookup_online("acrimoniously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muppet(self):
        html_dump = lookup_online("muppet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwavering(self):
        html_dump = lookup_online("unwavering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocal(self):
        html_dump = lookup_online("reciprocal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mediocre(self):
        html_dump = lookup_online("mediocre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jubilee(self):
        html_dump = lookup_online("jubilee")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpable(self):
        html_dump = lookup_online("culpable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obsequious(self):
        html_dump = lookup_online("obsequious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doldrums(self):
        html_dump = lookup_online("doldrums")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeremiad(self):
        html_dump = lookup_online("jeremiad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extortion(self):
        html_dump = lookup_online("extortion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_willy_nilly(self):
        html_dump = lookup_online("willy-nilly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescend(self):
        html_dump = lookup_online("condescend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shingle(self):
        html_dump = lookup_online("shingle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lisp(self):
        html_dump = lookup_online("lisp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turmoil(self):
        html_dump = lookup_online("turmoil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stillbirth(self):
        html_dump = lookup_online("stillbirth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knurled(self):
        html_dump = lookup_online("knurled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foul(self):
        html_dump = lookup_online("foul")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verbose(self):
        html_dump = lookup_online("verbose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pander(self):
        html_dump = lookup_online("pander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eclectic(self):
        html_dump = lookup_online("eclectic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catering(self):
        html_dump = lookup_online("catering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limber(self):
        html_dump = lookup_online("limber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lateral(self):
        html_dump = lookup_online("lateral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gland(self):
        html_dump = lookup_online("gland")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implicated(self):
        html_dump = lookup_online("implicated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilant(self):
        html_dump = lookup_online("vigilant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urea(self):
        html_dump = lookup_online("urea")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thoroughfare(self):
        html_dump = lookup_online("thoroughfare")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slavishly(self):
        html_dump = lookup_online("slavishly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_famine(self):
        html_dump = lookup_online("famine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expedite(self):
        html_dump = lookup_online("expedite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meticulous(self):
        html_dump = lookup_online("meticulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maple(self):
        html_dump = lookup_online("maple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rank(self):
        html_dump = lookup_online("rank")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraption(self):
        html_dump = lookup_online("contraption")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clutter(self):
        html_dump = lookup_online("clutter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_now(self):
        html_dump = lookup_online("now")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grower(self):
        html_dump = lookup_online("grower")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lectern(self):
        html_dump = lookup_online("lectern")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solemnity(self):
        html_dump = lookup_online("solemnity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heckler(self):
        html_dump = lookup_online("heckler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ensue(self):
        html_dump = lookup_online("ensue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_encumber(self):
        html_dump = lookup_online("encumber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swamped(self):
        html_dump = lookup_online("swamped")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_futilely(self):
        html_dump = lookup_online("futilely")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_angler(self):
        html_dump = lookup_online("angler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_medicore(self):
        html_dump = lookup_online("medicore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wean(self):
        html_dump = lookup_online("wean")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fusillade(self):
        html_dump = lookup_online("fusillade")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slender(self):
        html_dump = lookup_online("slender")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kismet(self):
        html_dump = lookup_online("kismet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nunnery(self):
        html_dump = lookup_online("nunnery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_truce(self):
        html_dump = lookup_online("truce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismay(self):
        html_dump = lookup_online("dismay")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intercede(self):
        html_dump = lookup_online("intercede")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accolade(self):
        html_dump = lookup_online("accolade")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ladle(self):
        html_dump = lookup_online("ladle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assess(self):
        html_dump = lookup_online("assess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intricate(self):
        html_dump = lookup_online("intricate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satchel(self):
        html_dump = lookup_online("satchel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virility(self):
        html_dump = lookup_online("virility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rakish(self):
        html_dump = lookup_online("rakish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abscond(self):
        html_dump = lookup_online("abscond")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sartorial(self):
        html_dump = lookup_online("sartorial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venison(self):
        html_dump = lookup_online("venison")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litigate(self):
        html_dump = lookup_online("litigate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagrant(self):
        html_dump = lookup_online("vagrant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_staid(self):
        html_dump = lookup_online("staid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superlative(self):
        html_dump = lookup_online("superlative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dotage(self):
        html_dump = lookup_online("dotage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gobble(self):
        html_dump = lookup_online("gobble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procession(self):
        html_dump = lookup_online("procession")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snarky(self):
        html_dump = lookup_online("snarky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adherence(self):
        html_dump = lookup_online("adherence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fledgling(self):
        html_dump = lookup_online("fledgling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastie(self):
        html_dump = lookup_online("pastie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peril(self):
        html_dump = lookup_online("peril")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inhibitor(self):
        html_dump = lookup_online("inhibitor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shunt(self):
        html_dump = lookup_online("shunt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skirt(self):
        html_dump = lookup_online("skirt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_winging(self):
        html_dump = lookup_online("winging")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brusque(self):
        html_dump = lookup_online("brusque")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stretch(self):
        html_dump = lookup_online("stretch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrawny(self):
        html_dump = lookup_online("scrawny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowery(self):
        html_dump = lookup_online("dowery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dyspraxia(self):
        html_dump = lookup_online("dyspraxia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gallbladder(self):
        html_dump = lookup_online("gallbladder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slapdash(self):
        html_dump = lookup_online("slapdash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_continence(self):
        html_dump = lookup_online("continence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unfazed(self):
        html_dump = lookup_online("unfazed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orneriness(self):
        html_dump = lookup_online("orneriness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enmity(self):
        html_dump = lookup_online("enmity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garrote(self):
        html_dump = lookup_online("garrote")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mussels(self):
        html_dump = lookup_online("mussels")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meek(self):
        html_dump = lookup_online("meek")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sift(self):
        html_dump = lookup_online("sift")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blanket(self):
        html_dump = lookup_online("blanket")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coax(self):
        html_dump = lookup_online("coax")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glaucoma(self):
        html_dump = lookup_online("glaucoma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_charade(self):
        html_dump = lookup_online("charade")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_audacious(self):
        html_dump = lookup_online("audacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disfunctional(self):
        html_dump = lookup_online("disfunctional")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sordid(self):
        html_dump = lookup_online("sordid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_respite(self):
        html_dump = lookup_online("respite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adulterate(self):
        html_dump = lookup_online("adulterate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blinkered(self):
        html_dump = lookup_online("blinkered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trebuchet(self):
        html_dump = lookup_online("trebuchet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quixotically(self):
        html_dump = lookup_online("quixotically")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resolve(self):
        html_dump = lookup_online("resolve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oppressed(self):
        html_dump = lookup_online("oppressed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lesions(self):
        html_dump = lookup_online("lesions")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bough(self):
        html_dump = lookup_online("bough")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hue(self):
        html_dump = lookup_online("hue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_farrier(self):
        html_dump = lookup_online("farrier")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stash(self):
        html_dump = lookup_online("stash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicious(self):
        html_dump = lookup_online("vicious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tortoise(self):
        html_dump = lookup_online("tortoise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewitched(self):
        html_dump = lookup_online("bewitched")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quip(self):
        html_dump = lookup_online("quip")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ancillary(self):
        html_dump = lookup_online("ancillary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congregant(self):
        html_dump = lookup_online("congregant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punter(self):
        html_dump = lookup_online("punter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wreathe(self):
        html_dump = lookup_online("wreathe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_durian(self):
        html_dump = lookup_online("durian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spigot(self):
        html_dump = lookup_online("spigot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patch(self):
        html_dump = lookup_online("patch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diligent(self):
        html_dump = lookup_online("diligent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_filial(self):
        html_dump = lookup_online("filial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implacably(self):
        html_dump = lookup_online("implacably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prediction(self):
        html_dump = lookup_online("prediction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rabies(self):
        html_dump = lookup_online("rabies")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ado(self):
        html_dump = lookup_online("ado")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudence(self):
        html_dump = lookup_online("prudence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vista(self):
        html_dump = lookup_online("vista")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benignly(self):
        html_dump = lookup_online("benignly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hog(self):
        html_dump = lookup_online("hog")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tempest(self):
        html_dump = lookup_online("tempest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vim(self):
        html_dump = lookup_online("vim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mead(self):
        html_dump = lookup_online("mead")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spendthrift(self):
        html_dump = lookup_online("spendthrift")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_panopticon(self):
        html_dump = lookup_online("panopticon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaggle(self):
        html_dump = lookup_online("gaggle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluminous(self):
        html_dump = lookup_online("voluminous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outline(self):
        html_dump = lookup_online("outline")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wharve(self):
        html_dump = lookup_online("wharve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expediency(self):
        html_dump = lookup_online("expediency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trivial(self):
        html_dump = lookup_online("trivial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bluff(self):
        html_dump = lookup_online("bluff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forlorn(self):
        html_dump = lookup_online("forlorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agrarian(self):
        html_dump = lookup_online("agrarian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tinnitus(self):
        html_dump = lookup_online("tinnitus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exult(self):
        html_dump = lookup_online("exult")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ornate(self):
        html_dump = lookup_online("ornate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peon(self):
        html_dump = lookup_online("peon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unhinged(self):
        html_dump = lookup_online("unhinged")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_selfishness(self):
        html_dump = lookup_online("selfishness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precarity(self):
        html_dump = lookup_online("precarity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetrator(self):
        html_dump = lookup_online("perpetrator")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luminary(self):
        html_dump = lookup_online("luminary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convex(self):
        html_dump = lookup_online("convex")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_begat(self):
        html_dump = lookup_online("begat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indolence(self):
        html_dump = lookup_online("indolence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vying(self):
        html_dump = lookup_online("vying")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_husbandry(self):
        html_dump = lookup_online("husbandry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quadriplegic(self):
        html_dump = lookup_online("quadriplegic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquaint(self):
        html_dump = lookup_online("acquaint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rattle(self):
        html_dump = lookup_online("rattle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corporeal(self):
        html_dump = lookup_online("corporeal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artifice(self):
        html_dump = lookup_online("artifice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crooked(self):
        html_dump = lookup_online("crooked")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eaves(self):
        html_dump = lookup_online("eaves")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sentient(self):
        html_dump = lookup_online("sentient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_instigate(self):
        html_dump = lookup_online("instigate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wizened(self):
        html_dump = lookup_online("wizened")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rising(self):
        html_dump = lookup_online("rising")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inimical(self):
        html_dump = lookup_online("inimical")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acumen(self):
        html_dump = lookup_online("acumen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discontent(self):
        html_dump = lookup_online("discontent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exuberance(self):
        html_dump = lookup_online("exuberance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discrepancy(self):
        html_dump = lookup_online("discrepancy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solicitor(self):
        html_dump = lookup_online("solicitor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parochialism(self):
        html_dump = lookup_online("parochialism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adulation(self):
        html_dump = lookup_online("adulation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Kowloon(self):
        html_dump = lookup_online("Kowloon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_warring(self):
        html_dump = lookup_online("warring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjunction(self):
        html_dump = lookup_online("conjunction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arcane(self):
        html_dump = lookup_online("arcane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refurbish(self):
        html_dump = lookup_online("refurbish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_negligent(self):
        html_dump = lookup_online("negligent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whilist(self):
        html_dump = lookup_online("whilist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lien(self):
        html_dump = lookup_online("lien")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_watercress(self):
        html_dump = lookup_online("watercress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dash(self):
        html_dump = lookup_online("dash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cherish(self):
        html_dump = lookup_online("cherish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indignation(self):
        html_dump = lookup_online("indignation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loft(self):
        html_dump = lookup_online("loft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disregard(self):
        html_dump = lookup_online("disregard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furor(self):
        html_dump = lookup_online("furor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_betrothed(self):
        html_dump = lookup_online("betrothed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheer(self):
        html_dump = lookup_online("sheer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maw(self):
        html_dump = lookup_online("maw")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influenza(self):
        html_dump = lookup_online("influenza")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affectation(self):
        html_dump = lookup_online("affectation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_précis(self):
        html_dump = lookup_online("précis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_freight(self):
        html_dump = lookup_online("freight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frigid(self):
        html_dump = lookup_online("frigid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remorse(self):
        html_dump = lookup_online("remorse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_headstrong(self):
        html_dump = lookup_online("headstrong")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bobbin(self):
        html_dump = lookup_online("bobbin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wonk(self):
        html_dump = lookup_online("wonk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poaching(self):
        html_dump = lookup_online("poaching")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eldritch(self):
        html_dump = lookup_online("eldritch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tomcat(self):
        html_dump = lookup_online("tomcat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranny(self):
        html_dump = lookup_online("tranny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thimble(self):
        html_dump = lookup_online("thimble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeremiads(self):
        html_dump = lookup_online("jeremiads")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quarry(self):
        html_dump = lookup_online("quarry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrepid(self):
        html_dump = lookup_online("intrepid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jerk(self):
        html_dump = lookup_online("jerk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salutatory(self):
        html_dump = lookup_online("salutatory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feud(self):
        html_dump = lookup_online("feud")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_progenitor(self):
        html_dump = lookup_online("progenitor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suppurate(self):
        html_dump = lookup_online("suppurate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duress(self):
        html_dump = lookup_online("duress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proximal(self):
        html_dump = lookup_online("proximal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_risible(self):
        html_dump = lookup_online("risible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mendacity(self):
        html_dump = lookup_online("mendacity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cole(self):
        html_dump = lookup_online("cole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dignified(self):
        html_dump = lookup_online("dignified")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_while(self):
        html_dump = lookup_online("while")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sap(self):
        html_dump = lookup_online("sap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abound(self):
        html_dump = lookup_online("abound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belie(self):
        html_dump = lookup_online("belie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diminishing(self):
        html_dump = lookup_online("diminishing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mutiny(self):
        html_dump = lookup_online("mutiny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_throb(self):
        html_dump = lookup_online("throb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bareness(self):
        html_dump = lookup_online("bareness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stow(self):
        html_dump = lookup_online("stow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eddying(self):
        html_dump = lookup_online("eddying")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dory(self):
        html_dump = lookup_online("dory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distract(self):
        html_dump = lookup_online("distract")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_for(self):
        html_dump = lookup_online("for")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stultify(self):
        html_dump = lookup_online("stultify")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detractor(self):
        html_dump = lookup_online("detractor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_magpie(self):
        html_dump = lookup_online("magpie")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigenous(self):
        html_dump = lookup_online("indigenous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hereditary(self):
        html_dump = lookup_online("hereditary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscegenation(self):
        html_dump = lookup_online("miscegenation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splinter(self):
        html_dump = lookup_online("splinter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curt(self):
        html_dump = lookup_online("curt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_casserole(self):
        html_dump = lookup_online("casserole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accord(self):
        html_dump = lookup_online("accord")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corollary(self):
        html_dump = lookup_online("corollary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excruciating(self):
        html_dump = lookup_online("excruciating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wistfully(self):
        html_dump = lookup_online("wistfully")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despondence(self):
        html_dump = lookup_online("despondence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_age(self):
        html_dump = lookup_online("age")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diverge(self):
        html_dump = lookup_online("diverge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferment(self):
        html_dump = lookup_online("ferment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fetch(self):
        html_dump = lookup_online("fetch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_facsimile(self):
        html_dump = lookup_online("facsimile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maim(self):
        html_dump = lookup_online("maim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mercantile(self):
        html_dump = lookup_online("mercantile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tendentious(self):
        html_dump = lookup_online("tendentious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hepatitis(self):
        html_dump = lookup_online("hepatitis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fret(self):
        html_dump = lookup_online("fret")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admonition(self):
        html_dump = lookup_online("admonition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ingenuity(self):
        html_dump = lookup_online("ingenuity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carb(self):
        html_dump = lookup_online("carb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brisant(self):
        html_dump = lookup_online("brisant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutters(self):
        html_dump = lookup_online("gutters")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spat(self):
        html_dump = lookup_online("spat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_testing(self):
        html_dump = lookup_online("testing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apathy(self):
        html_dump = lookup_online("apathy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trickster(self):
        html_dump = lookup_online("trickster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furtive(self):
        html_dump = lookup_online("furtive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rack(self):
        html_dump = lookup_online("rack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lime(self):
        html_dump = lookup_online("lime")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tawdriness(self):
        html_dump = lookup_online("tawdriness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limestone(self):
        html_dump = lookup_online("limestone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brim(self):
        html_dump = lookup_online("brim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_berth(self):
        html_dump = lookup_online("berth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bacillus(self):
        html_dump = lookup_online("bacillus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blunder(self):
        html_dump = lookup_online("blunder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stowaway(self):
        html_dump = lookup_online("stowaway")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coy(self):
        html_dump = lookup_online("coy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_porridge(self):
        html_dump = lookup_online("porridge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puttering(self):
        html_dump = lookup_online("puttering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unencumbered(self):
        html_dump = lookup_online("unencumbered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_narc(self):
        html_dump = lookup_online("narc")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slander(self):
        html_dump = lookup_online("slander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_homicide(self):
        html_dump = lookup_online("homicide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rued(self):
        html_dump = lookup_online("rued")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vested(self):
        html_dump = lookup_online("vested")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immaculate(self):
        html_dump = lookup_online("immaculate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulceration(self):
        html_dump = lookup_online("ulceration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lumber(self):
        html_dump = lookup_online("lumber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_containable(self):
        html_dump = lookup_online("containable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snag(self):
        html_dump = lookup_online("snag")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forfeit(self):
        html_dump = lookup_online("forfeit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inordinate(self):
        html_dump = lookup_online("inordinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afterbirth(self):
        html_dump = lookup_online("afterbirth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deter(self):
        html_dump = lookup_online("deter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adorn(self):
        html_dump = lookup_online("adorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adversarial(self):
        html_dump = lookup_online("adversarial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parchment(self):
        html_dump = lookup_online("parchment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_demeanor(self):
        html_dump = lookup_online("demeanor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_damp(self):
        html_dump = lookup_online("damp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_efficacy(self):
        html_dump = lookup_online("efficacy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garment(self):
        html_dump = lookup_online("garment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insofar(self):
        html_dump = lookup_online("insofar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_triplet(self):
        html_dump = lookup_online("triplet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_straddle(self):
        html_dump = lookup_online("straddle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beseech(self):
        html_dump = lookup_online("beseech")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frugally(self):
        html_dump = lookup_online("frugally")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hifalutin(self):
        html_dump = lookup_online("hifalutin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alloy(self):
        html_dump = lookup_online("alloy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gregarious(self):
        html_dump = lookup_online("gregarious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pontificate(self):
        html_dump = lookup_online("pontificate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impel(self):
        html_dump = lookup_online("impel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amusing(self):
        html_dump = lookup_online("amusing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alteration(self):
        html_dump = lookup_online("alteration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hew(self):
        html_dump = lookup_online("hew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convivial(self):
        html_dump = lookup_online("convivial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_docile(self):
        html_dump = lookup_online("docile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pewter(self):
        html_dump = lookup_online("pewter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manila(self):
        html_dump = lookup_online("manila")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notional(self):
        html_dump = lookup_online("notional")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeer(self):
        html_dump = lookup_online("jeer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_figuratively(self):
        html_dump = lookup_online("figuratively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rut(self):
        html_dump = lookup_online("rut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preclude(self):
        html_dump = lookup_online("preclude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hussle(self):
        html_dump = lookup_online("hussle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assent(self):
        html_dump = lookup_online("assent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unadorned(self):
        html_dump = lookup_online("unadorned")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gorge(self):
        html_dump = lookup_online("gorge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appropriate(self):
        html_dump = lookup_online("appropriate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coo(self):
        html_dump = lookup_online("coo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minnow(self):
        html_dump = lookup_online("minnow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carping(self):
        html_dump = lookup_online("carping")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chad(self):
        html_dump = lookup_online("chad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowel(self):
        html_dump = lookup_online("dowel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auger(self):
        html_dump = lookup_online("auger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prenuptial(self):
        html_dump = lookup_online("prenuptial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tic(self):
        html_dump = lookup_online("tic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malleability(self):
        html_dump = lookup_online("malleability")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shagging(self):
        html_dump = lookup_online("shagging")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discombobulated(self):
        html_dump = lookup_online("discombobulated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lavish(self):
        html_dump = lookup_online("lavish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vehemently(self):
        html_dump = lookup_online("vehemently")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unfettered(self):
        html_dump = lookup_online("unfettered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onwards(self):
        html_dump = lookup_online("onwards")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_racketeer(self):
        html_dump = lookup_online("racketeer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chide(self):
        html_dump = lookup_online("chide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prowess(self):
        html_dump = lookup_online("prowess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hump(self):
        html_dump = lookup_online("hump")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_purge(self):
        html_dump = lookup_online("purge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diatribe(self):
        html_dump = lookup_online("diatribe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_digress(self):
        html_dump = lookup_online("digress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scaffold(self):
        html_dump = lookup_online("scaffold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renunciations(self):
        html_dump = lookup_online("renunciations")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elated(self):
        html_dump = lookup_online("elated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marshal(self):
        html_dump = lookup_online("marshal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snivelling(self):
        html_dump = lookup_online("snivelling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strap(self):
        html_dump = lookup_online("strap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sucker(self):
        html_dump = lookup_online("sucker")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renunciation(self):
        html_dump = lookup_online("renunciation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_visceral(self):
        html_dump = lookup_online("visceral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sound(self):
        html_dump = lookup_online("sound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceivably(self):
        html_dump = lookup_online("conceivably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corduroy(self):
        html_dump = lookup_online("corduroy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frisky(self):
        html_dump = lookup_online("frisky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deprivation(self):
        html_dump = lookup_online("deprivation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proprietor(self):
        html_dump = lookup_online("proprietor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contiguous(self):
        html_dump = lookup_online("contiguous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disappointing(self):
        html_dump = lookup_online("disappointing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gush(self):
        html_dump = lookup_online("gush")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impish(self):
        html_dump = lookup_online("impish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_residence(self):
        html_dump = lookup_online("residence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unruffled(self):
        html_dump = lookup_online("unruffled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carnal(self):
        html_dump = lookup_online("carnal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regency(self):
        html_dump = lookup_online("regency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_churlish(self):
        html_dump = lookup_online("churlish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulchritudinous(self):
        html_dump = lookup_online("pulchritudinous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beech(self):
        html_dump = lookup_online("beech")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alder(self):
        html_dump = lookup_online("alder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quote(self):
        html_dump = lookup_online("quote")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confound(self):
        html_dump = lookup_online("confound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pitilessly(self):
        html_dump = lookup_online("pitilessly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hick(self):
        html_dump = lookup_online("hick")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excruciatingly(self):
        html_dump = lookup_online("excruciatingly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punitive(self):
        html_dump = lookup_online("punitive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patter(self):
        html_dump = lookup_online("patter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_darkness(self):
        html_dump = lookup_online("darkness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succumb(self):
        html_dump = lookup_online("succumb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lend(self):
        html_dump = lookup_online("lend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affinity(self):
        html_dump = lookup_online("affinity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supposition(self):
        html_dump = lookup_online("supposition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcers(self):
        html_dump = lookup_online("ulcers")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notch(self):
        html_dump = lookup_online("notch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perspicaciously(self):
        html_dump = lookup_online("perspicaciously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exegesis(self):
        html_dump = lookup_online("exegesis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chubby(self):
        html_dump = lookup_online("chubby")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenacious(self):
        html_dump = lookup_online("tenacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_console(self):
        html_dump = lookup_online("console")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dispatch(self):
        html_dump = lookup_online("dispatch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marred(self):
        html_dump = lookup_online("marred")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unassailable(self):
        html_dump = lookup_online("unassailable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissuade(self):
        html_dump = lookup_online("dissuade")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjure(self):
        html_dump = lookup_online("conjure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sagacity(self):
        html_dump = lookup_online("sagacity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reed(self):
        html_dump = lookup_online("reed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plight(self):
        html_dump = lookup_online("plight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taciturn(self):
        html_dump = lookup_online("taciturn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brass(self):
        html_dump = lookup_online("brass")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proselyte(self):
        html_dump = lookup_online("proselyte")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cringe(self):
        html_dump = lookup_online("cringe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morsel(self):
        html_dump = lookup_online("morsel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squeal(self):
        html_dump = lookup_online("squeal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggravating(self):
        html_dump = lookup_online("aggravating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intermittent(self):
        html_dump = lookup_online("intermittent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mezzanine(self):
        html_dump = lookup_online("mezzanine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meekness(self):
        html_dump = lookup_online("meekness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawn(self):
        html_dump = lookup_online("brawn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crufty(self):
        html_dump = lookup_online("crufty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coven(self):
        html_dump = lookup_online("coven")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jolt(self):
        html_dump = lookup_online("jolt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparage(self):
        html_dump = lookup_online("disparage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parlance(self):
        html_dump = lookup_online("parlance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confine(self):
        html_dump = lookup_online("confine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distributed(self):
        html_dump = lookup_online("distributed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leonine(self):
        html_dump = lookup_online("leonine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spain(self):
        html_dump = lookup_online("spain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slyly(self):
        html_dump = lookup_online("slyly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seminal(self):
        html_dump = lookup_online("seminal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpability(self):
        html_dump = lookup_online("culpability")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mediocrity(self):
        html_dump = lookup_online("mediocrity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auspice(self):
        html_dump = lookup_online("auspice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grandee(self):
        html_dump = lookup_online("grandee")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frankness(self):
        html_dump = lookup_online("frankness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wily(self):
        html_dump = lookup_online("wily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gored(self):
        html_dump = lookup_online("gored")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plonk(self):
        html_dump = lookup_online("plonk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbridled(self):
        html_dump = lookup_online("unbridled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spunk(self):
        html_dump = lookup_online("spunk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rile(self):
        html_dump = lookup_online("rile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_titter(self):
        html_dump = lookup_online("titter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_writhe(self):
        html_dump = lookup_online("writhe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crummy(self):
        html_dump = lookup_online("crummy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sob(self):
        html_dump = lookup_online("sob")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remedy(self):
        html_dump = lookup_online("remedy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparaging(self):
        html_dump = lookup_online("disparaging")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_keef(self):
        html_dump = lookup_online("keef")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lint(self):
        html_dump = lookup_online("lint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relieved(self):
        html_dump = lookup_online("relieved")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tits(self):
        html_dump = lookup_online("tits")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sorority(self):
        html_dump = lookup_online("sorority")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oleander(self):
        html_dump = lookup_online("oleander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mulberry(self):
        html_dump = lookup_online("mulberry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incredulity(self):
        html_dump = lookup_online("incredulity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boon(self):
        html_dump = lookup_online("boon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_freckle(self):
        html_dump = lookup_online("freckle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beget(self):
        html_dump = lookup_online("beget")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curtail(self):
        html_dump = lookup_online("curtail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sack(self):
        html_dump = lookup_online("sack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amalgamation(self):
        html_dump = lookup_online("amalgamation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slandering(self):
        html_dump = lookup_online("slandering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malt(self):
        html_dump = lookup_online("malt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allusive(self):
        html_dump = lookup_online("allusive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mewl(self):
        html_dump = lookup_online("mewl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tinny(self):
        html_dump = lookup_online("tinny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curl(self):
        html_dump = lookup_online("curl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liability(self):
        html_dump = lookup_online("liability")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consort(self):
        html_dump = lookup_online("consort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tar(self):
        html_dump = lookup_online("tar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vantage(self):
        html_dump = lookup_online("vantage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moped(self):
        html_dump = lookup_online("moped")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sludge(self):
        html_dump = lookup_online("sludge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gurney(self):
        html_dump = lookup_online("gurney")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nascent(self):
        html_dump = lookup_online("nascent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fender(self):
        html_dump = lookup_online("fender")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunker(self):
        html_dump = lookup_online("hunker")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adroitness(self):
        html_dump = lookup_online("adroitness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litmus(self):
        html_dump = lookup_online("litmus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salmon(self):
        html_dump = lookup_online("salmon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jessamine(self):
        html_dump = lookup_online("jessamine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gnarly(self):
        html_dump = lookup_online("gnarly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verge(self):
        html_dump = lookup_online("verge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_destitute(self):
        html_dump = lookup_online("destitute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refrain(self):
        html_dump = lookup_online("refrain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derange(self):
        html_dump = lookup_online("derange")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equestrian(self):
        html_dump = lookup_online("equestrian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grovel(self):
        html_dump = lookup_online("grovel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_articulate(self):
        html_dump = lookup_online("articulate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilance(self):
        html_dump = lookup_online("vigilance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dumb(self):
        html_dump = lookup_online("dumb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tutelage(self):
        html_dump = lookup_online("tutelage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toehold(self):
        html_dump = lookup_online("toehold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapacious(self):
        html_dump = lookup_online("rapacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puppet(self):
        html_dump = lookup_online("puppet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brute(self):
        html_dump = lookup_online("brute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_briskly(self):
        html_dump = lookup_online("briskly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_guile(self):
        html_dump = lookup_online("guile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chestnut(self):
        html_dump = lookup_online("chestnut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tort(self):
        html_dump = lookup_online("tort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frenetic(self):
        html_dump = lookup_online("frenetic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shambles(self):
        html_dump = lookup_online("shambles")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yoke(self):
        html_dump = lookup_online("yoke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lentil(self):
        html_dump = lookup_online("lentil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clobber(self):
        html_dump = lookup_online("clobber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appendix(self):
        html_dump = lookup_online("appendix")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conspicuous(self):
        html_dump = lookup_online("conspicuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_covet(self):
        html_dump = lookup_online("covet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repossess(self):
        html_dump = lookup_online("repossess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_baffle(self):
        html_dump = lookup_online("baffle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_henchman(self):
        html_dump = lookup_online("henchman")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regurgitate(self):
        html_dump = lookup_online("regurgitate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fabricated(self):
        html_dump = lookup_online("fabricated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leatherette(self):
        html_dump = lookup_online("leatherette")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inauspicious(self):
        html_dump = lookup_online("inauspicious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chattel(self):
        html_dump = lookup_online("chattel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imbibe(self):
        html_dump = lookup_online("imbibe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unclench(self):
        html_dump = lookup_online("unclench")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incidence(self):
        html_dump = lookup_online("incidence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flaky(self):
        html_dump = lookup_online("flaky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wager(self):
        html_dump = lookup_online("wager")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curdled(self):
        html_dump = lookup_online("curdled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insipid(self):
        html_dump = lookup_online("insipid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presumptuousness(self):
        html_dump = lookup_online("presumptuousness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menacingly(self):
        html_dump = lookup_online("menacingly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lousy(self):
        html_dump = lookup_online("lousy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_metonymy(self):
        html_dump = lookup_online("metonymy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parsimonious(self):
        html_dump = lookup_online("parsimonious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_denounce(self):
        html_dump = lookup_online("denounce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exert(self):
        html_dump = lookup_online("exert")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bumbling(self):
        html_dump = lookup_online("bumbling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whim(self):
        html_dump = lookup_online("whim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transgression(self):
        html_dump = lookup_online("transgression")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanction(self):
        html_dump = lookup_online("sanction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_theory(self):
        html_dump = lookup_online("theory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_faciliate(self):
        html_dump = lookup_online("faciliate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fugue(self):
        html_dump = lookup_online("fugue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bronchitis(self):
        html_dump = lookup_online("bronchitis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cockeyed(self):
        html_dump = lookup_online("cockeyed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pallor(self):
        html_dump = lookup_online("pallor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cliche(self):
        html_dump = lookup_online("cliche")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fleece(self):
        html_dump = lookup_online("fleece")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embellished(self):
        html_dump = lookup_online("embellished")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evokes(self):
        html_dump = lookup_online("evokes")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hedge(self):
        html_dump = lookup_online("hedge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pique(self):
        html_dump = lookup_online("pique")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_topiary(self):
        html_dump = lookup_online("topiary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slack(self):
        html_dump = lookup_online("slack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prune(self):
        html_dump = lookup_online("prune")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bleak(self):
        html_dump = lookup_online("bleak")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oxbow(self):
        html_dump = lookup_online("oxbow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coitus(self):
        html_dump = lookup_online("coitus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lightning(self):
        html_dump = lookup_online("lightning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morose(self):
        html_dump = lookup_online("morose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assiduous(self):
        html_dump = lookup_online("assiduous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_legitimate(self):
        html_dump = lookup_online("legitimate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nether(self):
        html_dump = lookup_online("nether")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_valiant(self):
        html_dump = lookup_online("valiant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fissure(self):
        html_dump = lookup_online("fissure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaded(self):
        html_dump = lookup_online("jaded")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_demean(self):
        html_dump = lookup_online("demean")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cairns(self):
        html_dump = lookup_online("cairns")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zest(self):
        html_dump = lookup_online("zest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preen(self):
        html_dump = lookup_online("preen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amanuensis(self):
        html_dump = lookup_online("amanuensis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raucous(self):
        html_dump = lookup_online("raucous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insatiable(self):
        html_dump = lookup_online("insatiable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litigious(self):
        html_dump = lookup_online("litigious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucre(self):
        html_dump = lookup_online("lucre")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sunset(self):
        html_dump = lookup_online("sunset")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abet(self):
        html_dump = lookup_online("abet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quench(self):
        html_dump = lookup_online("quench")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grueling(self):
        html_dump = lookup_online("grueling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcerate(self):
        html_dump = lookup_online("ulcerate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vogue(self):
        html_dump = lookup_online("vogue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fad(self):
        html_dump = lookup_online("fad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benign(self):
        html_dump = lookup_online("benign")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grout(self):
        html_dump = lookup_online("grout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lard(self):
        html_dump = lookup_online("lard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_labour(self):
        html_dump = lookup_online("labour")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barnacle(self):
        html_dump = lookup_online("barnacle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agitate(self):
        html_dump = lookup_online("agitate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soldier(self):
        html_dump = lookup_online("soldier")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infamous(self):
        html_dump = lookup_online("infamous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evince(self):
        html_dump = lookup_online("evince")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pungent(self):
        html_dump = lookup_online("pungent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bereft(self):
        html_dump = lookup_online("bereft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trailing(self):
        html_dump = lookup_online("trailing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_husky(self):
        html_dump = lookup_online("husky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miff(self):
        html_dump = lookup_online("miff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ointment(self):
        html_dump = lookup_online("ointment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disrupt(self):
        html_dump = lookup_online("disrupt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_later(self):
        html_dump = lookup_online("later")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gossamer(self):
        html_dump = lookup_online("gossamer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_courtship(self):
        html_dump = lookup_online("courtship")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appall(self):
        html_dump = lookup_online("appall")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wither(self):
        html_dump = lookup_online("wither")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despatch(self):
        html_dump = lookup_online("despatch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stooge(self):
        html_dump = lookup_online("stooge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arboretum(self):
        html_dump = lookup_online("arboretum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infraction(self):
        html_dump = lookup_online("infraction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flout(self):
        html_dump = lookup_online("flout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bunion(self):
        html_dump = lookup_online("bunion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_promiscuity(self):
        html_dump = lookup_online("promiscuity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraying(self):
        html_dump = lookup_online("fraying")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irate(self):
        html_dump = lookup_online("irate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loggerhead(self):
        html_dump = lookup_online("loggerhead")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strive(self):
        html_dump = lookup_online("strive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loony(self):
        html_dump = lookup_online("loony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midden(self):
        html_dump = lookup_online("midden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desultorily(self):
        html_dump = lookup_online("desultorily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_motley(self):
        html_dump = lookup_online("motley")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longing(self):
        html_dump = lookup_online("longing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bifurcation(self):
        html_dump = lookup_online("bifurcation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_groan(self):
        html_dump = lookup_online("groan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bile(self):
        html_dump = lookup_online("bile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pheasant(self):
        html_dump = lookup_online("pheasant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afoul(self):
        html_dump = lookup_online("afoul")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despondency(self):
        html_dump = lookup_online("despondency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tetanus(self):
        html_dump = lookup_online("tetanus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetuity(self):
        html_dump = lookup_online("perpetuity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pilfering(self):
        html_dump = lookup_online("pilfering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_substitute(self):
        html_dump = lookup_online("substitute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prowl(self):
        html_dump = lookup_online("prowl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grue(self):
        html_dump = lookup_online("grue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bole(self):
        html_dump = lookup_online("bole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duende(self):
        html_dump = lookup_online("duende")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_token(self):
        html_dump = lookup_online("token")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescension(self):
        html_dump = lookup_online("condescension")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indenture(self):
        html_dump = lookup_online("indenture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sham(self):
        html_dump = lookup_online("sham")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effluent(self):
        html_dump = lookup_online("effluent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infantry(self):
        html_dump = lookup_online("infantry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nematode(self):
        html_dump = lookup_online("nematode")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alopecia(self):
        html_dump = lookup_online("alopecia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bop(self):
        html_dump = lookup_online("bop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gamin(self):
        html_dump = lookup_online("gamin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relent(self):
        html_dump = lookup_online("relent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiddly(self):
        html_dump = lookup_online("fiddly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protein(self):
        html_dump = lookup_online("protein")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trailblazing(self):
        html_dump = lookup_online("trailblazing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exigency(self):
        html_dump = lookup_online("exigency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perilous(self):
        html_dump = lookup_online("perilous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gimp(self):
        html_dump = lookup_online("gimp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipice(self):
        html_dump = lookup_online("precipice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imperil(self):
        html_dump = lookup_online("imperil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quagmire(self):
        html_dump = lookup_online("quagmire")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cull(self):
        html_dump = lookup_online("cull")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litigator(self):
        html_dump = lookup_online("litigator")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indeterminate(self):
        html_dump = lookup_online("indeterminate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncharitable(self):
        html_dump = lookup_online("uncharitable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trope(self):
        html_dump = lookup_online("trope")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_roundel(self):
        html_dump = lookup_online("roundel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inveterate(self):
        html_dump = lookup_online("inveterate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heedlessly(self):
        html_dump = lookup_online("heedlessly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_littoral(self):
        html_dump = lookup_online("littoral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spuriously(self):
        html_dump = lookup_online("spuriously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_readability(self):
        html_dump = lookup_online("readability")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sunder(self):
        html_dump = lookup_online("sunder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curbing(self):
        html_dump = lookup_online("curbing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumes(self):
        html_dump = lookup_online("fumes")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congenital(self):
        html_dump = lookup_online("congenital")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumination(self):
        html_dump = lookup_online("rumination")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drape(self):
        html_dump = lookup_online("drape")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fulguration(self):
        html_dump = lookup_online("fulguration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pancreatitis(self):
        html_dump = lookup_online("pancreatitis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repugnance(self):
        html_dump = lookup_online("repugnance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bushel(self):
        html_dump = lookup_online("bushel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wayward(self):
        html_dump = lookup_online("wayward")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedulity(self):
        html_dump = lookup_online("sedulity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elision(self):
        html_dump = lookup_online("elision")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paltry(self):
        html_dump = lookup_online("paltry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_friar(self):
        html_dump = lookup_online("friar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flue(self):
        html_dump = lookup_online("flue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fluff(self):
        html_dump = lookup_online("fluff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deciduous(self):
        html_dump = lookup_online("deciduous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_invalid(self):
        html_dump = lookup_online("invalid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrimp(self):
        html_dump = lookup_online("shrimp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vapor(self):
        html_dump = lookup_online("vapor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vacation(self):
        html_dump = lookup_online("vacation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gritty(self):
        html_dump = lookup_online("gritty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crony(self):
        html_dump = lookup_online("crony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yarn(self):
        html_dump = lookup_online("yarn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gypsy(self):
        html_dump = lookup_online("gypsy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sulk(self):
        html_dump = lookup_online("sulk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eager(self):
        html_dump = lookup_online("eager")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savvy(self):
        html_dump = lookup_online("savvy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thrush(self):
        html_dump = lookup_online("thrush")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_famished(self):
        html_dump = lookup_online("famished")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wayfare(self):
        html_dump = lookup_online("wayfare")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bargain(self):
        html_dump = lookup_online("bargain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sinewy(self):
        html_dump = lookup_online("sinewy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexplicably(self):
        html_dump = lookup_online("inexplicably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beset(self):
        html_dump = lookup_online("beset")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unhinge(self):
        html_dump = lookup_online("unhinge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immane(self):
        html_dump = lookup_online("immane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eking(self):
        html_dump = lookup_online("eking")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanctimonious(self):
        html_dump = lookup_online("sanctimonious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_speakeasy(self):
        html_dump = lookup_online("speakeasy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raspy(self):
        html_dump = lookup_online("raspy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cattle(self):
        html_dump = lookup_online("cattle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marmite(self):
        html_dump = lookup_online("marmite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_screwup(self):
        html_dump = lookup_online("screwup")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckless(self):
        html_dump = lookup_online("reckless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thicket(self):
        html_dump = lookup_online("thicket")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_halter(self):
        html_dump = lookup_online("halter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goldilocks(self):
        html_dump = lookup_online("goldilocks")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yeoman(self):
        html_dump = lookup_online("yeoman")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gumption(self):
        html_dump = lookup_online("gumption")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harmonious(self):
        html_dump = lookup_online("harmonious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_guest(self):
        html_dump = lookup_online("guest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_butler(self):
        html_dump = lookup_online("butler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenacity(self):
        html_dump = lookup_online("tenacity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salacious(self):
        html_dump = lookup_online("salacious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sentience(self):
        html_dump = lookup_online("sentience")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peddle(self):
        html_dump = lookup_online("peddle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disbar(self):
        html_dump = lookup_online("disbar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equanimity(self):
        html_dump = lookup_online("equanimity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catamite(self):
        html_dump = lookup_online("catamite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taper(self):
        html_dump = lookup_online("taper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veneer(self):
        html_dump = lookup_online("veneer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effect(self):
        html_dump = lookup_online("effect")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hazmat(self):
        html_dump = lookup_online("hazmat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sobriquet(self):
        html_dump = lookup_online("sobriquet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_integrity(self):
        html_dump = lookup_online("integrity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avarice(self):
        html_dump = lookup_online("avarice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abate(self):
        html_dump = lookup_online("abate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salubrious(self):
        html_dump = lookup_online("salubrious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jocose(self):
        html_dump = lookup_online("jocose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dilation(self):
        html_dump = lookup_online("dilation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lemma(self):
        html_dump = lookup_online("lemma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_denigrate(self):
        html_dump = lookup_online("denigrate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beet(self):
        html_dump = lookup_online("beet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savour(self):
        html_dump = lookup_online("savour")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_martyr(self):
        html_dump = lookup_online("martyr")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laryngitis(self):
        html_dump = lookup_online("laryngitis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ignominious(self):
        html_dump = lookup_online("ignominious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_senile(self):
        html_dump = lookup_online("senile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intervention(self):
        html_dump = lookup_online("intervention")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embezzlement(self):
        html_dump = lookup_online("embezzlement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bitters(self):
        html_dump = lookup_online("bitters")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vivisection(self):
        html_dump = lookup_online("vivisection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frothy(self):
        html_dump = lookup_online("frothy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amity(self):
        html_dump = lookup_online("amity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hussy(self):
        html_dump = lookup_online("hussy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virile(self):
        html_dump = lookup_online("virile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snoop(self):
        html_dump = lookup_online("snoop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abeyance(self):
        html_dump = lookup_online("abeyance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raddled(self):
        html_dump = lookup_online("raddled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vacuous(self):
        html_dump = lookup_online("vacuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmuring(self):
        html_dump = lookup_online("murmuring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kindling(self):
        html_dump = lookup_online("kindling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sweep(self):
        html_dump = lookup_online("sweep")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defect(self):
        html_dump = lookup_online("defect")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skid(self):
        html_dump = lookup_online("skid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interweave(self):
        html_dump = lookup_online("interweave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beading(self):
        html_dump = lookup_online("beading")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_egotism(self):
        html_dump = lookup_online("egotism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aerated(self):
        html_dump = lookup_online("aerated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_con(self):
        html_dump = lookup_online("con")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commence(self):
        html_dump = lookup_online("commence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_care(self):
        html_dump = lookup_online("care")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genteel(self):
        html_dump = lookup_online("genteel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disavow(self):
        html_dump = lookup_online("disavow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjecture(self):
        html_dump = lookup_online("conjecture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skewer(self):
        html_dump = lookup_online("skewer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consolidate(self):
        html_dump = lookup_online("consolidate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remit(self):
        html_dump = lookup_online("remit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aging(self):
        html_dump = lookup_online("aging")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_badger(self):
        html_dump = lookup_online("badger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangible(self):
        html_dump = lookup_online("tangible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigil(self):
        html_dump = lookup_online("vigil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sag(self):
        html_dump = lookup_online("sag")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gerbil(self):
        html_dump = lookup_online("gerbil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fierceness(self):
        html_dump = lookup_online("fierceness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quiver(self):
        html_dump = lookup_online("quiver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_itinerary(self):
        html_dump = lookup_online("itinerary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presupposition(self):
        html_dump = lookup_online("presupposition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaol(self):
        html_dump = lookup_online("gaol")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ronin(self):
        html_dump = lookup_online("ronin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clatter(self):
        html_dump = lookup_online("clatter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eek(self):
        html_dump = lookup_online("eek")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaff(self):
        html_dump = lookup_online("quaff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shin(self):
        html_dump = lookup_online("shin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitation(self):
        html_dump = lookup_online("precipitation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flax(self):
        html_dump = lookup_online("flax")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quietude(self):
        html_dump = lookup_online("quietude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bohemian(self):
        html_dump = lookup_online("bohemian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palate(self):
        html_dump = lookup_online("palate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prolix(self):
        html_dump = lookup_online("prolix")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mink(self):
        html_dump = lookup_online("mink")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reconcile(self):
        html_dump = lookup_online("reconcile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morass(self):
        html_dump = lookup_online("morass")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallible(self):
        html_dump = lookup_online("fallible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skeweres(self):
        html_dump = lookup_online("skeweres")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_centrifuge(self):
        html_dump = lookup_online("centrifuge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inculcate(self):
        html_dump = lookup_online("inculcate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fussy(self):
        html_dump = lookup_online("fussy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boozer(self):
        html_dump = lookup_online("boozer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cairn(self):
        html_dump = lookup_online("cairn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cleft(self):
        html_dump = lookup_online("cleft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auxilary(self):
        html_dump = lookup_online("auxilary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stele(self):
        html_dump = lookup_online("stele")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_restitution(self):
        html_dump = lookup_online("restitution")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flippant(self):
        html_dump = lookup_online("flippant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidgety(self):
        html_dump = lookup_online("fidgety")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contortion(self):
        html_dump = lookup_online("contortion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obscene(self):
        html_dump = lookup_online("obscene")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeopardy(self):
        html_dump = lookup_online("jeopardy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_facetious(self):
        html_dump = lookup_online("facetious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venerate(self):
        html_dump = lookup_online("venerate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chunky(self):
        html_dump = lookup_online("chunky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_osprey(self):
        html_dump = lookup_online("osprey")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rally(self):
        html_dump = lookup_online("rally")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foster(self):
        html_dump = lookup_online("foster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pace(self):
        html_dump = lookup_online("pace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bland(self):
        html_dump = lookup_online("bland")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_partacz(self):
        html_dump = lookup_online("partacz")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sling(self):
        html_dump = lookup_online("sling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posh(self):
        html_dump = lookup_online("posh")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsightly(self):
        html_dump = lookup_online("unsightly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bobcat(self):
        html_dump = lookup_online("bobcat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stricture(self):
        html_dump = lookup_online("stricture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blindsided(self):
        html_dump = lookup_online("blindsided")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unilateral(self):
        html_dump = lookup_online("unilateral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perseverance(self):
        html_dump = lookup_online("perseverance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_herbicide(self):
        html_dump = lookup_online("herbicide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adversity(self):
        html_dump = lookup_online("adversity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garble(self):
        html_dump = lookup_online("garble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strained(self):
        html_dump = lookup_online("strained")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meadow(self):
        html_dump = lookup_online("meadow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spleen(self):
        html_dump = lookup_online("spleen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vassalage(self):
        html_dump = lookup_online("vassalage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_violent(self):
        html_dump = lookup_online("violent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenuous(self):
        html_dump = lookup_online("tenuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inhibit(self):
        html_dump = lookup_online("inhibit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untenable(self):
        html_dump = lookup_online("untenable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equity(self):
        html_dump = lookup_online("equity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertinently(self):
        html_dump = lookup_online("pertinently")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gasket(self):
        html_dump = lookup_online("gasket")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neglect(self):
        html_dump = lookup_online("neglect")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruffled(self):
        html_dump = lookup_online("ruffled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inoculation(self):
        html_dump = lookup_online("inoculation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tough(self):
        html_dump = lookup_online("tough")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solidarity(self):
        html_dump = lookup_online("solidarity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sulking(self):
        html_dump = lookup_online("sulking")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brittle(self):
        html_dump = lookup_online("brittle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsavory(self):
        html_dump = lookup_online("unsavory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_altogether(self):
        html_dump = lookup_online("altogether")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disturbed(self):
        html_dump = lookup_online("disturbed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parish(self):
        html_dump = lookup_online("parish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fanny(self):
        html_dump = lookup_online("fanny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prolific(self):
        html_dump = lookup_online("prolific")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cater(self):
        html_dump = lookup_online("cater")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punctilious(self):
        html_dump = lookup_online("punctilious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shaft(self):
        html_dump = lookup_online("shaft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jell(self):
        html_dump = lookup_online("jell")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acerbic(self):
        html_dump = lookup_online("acerbic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wicked(self):
        html_dump = lookup_online("wicked")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incarceration(self):
        html_dump = lookup_online("incarceration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chokehold(self):
        html_dump = lookup_online("chokehold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distressing(self):
        html_dump = lookup_online("distressing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clover(self):
        html_dump = lookup_online("clover")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teak(self):
        html_dump = lookup_online("teak")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pariah(self):
        html_dump = lookup_online("pariah")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pious(self):
        html_dump = lookup_online("pious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_homemaker(self):
        html_dump = lookup_online("homemaker")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rabble(self):
        html_dump = lookup_online("rabble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repugnant(self):
        html_dump = lookup_online("repugnant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_millet(self):
        html_dump = lookup_online("millet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hieratic(self):
        html_dump = lookup_online("hieratic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliable(self):
        html_dump = lookup_online("pliable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derived(self):
        html_dump = lookup_online("derived")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_surmise(self):
        html_dump = lookup_online("surmise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ominous(self):
        html_dump = lookup_online("ominous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whimsical(self):
        html_dump = lookup_online("whimsical")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indentured(self):
        html_dump = lookup_online("indentured")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_further(self):
        html_dump = lookup_online("further")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_argot(self):
        html_dump = lookup_online("argot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abode(self):
        html_dump = lookup_online("abode")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shed(self):
        html_dump = lookup_online("shed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chiefly(self):
        html_dump = lookup_online("chiefly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burden(self):
        html_dump = lookup_online("burden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placenta(self):
        html_dump = lookup_online("placenta")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hireling(self):
        html_dump = lookup_online("hireling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_saunter(self):
        html_dump = lookup_online("saunter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moniker(self):
        html_dump = lookup_online("moniker")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perseverative(self):
        html_dump = lookup_online("perseverative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tribunal(self):
        html_dump = lookup_online("tribunal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sputter(self):
        html_dump = lookup_online("sputter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_singular(self):
        html_dump = lookup_online("singular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_backhanded(self):
        html_dump = lookup_online("backhanded")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meld(self):
        html_dump = lookup_online("meld")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slim(self):
        html_dump = lookup_online("slim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_innuendo(self):
        html_dump = lookup_online("innuendo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brash(self):
        html_dump = lookup_online("brash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infirmary(self):
        html_dump = lookup_online("infirmary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eve(self):
        html_dump = lookup_online("eve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bullhorn(self):
        html_dump = lookup_online("bullhorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trepidation(self):
        html_dump = lookup_online("trepidation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clairvoyance(self):
        html_dump = lookup_online("clairvoyance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subversive(self):
        html_dump = lookup_online("subversive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bestow(self):
        html_dump = lookup_online("bestow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awash(self):
        html_dump = lookup_online("awash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tawdry(self):
        html_dump = lookup_online("tawdry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yield(self):
        html_dump = lookup_online("yield")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_molar(self):
        html_dump = lookup_online("molar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dispassionate(self):
        html_dump = lookup_online("dispassionate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unyielding(self):
        html_dump = lookup_online("unyielding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dull(self):
        html_dump = lookup_online("dull")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squish(self):
        html_dump = lookup_online("squish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dictum(self):
        html_dump = lookup_online("dictum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_comatose(self):
        html_dump = lookup_online("comatose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_musty(self):
        html_dump = lookup_online("musty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rigmarole(self):
        html_dump = lookup_online("rigmarole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spasm(self):
        html_dump = lookup_online("spasm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distress(self):
        html_dump = lookup_online("distress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stillborn(self):
        html_dump = lookup_online("stillborn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gloomy(self):
        html_dump = lookup_online("gloomy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incantatory(self):
        html_dump = lookup_online("incantatory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutter(self):
        html_dump = lookup_online("gutter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fond(self):
        html_dump = lookup_online("fond")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_melanoma(self):
        html_dump = lookup_online("melanoma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tread(self):
        html_dump = lookup_online("tread")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquit(self):
        html_dump = lookup_online("acquit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumigate(self):
        html_dump = lookup_online("fumigate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foil(self):
        html_dump = lookup_online("foil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bristle(self):
        html_dump = lookup_online("bristle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Fan(self):
        html_dump = lookup_online("Fan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stature(self):
        html_dump = lookup_online("stature")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_baulk(self):
        html_dump = lookup_online("baulk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apprehension(self):
        html_dump = lookup_online("apprehension")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abrasive(self):
        html_dump = lookup_online("abrasive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defy(self):
        html_dump = lookup_online("defy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminently(self):
        html_dump = lookup_online("eminently")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harken(self):
        html_dump = lookup_online("harken")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limper(self):
        html_dump = lookup_online("limper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disbarment(self):
        html_dump = lookup_online("disbarment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimonious(self):
        html_dump = lookup_online("acrimonious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enduring(self):
        html_dump = lookup_online("enduring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recap(self):
        html_dump = lookup_online("recap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transient(self):
        html_dump = lookup_online("transient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forgo(self):
        html_dump = lookup_online("forgo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enamel(self):
        html_dump = lookup_online("enamel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serenity(self):
        html_dump = lookup_online("serenity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soggy(self):
        html_dump = lookup_online("soggy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_binding(self):
        html_dump = lookup_online("binding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bulge(self):
        html_dump = lookup_online("bulge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loth(self):
        html_dump = lookup_online("loth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salve(self):
        html_dump = lookup_online("salve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shawl(self):
        html_dump = lookup_online("shawl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manger(self):
        html_dump = lookup_online("manger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_festering(self):
        html_dump = lookup_online("festering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feisty(self):
        html_dump = lookup_online("feisty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barmy(self):
        html_dump = lookup_online("barmy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_qualm(self):
        html_dump = lookup_online("qualm")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_and(self):
        html_dump = lookup_online("and")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patrimony(self):
        html_dump = lookup_online("patrimony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yelp(self):
        html_dump = lookup_online("yelp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prattle(self):
        html_dump = lookup_online("prattle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crow(self):
        html_dump = lookup_online("crow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jurisprudence(self):
        html_dump = lookup_online("jurisprudence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leach(self):
        html_dump = lookup_online("leach")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stencil(self):
        html_dump = lookup_online("stencil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cromulent(self):
        html_dump = lookup_online("cromulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_downtrodden(self):
        html_dump = lookup_online("downtrodden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_honeydew(self):
        html_dump = lookup_online("honeydew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cemetery(self):
        html_dump = lookup_online("cemetery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stippled(self):
        html_dump = lookup_online("stippled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solicitation(self):
        html_dump = lookup_online("solicitation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_determinate(self):
        html_dump = lookup_online("determinate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shingles(self):
        html_dump = lookup_online("shingles")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edgy(self):
        html_dump = lookup_online("edgy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myopia(self):
        html_dump = lookup_online("myopia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obsequiousness(self):
        html_dump = lookup_online("obsequiousness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misappropriate(self):
        html_dump = lookup_online("misappropriate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meanly(self):
        html_dump = lookup_online("meanly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardent(self):
        html_dump = lookup_online("ardent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cranium(self):
        html_dump = lookup_online("cranium")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_comma(self):
        html_dump = lookup_online("comma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insolent(self):
        html_dump = lookup_online("insolent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ramrod(self):
        html_dump = lookup_online("ramrod")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stringent(self):
        html_dump = lookup_online("stringent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_baleful(self):
        html_dump = lookup_online("baleful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haven(self):
        html_dump = lookup_online("haven")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dregs(self):
        html_dump = lookup_online("dregs")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upend(self):
        html_dump = lookup_online("upend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conduit(self):
        html_dump = lookup_online("conduit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toddle(self):
        html_dump = lookup_online("toddle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malady(self):
        html_dump = lookup_online("malady")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_olfaction(self):
        html_dump = lookup_online("olfaction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accrue(self):
        html_dump = lookup_online("accrue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slather(self):
        html_dump = lookup_online("slather")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranquil(self):
        html_dump = lookup_online("tranquil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plummet(self):
        html_dump = lookup_online("plummet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bustard(self):
        html_dump = lookup_online("bustard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_somber(self):
        html_dump = lookup_online("somber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hitch(self):
        html_dump = lookup_online("hitch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tiller(self):
        html_dump = lookup_online("tiller")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_varsity(self):
        html_dump = lookup_online("varsity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outpace(self):
        html_dump = lookup_online("outpace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plow(self):
        html_dump = lookup_online("plow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limpid(self):
        html_dump = lookup_online("limpid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heap(self):
        html_dump = lookup_online("heap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suite(self):
        html_dump = lookup_online("suite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harbinger(self):
        html_dump = lookup_online("harbinger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deft(self):
        html_dump = lookup_online("deft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ebb(self):
        html_dump = lookup_online("ebb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrewdness(self):
        html_dump = lookup_online("shrewdness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recant(self):
        html_dump = lookup_online("recant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exquisite(self):
        html_dump = lookup_online("exquisite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiat(self):
        html_dump = lookup_online("fiat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_primacy(self):
        html_dump = lookup_online("primacy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuff(self):
        html_dump = lookup_online("tuff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheen(self):
        html_dump = lookup_online("sheen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slope(self):
        html_dump = lookup_online("slope")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilantly(self):
        html_dump = lookup_online("vigilantly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kerfuffle(self):
        html_dump = lookup_online("kerfuffle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glare(self):
        html_dump = lookup_online("glare")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permaculture(self):
        html_dump = lookup_online("permaculture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grunch(self):
        html_dump = lookup_online("grunch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rayon(self):
        html_dump = lookup_online("rayon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effusive(self):
        html_dump = lookup_online("effusive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thine(self):
        html_dump = lookup_online("thine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_locus(self):
        html_dump = lookup_online("locus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aftermath(self):
        html_dump = lookup_online("aftermath")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savant(self):
        html_dump = lookup_online("savant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mongrel(self):
        html_dump = lookup_online("mongrel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_odometer(self):
        html_dump = lookup_online("odometer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_complacent(self):
        html_dump = lookup_online("complacent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crushed(self):
        html_dump = lookup_online("crushed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dimwit(self):
        html_dump = lookup_online("dimwit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_circumscribe(self):
        html_dump = lookup_online("circumscribe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concur(self):
        html_dump = lookup_online("concur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resentful(self):
        html_dump = lookup_online("resentful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redundancy(self):
        html_dump = lookup_online("redundancy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eventually(self):
        html_dump = lookup_online("eventually")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheaf(self):
        html_dump = lookup_online("sheaf")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrusive(self):
        html_dump = lookup_online("intrusive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refusenik(self):
        html_dump = lookup_online("refusenik")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunk(self):
        html_dump = lookup_online("hunk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_camomile(self):
        html_dump = lookup_online("camomile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veneration(self):
        html_dump = lookup_online("veneration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seesaw(self):
        html_dump = lookup_online("seesaw")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reek(self):
        html_dump = lookup_online("reek")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pine(self):
        html_dump = lookup_online("pine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_egress(self):
        html_dump = lookup_online("egress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_digest(self):
        html_dump = lookup_online("digest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rave(self):
        html_dump = lookup_online("rave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gargantuan(self):
        html_dump = lookup_online("gargantuan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yon(self):
        html_dump = lookup_online("yon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chaplain(self):
        html_dump = lookup_online("chaplain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atavistic(self):
        html_dump = lookup_online("atavistic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atone(self):
        html_dump = lookup_online("atone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aquiver(self):
        html_dump = lookup_online("aquiver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brisk(self):
        html_dump = lookup_online("brisk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestige(self):
        html_dump = lookup_online("vestige")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doubtless(self):
        html_dump = lookup_online("doubtless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exultant(self):
        html_dump = lookup_online("exultant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_post(self):
        html_dump = lookup_online("post")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simp(self):
        html_dump = lookup_online("simp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forage(self):
        html_dump = lookup_online("forage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lofty(self):
        html_dump = lookup_online("lofty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acuity(self):
        html_dump = lookup_online("acuity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cop(self):
        html_dump = lookup_online("cop")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rawhide(self):
        html_dump = lookup_online("rawhide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwind(self):
        html_dump = lookup_online("unwind")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferocity(self):
        html_dump = lookup_online("ferocity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vanguard(self):
        html_dump = lookup_online("vanguard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lattice(self):
        html_dump = lookup_online("lattice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curmudgeon(self):
        html_dump = lookup_online("curmudgeon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intractable(self):
        html_dump = lookup_online("intractable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_basking(self):
        html_dump = lookup_online("basking")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lackeys(self):
        html_dump = lookup_online("lackeys")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grazer(self):
        html_dump = lookup_online("grazer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunch(self):
        html_dump = lookup_online("hunch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapt(self):
        html_dump = lookup_online("rapt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incandescence(self):
        html_dump = lookup_online("incandescence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_behest(self):
        html_dump = lookup_online("behest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedate(self):
        html_dump = lookup_online("sedate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wilt(self):
        html_dump = lookup_online("wilt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_temerity(self):
        html_dump = lookup_online("temerity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humility(self):
        html_dump = lookup_online("humility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ripe(self):
        html_dump = lookup_online("ripe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncovered(self):
        html_dump = lookup_online("uncovered")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sweeping(self):
        html_dump = lookup_online("sweeping")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apperception(self):
        html_dump = lookup_online("apperception")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_destitution(self):
        html_dump = lookup_online("destitution")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_canny(self):
        html_dump = lookup_online("canny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voracious(self):
        html_dump = lookup_online("voracious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haggle(self):
        html_dump = lookup_online("haggle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overpass(self):
        html_dump = lookup_online("overpass")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disarray(self):
        html_dump = lookup_online("disarray")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unease(self):
        html_dump = lookup_online("unease")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alleviate(self):
        html_dump = lookup_online("alleviate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraction(self):
        html_dump = lookup_online("contraction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condone(self):
        html_dump = lookup_online("condone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tail(self):
        html_dump = lookup_online("tail")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unrelenting(self):
        html_dump = lookup_online("unrelenting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ditties(self):
        html_dump = lookup_online("ditties")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacit(self):
        html_dump = lookup_online("tacit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lam(self):
        html_dump = lookup_online("lam")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_annoyed(self):
        html_dump = lookup_online("annoyed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lash(self):
        html_dump = lookup_online("lash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wage(self):
        html_dump = lookup_online("wage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unpalatable(self):
        html_dump = lookup_online("unpalatable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glossary(self):
        html_dump = lookup_online("glossary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barge(self):
        html_dump = lookup_online("barge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_libel(self):
        html_dump = lookup_online("libel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teamster(self):
        html_dump = lookup_online("teamster")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repudiate(self):
        html_dump = lookup_online("repudiate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interwoven(self):
        html_dump = lookup_online("interwoven")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spate(self):
        html_dump = lookup_online("spate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pervasive(self):
        html_dump = lookup_online("pervasive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fusion(self):
        html_dump = lookup_online("fusion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abduct(self):
        html_dump = lookup_online("abduct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peccant(self):
        html_dump = lookup_online("peccant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outlandish(self):
        html_dump = lookup_online("outlandish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudish(self):
        html_dump = lookup_online("prudish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scupper(self):
        html_dump = lookup_online("scupper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conciliation(self):
        html_dump = lookup_online("conciliation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disdain(self):
        html_dump = lookup_online("disdain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incendiary(self):
        html_dump = lookup_online("incendiary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterrent(self):
        html_dump = lookup_online("deterrent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crippled(self):
        html_dump = lookup_online("crippled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arbitrage(self):
        html_dump = lookup_online("arbitrage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_same(self):
        html_dump = lookup_online("same")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forecast(self):
        html_dump = lookup_online("forecast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhilaration(self):
        html_dump = lookup_online("exhilaration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peregrination(self):
        html_dump = lookup_online("peregrination")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commune(self):
        html_dump = lookup_online("commune")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garishness(self):
        html_dump = lookup_online("garishness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creeping(self):
        html_dump = lookup_online("creeping")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sinister(self):
        html_dump = lookup_online("sinister")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placating(self):
        html_dump = lookup_online("placating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_narrow(self):
        html_dump = lookup_online("narrow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nimble(self):
        html_dump = lookup_online("nimble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bandicoot(self):
        html_dump = lookup_online("bandicoot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atrocious(self):
        html_dump = lookup_online("atrocious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garrulous(self):
        html_dump = lookup_online("garrulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bulk(self):
        html_dump = lookup_online("bulk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaundice(self):
        html_dump = lookup_online("jaundice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arguably(self):
        html_dump = lookup_online("arguably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleep(self):
        html_dump = lookup_online("sleep")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conciliatory(self):
        html_dump = lookup_online("conciliatory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaze(self):
        html_dump = lookup_online("gaze")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aniseed(self):
        html_dump = lookup_online("aniseed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desiccate(self):
        html_dump = lookup_online("desiccate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dreadful(self):
        html_dump = lookup_online("dreadful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shimmer(self):
        html_dump = lookup_online("shimmer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vice(self):
        html_dump = lookup_online("vice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incinerator(self):
        html_dump = lookup_online("incinerator")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_delineate(self):
        html_dump = lookup_online("delineate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alimony(self):
        html_dump = lookup_online("alimony")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_captivating(self):
        html_dump = lookup_online("captivating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hustle(self):
        html_dump = lookup_online("hustle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endearment(self):
        html_dump = lookup_online("endearment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limp(self):
        html_dump = lookup_online("limp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phubbing(self):
        html_dump = lookup_online("phubbing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flay(self):
        html_dump = lookup_online("flay")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoke(self):
        html_dump = lookup_online("spoke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbate(self):
        html_dump = lookup_online("exacerbate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hide(self):
        html_dump = lookup_online("hide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frankincense(self):
        html_dump = lookup_online("frankincense")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tale(self):
        html_dump = lookup_online("tale")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phalanx(self):
        html_dump = lookup_online("phalanx")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bellicose(self):
        html_dump = lookup_online("bellicose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perfunctory(self):
        html_dump = lookup_online("perfunctory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sarcoma(self):
        html_dump = lookup_online("sarcoma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruntled(self):
        html_dump = lookup_online("gruntled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exasperated(self):
        html_dump = lookup_online("exasperated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matron(self):
        html_dump = lookup_online("matron")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrinsically(self):
        html_dump = lookup_online("intrinsically")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaint(self):
        html_dump = lookup_online("quaint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_medulla(self):
        html_dump = lookup_online("medulla")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rueful(self):
        html_dump = lookup_online("rueful")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealotry(self):
        html_dump = lookup_online("zealotry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foraging(self):
        html_dump = lookup_online("foraging")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_theorem(self):
        html_dump = lookup_online("theorem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affront(self):
        html_dump = lookup_online("affront")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eponymous(self):
        html_dump = lookup_online("eponymous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pending(self):
        html_dump = lookup_online("pending")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jilt(self):
        html_dump = lookup_online("jilt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hulk(self):
        html_dump = lookup_online("hulk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_languid(self):
        html_dump = lookup_online("languid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gammon(self):
        html_dump = lookup_online("gammon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heckle(self):
        html_dump = lookup_online("heckle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squabble(self):
        html_dump = lookup_online("squabble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corny(self):
        html_dump = lookup_online("corny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ridge(self):
        html_dump = lookup_online("ridge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inherent(self):
        html_dump = lookup_online("inherent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nebulous(self):
        html_dump = lookup_online("nebulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blimp(self):
        html_dump = lookup_online("blimp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruddy(self):
        html_dump = lookup_online("ruddy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulmonary(self):
        html_dump = lookup_online("pulmonary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caress(self):
        html_dump = lookup_online("caress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proliferation(self):
        html_dump = lookup_online("proliferation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excavation(self):
        html_dump = lookup_online("excavation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revile(self):
        html_dump = lookup_online("revile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affine(self):
        html_dump = lookup_online("affine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraud(self):
        html_dump = lookup_online("fraud")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midwife(self):
        html_dump = lookup_online("midwife")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumpled(self):
        html_dump = lookup_online("rumpled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hone(self):
        html_dump = lookup_online("hone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_breadth(self):
        html_dump = lookup_online("breadth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dither(self):
        html_dump = lookup_online("dither")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paternalism(self):
        html_dump = lookup_online("paternalism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deference(self):
        html_dump = lookup_online("deference")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commission(self):
        html_dump = lookup_online("commission")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dejection(self):
        html_dump = lookup_online("dejection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ash(self):
        html_dump = lookup_online("ash")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_froth(self):
        html_dump = lookup_online("froth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upon(self):
        html_dump = lookup_online("upon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscreant(self):
        html_dump = lookup_online("miscreant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snide(self):
        html_dump = lookup_online("snide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sage(self):
        html_dump = lookup_online("sage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shriek(self):
        html_dump = lookup_online("shriek")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cronies(self):
        html_dump = lookup_online("cronies")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumble(self):
        html_dump = lookup_online("fumble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spotless(self):
        html_dump = lookup_online("spotless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_umpteenth(self):
        html_dump = lookup_online("umpteenth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_service(self):
        html_dump = lookup_online("service")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harried(self):
        html_dump = lookup_online("harried")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abstruse(self):
        html_dump = lookup_online("abstruse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bout(self):
        html_dump = lookup_online("bout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lanky(self):
        html_dump = lookup_online("lanky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stifle(self):
        html_dump = lookup_online("stifle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untrodden(self):
        html_dump = lookup_online("untrodden")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squint(self):
        html_dump = lookup_online("squint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slumber(self):
        html_dump = lookup_online("slumber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bemoan(self):
        html_dump = lookup_online("bemoan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shtick(self):
        html_dump = lookup_online("shtick")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraband(self):
        html_dump = lookup_online("contraband")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catsup(self):
        html_dump = lookup_online("catsup")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckoning(self):
        html_dump = lookup_online("reckoning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contain(self):
        html_dump = lookup_online("contain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peripheral(self):
        html_dump = lookup_online("peripheral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swagger(self):
        html_dump = lookup_online("swagger")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insular(self):
        html_dump = lookup_online("insular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sickle(self):
        html_dump = lookup_online("sickle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intertwine(self):
        html_dump = lookup_online("intertwine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extraordinary(self):
        html_dump = lookup_online("extraordinary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fir(self):
        html_dump = lookup_online("fir")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gullet(self):
        html_dump = lookup_online("gullet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foliage(self):
        html_dump = lookup_online("foliage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fetter(self):
        html_dump = lookup_online("fetter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malleable(self):
        html_dump = lookup_online("malleable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sylvan(self):
        html_dump = lookup_online("sylvan")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mock(self):
        html_dump = lookup_online("mock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cajole(self):
        html_dump = lookup_online("cajole")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nurture(self):
        html_dump = lookup_online("nurture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enjoin(self):
        html_dump = lookup_online("enjoin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reprehensible(self):
        html_dump = lookup_online("reprehensible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_folio(self):
        html_dump = lookup_online("folio")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prawn(self):
        html_dump = lookup_online("prawn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fern(self):
        html_dump = lookup_online("fern")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amicably(self):
        html_dump = lookup_online("amicably")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whig(self):
        html_dump = lookup_online("whig")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_listener(self):
        html_dump = lookup_online("listener")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bungler(self):
        html_dump = lookup_online("bungler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitous(self):
        html_dump = lookup_online("precipitous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reticence(self):
        html_dump = lookup_online("reticence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardor(self):
        html_dump = lookup_online("ardor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dubious(self):
        html_dump = lookup_online("dubious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limerick(self):
        html_dump = lookup_online("limerick")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emerald(self):
        html_dump = lookup_online("emerald")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stalwart(self):
        html_dump = lookup_online("stalwart")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brazen(self):
        html_dump = lookup_online("brazen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gnat(self):
        html_dump = lookup_online("gnat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appendage(self):
        html_dump = lookup_online("appendage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_germane(self):
        html_dump = lookup_online("germane")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preemptively(self):
        html_dump = lookup_online("preemptively")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cede(self):
        html_dump = lookup_online("cede")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cay(self):
        html_dump = lookup_online("cay")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_county(self):
        html_dump = lookup_online("county")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elation(self):
        html_dump = lookup_online("elation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curb(self):
        html_dump = lookup_online("curb")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_on(self):
        html_dump = lookup_online("on")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glam(self):
        html_dump = lookup_online("glam")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portents(self):
        html_dump = lookup_online("portents")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abolish(self):
        html_dump = lookup_online("abolish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bejeezus(self):
        html_dump = lookup_online("bejeezus")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_torrefaction(self):
        html_dump = lookup_online("torrefaction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flaneur(self):
        html_dump = lookup_online("flaneur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardour(self):
        html_dump = lookup_online("ardour")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candid(self):
        html_dump = lookup_online("candid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proper(self):
        html_dump = lookup_online("proper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sprain(self):
        html_dump = lookup_online("sprain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presuppose(self):
        html_dump = lookup_online("presuppose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hanker(self):
        html_dump = lookup_online("hanker")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holler(self):
        html_dump = lookup_online("holler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prevarication(self):
        html_dump = lookup_online("prevarication")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penitent(self):
        html_dump = lookup_online("penitent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garum(self):
        html_dump = lookup_online("garum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ilk(self):
        html_dump = lookup_online("ilk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pudgy(self):
        html_dump = lookup_online("pudgy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismember(self):
        html_dump = lookup_online("dismember")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quit(self):
        html_dump = lookup_online("quit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miser(self):
        html_dump = lookup_online("miser")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blight(self):
        html_dump = lookup_online("blight")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phthalates(self):
        html_dump = lookup_online("phthalates")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affidavit(self):
        html_dump = lookup_online("affidavit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relapse(self):
        html_dump = lookup_online("relapse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_character(self):
        html_dump = lookup_online("character")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slump(self):
        html_dump = lookup_online("slump")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garner(self):
        html_dump = lookup_online("garner")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hum(self):
        html_dump = lookup_online("hum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsound(self):
        html_dump = lookup_online("unsound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescending(self):
        html_dump = lookup_online("condescending")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ken(self):
        html_dump = lookup_online("ken")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewilder(self):
        html_dump = lookup_online("bewilder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crust(self):
        html_dump = lookup_online("crust")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compassionate(self):
        html_dump = lookup_online("compassionate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squid(self):
        html_dump = lookup_online("squid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reclusive(self):
        html_dump = lookup_online("reclusive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_are(self):
        html_dump = lookup_online("are")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gouge(self):
        html_dump = lookup_online("gouge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satiate(self):
        html_dump = lookup_online("satiate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravage(self):
        html_dump = lookup_online("ravage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ecstatic(self):
        html_dump = lookup_online("ecstatic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mull(self):
        html_dump = lookup_online("mull")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avowedly(self):
        html_dump = lookup_online("avowedly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lock(self):
        html_dump = lookup_online("lock")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fettle(self):
        html_dump = lookup_online("fettle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urchin(self):
        html_dump = lookup_online("urchin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferocious(self):
        html_dump = lookup_online("ferocious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrawl(self):
        html_dump = lookup_online("scrawl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_looey(self):
        html_dump = lookup_online("looey")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snitch(self):
        html_dump = lookup_online("snitch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squeamish(self):
        html_dump = lookup_online("squeamish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmurs(self):
        html_dump = lookup_online("murmurs")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harness(self):
        html_dump = lookup_online("harness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapture(self):
        html_dump = lookup_online("rapture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debauchery(self):
        html_dump = lookup_online("debauchery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amelioration(self):
        html_dump = lookup_online("amelioration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incapacity(self):
        html_dump = lookup_online("incapacity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scallion(self):
        html_dump = lookup_online("scallion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prism(self):
        html_dump = lookup_online("prism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desolate(self):
        html_dump = lookup_online("desolate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_niggle(self):
        html_dump = lookup_online("niggle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snap(self):
        html_dump = lookup_online("snap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucent(self):
        html_dump = lookup_online("lucent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurious(self):
        html_dump = lookup_online("spurious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertain(self):
        html_dump = lookup_online("pertain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allegiance(self):
        html_dump = lookup_online("allegiance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminent(self):
        html_dump = lookup_online("eminent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yore(self):
        html_dump = lookup_online("yore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dusk(self):
        html_dump = lookup_online("dusk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bondage(self):
        html_dump = lookup_online("bondage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_starch(self):
        html_dump = lookup_online("starch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fertile(self):
        html_dump = lookup_online("fertile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trump(self):
        html_dump = lookup_online("trump")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggrieve(self):
        html_dump = lookup_online("aggrieve")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cogitate(self):
        html_dump = lookup_online("cogitate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retrograde(self):
        html_dump = lookup_online("retrograde")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inchoate(self):
        html_dump = lookup_online("inchoate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quandary(self):
        html_dump = lookup_online("quandary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defenestration(self):
        html_dump = lookup_online("defenestration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vinegar(self):
        html_dump = lookup_online("vinegar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_greyhound(self):
        html_dump = lookup_online("greyhound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hem(self):
        html_dump = lookup_online("hem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_piety(self):
        html_dump = lookup_online("piety")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poof(self):
        html_dump = lookup_online("poof")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rue(self):
        html_dump = lookup_online("rue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawl(self):
        html_dump = lookup_online("brawl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_divest(self):
        html_dump = lookup_online("divest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hustings(self):
        html_dump = lookup_online("hustings")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lone(self):
        html_dump = lookup_online("lone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_countersink(self):
        html_dump = lookup_online("countersink")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apposition(self):
        html_dump = lookup_online("apposition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weep(self):
        html_dump = lookup_online("weep")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parallelogram(self):
        html_dump = lookup_online("parallelogram")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detain(self):
        html_dump = lookup_online("detain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extraneous(self):
        html_dump = lookup_online("extraneous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overwrought(self):
        html_dump = lookup_online("overwrought")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gape(self):
        html_dump = lookup_online("gape")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insidious(self):
        html_dump = lookup_online("insidious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobblestone(self):
        html_dump = lookup_online("cobblestone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puff(self):
        html_dump = lookup_online("puff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pestilence(self):
        html_dump = lookup_online("pestilence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crotchety(self):
        html_dump = lookup_online("crotchety")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verdant(self):
        html_dump = lookup_online("verdant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tart(self):
        html_dump = lookup_online("tart")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infallibility(self):
        html_dump = lookup_online("infallibility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fierce(self):
        html_dump = lookup_online("fierce")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curate(self):
        html_dump = lookup_online("curate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glimpse(self):
        html_dump = lookup_online("glimpse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simular(self):
        html_dump = lookup_online("simular")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extoll(self):
        html_dump = lookup_online("extoll")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grit(self):
        html_dump = lookup_online("grit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knead(self):
        html_dump = lookup_online("knead")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meting(self):
        html_dump = lookup_online("meting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ballot(self):
        html_dump = lookup_online("ballot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjugate(self):
        html_dump = lookup_online("conjugate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frolic(self):
        html_dump = lookup_online("frolic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_junction(self):
        html_dump = lookup_online("junction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hewing(self):
        html_dump = lookup_online("hewing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abscess(self):
        html_dump = lookup_online("abscess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinnace(self):
        html_dump = lookup_online("pinnace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recess(self):
        html_dump = lookup_online("recess")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recuperate(self):
        html_dump = lookup_online("recuperate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_progeny(self):
        html_dump = lookup_online("progeny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissemination(self):
        html_dump = lookup_online("dissemination")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_specious(self):
        html_dump = lookup_online("specious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heath(self):
        html_dump = lookup_online("heath")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foreshadow(self):
        html_dump = lookup_online("foreshadow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conflate(self):
        html_dump = lookup_online("conflate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sumac(self):
        html_dump = lookup_online("sumac")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dairy(self):
        html_dump = lookup_online("dairy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagellating(self):
        html_dump = lookup_online("flagellating")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precocious(self):
        html_dump = lookup_online("precocious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_address(self):
        html_dump = lookup_online("address")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_languish(self):
        html_dump = lookup_online("languish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amuse(self):
        html_dump = lookup_online("amuse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncanny(self):
        html_dump = lookup_online("uncanny")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetuate(self):
        html_dump = lookup_online("perpetuate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heathen(self):
        html_dump = lookup_online("heathen")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discernment(self):
        html_dump = lookup_online("discernment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abort(self):
        html_dump = lookup_online("abort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_iniquity(self):
        html_dump = lookup_online("iniquity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vary(self):
        html_dump = lookup_online("vary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_featureless(self):
        html_dump = lookup_online("featureless")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crave(self):
        html_dump = lookup_online("crave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glaze(self):
        html_dump = lookup_online("glaze")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cricket(self):
        html_dump = lookup_online("cricket")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reify(self):
        html_dump = lookup_online("reify")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amorphous(self):
        html_dump = lookup_online("amorphous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intangible(self):
        html_dump = lookup_online("intangible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_daft(self):
        html_dump = lookup_online("daft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_colander(self):
        html_dump = lookup_online("colander")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lesion(self):
        html_dump = lookup_online("lesion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rein(self):
        html_dump = lookup_online("rein")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teat(self):
        html_dump = lookup_online("teat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entice(self):
        html_dump = lookup_online("entice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expound(self):
        html_dump = lookup_online("expound")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resent(self):
        html_dump = lookup_online("resent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fling(self):
        html_dump = lookup_online("fling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matricide(self):
        html_dump = lookup_online("matricide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_buggery(self):
        html_dump = lookup_online("buggery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aegis(self):
        html_dump = lookup_online("aegis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_egregious(self):
        html_dump = lookup_online("egregious")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scourge(self):
        html_dump = lookup_online("scourge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mould(self):
        html_dump = lookup_online("mould")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rad(self):
        html_dump = lookup_online("rad")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extruding(self):
        html_dump = lookup_online("extruding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drama(self):
        html_dump = lookup_online("drama")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmur(self):
        html_dump = lookup_online("murmur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smug(self):
        html_dump = lookup_online("smug")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toil(self):
        html_dump = lookup_online("toil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fungible(self):
        html_dump = lookup_online("fungible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plodding(self):
        html_dump = lookup_online("plodding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bustle(self):
        html_dump = lookup_online("bustle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acute(self):
        html_dump = lookup_online("acute")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pouty(self):
        html_dump = lookup_online("pouty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harass(self):
        html_dump = lookup_online("harass")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pram(self):
        html_dump = lookup_online("pram")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dilate(self):
        html_dump = lookup_online("dilate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sow(self):
        html_dump = lookup_online("sow")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_requisite(self):
        html_dump = lookup_online("requisite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wedge(self):
        html_dump = lookup_online("wedge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disjunction(self):
        html_dump = lookup_online("disjunction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swell(self):
        html_dump = lookup_online("swell")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contempt(self):
        html_dump = lookup_online("contempt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_birch(self):
        html_dump = lookup_online("birch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stakeout(self):
        html_dump = lookup_online("stakeout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ibex(self):
        html_dump = lookup_online("ibex")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_submit(self):
        html_dump = lookup_online("submit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fowl(self):
        html_dump = lookup_online("fowl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ostensibly(self):
        html_dump = lookup_online("ostensibly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indignant(self):
        html_dump = lookup_online("indignant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbecoming(self):
        html_dump = lookup_online("unbecoming")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insensate(self):
        html_dump = lookup_online("insensate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influence(self):
        html_dump = lookup_online("influence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_noncommissioned(self):
        html_dump = lookup_online("noncommissioned")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matronly(self):
        html_dump = lookup_online("matronly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effeminate(self):
        html_dump = lookup_online("effeminate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nominal(self):
        html_dump = lookup_online("nominal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rife(self):
        html_dump = lookup_online("rife")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scuffed(self):
        html_dump = lookup_online("scuffed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unscathed(self):
        html_dump = lookup_online("unscathed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_roil(self):
        html_dump = lookup_online("roil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nadir(self):
        html_dump = lookup_online("nadir")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coffer(self):
        html_dump = lookup_online("coffer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gout(self):
        html_dump = lookup_online("gout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leap(self):
        html_dump = lookup_online("leap")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indirection(self):
        html_dump = lookup_online("indirection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ambler(self):
        html_dump = lookup_online("ambler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supress(self):
        html_dump = lookup_online("supress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_helot(self):
        html_dump = lookup_online("helot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dapper(self):
        html_dump = lookup_online("dapper")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_erstwhile(self):
        html_dump = lookup_online("erstwhile")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_geezer(self):
        html_dump = lookup_online("geezer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_audacity(self):
        html_dump = lookup_online("audacity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trombone(self):
        html_dump = lookup_online("trombone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascend(self):
        html_dump = lookup_online("ascend")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluptuous(self):
        html_dump = lookup_online("voluptuous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_denigration(self):
        html_dump = lookup_online("denigration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transcendent(self):
        html_dump = lookup_online("transcendent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corpulent(self):
        html_dump = lookup_online("corpulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haphazard(self):
        html_dump = lookup_online("haphazard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bowels(self):
        html_dump = lookup_online("bowels")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stem(self):
        html_dump = lookup_online("stem")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flaunt(self):
        html_dump = lookup_online("flaunt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_readily(self):
        html_dump = lookup_online("readily")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peer(self):
        html_dump = lookup_online("peer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despoil(self):
        html_dump = lookup_online("despoil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vex(self):
        html_dump = lookup_online("vex")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glibness(self):
        html_dump = lookup_online("glibness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artifact(self):
        html_dump = lookup_online("artifact")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ord(self):
        html_dump = lookup_online("ord")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utilitarian(self):
        html_dump = lookup_online("utilitarian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dolt(self):
        html_dump = lookup_online("dolt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stint(self):
        html_dump = lookup_online("stint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_estranged(self):
        html_dump = lookup_online("estranged")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succint(self):
        html_dump = lookup_online("succint")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hassle(self):
        html_dump = lookup_online("hassle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rivet(self):
        html_dump = lookup_online("rivet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_undertones(self):
        html_dump = lookup_online("undertones")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whiff(self):
        html_dump = lookup_online("whiff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unraveling(self):
        html_dump = lookup_online("unraveling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruff(self):
        html_dump = lookup_online("gruff")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vocation(self):
        html_dump = lookup_online("vocation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_committ(self):
        html_dump = lookup_online("committ")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mince(self):
        html_dump = lookup_online("mince")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flimsy(self):
        html_dump = lookup_online("flimsy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bumble(self):
        html_dump = lookup_online("bumble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whirling(self):
        html_dump = lookup_online("whirling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbridle(self):
        html_dump = lookup_online("unbridle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gingerly(self):
        html_dump = lookup_online("gingerly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_twang(self):
        html_dump = lookup_online("twang")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teeter(self):
        html_dump = lookup_online("teeter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manatee(self):
        html_dump = lookup_online("manatee")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succulent(self):
        html_dump = lookup_online("succulent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_centrifugal(self):
        html_dump = lookup_online("centrifugal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edifice(self):
        html_dump = lookup_online("edifice")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tungsten(self):
        html_dump = lookup_online("tungsten")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asphyxia(self):
        html_dump = lookup_online("asphyxia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obscurity(self):
        html_dump = lookup_online("obscurity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unscrupulous(self):
        html_dump = lookup_online("unscrupulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intercession(self):
        html_dump = lookup_online("intercession")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexorable(self):
        html_dump = lookup_online("inexorable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fleeting(self):
        html_dump = lookup_online("fleeting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sounder(self):
        html_dump = lookup_online("sounder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disgruntled(self):
        html_dump = lookup_online("disgruntled")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inducement(self):
        html_dump = lookup_online("inducement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travois(self):
        html_dump = lookup_online("travois")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crankshaft(self):
        html_dump = lookup_online("crankshaft")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caraway(self):
        html_dump = lookup_online("caraway")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awry(self):
        html_dump = lookup_online("awry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleuth(self):
        html_dump = lookup_online("sleuth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pellet(self):
        html_dump = lookup_online("pellet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phlebotomy(self):
        html_dump = lookup_online("phlebotomy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crackle(self):
        html_dump = lookup_online("crackle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incursion(self):
        html_dump = lookup_online("incursion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leeway(self):
        html_dump = lookup_online("leeway")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accessible(self):
        html_dump = lookup_online("accessible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contract(self):
        html_dump = lookup_online("contract")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simplistic(self):
        html_dump = lookup_online("simplistic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_almanac(self):
        html_dump = lookup_online("almanac")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desultory(self):
        html_dump = lookup_online("desultory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outpatient(self):
        html_dump = lookup_online("outpatient")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_array(self):
        html_dump = lookup_online("array")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neuroticism(self):
        html_dump = lookup_online("neuroticism")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_augur(self):
        html_dump = lookup_online("augur")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dyke(self):
        html_dump = lookup_online("dyke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antsy(self):
        html_dump = lookup_online("antsy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admission(self):
        html_dump = lookup_online("admission")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleazy(self):
        html_dump = lookup_online("sleazy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_writ(self):
        html_dump = lookup_online("writ")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cauldron(self):
        html_dump = lookup_online("cauldron")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_withering(self):
        html_dump = lookup_online("withering")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cadence(self):
        html_dump = lookup_online("cadence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cavity(self):
        html_dump = lookup_online("cavity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_collateral(self):
        html_dump = lookup_online("collateral")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feature(self):
        html_dump = lookup_online("feature")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acorn(self):
        html_dump = lookup_online("acorn")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murky(self):
        html_dump = lookup_online("murky")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jovial(self):
        html_dump = lookup_online("jovial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangent(self):
        html_dump = lookup_online("tangent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enormity(self):
        html_dump = lookup_online("enormity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prostrate(self):
        html_dump = lookup_online("prostrate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sever(self):
        html_dump = lookup_online("sever")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venereal(self):
        html_dump = lookup_online("venereal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loiter(self):
        html_dump = lookup_online("loiter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accosted(self):
        html_dump = lookup_online("accosted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adore(self):
        html_dump = lookup_online("adore")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flexibility(self):
        html_dump = lookup_online("flexibility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embroidery(self):
        html_dump = lookup_online("embroidery")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juncture(self):
        html_dump = lookup_online("juncture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boast(self):
        html_dump = lookup_online("boast")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longitude(self):
        html_dump = lookup_online("longitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ingot(self):
        html_dump = lookup_online("ingot")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_katydid(self):
        html_dump = lookup_online("katydid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Shia(self):
        html_dump = lookup_online("Shia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_actuary(self):
        html_dump = lookup_online("actuary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_throe(self):
        html_dump = lookup_online("throe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bifurcate(self):
        html_dump = lookup_online("bifurcate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placate(self):
        html_dump = lookup_online("placate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leek(self):
        html_dump = lookup_online("leek")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scurry(self):
        html_dump = lookup_online("scurry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excoriation(self):
        html_dump = lookup_online("excoriation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_primordial(self):
        html_dump = lookup_online("primordial")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_potty(self):
        html_dump = lookup_online("potty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accentuate(self):
        html_dump = lookup_online("accentuate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wholly(self):
        html_dump = lookup_online("wholly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantalizing(self):
        html_dump = lookup_online("tantalizing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fossick(self):
        html_dump = lookup_online("fossick")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gale(self):
        html_dump = lookup_online("gale")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interlocutor(self):
        html_dump = lookup_online("interlocutor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparagement(self):
        html_dump = lookup_online("disparagement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaver(self):
        html_dump = lookup_online("quaver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amiable(self):
        html_dump = lookup_online("amiable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harrowing(self):
        html_dump = lookup_online("harrowing")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subsist(self):
        html_dump = lookup_online("subsist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concede(self):
        html_dump = lookup_online("concede")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scanty(self):
        html_dump = lookup_online("scanty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harbour(self):
        html_dump = lookup_online("harbour")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hideously(self):
        html_dump = lookup_online("hideously")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_canuck(self):
        html_dump = lookup_online("canuck")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lorry(self):
        html_dump = lookup_online("lorry")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallout(self):
        html_dump = lookup_online("fallout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pineal(self):
        html_dump = lookup_online("pineal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigence(self):
        html_dump = lookup_online("indigence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ponder(self):
        html_dump = lookup_online("ponder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doe(self):
        html_dump = lookup_online("doe")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deviant(self):
        html_dump = lookup_online("deviant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excerpt(self):
        html_dump = lookup_online("excerpt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contractions(self):
        html_dump = lookup_online("contractions")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beignet(self):
        html_dump = lookup_online("beignet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caregivers(self):
        html_dump = lookup_online("caregivers")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cellar(self):
        html_dump = lookup_online("cellar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pejorative(self):
        html_dump = lookup_online("pejorative")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soar(self):
        html_dump = lookup_online("soar")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Formica(self):
        html_dump = lookup_online("Formica")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prescriptive(self):
        html_dump = lookup_online("prescriptive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_switch(self):
        html_dump = lookup_online("switch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miasma(self):
        html_dump = lookup_online("miasma")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mite(self):
        html_dump = lookup_online("mite")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravenous(self):
        html_dump = lookup_online("ravenous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frame(self):
        html_dump = lookup_online("frame")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caustic(self):
        html_dump = lookup_online("caustic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_largesse(self):
        html_dump = lookup_online("largesse")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trifle(self):
        html_dump = lookup_online("trifle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resort(self):
        html_dump = lookup_online("resort")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_augment(self):
        html_dump = lookup_online("augment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_startling(self):
        html_dump = lookup_online("startling")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frugality(self):
        html_dump = lookup_online("frugality")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_introspective(self):
        html_dump = lookup_online("introspective")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catalyze(self):
        html_dump = lookup_online("catalyze")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benighted(self):
        html_dump = lookup_online("benighted")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sway(self):
        html_dump = lookup_online("sway")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agency(self):
        html_dump = lookup_online("agency")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caption(self):
        html_dump = lookup_online("caption")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_horcrux(self):
        html_dump = lookup_online("horcrux")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aloof(self):
        html_dump = lookup_online("aloof")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anguish(self):
        html_dump = lookup_online("anguish")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menace(self):
        html_dump = lookup_online("menace")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maudlin(self):
        html_dump = lookup_online("maudlin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predator(self):
        html_dump = lookup_online("predator")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sown(self):
        html_dump = lookup_online("sown")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_den(self):
        html_dump = lookup_online("den")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_severance(self):
        html_dump = lookup_online("severance")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recrudescence(self):
        html_dump = lookup_online("recrudescence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impeccable(self):
        html_dump = lookup_online("impeccable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barrage(self):
        html_dump = lookup_online("barrage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urge(self):
        html_dump = lookup_online("urge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mild(self):
        html_dump = lookup_online("mild")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rectitude(self):
        html_dump = lookup_online("rectitude")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceited(self):
        html_dump = lookup_online("conceited")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pledge(self):
        html_dump = lookup_online("pledge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangential(self):
        html_dump = lookup_online("tangential")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tailgate(self):
        html_dump = lookup_online("tailgate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concierge(self):
        html_dump = lookup_online("concierge")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_didn_t(self):
        html_dump = lookup_online("didn't")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moat(self):
        html_dump = lookup_online("moat")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calamities(self):
        html_dump = lookup_online("calamities")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scag(self):
        html_dump = lookup_online("scag")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commendable(self):
        html_dump = lookup_online("commendable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defiant(self):
        html_dump = lookup_online("defiant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hawk(self):
        html_dump = lookup_online("hawk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orthogonal(self):
        html_dump = lookup_online("orthogonal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nitwit(self):
        html_dump = lookup_online("nitwit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stain(self):
        html_dump = lookup_online("stain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_treacherous(self):
        html_dump = lookup_online("treacherous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lynchpin(self):
        html_dump = lookup_online("lynchpin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mainland(self):
        html_dump = lookup_online("mainland")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grope(self):
        html_dump = lookup_online("grope")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bloke(self):
        html_dump = lookup_online("bloke")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hemorrhage(self):
        html_dump = lookup_online("hemorrhage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palpable(self):
        html_dump = lookup_online("palpable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_echelon(self):
        html_dump = lookup_online("echelon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hewer(self):
        html_dump = lookup_online("hewer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affliction(self):
        html_dump = lookup_online("affliction")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glisten(self):
        html_dump = lookup_online("glisten")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obviate(self):
        html_dump = lookup_online("obviate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_playdate(self):
        html_dump = lookup_online("playdate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elide(self):
        html_dump = lookup_online("elide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_planter(self):
        html_dump = lookup_online("planter")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sabbatical(self):
        html_dump = lookup_online("sabbatical")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incongruous(self):
        html_dump = lookup_online("incongruous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burl(self):
        html_dump = lookup_online("burl")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vitriolic(self):
        html_dump = lookup_online("vitriolic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulterior(self):
        html_dump = lookup_online("ulterior")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abjure(self):
        html_dump = lookup_online("abjure")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taxis(self):
        html_dump = lookup_online("taxis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigo(self):
        html_dump = lookup_online("indigo")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shone(self):
        html_dump = lookup_online("shone")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Lapp(self):
        html_dump = lookup_online("Lapp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deride(self):
        html_dump = lookup_online("deride")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eulogise(self):
        html_dump = lookup_online("eulogise")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hectic(self):
        html_dump = lookup_online("hectic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stave(self):
        html_dump = lookup_online("stave")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncouth(self):
        html_dump = lookup_online("uncouth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ordain(self):
        html_dump = lookup_online("ordain")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lynx(self):
        html_dump = lookup_online("lynx")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuflection(self):
        html_dump = lookup_online("genuflection")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liver(self):
        html_dump = lookup_online("liver")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_modest(self):
        html_dump = lookup_online("modest")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mooring(self):
        html_dump = lookup_online("mooring")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobbler(self):
        html_dump = lookup_online("cobbler")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savor(self):
        html_dump = lookup_online("savor")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impunity(self):
        html_dump = lookup_online("impunity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entrust(self):
        html_dump = lookup_online("entrust")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_judder(self):
        html_dump = lookup_online("judder")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clout(self):
        html_dump = lookup_online("clout")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cogent(self):
        html_dump = lookup_online("cogent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derangement(self):
        html_dump = lookup_online("derangement")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smiting(self):
        html_dump = lookup_online("smiting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rummage(self):
        html_dump = lookup_online("rummage")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_noose(self):
        html_dump = lookup_online("noose")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amalgam(self):
        html_dump = lookup_online("amalgam")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petit(self):
        html_dump = lookup_online("petit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boilerplate(self):
        html_dump = lookup_online("boilerplate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_front(self):
        html_dump = lookup_online("front")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tremble(self):
        html_dump = lookup_online("tremble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_volition(self):
        html_dump = lookup_online("volition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proclivity(self):
        html_dump = lookup_online("proclivity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_waning(self):
        html_dump = lookup_online("waning")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jovially(self):
        html_dump = lookup_online("jovially")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoary(self):
        html_dump = lookup_online("hoary")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitate(self):
        html_dump = lookup_online("precipitate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eschew(self):
        html_dump = lookup_online("eschew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superstition(self):
        html_dump = lookup_online("superstition")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bold(self):
        html_dump = lookup_online("bold")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobble(self):
        html_dump = lookup_online("cobble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedation(self):
        html_dump = lookup_online("sedation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belcher(self):
        html_dump = lookup_online("belcher")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cramp(self):
        html_dump = lookup_online("cramp")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excessive(self):
        html_dump = lookup_online("excessive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plainly(self):
        html_dump = lookup_online("plainly")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clandestine(self):
        html_dump = lookup_online("clandestine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bollard(self):
        html_dump = lookup_online("bollard")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_credulous(self):
        html_dump = lookup_online("credulous")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ante(self):
        html_dump = lookup_online("ante")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_futon(self):
        html_dump = lookup_online("futon")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_synesthesia(self):
        html_dump = lookup_online("synesthesia")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_single_out(self):
        html_dump = lookup_online("single out")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mystical(self):
        html_dump = lookup_online("mystical")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouch(self):
        html_dump = lookup_online("grouch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncanniness(self):
        html_dump = lookup_online("uncanniness")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epiphany(self):
        html_dump = lookup_online("epiphany")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cowed(self):
        html_dump = lookup_online("cowed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exonerate(self):
        html_dump = lookup_online("exonerate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_during(self):
        html_dump = lookup_online("during")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affluence(self):
        html_dump = lookup_online("affluence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bucolic(self):
        html_dump = lookup_online("bucolic")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feasible(self):
        html_dump = lookup_online("feasible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_comestible(self):
        html_dump = lookup_online("comestible")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compulsion(self):
        html_dump = lookup_online("compulsion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bromide(self):
        html_dump = lookup_online("bromide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestibule(self):
        html_dump = lookup_online("vestibule")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relief(self):
        html_dump = lookup_online("relief")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abrupt(self):
        html_dump = lookup_online("abrupt")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dapple(self):
        html_dump = lookup_online("dapple")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stye(self):
        html_dump = lookup_online("stye")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_angsty(self):
        html_dump = lookup_online("angsty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larks(self):
        html_dump = lookup_online("larks")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbation(self):
        html_dump = lookup_online("exacerbation")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turgid(self):
        html_dump = lookup_online("turgid")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elk(self):
        html_dump = lookup_online("elk")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paunch(self):
        html_dump = lookup_online("paunch")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hornbeam(self):
        html_dump = lookup_online("hornbeam")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scaffolding(self):
        html_dump = lookup_online("scaffolding")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstruct(self):
        html_dump = lookup_online("obstruct")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kestrel(self):
        html_dump = lookup_online("kestrel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impertinent(self):
        html_dump = lookup_online("impertinent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concision(self):
        html_dump = lookup_online("concision")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myelin(self):
        html_dump = lookup_online("myelin")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_possibility(self):
        html_dump = lookup_online("possibility")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revel(self):
        html_dump = lookup_online("revel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supplicant(self):
        html_dump = lookup_online("supplicant")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caldron(self):
        html_dump = lookup_online("caldron")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amenity(self):
        html_dump = lookup_online("amenity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supersede(self):
        html_dump = lookup_online("supersede")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fracture(self):
        html_dump = lookup_online("fracture")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nettle(self):
        html_dump = lookup_online("nettle")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heed(self):
        html_dump = lookup_online("heed")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aproximate(self):
        html_dump = lookup_online("aproximate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regicide(self):
        html_dump = lookup_online("regicide")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cursory(self):
        html_dump = lookup_online("cursory")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pamphlet(self):
        html_dump = lookup_online("pamphlet")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uppercut(self):
        html_dump = lookup_online("uppercut")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duffer(self):
        html_dump = lookup_online("duffer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thence(self):
        html_dump = lookup_online("thence")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humdrum(self):
        html_dump = lookup_online("humdrum")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanguine(self):
        html_dump = lookup_online("sanguine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrivel(self):
        html_dump = lookup_online("shrivel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ermine(self):
        html_dump = lookup_online("ermine")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repress(self):
        html_dump = lookup_online("repress")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bruiser(self):
        html_dump = lookup_online("bruiser")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acclaim(self):
        html_dump = lookup_online("acclaim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poltergeist(self):
        html_dump = lookup_online("poltergeist")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_summit(self):
        html_dump = lookup_online("summit")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quack(self):
        html_dump = lookup_online("quack")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spiffy(self):
        html_dump = lookup_online("spiffy")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dew(self):
        html_dump = lookup_online("dew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aliment(self):
        html_dump = lookup_online("aliment")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concussion(self):
        html_dump = lookup_online("concussion")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_septuagenarian(self):
        html_dump = lookup_online("septuagenarian")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strew(self):
        html_dump = lookup_online("strew")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slobber(self):
        html_dump = lookup_online("slobber")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solvent(self):
        html_dump = lookup_online("solvent")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frank(self):
        html_dump = lookup_online("frank")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_royal(self):
        html_dump = lookup_online("royal")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barley(self):
        html_dump = lookup_online("barley")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clench(self):
        html_dump = lookup_online("clench")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imperturbable(self):
        html_dump = lookup_online("imperturbable")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranquilize(self):
        html_dump = lookup_online("tranquilize")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virgil(self):
        html_dump = lookup_online("virgil")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lentils(self):
        html_dump = lookup_online("lentils")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incongruity(self):
        html_dump = lookup_online("incongruity")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proclaim(self):
        html_dump = lookup_online("proclaim")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appreciate(self):
        html_dump = lookup_online("appreciate")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broth(self):
        html_dump = lookup_online("broth")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humble(self):
        html_dump = lookup_online("humble")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vitriol(self):
        html_dump = lookup_online("vitriol")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afflict(self):
        html_dump = lookup_online("afflict")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subdue(self):
        html_dump = lookup_online("subdue")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laceration(self):
        html_dump = lookup_online("laceration")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arthritis(self):
        html_dump = lookup_online("arthritis")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liason(self):
        html_dump = lookup_online("liason")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaporware(self):
        html_dump = lookup_online("vaporware")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oust(self):
        html_dump = lookup_online("oust")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaunty(self):
        html_dump = lookup_online("jaunty")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haunting(self):
        html_dump = lookup_online("haunting")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misnomer(self):
        html_dump = lookup_online("misnomer")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_layman(self):
        html_dump = lookup_online("layman")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elusive(self):
        html_dump = lookup_online("elusive")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedated(self):
        html_dump = lookup_online("sedated")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hovel(self):
        html_dump = lookup_online("hovel")
        result = parse_en_pl(html_dump)
        f_result = to_dict(_parse_html(html_dump))
        assert result == f_result

