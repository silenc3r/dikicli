import os
import tempfile
import shutil
import pytest
from dikicli.core import lookup_online
from dikicli.core import _parse_html
from dikicli.helpers import flatten
from dikicli.parsers import (
    parse_en_pl,
    Entity,
    Meaning,
    PartOfSpeech,
    Sentence,
)


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
        html_dump = lookup_online("pawning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apparently(self):
        html_dump = lookup_online("apparently").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scathe(self):
        html_dump = lookup_online("scathe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fecund(self):
        html_dump = lookup_online("fecund").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caucus(self):
        html_dump = lookup_online("caucus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pamper(self):
        html_dump = lookup_online("pamper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venerated(self):
        html_dump = lookup_online("venerated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suppleness(self):
        html_dump = lookup_online("suppleness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mingle(self):
        html_dump = lookup_online("mingle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blitheness(self):
        html_dump = lookup_online("blitheness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mulligan(self):
        html_dump = lookup_online("mulligan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascent(self):
        html_dump = lookup_online("ascent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nonchalant(self):
        html_dump = lookup_online("nonchalant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pundit(self):
        html_dump = lookup_online("pundit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cervical(self):
        html_dump = lookup_online("cervical").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggravate(self):
        html_dump = lookup_online("aggravate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commissioner(self):
        html_dump = lookup_online("commissioner").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oracular(self):
        html_dump = lookup_online("oracular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_giardia(self):
        html_dump = lookup_online("giardia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swathe(self):
        html_dump = lookup_online("swathe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_daub(self):
        html_dump = lookup_online("daub").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feline(self):
        html_dump = lookup_online("feline").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garret(self):
        html_dump = lookup_online("garret").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Solidarity(self):
        html_dump = lookup_online("Solidarity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drudgery(self):
        html_dump = lookup_online("drudgery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hosier(self):
        html_dump = lookup_online("hosier").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remarkable(self):
        html_dump = lookup_online("remarkable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cusp(self):
        html_dump = lookup_online("cusp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endeavor(self):
        html_dump = lookup_online("endeavor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embellishment(self):
        html_dump = lookup_online("embellishment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commend(self):
        html_dump = lookup_online("commend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palliative(self):
        html_dump = lookup_online("palliative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parishioner(self):
        html_dump = lookup_online("parishioner").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_millipede(self):
        html_dump = lookup_online("millipede").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kludge(self):
        html_dump = lookup_online("kludge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_introspection(self):
        html_dump = lookup_online("introspection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinnacle(self):
        html_dump = lookup_online("pinnacle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ballpark(self):
        html_dump = lookup_online("ballpark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantrum(self):
        html_dump = lookup_online("tantrum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disconcerting(self):
        html_dump = lookup_online("disconcerting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_missive(self):
        html_dump = lookup_online("missive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feigned(self):
        html_dump = lookup_online("feigned").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deferral(self):
        html_dump = lookup_online("deferral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manure(self):
        html_dump = lookup_online("manure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penury(self):
        html_dump = lookup_online("penury").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fringe(self):
        html_dump = lookup_online("fringe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coincidence(self):
        html_dump = lookup_online("coincidence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_surmount(self):
        html_dump = lookup_online("surmount").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succor(self):
        html_dump = lookup_online("succor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amatory(self):
        html_dump = lookup_online("amatory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_needlessly(self):
        html_dump = lookup_online("needlessly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yearn(self):
        html_dump = lookup_online("yearn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upheaval(self):
        html_dump = lookup_online("upheaval").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contented(self):
        html_dump = lookup_online("contented").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snarly(self):
        html_dump = lookup_online("snarly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transitively(self):
        html_dump = lookup_online("transitively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenable(self):
        html_dump = lookup_online("tenable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chlamydia(self):
        html_dump = lookup_online("chlamydia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cache(self):
        html_dump = lookup_online("cache").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crude(self):
        html_dump = lookup_online("crude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bint(self):
        html_dump = lookup_online("bint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dour(self):
        html_dump = lookup_online("dour").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pillock(self):
        html_dump = lookup_online("pillock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crater(self):
        html_dump = lookup_online("crater").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_finagle(self):
        html_dump = lookup_online("finagle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veer(self):
        html_dump = lookup_online("veer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boomlet(self):
        html_dump = lookup_online("boomlet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rose(self):
        html_dump = lookup_online("rose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mayhem(self):
        html_dump = lookup_online("mayhem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renowned(self):
        html_dump = lookup_online("renowned").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ephemeral(self):
        html_dump = lookup_online("ephemeral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sensible(self):
        html_dump = lookup_online("sensible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blustery(self):
        html_dump = lookup_online("blustery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virulent(self):
        html_dump = lookup_online("virulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adrift(self):
        html_dump = lookup_online("adrift").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rascal(self):
        html_dump = lookup_online("rascal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hodgepodge(self):
        html_dump = lookup_online("hodgepodge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humongous(self):
        html_dump = lookup_online("humongous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stocky(self):
        html_dump = lookup_online("stocky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reef(self):
        html_dump = lookup_online("reef").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cervix(self):
        html_dump = lookup_online("cervix").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maroon(self):
        html_dump = lookup_online("maroon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grubby(self):
        html_dump = lookup_online("grubby").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serendipitous(self):
        html_dump = lookup_online("serendipitous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_altercation(self):
        html_dump = lookup_online("altercation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bravado(self):
        html_dump = lookup_online("bravado").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eerie(self):
        html_dump = lookup_online("eerie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thaw(self):
        html_dump = lookup_online("thaw").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewildering(self):
        html_dump = lookup_online("bewildering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taint(self):
        html_dump = lookup_online("taint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vie(self):
        html_dump = lookup_online("vie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agenda(self):
        html_dump = lookup_online("agenda").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midst(self):
        html_dump = lookup_online("midst").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_churn(self):
        html_dump = lookup_online("churn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nexus(self):
        html_dump = lookup_online("nexus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oat(self):
        html_dump = lookup_online("oat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chastity(self):
        html_dump = lookup_online("chastity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poplar(self):
        html_dump = lookup_online("poplar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glazed(self):
        html_dump = lookup_online("glazed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seethe(self):
        html_dump = lookup_online("seethe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serene(self):
        html_dump = lookup_online("serene").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tempestuous(self):
        html_dump = lookup_online("tempestuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stoked(self):
        html_dump = lookup_online("stoked").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantalize(self):
        html_dump = lookup_online("tantalize").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mesmerizing(self):
        html_dump = lookup_online("mesmerizing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gull(self):
        html_dump = lookup_online("gull").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stratify(self):
        html_dump = lookup_online("stratify").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derive(self):
        html_dump = lookup_online("derive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_absentminded(self):
        html_dump = lookup_online("absentminded").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoonful(self):
        html_dump = lookup_online("spoonful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_munchkin(self):
        html_dump = lookup_online("munchkin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peppy(self):
        html_dump = lookup_online("peppy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flummoxed(self):
        html_dump = lookup_online("flummoxed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurt(self):
        html_dump = lookup_online("spurt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_linger(self):
        html_dump = lookup_online("linger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crumple(self):
        html_dump = lookup_online("crumple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inundate(self):
        html_dump = lookup_online("inundate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smut(self):
        html_dump = lookup_online("smut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elicit(self):
        html_dump = lookup_online("elicit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acme(self):
        html_dump = lookup_online("acme").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neurotic(self):
        html_dump = lookup_online("neurotic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_restless(self):
        html_dump = lookup_online("restless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exaltation(self):
        html_dump = lookup_online("exaltation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tether(self):
        html_dump = lookup_online("tether").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_communion(self):
        html_dump = lookup_online("communion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fuselage(self):
        html_dump = lookup_online("fuselage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plenitude(self):
        html_dump = lookup_online("plenitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proxy(self):
        html_dump = lookup_online("proxy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucidity(self):
        html_dump = lookup_online("lucidity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_navel(self):
        html_dump = lookup_online("navel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opulent(self):
        html_dump = lookup_online("opulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bijective(self):
        html_dump = lookup_online("bijective").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_underpin(self):
        html_dump = lookup_online("underpin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pneumonia(self):
        html_dump = lookup_online("pneumonia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relentlessly(self):
        html_dump = lookup_online("relentlessly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_provost(self):
        html_dump = lookup_online("provost").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spruce(self):
        html_dump = lookup_online("spruce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nix(self):
        html_dump = lookup_online("nix").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_damsel(self):
        html_dump = lookup_online("damsel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enthrall(self):
        html_dump = lookup_online("enthrall").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glitzy(self):
        html_dump = lookup_online("glitzy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tithing(self):
        html_dump = lookup_online("tithing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jettison(self):
        html_dump = lookup_online("jettison").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bugle(self):
        html_dump = lookup_online("bugle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aspen(self):
        html_dump = lookup_online("aspen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pang(self):
        html_dump = lookup_online("pang").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limbo(self):
        html_dump = lookup_online("limbo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opportunistic(self):
        html_dump = lookup_online("opportunistic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_platitude(self):
        html_dump = lookup_online("platitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kale(self):
        html_dump = lookup_online("kale").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apricot(self):
        html_dump = lookup_online("apricot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flak(self):
        html_dump = lookup_online("flak").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowry(self):
        html_dump = lookup_online("dowry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concoct(self):
        html_dump = lookup_online("concoct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mute(self):
        html_dump = lookup_online("mute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuine(self):
        html_dump = lookup_online("genuine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impartial(self):
        html_dump = lookup_online("impartial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliers(self):
        html_dump = lookup_online("pliers").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plod(self):
        html_dump = lookup_online("plod").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestigial(self):
        html_dump = lookup_online("vestigial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vest(self):
        html_dump = lookup_online("vest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cohesion(self):
        html_dump = lookup_online("cohesion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pauper(self):
        html_dump = lookup_online("pauper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhilarating(self):
        html_dump = lookup_online("exhilarating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sumptuous(self):
        html_dump = lookup_online("sumptuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gratuitous(self):
        html_dump = lookup_online("gratuitous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meddle(self):
        html_dump = lookup_online("meddle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yam(self):
        html_dump = lookup_online("yam").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deftly(self):
        html_dump = lookup_online("deftly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fitful(self):
        html_dump = lookup_online("fitful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stilted(self):
        html_dump = lookup_online("stilted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unprepossessing(self):
        html_dump = lookup_online("unprepossessing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redemption(self):
        html_dump = lookup_online("redemption").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_planer(self):
        html_dump = lookup_online("planer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wimpy(self):
        html_dump = lookup_online("wimpy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evocative(self):
        html_dump = lookup_online("evocative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predicate(self):
        html_dump = lookup_online("predicate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sophistry(self):
        html_dump = lookup_online("sophistry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permanence(self):
        html_dump = lookup_online("permanence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deranged(self):
        html_dump = lookup_online("deranged").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disingenuous(self):
        html_dump = lookup_online("disingenuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fizzle(self):
        html_dump = lookup_online("fizzle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dinky(self):
        html_dump = lookup_online("dinky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stranglehold(self):
        html_dump = lookup_online("stranglehold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yap(self):
        html_dump = lookup_online("yap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grogginess(self):
        html_dump = lookup_online("grogginess").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exertion(self):
        html_dump = lookup_online("exertion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solicite(self):
        html_dump = lookup_online("solicite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_custard(self):
        html_dump = lookup_online("custard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irreverence(self):
        html_dump = lookup_online("irreverence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutted(self):
        html_dump = lookup_online("gutted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cashew(self):
        html_dump = lookup_online("cashew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaff(self):
        html_dump = lookup_online("gaff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seclude(self):
        html_dump = lookup_online("seclude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seditious(self):
        html_dump = lookup_online("seditious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sassy(self):
        html_dump = lookup_online("sassy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endearing(self):
        html_dump = lookup_online("endearing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maintainer(self):
        html_dump = lookup_online("maintainer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealous(self):
        html_dump = lookup_online("zealous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kiln(self):
        html_dump = lookup_online("kiln").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chagrin(self):
        html_dump = lookup_online("chagrin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oud(self):
        html_dump = lookup_online("oud").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squalid(self):
        html_dump = lookup_online("squalid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plaster(self):
        html_dump = lookup_online("plaster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obnoxious(self):
        html_dump = lookup_online("obnoxious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_idem(self):
        html_dump = lookup_online("idem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_realtor(self):
        html_dump = lookup_online("realtor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chivalry(self):
        html_dump = lookup_online("chivalry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tussle(self):
        html_dump = lookup_online("tussle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vile(self):
        html_dump = lookup_online("vile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clumsy(self):
        html_dump = lookup_online("clumsy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derelict(self):
        html_dump = lookup_online("derelict").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trite(self):
        html_dump = lookup_online("trite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procurement(self):
        html_dump = lookup_online("procurement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cannily(self):
        html_dump = lookup_online("cannily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_femur(self):
        html_dump = lookup_online("femur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infibulate(self):
        html_dump = lookup_online("infibulate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rampage(self):
        html_dump = lookup_online("rampage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruinous(self):
        html_dump = lookup_online("ruinous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soliloquy(self):
        html_dump = lookup_online("soliloquy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wreath(self):
        html_dump = lookup_online("wreath").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deceit(self):
        html_dump = lookup_online("deceit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vermin(self):
        html_dump = lookup_online("vermin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrid(self):
        html_dump = lookup_online("acrid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foreman(self):
        html_dump = lookup_online("foreman").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pep(self):
        html_dump = lookup_online("pep").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meadowlark(self):
        html_dump = lookup_online("meadowlark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petite(self):
        html_dump = lookup_online("petite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thistle(self):
        html_dump = lookup_online("thistle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenure(self):
        html_dump = lookup_online("tenure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incense(self):
        html_dump = lookup_online("incense").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_easel(self):
        html_dump = lookup_online("easel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predicament(self):
        html_dump = lookup_online("predicament").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portly(self):
        html_dump = lookup_online("portly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exasperating(self):
        html_dump = lookup_online("exasperating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rancorous(self):
        html_dump = lookup_online("rancorous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punditry(self):
        html_dump = lookup_online("punditry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notoriety(self):
        html_dump = lookup_online("notoriety").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holster(self):
        html_dump = lookup_online("holster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pithy(self):
        html_dump = lookup_online("pithy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ableism(self):
        html_dump = lookup_online("ableism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congruence(self):
        html_dump = lookup_online("congruence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pronounced(self):
        html_dump = lookup_online("pronounced").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flounder(self):
        html_dump = lookup_online("flounder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serendipity(self):
        html_dump = lookup_online("serendipity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coveted(self):
        html_dump = lookup_online("coveted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revet(self):
        html_dump = lookup_online("revet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_etch(self):
        html_dump = lookup_online("etch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleight(self):
        html_dump = lookup_online("sleight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poignant(self):
        html_dump = lookup_online("poignant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chirality(self):
        html_dump = lookup_online("chirality").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assiduously(self):
        html_dump = lookup_online("assiduously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gait(self):
        html_dump = lookup_online("gait").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blindside(self):
        html_dump = lookup_online("blindside").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_putter(self):
        html_dump = lookup_online("putter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phony(self):
        html_dump = lookup_online("phony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidelity(self):
        html_dump = lookup_online("fidelity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sore(self):
        html_dump = lookup_online("sore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splendid(self):
        html_dump = lookup_online("splendid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hamlet(self):
        html_dump = lookup_online("hamlet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoist(self):
        html_dump = lookup_online("hoist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_depress(self):
        html_dump = lookup_online("depress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_felony(self):
        html_dump = lookup_online("felony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_androgen(self):
        html_dump = lookup_online("androgen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asset(self):
        html_dump = lookup_online("asset").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auspicious(self):
        html_dump = lookup_online("auspicious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallow(self):
        html_dump = lookup_online("fallow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discord(self):
        html_dump = lookup_online("discord").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gullible(self):
        html_dump = lookup_online("gullible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enema(self):
        html_dump = lookup_online("enema").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vindicate(self):
        html_dump = lookup_online("vindicate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kelp(self):
        html_dump = lookup_online("kelp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouse(self):
        html_dump = lookup_online("grouse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lenient(self):
        html_dump = lookup_online("lenient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_esophagus(self):
        html_dump = lookup_online("esophagus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_angst(self):
        html_dump = lookup_online("angst").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fink(self):
        html_dump = lookup_online("fink").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foo(self):
        html_dump = lookup_online("foo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congruent(self):
        html_dump = lookup_online("congruent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cerebellum(self):
        html_dump = lookup_online("cerebellum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creepy(self):
        html_dump = lookup_online("creepy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobweb(self):
        html_dump = lookup_online("cobweb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inertia(self):
        html_dump = lookup_online("inertia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_legibility(self):
        html_dump = lookup_online("legibility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flock(self):
        html_dump = lookup_online("flock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foray(self):
        html_dump = lookup_online("foray").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tender(self):
        html_dump = lookup_online("tender").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exude(self):
        html_dump = lookup_online("exude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiefdom(self):
        html_dump = lookup_online("fiefdom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inert(self):
        html_dump = lookup_online("inert").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_devise(self):
        html_dump = lookup_online("devise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knuckle(self):
        html_dump = lookup_online("knuckle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulverize(self):
        html_dump = lookup_online("pulverize").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantamount(self):
        html_dump = lookup_online("tantamount").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dole(self):
        html_dump = lookup_online("dole").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attrit(self):
        html_dump = lookup_online("attrit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_battery(self):
        html_dump = lookup_online("battery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myopic(self):
        html_dump = lookup_online("myopic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affectionate(self):
        html_dump = lookup_online("affectionate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malodorous(self):
        html_dump = lookup_online("malodorous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seaweed(self):
        html_dump = lookup_online("seaweed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resentment(self):
        html_dump = lookup_online("resentment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_causation(self):
        html_dump = lookup_online("causation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_critic(self):
        html_dump = lookup_online("critic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stiffen(self):
        html_dump = lookup_online("stiffen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minimalist(self):
        html_dump = lookup_online("minimalist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deprecate(self):
        html_dump = lookup_online("deprecate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pet(self):
        html_dump = lookup_online("pet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dye(self):
        html_dump = lookup_online("dye").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluble(self):
        html_dump = lookup_online("voluble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chisel(self):
        html_dump = lookup_online("chisel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renounce(self):
        html_dump = lookup_online("renounce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bereavement(self):
        html_dump = lookup_online("bereavement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sustain(self):
        html_dump = lookup_online("sustain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carbohydrate(self):
        html_dump = lookup_online("carbohydrate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luddite(self):
        html_dump = lookup_online("luddite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verbiage(self):
        html_dump = lookup_online("verbiage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anoint(self):
        html_dump = lookup_online("anoint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mint(self):
        html_dump = lookup_online("mint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_would(self):
        html_dump = lookup_online("would").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insinuate(self):
        html_dump = lookup_online("insinuate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malice(self):
        html_dump = lookup_online("malice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rescind(self):
        html_dump = lookup_online("rescind").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broil(self):
        html_dump = lookup_online("broil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stout(self):
        html_dump = lookup_online("stout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobbles(self):
        html_dump = lookup_online("cobbles").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parse(self):
        html_dump = lookup_online("parse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dysentery(self):
        html_dump = lookup_online("dysentery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abide(self):
        html_dump = lookup_online("abide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraught(self):
        html_dump = lookup_online("fraught").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastoral(self):
        html_dump = lookup_online("pastoral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quell(self):
        html_dump = lookup_online("quell").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awl(self):
        html_dump = lookup_online("awl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_darkly(self):
        html_dump = lookup_online("darkly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_viceroy(self):
        html_dump = lookup_online("viceroy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagrant(self):
        html_dump = lookup_online("flagrant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_could(self):
        html_dump = lookup_online("could").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trenchant(self):
        html_dump = lookup_online("trenchant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rupture(self):
        html_dump = lookup_online("rupture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcer(self):
        html_dump = lookup_online("ulcer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaguely(self):
        html_dump = lookup_online("vaguely").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumult(self):
        html_dump = lookup_online("tumult").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candor(self):
        html_dump = lookup_online("candor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conducive(self):
        html_dump = lookup_online("conducive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subordinate(self):
        html_dump = lookup_online("subordinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excoriate(self):
        html_dump = lookup_online("excoriate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merciless(self):
        html_dump = lookup_online("merciless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abominable(self):
        html_dump = lookup_online("abominable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turbulent(self):
        html_dump = lookup_online("turbulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lambast(self):
        html_dump = lookup_online("lambast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defiance(self):
        html_dump = lookup_online("defiance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overcast(self):
        html_dump = lookup_online("overcast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salient(self):
        html_dump = lookup_online("salient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_these(self):
        html_dump = lookup_online("these").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_valiantly(self):
        html_dump = lookup_online("valiantly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucid(self):
        html_dump = lookup_online("lucid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbated(self):
        html_dump = lookup_online("exacerbated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commutative(self):
        html_dump = lookup_online("commutative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coarse(self):
        html_dump = lookup_online("coarse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superficial(self):
        html_dump = lookup_online("superficial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscientious(self):
        html_dump = lookup_online("conscientious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hillock(self):
        html_dump = lookup_online("hillock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alluvial(self):
        html_dump = lookup_online("alluvial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_viscous(self):
        html_dump = lookup_online("viscous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beguiling(self):
        html_dump = lookup_online("beguiling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manifold(self):
        html_dump = lookup_online("manifold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scallop(self):
        html_dump = lookup_online("scallop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recourse(self):
        html_dump = lookup_online("recourse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whisked(self):
        html_dump = lookup_online("whisked").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feeble(self):
        html_dump = lookup_online("feeble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_levy(self):
        html_dump = lookup_online("levy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corral(self):
        html_dump = lookup_online("corral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cluck(self):
        html_dump = lookup_online("cluck").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chasm(self):
        html_dump = lookup_online("chasm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_latitude(self):
        html_dump = lookup_online("latitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incessant(self):
        html_dump = lookup_online("incessant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mar(self):
        html_dump = lookup_online("mar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mandarin(self):
        html_dump = lookup_online("mandarin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangy(self):
        html_dump = lookup_online("tangy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palatable(self):
        html_dump = lookup_online("palatable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avery(self):
        html_dump = lookup_online("avery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insidiously(self):
        html_dump = lookup_online("insidiously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouchiness(self):
        html_dump = lookup_online("grouchiness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_traduce(self):
        html_dump = lookup_online("traduce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumble(self):
        html_dump = lookup_online("rumble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_timber(self):
        html_dump = lookup_online("timber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indulgence(self):
        html_dump = lookup_online("indulgence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yttria(self):
        html_dump = lookup_online("yttria").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crest(self):
        html_dump = lookup_online("crest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apple(self):
        html_dump = lookup_online("apple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whirl(self):
        html_dump = lookup_online("whirl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrutiny(self):
        html_dump = lookup_online("scrutiny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abandon(self):
        html_dump = lookup_online("abandon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creed(self):
        html_dump = lookup_online("creed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aghast(self):
        html_dump = lookup_online("aghast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concession(self):
        html_dump = lookup_online("concession").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contest(self):
        html_dump = lookup_online("contest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unravel(self):
        html_dump = lookup_online("unravel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whimper(self):
        html_dump = lookup_online("whimper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nigh(self):
        html_dump = lookup_online("nigh").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_molasses(self):
        html_dump = lookup_online("molasses").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revered(self):
        html_dump = lookup_online("revered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_captivity(self):
        html_dump = lookup_online("captivity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unanimous(self):
        html_dump = lookup_online("unanimous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminence(self):
        html_dump = lookup_online("eminence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juggernaut(self):
        html_dump = lookup_online("juggernaut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laudanum(self):
        html_dump = lookup_online("laudanum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interdict(self):
        html_dump = lookup_online("interdict").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fulfill(self):
        html_dump = lookup_online("fulfill").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_groggy(self):
        html_dump = lookup_online("groggy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paucity(self):
        html_dump = lookup_online("paucity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morrow(self):
        html_dump = lookup_online("morrow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_porous(self):
        html_dump = lookup_online("porous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sodding(self):
        html_dump = lookup_online("sodding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beholden(self):
        html_dump = lookup_online("beholden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eyesore(self):
        html_dump = lookup_online("eyesore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vainglory(self):
        html_dump = lookup_online("vainglory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coalesce(self):
        html_dump = lookup_online("coalesce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fester(self):
        html_dump = lookup_online("fester").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petulance(self):
        html_dump = lookup_online("petulance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leniency(self):
        html_dump = lookup_online("leniency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debris(self):
        html_dump = lookup_online("debris").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vanity(self):
        html_dump = lookup_online("vanity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compel(self):
        html_dump = lookup_online("compel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solipsist(self):
        html_dump = lookup_online("solipsist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_betide(self):
        html_dump = lookup_online("betide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ludicrous(self):
        html_dump = lookup_online("ludicrous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chant(self):
        html_dump = lookup_online("chant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hound(self):
        html_dump = lookup_online("hound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ideation(self):
        html_dump = lookup_online("ideation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infamy(self):
        html_dump = lookup_online("infamy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leshy(self):
        html_dump = lookup_online("leshy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contemporary(self):
        html_dump = lookup_online("contemporary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muck(self):
        html_dump = lookup_online("muck").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abutting(self):
        html_dump = lookup_online("abutting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaunt(self):
        html_dump = lookup_online("gaunt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distaste(self):
        html_dump = lookup_online("distaste").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjugation(self):
        html_dump = lookup_online("conjugation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicissitude(self):
        html_dump = lookup_online("vicissitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouper(self):
        html_dump = lookup_online("grouper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bespoke(self):
        html_dump = lookup_online("bespoke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protraction(self):
        html_dump = lookup_online("protraction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aphasia(self):
        html_dump = lookup_online("aphasia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sluice(self):
        html_dump = lookup_online("sluice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ivory(self):
        html_dump = lookup_online("ivory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lichen(self):
        html_dump = lookup_online("lichen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avon(self):
        html_dump = lookup_online("avon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscientiousness(self):
        html_dump = lookup_online("conscientiousness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_complex(self):
        html_dump = lookup_online("complex").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pried(self):
        html_dump = lookup_online("pried").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entail(self):
        html_dump = lookup_online("entail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unrepentant(self):
        html_dump = lookup_online("unrepentant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plateau(self):
        html_dump = lookup_online("plateau").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pus(self):
        html_dump = lookup_online("pus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vignette(self):
        html_dump = lookup_online("vignette").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenet(self):
        html_dump = lookup_online("tenet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedition(self):
        html_dump = lookup_online("sedition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snub(self):
        html_dump = lookup_online("snub").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_buoyant(self):
        html_dump = lookup_online("buoyant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pushy(self):
        html_dump = lookup_online("pushy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_walnut(self):
        html_dump = lookup_online("walnut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stuffy(self):
        html_dump = lookup_online("stuffy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetual(self):
        html_dump = lookup_online("perpetual").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procurer(self):
        html_dump = lookup_online("procurer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sander(self):
        html_dump = lookup_online("sander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wokeness(self):
        html_dump = lookup_online("wokeness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fluke(self):
        html_dump = lookup_online("fluke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrill(self):
        html_dump = lookup_online("shrill").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snubbed(self):
        html_dump = lookup_online("snubbed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orifice(self):
        html_dump = lookup_online("orifice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ignoramus(self):
        html_dump = lookup_online("ignoramus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remission(self):
        html_dump = lookup_online("remission").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diligence(self):
        html_dump = lookup_online("diligence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heredity(self):
        html_dump = lookup_online("heredity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vertebrate(self):
        html_dump = lookup_online("vertebrate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pegboard(self):
        html_dump = lookup_online("pegboard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infringement(self):
        html_dump = lookup_online("infringement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desolation(self):
        html_dump = lookup_online("desolation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tend(self):
        html_dump = lookup_online("tend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adjourn(self):
        html_dump = lookup_online("adjourn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permeate(self):
        html_dump = lookup_online("permeate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heft(self):
        html_dump = lookup_online("heft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utterance(self):
        html_dump = lookup_online("utterance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_careen(self):
        html_dump = lookup_online("careen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_VAT(self):
        html_dump = lookup_online("VAT").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turnip(self):
        html_dump = lookup_online("turnip").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paragon(self):
        html_dump = lookup_online("paragon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pecan(self):
        html_dump = lookup_online("pecan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peruse(self):
        html_dump = lookup_online("peruse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_putty(self):
        html_dump = lookup_online("putty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cotton(self):
        html_dump = lookup_online("cotton").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraternity(self):
        html_dump = lookup_online("fraternity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caldera(self):
        html_dump = lookup_online("caldera").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mellow(self):
        html_dump = lookup_online("mellow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emasculate(self):
        html_dump = lookup_online("emasculate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stewardship(self):
        html_dump = lookup_online("stewardship").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incontinence(self):
        html_dump = lookup_online("incontinence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gendarmerie(self):
        html_dump = lookup_online("gendarmerie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splurge(self):
        html_dump = lookup_online("splurge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ebony(self):
        html_dump = lookup_online("ebony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redeem(self):
        html_dump = lookup_online("redeem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slut(self):
        html_dump = lookup_online("slut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_invalidation(self):
        html_dump = lookup_online("invalidation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoil(self):
        html_dump = lookup_online("spoil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heinous(self):
        html_dump = lookup_online("heinous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grazing(self):
        html_dump = lookup_online("grazing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_galore(self):
        html_dump = lookup_online("galore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brine(self):
        html_dump = lookup_online("brine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mirthless(self):
        html_dump = lookup_online("mirthless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstructive(self):
        html_dump = lookup_online("obstructive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ponderous(self):
        html_dump = lookup_online("ponderous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indispensable(self):
        html_dump = lookup_online("indispensable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sullen(self):
        html_dump = lookup_online("sullen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prance(self):
        html_dump = lookup_online("prance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_content(self):
        html_dump = lookup_online("content").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squander(self):
        html_dump = lookup_online("squander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bedridden(self):
        html_dump = lookup_online("bedridden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bore(self):
        html_dump = lookup_online("bore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pursuer(self):
        html_dump = lookup_online("pursuer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_offspring(self):
        html_dump = lookup_online("offspring").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manacle(self):
        html_dump = lookup_online("manacle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parochial(self):
        html_dump = lookup_online("parochial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ribald(self):
        html_dump = lookup_online("ribald").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loaf(self):
        html_dump = lookup_online("loaf").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crevice(self):
        html_dump = lookup_online("crevice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cow(self):
        html_dump = lookup_online("cow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cello(self):
        html_dump = lookup_online("cello").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cuneiform(self):
        html_dump = lookup_online("cuneiform").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contort(self):
        html_dump = lookup_online("contort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudent(self):
        html_dump = lookup_online("prudent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riveting(self):
        html_dump = lookup_online("riveting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wryly(self):
        html_dump = lookup_online("wryly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protomartyr(self):
        html_dump = lookup_online("protomartyr").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taxidermist(self):
        html_dump = lookup_online("taxidermist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_addled(self):
        html_dump = lookup_online("addled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_germinate(self):
        html_dump = lookup_online("germinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stipulate(self):
        html_dump = lookup_online("stipulate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anathema(self):
        html_dump = lookup_online("anathema").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feathered(self):
        html_dump = lookup_online("feathered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rowan(self):
        html_dump = lookup_online("rowan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rectifier(self):
        html_dump = lookup_online("rectifier").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immediacy(self):
        html_dump = lookup_online("immediacy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_batter(self):
        html_dump = lookup_online("batter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_honky(self):
        html_dump = lookup_online("honky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruthless(self):
        html_dump = lookup_online("ruthless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deliberation(self):
        html_dump = lookup_online("deliberation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squib(self):
        html_dump = lookup_online("squib").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prophecy(self):
        html_dump = lookup_online("prophecy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slew(self):
        html_dump = lookup_online("slew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravine(self):
        html_dump = lookup_online("ravine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Levi(self):
        html_dump = lookup_online("Levi").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stunt(self):
        html_dump = lookup_online("stunt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effusively(self):
        html_dump = lookup_online("effusively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defer(self):
        html_dump = lookup_online("defer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coattail(self):
        html_dump = lookup_online("coattail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incriminate(self):
        html_dump = lookup_online("incriminate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feast(self):
        html_dump = lookup_online("feast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heave(self):
        html_dump = lookup_online("heave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_escalator(self):
        html_dump = lookup_online("escalator").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longshoreman(self):
        html_dump = lookup_online("longshoreman").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incinerate(self):
        html_dump = lookup_online("incinerate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glee(self):
        html_dump = lookup_online("glee").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consign(self):
        html_dump = lookup_online("consign").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coercion(self):
        html_dump = lookup_online("coercion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procure(self):
        html_dump = lookup_online("procure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_usher(self):
        html_dump = lookup_online("usher").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protagonist(self):
        html_dump = lookup_online("protagonist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discernible(self):
        html_dump = lookup_online("discernible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tropic(self):
        html_dump = lookup_online("tropic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_masonite(self):
        html_dump = lookup_online("masonite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spun(self):
        html_dump = lookup_online("spun").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penchant(self):
        html_dump = lookup_online("penchant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sombre(self):
        html_dump = lookup_online("sombre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_graze(self):
        html_dump = lookup_online("graze").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reeling(self):
        html_dump = lookup_online("reeling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plaid(self):
        html_dump = lookup_online("plaid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conscience(self):
        html_dump = lookup_online("conscience").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kindred(self):
        html_dump = lookup_online("kindred").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flatulence(self):
        html_dump = lookup_online("flatulence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adherent(self):
        html_dump = lookup_online("adherent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sacrosanct(self):
        html_dump = lookup_online("sacrosanct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heartburn(self):
        html_dump = lookup_online("heartburn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arduous(self):
        html_dump = lookup_online("arduous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_specter(self):
        html_dump = lookup_online("specter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pretence(self):
        html_dump = lookup_online("pretence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vain(self):
        html_dump = lookup_online("vain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emaciate(self):
        html_dump = lookup_online("emaciate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impediment(self):
        html_dump = lookup_online("impediment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salience(self):
        html_dump = lookup_online("salience").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_klutzy(self):
        html_dump = lookup_online("klutzy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disclosure(self):
        html_dump = lookup_online("disclosure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_philander(self):
        html_dump = lookup_online("philander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tidbit(self):
        html_dump = lookup_online("tidbit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jostle(self):
        html_dump = lookup_online("jostle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concord(self):
        html_dump = lookup_online("concord").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_residue(self):
        html_dump = lookup_online("residue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumultuous(self):
        html_dump = lookup_online("tumultuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_translucent(self):
        html_dump = lookup_online("translucent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cooties(self):
        html_dump = lookup_online("cooties").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_underlining(self):
        html_dump = lookup_online("underlining").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sog(self):
        html_dump = lookup_online("sog").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moose(self):
        html_dump = lookup_online("moose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eke(self):
        html_dump = lookup_online("eke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoggish(self):
        html_dump = lookup_online("hoggish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chafing(self):
        html_dump = lookup_online("chafing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nitpick(self):
        html_dump = lookup_online("nitpick").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clamp(self):
        html_dump = lookup_online("clamp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_usufruct(self):
        html_dump = lookup_online("usufruct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuple(self):
        html_dump = lookup_online("tuple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_volatile(self):
        html_dump = lookup_online("volatile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrink(self):
        html_dump = lookup_online("shrink").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cleavage(self):
        html_dump = lookup_online("cleavage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dint(self):
        html_dump = lookup_online("dint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckon(self):
        html_dump = lookup_online("reckon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nausea(self):
        html_dump = lookup_online("nausea").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vixen(self):
        html_dump = lookup_online("vixen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goop(self):
        html_dump = lookup_online("goop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strident(self):
        html_dump = lookup_online("strident").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_server(self):
        html_dump = lookup_online("server").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pebble(self):
        html_dump = lookup_online("pebble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turtle(self):
        html_dump = lookup_online("turtle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shard(self):
        html_dump = lookup_online("shard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smear(self):
        html_dump = lookup_online("smear").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterministic(self):
        html_dump = lookup_online("deterministic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chump(self):
        html_dump = lookup_online("chump").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mortician(self):
        html_dump = lookup_online("mortician").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penance(self):
        html_dump = lookup_online("penance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placid(self):
        html_dump = lookup_online("placid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maven(self):
        html_dump = lookup_online("maven").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertinent(self):
        html_dump = lookup_online("pertinent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cornucopia(self):
        html_dump = lookup_online("cornucopia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unmoored(self):
        html_dump = lookup_online("unmoored").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larch(self):
        html_dump = lookup_online("larch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blistering(self):
        html_dump = lookup_online("blistering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nutmeg(self):
        html_dump = lookup_online("nutmeg").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posit(self):
        html_dump = lookup_online("posit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_charter(self):
        html_dump = lookup_online("charter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oblivious(self):
        html_dump = lookup_online("oblivious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_schist(self):
        html_dump = lookup_online("schist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predilection(self):
        html_dump = lookup_online("predilection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solace(self):
        html_dump = lookup_online("solace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaunt(self):
        html_dump = lookup_online("vaunt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulchritude(self):
        html_dump = lookup_online("pulchritude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheapening(self):
        html_dump = lookup_online("cheapening").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impalpable(self):
        html_dump = lookup_online("impalpable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_severe(self):
        html_dump = lookup_online("severe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contingent(self):
        html_dump = lookup_online("contingent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_falter(self):
        html_dump = lookup_online("falter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swirl(self):
        html_dump = lookup_online("swirl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cratering(self):
        html_dump = lookup_online("cratering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_industrious(self):
        html_dump = lookup_online("industrious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crass(self):
        html_dump = lookup_online("crass").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quibble(self):
        html_dump = lookup_online("quibble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lacerate(self):
        html_dump = lookup_online("lacerate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arrear(self):
        html_dump = lookup_online("arrear").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wariness(self):
        html_dump = lookup_online("wariness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parable(self):
        html_dump = lookup_online("parable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congenial(self):
        html_dump = lookup_online("congenial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pusillanimity(self):
        html_dump = lookup_online("pusillanimity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grizzled(self):
        html_dump = lookup_online("grizzled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endorsement(self):
        html_dump = lookup_online("endorsement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upsell(self):
        html_dump = lookup_online("upsell").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blackened(self):
        html_dump = lookup_online("blackened").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sizzle(self):
        html_dump = lookup_online("sizzle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hawthorn(self):
        html_dump = lookup_online("hawthorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lotion(self):
        html_dump = lookup_online("lotion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_macaw(self):
        html_dump = lookup_online("macaw").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gust(self):
        html_dump = lookup_online("gust").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shank(self):
        html_dump = lookup_online("shank").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bramble(self):
        html_dump = lookup_online("bramble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corvid(self):
        html_dump = lookup_online("corvid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stud(self):
        html_dump = lookup_online("stud").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ceaselessly(self):
        html_dump = lookup_online("ceaselessly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crayfish(self):
        html_dump = lookup_online("crayfish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stern(self):
        html_dump = lookup_online("stern").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sapient(self):
        html_dump = lookup_online("sapient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arresting(self):
        html_dump = lookup_online("arresting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tentatively(self):
        html_dump = lookup_online("tentatively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retain(self):
        html_dump = lookup_online("retain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posterity(self):
        html_dump = lookup_online("posterity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lacklustre(self):
        html_dump = lookup_online("lacklustre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grungy(self):
        html_dump = lookup_online("grungy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_establish(self):
        html_dump = lookup_online("establish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asinine(self):
        html_dump = lookup_online("asinine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interdiction(self):
        html_dump = lookup_online("interdiction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clemency(self):
        html_dump = lookup_online("clemency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_circumvent(self):
        html_dump = lookup_online("circumvent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lark(self):
        html_dump = lookup_online("lark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adenoids(self):
        html_dump = lookup_online("adenoids").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veracity(self):
        html_dump = lookup_online("veracity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effuse(self):
        html_dump = lookup_online("effuse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_panache(self):
        html_dump = lookup_online("panache").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_isthmus(self):
        html_dump = lookup_online("isthmus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gestation(self):
        html_dump = lookup_online("gestation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quinine(self):
        html_dump = lookup_online("quinine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jugular(self):
        html_dump = lookup_online("jugular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exuberant(self):
        html_dump = lookup_online("exuberant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastry(self):
        html_dump = lookup_online("pastry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapscallion(self):
        html_dump = lookup_online("rapscallion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coherence(self):
        html_dump = lookup_online("coherence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poised(self):
        html_dump = lookup_online("poised").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pls(self):
        html_dump = lookup_online("pls").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quirky(self):
        html_dump = lookup_online("quirky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hopefully(self):
        html_dump = lookup_online("hopefully").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mantle(self):
        html_dump = lookup_online("mantle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tribulation(self):
        html_dump = lookup_online("tribulation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_to(self):
        html_dump = lookup_online("to").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knoll(self):
        html_dump = lookup_online("knoll").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abhor(self):
        html_dump = lookup_online("abhor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_illegitimacy(self):
        html_dump = lookup_online("illegitimacy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juxtaposition(self):
        html_dump = lookup_online("juxtaposition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shag(self):
        html_dump = lookup_online("shag").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immersion(self):
        html_dump = lookup_online("immersion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tactile(self):
        html_dump = lookup_online("tactile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haphazardly(self):
        html_dump = lookup_online("haphazardly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turf(self):
        html_dump = lookup_online("turf").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_basswood(self):
        html_dump = lookup_online("basswood").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rowdy(self):
        html_dump = lookup_online("rowdy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outwardly(self):
        html_dump = lookup_online("outwardly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_credible(self):
        html_dump = lookup_online("credible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fawning(self):
        html_dump = lookup_online("fawning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_closure(self):
        html_dump = lookup_online("closure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duplicitous(self):
        html_dump = lookup_online("duplicitous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scald(self):
        html_dump = lookup_online("scald").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparate(self):
        html_dump = lookup_online("disparate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endow(self):
        html_dump = lookup_online("endow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weasel(self):
        html_dump = lookup_online("weasel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gravitas(self):
        html_dump = lookup_online("gravitas").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_omniscient(self):
        html_dump = lookup_online("omniscient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rag(self):
        html_dump = lookup_online("rag").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rod(self):
        html_dump = lookup_online("rod").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suckle(self):
        html_dump = lookup_online("suckle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oxblood(self):
        html_dump = lookup_online("oxblood").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peckish(self):
        html_dump = lookup_online("peckish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tableau(self):
        html_dump = lookup_online("tableau").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attrition(self):
        html_dump = lookup_online("attrition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawler(self):
        html_dump = lookup_online("brawler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggrieved(self):
        html_dump = lookup_online("aggrieved").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shawty(self):
        html_dump = lookup_online("shawty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foible(self):
        html_dump = lookup_online("foible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slant(self):
        html_dump = lookup_online("slant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deer(self):
        html_dump = lookup_online("deer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flamboyant(self):
        html_dump = lookup_online("flamboyant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pat(self):
        html_dump = lookup_online("pat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vine(self):
        html_dump = lookup_online("vine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_iridescent(self):
        html_dump = lookup_online("iridescent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glean(self):
        html_dump = lookup_online("glean").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dope(self):
        html_dump = lookup_online("dope").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wanton(self):
        html_dump = lookup_online("wanton").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uppity(self):
        html_dump = lookup_online("uppity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_composure(self):
        html_dump = lookup_online("composure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pabulum(self):
        html_dump = lookup_online("pabulum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unremarkable(self):
        html_dump = lookup_online("unremarkable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clark(self):
        html_dump = lookup_online("clark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bosom(self):
        html_dump = lookup_online("bosom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discrete(self):
        html_dump = lookup_online("discrete").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleet(self):
        html_dump = lookup_online("sleet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rarefaction(self):
        html_dump = lookup_online("rarefaction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hubcap(self):
        html_dump = lookup_online("hubcap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tatters(self):
        html_dump = lookup_online("tatters").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tack(self):
        html_dump = lookup_online("tack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crumpet(self):
        html_dump = lookup_online("crumpet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bawl(self):
        html_dump = lookup_online("bawl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_funnel(self):
        html_dump = lookup_online("funnel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leisure(self):
        html_dump = lookup_online("leisure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rolodex(self):
        html_dump = lookup_online("rolodex").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cupola(self):
        html_dump = lookup_online("cupola").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eczema(self):
        html_dump = lookup_online("eczema").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_festoon(self):
        html_dump = lookup_online("festoon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drivel(self):
        html_dump = lookup_online("drivel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicinity(self):
        html_dump = lookup_online("vicinity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_starlight(self):
        html_dump = lookup_online("starlight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_decimate(self):
        html_dump = lookup_online("decimate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impugning(self):
        html_dump = lookup_online("impugning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stew(self):
        html_dump = lookup_online("stew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sensibly(self):
        html_dump = lookup_online("sensibly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dengue(self):
        html_dump = lookup_online("dengue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convent(self):
        html_dump = lookup_online("convent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allotment(self):
        html_dump = lookup_online("allotment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bicentennial(self):
        html_dump = lookup_online("bicentennial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_astute(self):
        html_dump = lookup_online("astute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edification(self):
        html_dump = lookup_online("edification").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ail(self):
        html_dump = lookup_online("ail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tally(self):
        html_dump = lookup_online("tally").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cordial(self):
        html_dump = lookup_online("cordial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_racoon(self):
        html_dump = lookup_online("racoon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tepid(self):
        html_dump = lookup_online("tepid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detriment(self):
        html_dump = lookup_online("detriment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mercurial(self):
        html_dump = lookup_online("mercurial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_timbre(self):
        html_dump = lookup_online("timbre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appalling(self):
        html_dump = lookup_online("appalling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewilderment(self):
        html_dump = lookup_online("bewilderment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_livid(self):
        html_dump = lookup_online("livid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wailing(self):
        html_dump = lookup_online("wailing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_devious(self):
        html_dump = lookup_online("devious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_axiom(self):
        html_dump = lookup_online("axiom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tarp(self):
        html_dump = lookup_online("tarp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacitly(self):
        html_dump = lookup_online("tacitly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tug(self):
        html_dump = lookup_online("tug").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrappy(self):
        html_dump = lookup_online("scrappy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_payoff(self):
        html_dump = lookup_online("payoff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_animosity(self):
        html_dump = lookup_online("animosity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lupine(self):
        html_dump = lookup_online("lupine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asunder(self):
        html_dump = lookup_online("asunder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwitting(self):
        html_dump = lookup_online("unwitting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quisling(self):
        html_dump = lookup_online("quisling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_connoisseur(self):
        html_dump = lookup_online("connoisseur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaporous(self):
        html_dump = lookup_online("vaporous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harlot(self):
        html_dump = lookup_online("harlot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blunderbuss(self):
        html_dump = lookup_online("blunderbuss").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muddler(self):
        html_dump = lookup_online("muddler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commotion(self):
        html_dump = lookup_online("commotion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trout(self):
        html_dump = lookup_online("trout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extort(self):
        html_dump = lookup_online("extort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vernacular(self):
        html_dump = lookup_online("vernacular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_queasy(self):
        html_dump = lookup_online("queasy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pretentious(self):
        html_dump = lookup_online("pretentious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrewd(self):
        html_dump = lookup_online("shrewd").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mantel(self):
        html_dump = lookup_online("mantel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onus(self):
        html_dump = lookup_online("onus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hypodermic(self):
        html_dump = lookup_online("hypodermic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prophesying(self):
        html_dump = lookup_online("prophesying").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pry(self):
        html_dump = lookup_online("pry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holistic(self):
        html_dump = lookup_online("holistic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aperture(self):
        html_dump = lookup_online("aperture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grasp(self):
        html_dump = lookup_online("grasp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_searing(self):
        html_dump = lookup_online("searing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recalcitrant(self):
        html_dump = lookup_online("recalcitrant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moribund(self):
        html_dump = lookup_online("moribund").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transitive(self):
        html_dump = lookup_online("transitive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brat(self):
        html_dump = lookup_online("brat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mush(self):
        html_dump = lookup_online("mush").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immerse(self):
        html_dump = lookup_online("immerse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imbue(self):
        html_dump = lookup_online("imbue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shutter(self):
        html_dump = lookup_online("shutter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fingertip(self):
        html_dump = lookup_online("fingertip").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurn(self):
        html_dump = lookup_online("spurn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curfew(self):
        html_dump = lookup_online("curfew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subpoena(self):
        html_dump = lookup_online("subpoena").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plunge(self):
        html_dump = lookup_online("plunge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissent(self):
        html_dump = lookup_online("dissent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contagion(self):
        html_dump = lookup_online("contagion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petty(self):
        html_dump = lookup_online("petty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preordain(self):
        html_dump = lookup_online("preordain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revery(self):
        html_dump = lookup_online("revery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amygdala(self):
        html_dump = lookup_online("amygdala").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rendition(self):
        html_dump = lookup_online("rendition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incumbent(self):
        html_dump = lookup_online("incumbent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_analgesic(self):
        html_dump = lookup_online("analgesic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prejudice(self):
        html_dump = lookup_online("prejudice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savage(self):
        html_dump = lookup_online("savage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marvellous(self):
        html_dump = lookup_online("marvellous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dulcimer(self):
        html_dump = lookup_online("dulcimer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stupor(self):
        html_dump = lookup_online("stupor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rickets(self):
        html_dump = lookup_online("rickets").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utensil(self):
        html_dump = lookup_online("utensil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mollify(self):
        html_dump = lookup_online("mollify").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dot(self):
        html_dump = lookup_online("dot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mansion(self):
        html_dump = lookup_online("mansion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corroborate(self):
        html_dump = lookup_online("corroborate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vapid(self):
        html_dump = lookup_online("vapid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quixotic(self):
        html_dump = lookup_online("quixotic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effigy(self):
        html_dump = lookup_online("effigy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bungle(self):
        html_dump = lookup_online("bungle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wane(self):
        html_dump = lookup_online("wane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mend(self):
        html_dump = lookup_online("mend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ambient(self):
        html_dump = lookup_online("ambient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gluttony(self):
        html_dump = lookup_online("gluttony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheeky(self):
        html_dump = lookup_online("cheeky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lymphoma(self):
        html_dump = lookup_online("lymphoma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affirm(self):
        html_dump = lookup_online("affirm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confide(self):
        html_dump = lookup_online("confide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preternatural(self):
        html_dump = lookup_online("preternatural").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evanescent(self):
        html_dump = lookup_online("evanescent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ineffectual(self):
        html_dump = lookup_online("ineffectual").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alacrity(self):
        html_dump = lookup_online("alacrity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marsupial(self):
        html_dump = lookup_online("marsupial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_courting(self):
        html_dump = lookup_online("courting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_balk(self):
        html_dump = lookup_online("balk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_collate(self):
        html_dump = lookup_online("collate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_denouement(self):
        html_dump = lookup_online("denouement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oaf(self):
        html_dump = lookup_online("oaf").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riverine(self):
        html_dump = lookup_online("riverine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuberculosis(self):
        html_dump = lookup_online("tuberculosis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mottle(self):
        html_dump = lookup_online("mottle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savory(self):
        html_dump = lookup_online("savory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sobriety(self):
        html_dump = lookup_online("sobriety").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Mace(self):
        html_dump = lookup_online("Mace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wrong_headed(self):
        html_dump = lookup_online("wrong-headed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reticent(self):
        html_dump = lookup_online("reticent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abruptly(self):
        html_dump = lookup_online("abruptly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slime(self):
        html_dump = lookup_online("slime").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awning(self):
        html_dump = lookup_online("awning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bowled(self):
        html_dump = lookup_online("bowled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glum(self):
        html_dump = lookup_online("glum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calcify(self):
        html_dump = lookup_online("calcify").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forthright(self):
        html_dump = lookup_online("forthright").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mischief(self):
        html_dump = lookup_online("mischief").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_granadilla(self):
        html_dump = lookup_online("granadilla").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garish(self):
        html_dump = lookup_online("garish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compulsory(self):
        html_dump = lookup_online("compulsory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lotus(self):
        html_dump = lookup_online("lotus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quotidian(self):
        html_dump = lookup_online("quotidian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perch(self):
        html_dump = lookup_online("perch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_segues(self):
        html_dump = lookup_online("segues").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flirty(self):
        html_dump = lookup_online("flirty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smugness(self):
        html_dump = lookup_online("smugness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spic(self):
        html_dump = lookup_online("spic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mastic(self):
        html_dump = lookup_online("mastic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pompous(self):
        html_dump = lookup_online("pompous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minimalistic(self):
        html_dump = lookup_online("minimalistic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hovercraft(self):
        html_dump = lookup_online("hovercraft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compound(self):
        html_dump = lookup_online("compound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crusty(self):
        html_dump = lookup_online("crusty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spite(self):
        html_dump = lookup_online("spite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_buzzard(self):
        html_dump = lookup_online("buzzard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_waver(self):
        html_dump = lookup_online("waver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravel(self):
        html_dump = lookup_online("ravel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismal(self):
        html_dump = lookup_online("dismal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impotence(self):
        html_dump = lookup_online("impotence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assuage(self):
        html_dump = lookup_online("assuage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conduct(self):
        html_dump = lookup_online("conduct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indict(self):
        html_dump = lookup_online("indict").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emaciated(self):
        html_dump = lookup_online("emaciated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solitude(self):
        html_dump = lookup_online("solitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brill(self):
        html_dump = lookup_online("brill").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_constraint(self):
        html_dump = lookup_online("constraint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derogatory(self):
        html_dump = lookup_online("derogatory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruesome(self):
        html_dump = lookup_online("gruesome").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_umpire(self):
        html_dump = lookup_online("umpire").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rout(self):
        html_dump = lookup_online("rout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_runt(self):
        html_dump = lookup_online("runt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bovine(self):
        html_dump = lookup_online("bovine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_this(self):
        html_dump = lookup_online("this").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mold(self):
        html_dump = lookup_online("mold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagaries(self):
        html_dump = lookup_online("vagaries").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epiphanic(self):
        html_dump = lookup_online("epiphanic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overhead(self):
        html_dump = lookup_online("overhead").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perennial(self):
        html_dump = lookup_online("perennial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aptly(self):
        html_dump = lookup_online("aptly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menacing(self):
        html_dump = lookup_online("menacing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loon(self):
        html_dump = lookup_online("loon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satiable(self):
        html_dump = lookup_online("satiable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_callousness(self):
        html_dump = lookup_online("callousness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_huff(self):
        html_dump = lookup_online("huff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incidentally(self):
        html_dump = lookup_online("incidentally").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brassiere(self):
        html_dump = lookup_online("brassiere").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_torpor(self):
        html_dump = lookup_online("torpor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_profane(self):
        html_dump = lookup_online("profane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calamity(self):
        html_dump = lookup_online("calamity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hard_boiled(self):
        html_dump = lookup_online("hard-boiled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burly(self):
        html_dump = lookup_online("burly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epistemology(self):
        html_dump = lookup_online("epistemology").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artisan(self):
        html_dump = lookup_online("artisan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epitomize(self):
        html_dump = lookup_online("epitomize").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpably(self):
        html_dump = lookup_online("culpably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mitten(self):
        html_dump = lookup_online("mitten").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bequeath(self):
        html_dump = lookup_online("bequeath").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endowment(self):
        html_dump = lookup_online("endowment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rebuke(self):
        html_dump = lookup_online("rebuke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refute(self):
        html_dump = lookup_online("refute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merit(self):
        html_dump = lookup_online("merit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilante(self):
        html_dump = lookup_online("vigilante").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frontier(self):
        html_dump = lookup_online("frontier").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confidant(self):
        html_dump = lookup_online("confidant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallacy(self):
        html_dump = lookup_online("fallacy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mockery(self):
        html_dump = lookup_online("mockery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lugubrious(self):
        html_dump = lookup_online("lugubrious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hemlock(self):
        html_dump = lookup_online("hemlock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discern(self):
        html_dump = lookup_online("discern").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derisively(self):
        html_dump = lookup_online("derisively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_woe(self):
        html_dump = lookup_online("woe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conn(self):
        html_dump = lookup_online("conn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_telltale(self):
        html_dump = lookup_online("telltale").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fawn(self):
        html_dump = lookup_online("fawn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conclude(self):
        html_dump = lookup_online("conclude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flinching(self):
        html_dump = lookup_online("flinching").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subpar(self):
        html_dump = lookup_online("subpar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rosewood(self):
        html_dump = lookup_online("rosewood").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fare(self):
        html_dump = lookup_online("fare").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumple(self):
        html_dump = lookup_online("rumple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irascible(self):
        html_dump = lookup_online("irascible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weld(self):
        html_dump = lookup_online("weld").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lean(self):
        html_dump = lookup_online("lean").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hither(self):
        html_dump = lookup_online("hither").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lump(self):
        html_dump = lookup_online("lump").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compunction(self):
        html_dump = lookup_online("compunction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_measles(self):
        html_dump = lookup_online("measles").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trigger(self):
        html_dump = lookup_online("trigger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wallaby(self):
        html_dump = lookup_online("wallaby").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adamant(self):
        html_dump = lookup_online("adamant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irritable(self):
        html_dump = lookup_online("irritable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_querulous(self):
        html_dump = lookup_online("querulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocate(self):
        html_dump = lookup_online("reciprocate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_offal(self):
        html_dump = lookup_online("offal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coop(self):
        html_dump = lookup_online("coop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eerily(self):
        html_dump = lookup_online("eerily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inane(self):
        html_dump = lookup_online("inane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexorably(self):
        html_dump = lookup_online("inexorably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concave(self):
        html_dump = lookup_online("concave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retrieve(self):
        html_dump = lookup_online("retrieve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cadaver(self):
        html_dump = lookup_online("cadaver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dereliction(self):
        html_dump = lookup_online("dereliction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_licorice(self):
        html_dump = lookup_online("licorice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knapsack(self):
        html_dump = lookup_online("knapsack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overhaul(self):
        html_dump = lookup_online("overhaul").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shill(self):
        html_dump = lookup_online("shill").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hallmark(self):
        html_dump = lookup_online("hallmark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poise(self):
        html_dump = lookup_online("poise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affluent(self):
        html_dump = lookup_online("affluent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verboten(self):
        html_dump = lookup_online("verboten").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refutation(self):
        html_dump = lookup_online("refutation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fealty(self):
        html_dump = lookup_online("fealty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minted(self):
        html_dump = lookup_online("minted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_odious(self):
        html_dump = lookup_online("odious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blithely(self):
        html_dump = lookup_online("blithely").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trap(self):
        html_dump = lookup_online("trap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_felt(self):
        html_dump = lookup_online("felt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spur(self):
        html_dump = lookup_online("spur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Bedouin(self):
        html_dump = lookup_online("Bedouin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_espouse(self):
        html_dump = lookup_online("espouse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fecundity(self):
        html_dump = lookup_online("fecundity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gourd(self):
        html_dump = lookup_online("gourd").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adage(self):
        html_dump = lookup_online("adage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scotch(self):
        html_dump = lookup_online("scotch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quark(self):
        html_dump = lookup_online("quark").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruse(self):
        html_dump = lookup_online("ruse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vein(self):
        html_dump = lookup_online("vein").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_winch(self):
        html_dump = lookup_online("winch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruminate(self):
        html_dump = lookup_online("ruminate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revelry(self):
        html_dump = lookup_online("revelry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_colon(self):
        html_dump = lookup_online("colon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scooped(self):
        html_dump = lookup_online("scooped").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_itinerant(self):
        html_dump = lookup_online("itinerant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oeuvre(self):
        html_dump = lookup_online("oeuvre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scion(self):
        html_dump = lookup_online("scion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exalted(self):
        html_dump = lookup_online("exalted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_playwright(self):
        html_dump = lookup_online("playwright").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liaison(self):
        html_dump = lookup_online("liaison").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abject(self):
        html_dump = lookup_online("abject").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexpressible(self):
        html_dump = lookup_online("inexpressible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mound(self):
        html_dump = lookup_online("mound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despair(self):
        html_dump = lookup_online("despair").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pettiness(self):
        html_dump = lookup_online("pettiness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portentous(self):
        html_dump = lookup_online("portentous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stagger(self):
        html_dump = lookup_online("stagger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hopeless(self):
        html_dump = lookup_online("hopeless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debonair(self):
        html_dump = lookup_online("debonair").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_columnist(self):
        html_dump = lookup_online("columnist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precarious(self):
        html_dump = lookup_online("precarious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candidly(self):
        html_dump = lookup_online("candidly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loom(self):
        html_dump = lookup_online("loom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bilateral(self):
        html_dump = lookup_online("bilateral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shellac(self):
        html_dump = lookup_online("shellac").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fennel(self):
        html_dump = lookup_online("fennel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slavish(self):
        html_dump = lookup_online("slavish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feckless(self):
        html_dump = lookup_online("feckless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feral(self):
        html_dump = lookup_online("feral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fortitude(self):
        html_dump = lookup_online("fortitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slantwise(self):
        html_dump = lookup_online("slantwise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convoluted(self):
        html_dump = lookup_online("convoluted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defector(self):
        html_dump = lookup_online("defector").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cheekily(self):
        html_dump = lookup_online("cheekily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocity(self):
        html_dump = lookup_online("reciprocity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subliminal(self):
        html_dump = lookup_online("subliminal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furry(self):
        html_dump = lookup_online("furry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crayon(self):
        html_dump = lookup_online("crayon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blotter(self):
        html_dump = lookup_online("blotter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_callous(self):
        html_dump = lookup_online("callous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prescient(self):
        html_dump = lookup_online("prescient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinch(self):
        html_dump = lookup_online("pinch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equine(self):
        html_dump = lookup_online("equine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adamantine(self):
        html_dump = lookup_online("adamantine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigent(self):
        html_dump = lookup_online("indigent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_musk(self):
        html_dump = lookup_online("musk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impugned(self):
        html_dump = lookup_online("impugned").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tumble(self):
        html_dump = lookup_online("tumble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shim(self):
        html_dump = lookup_online("shim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_billet(self):
        html_dump = lookup_online("billet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blossom(self):
        html_dump = lookup_online("blossom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thrall(self):
        html_dump = lookup_online("thrall").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conifer(self):
        html_dump = lookup_online("conifer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_milter(self):
        html_dump = lookup_online("milter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scuttle(self):
        html_dump = lookup_online("scuttle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_injunction(self):
        html_dump = lookup_online("injunction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jot(self):
        html_dump = lookup_online("jot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lye(self):
        html_dump = lookup_online("lye").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petulant(self):
        html_dump = lookup_online("petulant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recriminate(self):
        html_dump = lookup_online("recriminate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inviolate(self):
        html_dump = lookup_online("inviolate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moderate(self):
        html_dump = lookup_online("moderate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_merle(self):
        html_dump = lookup_online("merle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_streaked(self):
        html_dump = lookup_online("streaked").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disrobe(self):
        html_dump = lookup_online("disrobe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elm(self):
        html_dump = lookup_online("elm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_descending(self):
        html_dump = lookup_online("descending").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reverie(self):
        html_dump = lookup_online("reverie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clot(self):
        html_dump = lookup_online("clot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trough(self):
        html_dump = lookup_online("trough").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luster(self):
        html_dump = lookup_online("luster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rind(self):
        html_dump = lookup_online("rind").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reserved(self):
        html_dump = lookup_online("reserved").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drizzle(self):
        html_dump = lookup_online("drizzle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_descendant(self):
        html_dump = lookup_online("descendant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_butch(self):
        html_dump = lookup_online("butch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_court(self):
        html_dump = lookup_online("court").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discreet(self):
        html_dump = lookup_online("discreet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascertain(self):
        html_dump = lookup_online("ascertain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jacob(self):
        html_dump = lookup_online("jacob").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aneurysm(self):
        html_dump = lookup_online("aneurysm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaudy(self):
        html_dump = lookup_online("gaudy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bespectacled(self):
        html_dump = lookup_online("bespectacled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placidity(self):
        html_dump = lookup_online("placidity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zeal(self):
        html_dump = lookup_online("zeal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flatter(self):
        html_dump = lookup_online("flatter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliability(self):
        html_dump = lookup_online("pliability").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flabbily(self):
        html_dump = lookup_online("flabbily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quadrilateral(self):
        html_dump = lookup_online("quadrilateral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snapshot(self):
        html_dump = lookup_online("snapshot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nephew(self):
        html_dump = lookup_online("nephew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stymie(self):
        html_dump = lookup_online("stymie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dreadnought(self):
        html_dump = lookup_online("dreadnought").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wizard(self):
        html_dump = lookup_online("wizard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tertiary(self):
        html_dump = lookup_online("tertiary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amicable(self):
        html_dump = lookup_online("amicable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unnerving(self):
        html_dump = lookup_online("unnerving").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ordeal(self):
        html_dump = lookup_online("ordeal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peritonitis(self):
        html_dump = lookup_online("peritonitis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_profligate(self):
        html_dump = lookup_online("profligate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_industry(self):
        html_dump = lookup_online("industry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kith(self):
        html_dump = lookup_online("kith").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceal(self):
        html_dump = lookup_online("conceal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antebellum(self):
        html_dump = lookup_online("antebellum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venerable(self):
        html_dump = lookup_online("venerable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clarion(self):
        html_dump = lookup_online("clarion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goldfinch(self):
        html_dump = lookup_online("goldfinch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ornery(self):
        html_dump = lookup_online("ornery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wart(self):
        html_dump = lookup_online("wart").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitously(self):
        html_dump = lookup_online("precipitously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sly(self):
        html_dump = lookup_online("sly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterred(self):
        html_dump = lookup_online("deterred").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquiesce(self):
        html_dump = lookup_online("acquiesce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deteriorate(self):
        html_dump = lookup_online("deteriorate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strayed(self):
        html_dump = lookup_online("strayed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fore(self):
        html_dump = lookup_online("fore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paulownia(self):
        html_dump = lookup_online("paulownia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apologetic(self):
        html_dump = lookup_online("apologetic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enticing(self):
        html_dump = lookup_online("enticing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ensconced(self):
        html_dump = lookup_online("ensconced").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lead(self):
        html_dump = lookup_online("lead").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antecedent(self):
        html_dump = lookup_online("antecedent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meandering(self):
        html_dump = lookup_online("meandering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealot(self):
        html_dump = lookup_online("zealot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rudderless(self):
        html_dump = lookup_online("rudderless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_judicious(self):
        html_dump = lookup_online("judicious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_promiscuous(self):
        html_dump = lookup_online("promiscuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squirm(self):
        html_dump = lookup_online("squirm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gallantry(self):
        html_dump = lookup_online("gallantry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forestall(self):
        html_dump = lookup_online("forestall").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incessantly(self):
        html_dump = lookup_online("incessantly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_esoteric(self):
        html_dump = lookup_online("esoteric").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_banter(self):
        html_dump = lookup_online("banter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_injective(self):
        html_dump = lookup_online("injective").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_environment(self):
        html_dump = lookup_online("environment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tentative(self):
        html_dump = lookup_online("tentative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jarring(self):
        html_dump = lookup_online("jarring").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moot(self):
        html_dump = lookup_online("moot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_faze(self):
        html_dump = lookup_online("faze").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lath(self):
        html_dump = lookup_online("lath").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscarry(self):
        html_dump = lookup_online("miscarry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contingency(self):
        html_dump = lookup_online("contingency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceit(self):
        html_dump = lookup_online("conceit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malaise(self):
        html_dump = lookup_online("malaise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resolute(self):
        html_dump = lookup_online("resolute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidget(self):
        html_dump = lookup_online("fidget").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crux(self):
        html_dump = lookup_online("crux").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flip(self):
        html_dump = lookup_online("flip").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gorgeous(self):
        html_dump = lookup_online("gorgeous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Mongoloid(self):
        html_dump = lookup_online("Mongoloid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serpentine(self):
        html_dump = lookup_online("serpentine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pancreas(self):
        html_dump = lookup_online("pancreas").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poultry(self):
        html_dump = lookup_online("poultry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_explicit(self):
        html_dump = lookup_online("explicit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gander(self):
        html_dump = lookup_online("gander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palliate(self):
        html_dump = lookup_online("palliate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lay(self):
        html_dump = lookup_online("lay").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deferential(self):
        html_dump = lookup_online("deferential").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interleaving(self):
        html_dump = lookup_online("interleaving").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travesty(self):
        html_dump = lookup_online("travesty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spindly(self):
        html_dump = lookup_online("spindly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quail(self):
        html_dump = lookup_online("quail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_southpaw(self):
        html_dump = lookup_online("southpaw").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trampled(self):
        html_dump = lookup_online("trampled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furlough(self):
        html_dump = lookup_online("furlough").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trifling(self):
        html_dump = lookup_online("trifling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repudiation(self):
        html_dump = lookup_online("repudiation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implicit(self):
        html_dump = lookup_online("implicit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recoil(self):
        html_dump = lookup_online("recoil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_provenance(self):
        html_dump = lookup_online("provenance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overzealous(self):
        html_dump = lookup_online("overzealous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhortation(self):
        html_dump = lookup_online("exhortation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implacable(self):
        html_dump = lookup_online("implacable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mumble(self):
        html_dump = lookup_online("mumble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rube(self):
        html_dump = lookup_online("rube").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ennui(self):
        html_dump = lookup_online("ennui").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chastised(self):
        html_dump = lookup_online("chastised").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nous(self):
        html_dump = lookup_online("nous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elope(self):
        html_dump = lookup_online("elope").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nab(self):
        html_dump = lookup_online("nab").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untether(self):
        html_dump = lookup_online("untether").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_septum(self):
        html_dump = lookup_online("septum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redress(self):
        html_dump = lookup_online("redress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weight(self):
        html_dump = lookup_online("weight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_folly(self):
        html_dump = lookup_online("folly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hernia(self):
        html_dump = lookup_online("hernia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brained(self):
        html_dump = lookup_online("brained").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vexed(self):
        html_dump = lookup_online("vexed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_riff(self):
        html_dump = lookup_online("riff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maggot(self):
        html_dump = lookup_online("maggot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serfdom(self):
        html_dump = lookup_online("serfdom").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raunchy(self):
        html_dump = lookup_online("raunchy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impressively(self):
        html_dump = lookup_online("impressively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rehearse(self):
        html_dump = lookup_online("rehearse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travail(self):
        html_dump = lookup_online("travail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_propensity(self):
        html_dump = lookup_online("propensity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influx(self):
        html_dump = lookup_online("influx").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_opaque(self):
        html_dump = lookup_online("opaque").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shibboleth(self):
        html_dump = lookup_online("shibboleth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scorn(self):
        html_dump = lookup_online("scorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pilfer(self):
        html_dump = lookup_online("pilfer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asphyxiation(self):
        html_dump = lookup_online("asphyxiation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lethargy(self):
        html_dump = lookup_online("lethargy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unequivocal(self):
        html_dump = lookup_online("unequivocal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_converse(self):
        html_dump = lookup_online("converse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parlor(self):
        html_dump = lookup_online("parlor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_latch(self):
        html_dump = lookup_online("latch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expedient(self):
        html_dump = lookup_online("expedient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reimburse(self):
        html_dump = lookup_online("reimburse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bruin(self):
        html_dump = lookup_online("bruin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stepchild(self):
        html_dump = lookup_online("stepchild").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lackey(self):
        html_dump = lookup_online("lackey").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rap(self):
        html_dump = lookup_online("rap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Melanoma(self):
        html_dump = lookup_online("Melanoma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hefty(self):
        html_dump = lookup_online("hefty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_monosomy(self):
        html_dump = lookup_online("monosomy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penitence(self):
        html_dump = lookup_online("penitence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_backlash(self):
        html_dump = lookup_online("backlash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onerous(self):
        html_dump = lookup_online("onerous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ailing(self):
        html_dump = lookup_online("ailing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sternum(self):
        html_dump = lookup_online("sternum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chasten(self):
        html_dump = lookup_online("chasten").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beleaguer(self):
        html_dump = lookup_online("beleaguer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuinely(self):
        html_dump = lookup_online("genuinely").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_piteously(self):
        html_dump = lookup_online("piteously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larceny(self):
        html_dump = lookup_online("larceny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insurmountable(self):
        html_dump = lookup_online("insurmountable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extirpation(self):
        html_dump = lookup_online("extirpation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ventriloquist(self):
        html_dump = lookup_online("ventriloquist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_innocuous(self):
        html_dump = lookup_online("innocuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remedial(self):
        html_dump = lookup_online("remedial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bickering(self):
        html_dump = lookup_online("bickering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unilaterally(self):
        html_dump = lookup_online("unilaterally").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_attaboy(self):
        html_dump = lookup_online("attaboy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_continuous(self):
        html_dump = lookup_online("continuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mullet(self):
        html_dump = lookup_online("mullet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimony(self):
        html_dump = lookup_online("acrimony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glib(self):
        html_dump = lookup_online("glib").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fray(self):
        html_dump = lookup_online("fray").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mundane(self):
        html_dump = lookup_online("mundane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haptic(self):
        html_dump = lookup_online("haptic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relenting(self):
        html_dump = lookup_online("relenting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grandiose(self):
        html_dump = lookup_online("grandiose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wacky(self):
        html_dump = lookup_online("wacky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_engender(self):
        html_dump = lookup_online("engender").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nowt(self):
        html_dump = lookup_online("nowt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wispy(self):
        html_dump = lookup_online("wispy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_left(self):
        html_dump = lookup_online("left").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hip(self):
        html_dump = lookup_online("hip").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transience(self):
        html_dump = lookup_online("transience").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parsnips(self):
        html_dump = lookup_online("parsnips").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shoddy(self):
        html_dump = lookup_online("shoddy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ochre(self):
        html_dump = lookup_online("ochre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coerce(self):
        html_dump = lookup_online("coerce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_castigate(self):
        html_dump = lookup_online("castigate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loftiness(self):
        html_dump = lookup_online("loftiness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wand(self):
        html_dump = lookup_online("wand").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barren(self):
        html_dump = lookup_online("barren").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bras(self):
        html_dump = lookup_online("bras").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recondite(self):
        html_dump = lookup_online("recondite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derision(self):
        html_dump = lookup_online("derision").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pelvis(self):
        html_dump = lookup_online("pelvis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacky(self):
        html_dump = lookup_online("tacky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pail(self):
        html_dump = lookup_online("pail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pernicious(self):
        html_dump = lookup_online("pernicious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagrantly(self):
        html_dump = lookup_online("flagrantly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emphysema(self):
        html_dump = lookup_online("emphysema").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_streak(self):
        html_dump = lookup_online("streak").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yttrium(self):
        html_dump = lookup_online("yttrium").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jocular(self):
        html_dump = lookup_online("jocular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstinate(self):
        html_dump = lookup_online("obstinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protruding(self):
        html_dump = lookup_online("protruding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nudge(self):
        html_dump = lookup_online("nudge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apprehensive(self):
        html_dump = lookup_online("apprehensive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squash(self):
        html_dump = lookup_online("squash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_udder(self):
        html_dump = lookup_online("udder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prevalent(self):
        html_dump = lookup_online("prevalent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eal(self):
        html_dump = lookup_online("eal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scholarly(self):
        html_dump = lookup_online("scholarly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rye(self):
        html_dump = lookup_online("rye").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belligerent(self):
        html_dump = lookup_online("belligerent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loquacious(self):
        html_dump = lookup_online("loquacious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extracurricular(self):
        html_dump = lookup_online("extracurricular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inextricably(self):
        html_dump = lookup_online("inextricably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_graceful(self):
        html_dump = lookup_online("graceful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sybaritic(self):
        html_dump = lookup_online("sybaritic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broad(self):
        html_dump = lookup_online("broad").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inconvenience(self):
        html_dump = lookup_online("inconvenience").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rejoice(self):
        html_dump = lookup_online("rejoice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagrancy(self):
        html_dump = lookup_online("vagrancy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vexatious(self):
        html_dump = lookup_online("vexatious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spook(self):
        html_dump = lookup_online("spook").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glimpsing(self):
        html_dump = lookup_online("glimpsing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wallow(self):
        html_dump = lookup_online("wallow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strife(self):
        html_dump = lookup_online("strife").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tone_deaf(self):
        html_dump = lookup_online("tone-deaf").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_triage(self):
        html_dump = lookup_online("triage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heiress(self):
        html_dump = lookup_online("heiress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slither(self):
        html_dump = lookup_online("slither").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanctity(self):
        html_dump = lookup_online("sanctity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penultimate(self):
        html_dump = lookup_online("penultimate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gimpy(self):
        html_dump = lookup_online("gimpy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neural(self):
        html_dump = lookup_online("neural").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preserve(self):
        html_dump = lookup_online("preserve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prodigious(self):
        html_dump = lookup_online("prodigious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inept(self):
        html_dump = lookup_online("inept").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oedipal(self):
        html_dump = lookup_online("oedipal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_astray(self):
        html_dump = lookup_online("astray").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gawp(self):
        html_dump = lookup_online("gawp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_escarpment(self):
        html_dump = lookup_online("escarpment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimoniously(self):
        html_dump = lookup_online("acrimoniously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_muppet(self):
        html_dump = lookup_online("muppet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwavering(self):
        html_dump = lookup_online("unwavering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reciprocal(self):
        html_dump = lookup_online("reciprocal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mediocre(self):
        html_dump = lookup_online("mediocre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jubilee(self):
        html_dump = lookup_online("jubilee").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpable(self):
        html_dump = lookup_online("culpable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obsequious(self):
        html_dump = lookup_online("obsequious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doldrums(self):
        html_dump = lookup_online("doldrums").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeremiad(self):
        html_dump = lookup_online("jeremiad").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extortion(self):
        html_dump = lookup_online("extortion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_willy_nilly(self):
        html_dump = lookup_online("willy-nilly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescend(self):
        html_dump = lookup_online("condescend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shingle(self):
        html_dump = lookup_online("shingle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lisp(self):
        html_dump = lookup_online("lisp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turmoil(self):
        html_dump = lookup_online("turmoil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stillbirth(self):
        html_dump = lookup_online("stillbirth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knurled(self):
        html_dump = lookup_online("knurled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foul(self):
        html_dump = lookup_online("foul").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verbose(self):
        html_dump = lookup_online("verbose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pander(self):
        html_dump = lookup_online("pander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eclectic(self):
        html_dump = lookup_online("eclectic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catering(self):
        html_dump = lookup_online("catering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limber(self):
        html_dump = lookup_online("limber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lateral(self):
        html_dump = lookup_online("lateral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gland(self):
        html_dump = lookup_online("gland").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implicated(self):
        html_dump = lookup_online("implicated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilant(self):
        html_dump = lookup_online("vigilant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urea(self):
        html_dump = lookup_online("urea").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thoroughfare(self):
        html_dump = lookup_online("thoroughfare").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slavishly(self):
        html_dump = lookup_online("slavishly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_famine(self):
        html_dump = lookup_online("famine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expedite(self):
        html_dump = lookup_online("expedite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meticulous(self):
        html_dump = lookup_online("meticulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maple(self):
        html_dump = lookup_online("maple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rank(self):
        html_dump = lookup_online("rank").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraption(self):
        html_dump = lookup_online("contraption").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clutter(self):
        html_dump = lookup_online("clutter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_now(self):
        html_dump = lookup_online("now").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grower(self):
        html_dump = lookup_online("grower").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solemnity(self):
        html_dump = lookup_online("solemnity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heckler(self):
        html_dump = lookup_online("heckler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ensue(self):
        html_dump = lookup_online("ensue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_encumber(self):
        html_dump = lookup_online("encumber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swamped(self):
        html_dump = lookup_online("swamped").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_futilely(self):
        html_dump = lookup_online("futilely").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_angler(self):
        html_dump = lookup_online("angler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_medicore(self):
        html_dump = lookup_online("medicore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wean(self):
        html_dump = lookup_online("wean").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fusillade(self):
        html_dump = lookup_online("fusillade").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slender(self):
        html_dump = lookup_online("slender").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kismet(self):
        html_dump = lookup_online("kismet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nunnery(self):
        html_dump = lookup_online("nunnery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_truce(self):
        html_dump = lookup_online("truce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismay(self):
        html_dump = lookup_online("dismay").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intercede(self):
        html_dump = lookup_online("intercede").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accolade(self):
        html_dump = lookup_online("accolade").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ladle(self):
        html_dump = lookup_online("ladle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assess(self):
        html_dump = lookup_online("assess").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intricate(self):
        html_dump = lookup_online("intricate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satchel(self):
        html_dump = lookup_online("satchel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virility(self):
        html_dump = lookup_online("virility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rakish(self):
        html_dump = lookup_online("rakish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abscond(self):
        html_dump = lookup_online("abscond").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sartorial(self):
        html_dump = lookup_online("sartorial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venison(self):
        html_dump = lookup_online("venison").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litigate(self):
        html_dump = lookup_online("litigate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vagrant(self):
        html_dump = lookup_online("vagrant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_staid(self):
        html_dump = lookup_online("staid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superlative(self):
        html_dump = lookup_online("superlative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dotage(self):
        html_dump = lookup_online("dotage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gobble(self):
        html_dump = lookup_online("gobble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_procession(self):
        html_dump = lookup_online("procession").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snarky(self):
        html_dump = lookup_online("snarky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adherence(self):
        html_dump = lookup_online("adherence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fledgling(self):
        html_dump = lookup_online("fledgling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pastie(self):
        html_dump = lookup_online("pastie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peril(self):
        html_dump = lookup_online("peril").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inhibitor(self):
        html_dump = lookup_online("inhibitor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shunt(self):
        html_dump = lookup_online("shunt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skirt(self):
        html_dump = lookup_online("skirt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_winging(self):
        html_dump = lookup_online("winging").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brusque(self):
        html_dump = lookup_online("brusque").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stretch(self):
        html_dump = lookup_online("stretch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrawny(self):
        html_dump = lookup_online("scrawny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowery(self):
        html_dump = lookup_online("dowery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dyspraxia(self):
        html_dump = lookup_online("dyspraxia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gallbladder(self):
        html_dump = lookup_online("gallbladder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slapdash(self):
        html_dump = lookup_online("slapdash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_continence(self):
        html_dump = lookup_online("continence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unfazed(self):
        html_dump = lookup_online("unfazed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orneriness(self):
        html_dump = lookup_online("orneriness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enmity(self):
        html_dump = lookup_online("enmity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garrote(self):
        html_dump = lookup_online("garrote").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meek(self):
        html_dump = lookup_online("meek").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sift(self):
        html_dump = lookup_online("sift").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blanket(self):
        html_dump = lookup_online("blanket").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coax(self):
        html_dump = lookup_online("coax").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glaucoma(self):
        html_dump = lookup_online("glaucoma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_charade(self):
        html_dump = lookup_online("charade").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_audacious(self):
        html_dump = lookup_online("audacious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disfunctional(self):
        html_dump = lookup_online("disfunctional").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sordid(self):
        html_dump = lookup_online("sordid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_respite(self):
        html_dump = lookup_online("respite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adulterate(self):
        html_dump = lookup_online("adulterate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blinkered(self):
        html_dump = lookup_online("blinkered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trebuchet(self):
        html_dump = lookup_online("trebuchet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quixotically(self):
        html_dump = lookup_online("quixotically").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resolve(self):
        html_dump = lookup_online("resolve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oppressed(self):
        html_dump = lookup_online("oppressed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lesions(self):
        html_dump = lookup_online("lesions").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bough(self):
        html_dump = lookup_online("bough").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hue(self):
        html_dump = lookup_online("hue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_farrier(self):
        html_dump = lookup_online("farrier").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stash(self):
        html_dump = lookup_online("stash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vicious(self):
        html_dump = lookup_online("vicious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tortoise(self):
        html_dump = lookup_online("tortoise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewitched(self):
        html_dump = lookup_online("bewitched").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quip(self):
        html_dump = lookup_online("quip").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ancillary(self):
        html_dump = lookup_online("ancillary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congregant(self):
        html_dump = lookup_online("congregant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wreathe(self):
        html_dump = lookup_online("wreathe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_durian(self):
        html_dump = lookup_online("durian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spigot(self):
        html_dump = lookup_online("spigot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patch(self):
        html_dump = lookup_online("patch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diligent(self):
        html_dump = lookup_online("diligent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_filial(self):
        html_dump = lookup_online("filial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_implacably(self):
        html_dump = lookup_online("implacably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prediction(self):
        html_dump = lookup_online("prediction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rabies(self):
        html_dump = lookup_online("rabies").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ado(self):
        html_dump = lookup_online("ado").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudence(self):
        html_dump = lookup_online("prudence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vista(self):
        html_dump = lookup_online("vista").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benignly(self):
        html_dump = lookup_online("benignly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tempest(self):
        html_dump = lookup_online("tempest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vim(self):
        html_dump = lookup_online("vim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mead(self):
        html_dump = lookup_online("mead").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spendthrift(self):
        html_dump = lookup_online("spendthrift").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_panopticon(self):
        html_dump = lookup_online("panopticon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaggle(self):
        html_dump = lookup_online("gaggle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluminous(self):
        html_dump = lookup_online("voluminous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outline(self):
        html_dump = lookup_online("outline").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wharve(self):
        html_dump = lookup_online("wharve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expediency(self):
        html_dump = lookup_online("expediency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trivial(self):
        html_dump = lookup_online("trivial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bluff(self):
        html_dump = lookup_online("bluff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forlorn(self):
        html_dump = lookup_online("forlorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agrarian(self):
        html_dump = lookup_online("agrarian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tinnitus(self):
        html_dump = lookup_online("tinnitus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exult(self):
        html_dump = lookup_online("exult").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ornate(self):
        html_dump = lookup_online("ornate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peon(self):
        html_dump = lookup_online("peon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_selfishness(self):
        html_dump = lookup_online("selfishness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precarity(self):
        html_dump = lookup_online("precarity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetrator(self):
        html_dump = lookup_online("perpetrator").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_luminary(self):
        html_dump = lookup_online("luminary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convex(self):
        html_dump = lookup_online("convex").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_begat(self):
        html_dump = lookup_online("begat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indolence(self):
        html_dump = lookup_online("indolence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vying(self):
        html_dump = lookup_online("vying").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_husbandry(self):
        html_dump = lookup_online("husbandry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quadriplegic(self):
        html_dump = lookup_online("quadriplegic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquaint(self):
        html_dump = lookup_online("acquaint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rattle(self):
        html_dump = lookup_online("rattle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corporeal(self):
        html_dump = lookup_online("corporeal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artifice(self):
        html_dump = lookup_online("artifice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crooked(self):
        html_dump = lookup_online("crooked").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eaves(self):
        html_dump = lookup_online("eaves").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sentient(self):
        html_dump = lookup_online("sentient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_instigate(self):
        html_dump = lookup_online("instigate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wizened(self):
        html_dump = lookup_online("wizened").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rising(self):
        html_dump = lookup_online("rising").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inimical(self):
        html_dump = lookup_online("inimical").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acumen(self):
        html_dump = lookup_online("acumen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discontent(self):
        html_dump = lookup_online("discontent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exuberance(self):
        html_dump = lookup_online("exuberance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discrepancy(self):
        html_dump = lookup_online("discrepancy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solicitor(self):
        html_dump = lookup_online("solicitor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parochialism(self):
        html_dump = lookup_online("parochialism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adulation(self):
        html_dump = lookup_online("adulation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Kowloon(self):
        html_dump = lookup_online("Kowloon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_warring(self):
        html_dump = lookup_online("warring").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjunction(self):
        html_dump = lookup_online("conjunction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arcane(self):
        html_dump = lookup_online("arcane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refurbish(self):
        html_dump = lookup_online("refurbish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_negligent(self):
        html_dump = lookup_online("negligent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whilist(self):
        html_dump = lookup_online("whilist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lien(self):
        html_dump = lookup_online("lien").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_watercress(self):
        html_dump = lookup_online("watercress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dash(self):
        html_dump = lookup_online("dash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cherish(self):
        html_dump = lookup_online("cherish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indignation(self):
        html_dump = lookup_online("indignation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loft(self):
        html_dump = lookup_online("loft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disregard(self):
        html_dump = lookup_online("disregard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furor(self):
        html_dump = lookup_online("furor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_betrothed(self):
        html_dump = lookup_online("betrothed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheer(self):
        html_dump = lookup_online("sheer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maw(self):
        html_dump = lookup_online("maw").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influenza(self):
        html_dump = lookup_online("influenza").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affectation(self):
        html_dump = lookup_online("affectation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_précis(self):
        html_dump = lookup_online("précis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_freight(self):
        html_dump = lookup_online("freight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remorse(self):
        html_dump = lookup_online("remorse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_headstrong(self):
        html_dump = lookup_online("headstrong").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bobbin(self):
        html_dump = lookup_online("bobbin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wonk(self):
        html_dump = lookup_online("wonk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poaching(self):
        html_dump = lookup_online("poaching").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eldritch(self):
        html_dump = lookup_online("eldritch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tomcat(self):
        html_dump = lookup_online("tomcat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranny(self):
        html_dump = lookup_online("tranny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thimble(self):
        html_dump = lookup_online("thimble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeremiads(self):
        html_dump = lookup_online("jeremiads").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quarry(self):
        html_dump = lookup_online("quarry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrepid(self):
        html_dump = lookup_online("intrepid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jerk(self):
        html_dump = lookup_online("jerk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salutatory(self):
        html_dump = lookup_online("salutatory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feud(self):
        html_dump = lookup_online("feud").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_progenitor(self):
        html_dump = lookup_online("progenitor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suppurate(self):
        html_dump = lookup_online("suppurate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duress(self):
        html_dump = lookup_online("duress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proximal(self):
        html_dump = lookup_online("proximal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_risible(self):
        html_dump = lookup_online("risible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mendacity(self):
        html_dump = lookup_online("mendacity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cole(self):
        html_dump = lookup_online("cole").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dignified(self):
        html_dump = lookup_online("dignified").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_while(self):
        html_dump = lookup_online("while").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sap(self):
        html_dump = lookup_online("sap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abound(self):
        html_dump = lookup_online("abound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belie(self):
        html_dump = lookup_online("belie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diminishing(self):
        html_dump = lookup_online("diminishing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mutiny(self):
        html_dump = lookup_online("mutiny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_throb(self):
        html_dump = lookup_online("throb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bareness(self):
        html_dump = lookup_online("bareness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eddying(self):
        html_dump = lookup_online("eddying").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dory(self):
        html_dump = lookup_online("dory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distract(self):
        html_dump = lookup_online("distract").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_for(self):
        html_dump = lookup_online("for").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stultify(self):
        html_dump = lookup_online("stultify").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detractor(self):
        html_dump = lookup_online("detractor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_magpie(self):
        html_dump = lookup_online("magpie").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigenous(self):
        html_dump = lookup_online("indigenous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hereditary(self):
        html_dump = lookup_online("hereditary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscegenation(self):
        html_dump = lookup_online("miscegenation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_splinter(self):
        html_dump = lookup_online("splinter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curt(self):
        html_dump = lookup_online("curt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accord(self):
        html_dump = lookup_online("accord").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corollary(self):
        html_dump = lookup_online("corollary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excruciating(self):
        html_dump = lookup_online("excruciating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wistfully(self):
        html_dump = lookup_online("wistfully").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despondence(self):
        html_dump = lookup_online("despondence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_age(self):
        html_dump = lookup_online("age").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diverge(self):
        html_dump = lookup_online("diverge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferment(self):
        html_dump = lookup_online("ferment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fetch(self):
        html_dump = lookup_online("fetch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_facsimile(self):
        html_dump = lookup_online("facsimile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maim(self):
        html_dump = lookup_online("maim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mercantile(self):
        html_dump = lookup_online("mercantile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tendentious(self):
        html_dump = lookup_online("tendentious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hepatitis(self):
        html_dump = lookup_online("hepatitis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fret(self):
        html_dump = lookup_online("fret").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admonition(self):
        html_dump = lookup_online("admonition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ingenuity(self):
        html_dump = lookup_online("ingenuity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carb(self):
        html_dump = lookup_online("carb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brisant(self):
        html_dump = lookup_online("brisant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutters(self):
        html_dump = lookup_online("gutters").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spat(self):
        html_dump = lookup_online("spat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_testing(self):
        html_dump = lookup_online("testing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apathy(self):
        html_dump = lookup_online("apathy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trickster(self):
        html_dump = lookup_online("trickster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_furtive(self):
        html_dump = lookup_online("furtive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rack(self):
        html_dump = lookup_online("rack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lime(self):
        html_dump = lookup_online("lime").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tawdriness(self):
        html_dump = lookup_online("tawdriness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limestone(self):
        html_dump = lookup_online("limestone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brim(self):
        html_dump = lookup_online("brim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_berth(self):
        html_dump = lookup_online("berth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bacillus(self):
        html_dump = lookup_online("bacillus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blunder(self):
        html_dump = lookup_online("blunder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stowaway(self):
        html_dump = lookup_online("stowaway").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coy(self):
        html_dump = lookup_online("coy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_porridge(self):
        html_dump = lookup_online("porridge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puttering(self):
        html_dump = lookup_online("puttering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unencumbered(self):
        html_dump = lookup_online("unencumbered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_narc(self):
        html_dump = lookup_online("narc").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slander(self):
        html_dump = lookup_online("slander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_homicide(self):
        html_dump = lookup_online("homicide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rued(self):
        html_dump = lookup_online("rued").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vested(self):
        html_dump = lookup_online("vested").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immaculate(self):
        html_dump = lookup_online("immaculate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulceration(self):
        html_dump = lookup_online("ulceration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lumber(self):
        html_dump = lookup_online("lumber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_containable(self):
        html_dump = lookup_online("containable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snag(self):
        html_dump = lookup_online("snag").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forfeit(self):
        html_dump = lookup_online("forfeit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inordinate(self):
        html_dump = lookup_online("inordinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afterbirth(self):
        html_dump = lookup_online("afterbirth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deter(self):
        html_dump = lookup_online("deter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adorn(self):
        html_dump = lookup_online("adorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adversarial(self):
        html_dump = lookup_online("adversarial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parchment(self):
        html_dump = lookup_online("parchment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_demeanor(self):
        html_dump = lookup_online("demeanor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_damp(self):
        html_dump = lookup_online("damp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_efficacy(self):
        html_dump = lookup_online("efficacy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garment(self):
        html_dump = lookup_online("garment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insofar(self):
        html_dump = lookup_online("insofar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_triplet(self):
        html_dump = lookup_online("triplet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_straddle(self):
        html_dump = lookup_online("straddle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beseech(self):
        html_dump = lookup_online("beseech").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frugally(self):
        html_dump = lookup_online("frugally").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hifalutin(self):
        html_dump = lookup_online("hifalutin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alloy(self):
        html_dump = lookup_online("alloy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gregarious(self):
        html_dump = lookup_online("gregarious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pontificate(self):
        html_dump = lookup_online("pontificate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impel(self):
        html_dump = lookup_online("impel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amusing(self):
        html_dump = lookup_online("amusing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alteration(self):
        html_dump = lookup_online("alteration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hew(self):
        html_dump = lookup_online("hew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_convivial(self):
        html_dump = lookup_online("convivial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_docile(self):
        html_dump = lookup_online("docile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pewter(self):
        html_dump = lookup_online("pewter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manila(self):
        html_dump = lookup_online("manila").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notional(self):
        html_dump = lookup_online("notional").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeer(self):
        html_dump = lookup_online("jeer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_figuratively(self):
        html_dump = lookup_online("figuratively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rut(self):
        html_dump = lookup_online("rut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preclude(self):
        html_dump = lookup_online("preclude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hussle(self):
        html_dump = lookup_online("hussle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assent(self):
        html_dump = lookup_online("assent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unadorned(self):
        html_dump = lookup_online("unadorned").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gorge(self):
        html_dump = lookup_online("gorge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appropriate(self):
        html_dump = lookup_online("appropriate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coo(self):
        html_dump = lookup_online("coo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_minnow(self):
        html_dump = lookup_online("minnow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carping(self):
        html_dump = lookup_online("carping").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chad(self):
        html_dump = lookup_online("chad").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dowel(self):
        html_dump = lookup_online("dowel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auger(self):
        html_dump = lookup_online("auger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prenuptial(self):
        html_dump = lookup_online("prenuptial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tic(self):
        html_dump = lookup_online("tic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malleability(self):
        html_dump = lookup_online("malleability").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shagging(self):
        html_dump = lookup_online("shagging").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discombobulated(self):
        html_dump = lookup_online("discombobulated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lavish(self):
        html_dump = lookup_online("lavish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vehemently(self):
        html_dump = lookup_online("vehemently").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unfettered(self):
        html_dump = lookup_online("unfettered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_onwards(self):
        html_dump = lookup_online("onwards").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_racketeer(self):
        html_dump = lookup_online("racketeer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prowess(self):
        html_dump = lookup_online("prowess").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hump(self):
        html_dump = lookup_online("hump").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_purge(self):
        html_dump = lookup_online("purge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_diatribe(self):
        html_dump = lookup_online("diatribe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_digress(self):
        html_dump = lookup_online("digress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scaffold(self):
        html_dump = lookup_online("scaffold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elated(self):
        html_dump = lookup_online("elated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marshal(self):
        html_dump = lookup_online("marshal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snivelling(self):
        html_dump = lookup_online("snivelling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strap(self):
        html_dump = lookup_online("strap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sucker(self):
        html_dump = lookup_online("sucker").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_renunciation(self):
        html_dump = lookup_online("renunciation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_visceral(self):
        html_dump = lookup_online("visceral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sound(self):
        html_dump = lookup_online("sound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conceivably(self):
        html_dump = lookup_online("conceivably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corduroy(self):
        html_dump = lookup_online("corduroy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frisky(self):
        html_dump = lookup_online("frisky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deprivation(self):
        html_dump = lookup_online("deprivation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proprietor(self):
        html_dump = lookup_online("proprietor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contiguous(self):
        html_dump = lookup_online("contiguous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disappointing(self):
        html_dump = lookup_online("disappointing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gush(self):
        html_dump = lookup_online("gush").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impish(self):
        html_dump = lookup_online("impish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_residence(self):
        html_dump = lookup_online("residence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unruffled(self):
        html_dump = lookup_online("unruffled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_carnal(self):
        html_dump = lookup_online("carnal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regency(self):
        html_dump = lookup_online("regency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_churlish(self):
        html_dump = lookup_online("churlish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulchritudinous(self):
        html_dump = lookup_online("pulchritudinous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beech(self):
        html_dump = lookup_online("beech").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alder(self):
        html_dump = lookup_online("alder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quote(self):
        html_dump = lookup_online("quote").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confound(self):
        html_dump = lookup_online("confound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pitilessly(self):
        html_dump = lookup_online("pitilessly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hick(self):
        html_dump = lookup_online("hick").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excruciatingly(self):
        html_dump = lookup_online("excruciatingly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punitive(self):
        html_dump = lookup_online("punitive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_patter(self):
        html_dump = lookup_online("patter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_darkness(self):
        html_dump = lookup_online("darkness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succumb(self):
        html_dump = lookup_online("succumb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lend(self):
        html_dump = lookup_online("lend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affinity(self):
        html_dump = lookup_online("affinity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supposition(self):
        html_dump = lookup_online("supposition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcers(self):
        html_dump = lookup_online("ulcers").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_notch(self):
        html_dump = lookup_online("notch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perspicaciously(self):
        html_dump = lookup_online("perspicaciously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exegesis(self):
        html_dump = lookup_online("exegesis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chubby(self):
        html_dump = lookup_online("chubby").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenacious(self):
        html_dump = lookup_online("tenacious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_console(self):
        html_dump = lookup_online("console").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dispatch(self):
        html_dump = lookup_online("dispatch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marred(self):
        html_dump = lookup_online("marred").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unassailable(self):
        html_dump = lookup_online("unassailable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissuade(self):
        html_dump = lookup_online("dissuade").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjure(self):
        html_dump = lookup_online("conjure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sagacity(self):
        html_dump = lookup_online("sagacity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plight(self):
        html_dump = lookup_online("plight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taciturn(self):
        html_dump = lookup_online("taciturn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brass(self):
        html_dump = lookup_online("brass").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proselyte(self):
        html_dump = lookup_online("proselyte").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cringe(self):
        html_dump = lookup_online("cringe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morsel(self):
        html_dump = lookup_online("morsel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squeal(self):
        html_dump = lookup_online("squeal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intermittent(self):
        html_dump = lookup_online("intermittent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mezzanine(self):
        html_dump = lookup_online("mezzanine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meekness(self):
        html_dump = lookup_online("meekness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawn(self):
        html_dump = lookup_online("brawn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coven(self):
        html_dump = lookup_online("coven").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jolt(self):
        html_dump = lookup_online("jolt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparage(self):
        html_dump = lookup_online("disparage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parlance(self):
        html_dump = lookup_online("parlance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_confine(self):
        html_dump = lookup_online("confine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distributed(self):
        html_dump = lookup_online("distributed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leonine(self):
        html_dump = lookup_online("leonine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spain(self):
        html_dump = lookup_online("spain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slyly(self):
        html_dump = lookup_online("slyly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seminal(self):
        html_dump = lookup_online("seminal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_culpability(self):
        html_dump = lookup_online("culpability").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mediocrity(self):
        html_dump = lookup_online("mediocrity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auspice(self):
        html_dump = lookup_online("auspice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grandee(self):
        html_dump = lookup_online("grandee").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frankness(self):
        html_dump = lookup_online("frankness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wily(self):
        html_dump = lookup_online("wily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gored(self):
        html_dump = lookup_online("gored").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plonk(self):
        html_dump = lookup_online("plonk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbridled(self):
        html_dump = lookup_online("unbridled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spunk(self):
        html_dump = lookup_online("spunk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rile(self):
        html_dump = lookup_online("rile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_titter(self):
        html_dump = lookup_online("titter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_writhe(self):
        html_dump = lookup_online("writhe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crummy(self):
        html_dump = lookup_online("crummy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sob(self):
        html_dump = lookup_online("sob").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remedy(self):
        html_dump = lookup_online("remedy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparaging(self):
        html_dump = lookup_online("disparaging").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_keef(self):
        html_dump = lookup_online("keef").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lint(self):
        html_dump = lookup_online("lint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relieved(self):
        html_dump = lookup_online("relieved").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tits(self):
        html_dump = lookup_online("tits").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sorority(self):
        html_dump = lookup_online("sorority").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oleander(self):
        html_dump = lookup_online("oleander").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mulberry(self):
        html_dump = lookup_online("mulberry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incredulity(self):
        html_dump = lookup_online("incredulity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boon(self):
        html_dump = lookup_online("boon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_freckle(self):
        html_dump = lookup_online("freckle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beget(self):
        html_dump = lookup_online("beget").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curtail(self):
        html_dump = lookup_online("curtail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sack(self):
        html_dump = lookup_online("sack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amalgamation(self):
        html_dump = lookup_online("amalgamation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slandering(self):
        html_dump = lookup_online("slandering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malt(self):
        html_dump = lookup_online("malt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allusive(self):
        html_dump = lookup_online("allusive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mewl(self):
        html_dump = lookup_online("mewl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tinny(self):
        html_dump = lookup_online("tinny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curl(self):
        html_dump = lookup_online("curl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liability(self):
        html_dump = lookup_online("liability").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consort(self):
        html_dump = lookup_online("consort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tar(self):
        html_dump = lookup_online("tar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vantage(self):
        html_dump = lookup_online("vantage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moped(self):
        html_dump = lookup_online("moped").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sludge(self):
        html_dump = lookup_online("sludge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gurney(self):
        html_dump = lookup_online("gurney").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nascent(self):
        html_dump = lookup_online("nascent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fender(self):
        html_dump = lookup_online("fender").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunker(self):
        html_dump = lookup_online("hunker").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adroitness(self):
        html_dump = lookup_online("adroitness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litmus(self):
        html_dump = lookup_online("litmus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salmon(self):
        html_dump = lookup_online("salmon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jessamine(self):
        html_dump = lookup_online("jessamine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gnarly(self):
        html_dump = lookup_online("gnarly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_verge(self):
        html_dump = lookup_online("verge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_destitute(self):
        html_dump = lookup_online("destitute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refrain(self):
        html_dump = lookup_online("refrain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derange(self):
        html_dump = lookup_online("derange").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equestrian(self):
        html_dump = lookup_online("equestrian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grovel(self):
        html_dump = lookup_online("grovel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_articulate(self):
        html_dump = lookup_online("articulate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilance(self):
        html_dump = lookup_online("vigilance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dumb(self):
        html_dump = lookup_online("dumb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tutelage(self):
        html_dump = lookup_online("tutelage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toehold(self):
        html_dump = lookup_online("toehold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapacious(self):
        html_dump = lookup_online("rapacious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puppet(self):
        html_dump = lookup_online("puppet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brute(self):
        html_dump = lookup_online("brute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_briskly(self):
        html_dump = lookup_online("briskly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_guile(self):
        html_dump = lookup_online("guile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chestnut(self):
        html_dump = lookup_online("chestnut").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tort(self):
        html_dump = lookup_online("tort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frenetic(self):
        html_dump = lookup_online("frenetic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shambles(self):
        html_dump = lookup_online("shambles").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yoke(self):
        html_dump = lookup_online("yoke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lentil(self):
        html_dump = lookup_online("lentil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clobber(self):
        html_dump = lookup_online("clobber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appendix(self):
        html_dump = lookup_online("appendix").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conspicuous(self):
        html_dump = lookup_online("conspicuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_covet(self):
        html_dump = lookup_online("covet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_henchman(self):
        html_dump = lookup_online("henchman").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regurgitate(self):
        html_dump = lookup_online("regurgitate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fabricated(self):
        html_dump = lookup_online("fabricated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leatherette(self):
        html_dump = lookup_online("leatherette").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inauspicious(self):
        html_dump = lookup_online("inauspicious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chattel(self):
        html_dump = lookup_online("chattel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imbibe(self):
        html_dump = lookup_online("imbibe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unclench(self):
        html_dump = lookup_online("unclench").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incidence(self):
        html_dump = lookup_online("incidence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wager(self):
        html_dump = lookup_online("wager").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curdled(self):
        html_dump = lookup_online("curdled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insipid(self):
        html_dump = lookup_online("insipid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presumptuousness(self):
        html_dump = lookup_online("presumptuousness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menacingly(self):
        html_dump = lookup_online("menacingly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lousy(self):
        html_dump = lookup_online("lousy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_metonymy(self):
        html_dump = lookup_online("metonymy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parsimonious(self):
        html_dump = lookup_online("parsimonious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exert(self):
        html_dump = lookup_online("exert").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bumbling(self):
        html_dump = lookup_online("bumbling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whim(self):
        html_dump = lookup_online("whim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transgression(self):
        html_dump = lookup_online("transgression").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanction(self):
        html_dump = lookup_online("sanction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_theory(self):
        html_dump = lookup_online("theory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_faciliate(self):
        html_dump = lookup_online("faciliate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fugue(self):
        html_dump = lookup_online("fugue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bronchitis(self):
        html_dump = lookup_online("bronchitis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cockeyed(self):
        html_dump = lookup_online("cockeyed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pallor(self):
        html_dump = lookup_online("pallor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cliche(self):
        html_dump = lookup_online("cliche").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fleece(self):
        html_dump = lookup_online("fleece").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embellished(self):
        html_dump = lookup_online("embellished").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evokes(self):
        html_dump = lookup_online("evokes").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hedge(self):
        html_dump = lookup_online("hedge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pique(self):
        html_dump = lookup_online("pique").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_topiary(self):
        html_dump = lookup_online("topiary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slack(self):
        html_dump = lookup_online("slack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prune(self):
        html_dump = lookup_online("prune").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bleak(self):
        html_dump = lookup_online("bleak").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oxbow(self):
        html_dump = lookup_online("oxbow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coitus(self):
        html_dump = lookup_online("coitus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lightning(self):
        html_dump = lookup_online("lightning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morose(self):
        html_dump = lookup_online("morose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_assiduous(self):
        html_dump = lookup_online("assiduous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_legitimate(self):
        html_dump = lookup_online("legitimate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nether(self):
        html_dump = lookup_online("nether").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_valiant(self):
        html_dump = lookup_online("valiant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fissure(self):
        html_dump = lookup_online("fissure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaded(self):
        html_dump = lookup_online("jaded").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_demean(self):
        html_dump = lookup_online("demean").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zest(self):
        html_dump = lookup_online("zest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preen(self):
        html_dump = lookup_online("preen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amanuensis(self):
        html_dump = lookup_online("amanuensis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raucous(self):
        html_dump = lookup_online("raucous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insatiable(self):
        html_dump = lookup_online("insatiable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_litigious(self):
        html_dump = lookup_online("litigious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucre(self):
        html_dump = lookup_online("lucre").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sunset(self):
        html_dump = lookup_online("sunset").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abet(self):
        html_dump = lookup_online("abet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quench(self):
        html_dump = lookup_online("quench").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grueling(self):
        html_dump = lookup_online("grueling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulcerate(self):
        html_dump = lookup_online("ulcerate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vogue(self):
        html_dump = lookup_online("vogue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fad(self):
        html_dump = lookup_online("fad").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benign(self):
        html_dump = lookup_online("benign").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grout(self):
        html_dump = lookup_online("grout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lard(self):
        html_dump = lookup_online("lard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_labour(self):
        html_dump = lookup_online("labour").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barnacle(self):
        html_dump = lookup_online("barnacle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agitate(self):
        html_dump = lookup_online("agitate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soldier(self):
        html_dump = lookup_online("soldier").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infamous(self):
        html_dump = lookup_online("infamous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_evince(self):
        html_dump = lookup_online("evince").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pungent(self):
        html_dump = lookup_online("pungent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bereft(self):
        html_dump = lookup_online("bereft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trailing(self):
        html_dump = lookup_online("trailing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_husky(self):
        html_dump = lookup_online("husky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miff(self):
        html_dump = lookup_online("miff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ointment(self):
        html_dump = lookup_online("ointment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disrupt(self):
        html_dump = lookup_online("disrupt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_later(self):
        html_dump = lookup_online("later").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gossamer(self):
        html_dump = lookup_online("gossamer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_courtship(self):
        html_dump = lookup_online("courtship").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appall(self):
        html_dump = lookup_online("appall").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wither(self):
        html_dump = lookup_online("wither").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despatch(self):
        html_dump = lookup_online("despatch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stooge(self):
        html_dump = lookup_online("stooge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arboretum(self):
        html_dump = lookup_online("arboretum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flout(self):
        html_dump = lookup_online("flout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_promiscuity(self):
        html_dump = lookup_online("promiscuity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_irate(self):
        html_dump = lookup_online("irate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loggerhead(self):
        html_dump = lookup_online("loggerhead").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strive(self):
        html_dump = lookup_online("strive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loony(self):
        html_dump = lookup_online("loony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midden(self):
        html_dump = lookup_online("midden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desultorily(self):
        html_dump = lookup_online("desultorily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_motley(self):
        html_dump = lookup_online("motley").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longing(self):
        html_dump = lookup_online("longing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bifurcation(self):
        html_dump = lookup_online("bifurcation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_groan(self):
        html_dump = lookup_online("groan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bile(self):
        html_dump = lookup_online("bile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pheasant(self):
        html_dump = lookup_online("pheasant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afoul(self):
        html_dump = lookup_online("afoul").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despondency(self):
        html_dump = lookup_online("despondency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tetanus(self):
        html_dump = lookup_online("tetanus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetuity(self):
        html_dump = lookup_online("perpetuity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pilfering(self):
        html_dump = lookup_online("pilfering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_substitute(self):
        html_dump = lookup_online("substitute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prowl(self):
        html_dump = lookup_online("prowl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grue(self):
        html_dump = lookup_online("grue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bole(self):
        html_dump = lookup_online("bole").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duende(self):
        html_dump = lookup_online("duende").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_token(self):
        html_dump = lookup_online("token").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescension(self):
        html_dump = lookup_online("condescension").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indenture(self):
        html_dump = lookup_online("indenture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sham(self):
        html_dump = lookup_online("sham").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effluent(self):
        html_dump = lookup_online("effluent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infantry(self):
        html_dump = lookup_online("infantry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nematode(self):
        html_dump = lookup_online("nematode").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alopecia(self):
        html_dump = lookup_online("alopecia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bop(self):
        html_dump = lookup_online("bop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gamin(self):
        html_dump = lookup_online("gamin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relent(self):
        html_dump = lookup_online("relent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiddly(self):
        html_dump = lookup_online("fiddly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_protein(self):
        html_dump = lookup_online("protein").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trailblazing(self):
        html_dump = lookup_online("trailblazing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exigency(self):
        html_dump = lookup_online("exigency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perilous(self):
        html_dump = lookup_online("perilous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gimp(self):
        html_dump = lookup_online("gimp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipice(self):
        html_dump = lookup_online("precipice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imperil(self):
        html_dump = lookup_online("imperil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quagmire(self):
        html_dump = lookup_online("quagmire").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cull(self):
        html_dump = lookup_online("cull").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indeterminate(self):
        html_dump = lookup_online("indeterminate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncharitable(self):
        html_dump = lookup_online("uncharitable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trope(self):
        html_dump = lookup_online("trope").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_roundel(self):
        html_dump = lookup_online("roundel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inveterate(self):
        html_dump = lookup_online("inveterate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heedlessly(self):
        html_dump = lookup_online("heedlessly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_littoral(self):
        html_dump = lookup_online("littoral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spuriously(self):
        html_dump = lookup_online("spuriously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_readability(self):
        html_dump = lookup_online("readability").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sunder(self):
        html_dump = lookup_online("sunder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curbing(self):
        html_dump = lookup_online("curbing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumes(self):
        html_dump = lookup_online("fumes").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_congenital(self):
        html_dump = lookup_online("congenital").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumination(self):
        html_dump = lookup_online("rumination").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drape(self):
        html_dump = lookup_online("drape").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fulguration(self):
        html_dump = lookup_online("fulguration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pancreatitis(self):
        html_dump = lookup_online("pancreatitis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repugnance(self):
        html_dump = lookup_online("repugnance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bushel(self):
        html_dump = lookup_online("bushel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wayward(self):
        html_dump = lookup_online("wayward").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedulity(self):
        html_dump = lookup_online("sedulity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elision(self):
        html_dump = lookup_online("elision").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paltry(self):
        html_dump = lookup_online("paltry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_friar(self):
        html_dump = lookup_online("friar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flue(self):
        html_dump = lookup_online("flue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fluff(self):
        html_dump = lookup_online("fluff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deciduous(self):
        html_dump = lookup_online("deciduous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_invalid(self):
        html_dump = lookup_online("invalid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrimp(self):
        html_dump = lookup_online("shrimp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vapor(self):
        html_dump = lookup_online("vapor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vacation(self):
        html_dump = lookup_online("vacation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gritty(self):
        html_dump = lookup_online("gritty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crony(self):
        html_dump = lookup_online("crony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yarn(self):
        html_dump = lookup_online("yarn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gypsy(self):
        html_dump = lookup_online("gypsy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sulk(self):
        html_dump = lookup_online("sulk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eager(self):
        html_dump = lookup_online("eager").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savvy(self):
        html_dump = lookup_online("savvy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thrush(self):
        html_dump = lookup_online("thrush").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_famished(self):
        html_dump = lookup_online("famished").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wayfare(self):
        html_dump = lookup_online("wayfare").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bargain(self):
        html_dump = lookup_online("bargain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sinewy(self):
        html_dump = lookup_online("sinewy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexplicably(self):
        html_dump = lookup_online("inexplicably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beset(self):
        html_dump = lookup_online("beset").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unhinge(self):
        html_dump = lookup_online("unhinge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_immane(self):
        html_dump = lookup_online("immane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eking(self):
        html_dump = lookup_online("eking").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanctimonious(self):
        html_dump = lookup_online("sanctimonious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raspy(self):
        html_dump = lookup_online("raspy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cattle(self):
        html_dump = lookup_online("cattle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_marmite(self):
        html_dump = lookup_online("marmite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckless(self):
        html_dump = lookup_online("reckless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thicket(self):
        html_dump = lookup_online("thicket").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_halter(self):
        html_dump = lookup_online("halter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_goldilocks(self):
        html_dump = lookup_online("goldilocks").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yeoman(self):
        html_dump = lookup_online("yeoman").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gumption(self):
        html_dump = lookup_online("gumption").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harmonious(self):
        html_dump = lookup_online("harmonious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_guest(self):
        html_dump = lookup_online("guest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_butler(self):
        html_dump = lookup_online("butler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenacity(self):
        html_dump = lookup_online("tenacity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salacious(self):
        html_dump = lookup_online("salacious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sentience(self):
        html_dump = lookup_online("sentience").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peddle(self):
        html_dump = lookup_online("peddle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disbar(self):
        html_dump = lookup_online("disbar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equanimity(self):
        html_dump = lookup_online("equanimity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catamite(self):
        html_dump = lookup_online("catamite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taper(self):
        html_dump = lookup_online("taper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veneer(self):
        html_dump = lookup_online("veneer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effect(self):
        html_dump = lookup_online("effect").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hazmat(self):
        html_dump = lookup_online("hazmat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sobriquet(self):
        html_dump = lookup_online("sobriquet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_integrity(self):
        html_dump = lookup_online("integrity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avarice(self):
        html_dump = lookup_online("avarice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abate(self):
        html_dump = lookup_online("abate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salubrious(self):
        html_dump = lookup_online("salubrious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jocose(self):
        html_dump = lookup_online("jocose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dilation(self):
        html_dump = lookup_online("dilation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lemma(self):
        html_dump = lookup_online("lemma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beet(self):
        html_dump = lookup_online("beet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savour(self):
        html_dump = lookup_online("savour").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_martyr(self):
        html_dump = lookup_online("martyr").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laryngitis(self):
        html_dump = lookup_online("laryngitis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ignominious(self):
        html_dump = lookup_online("ignominious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_senile(self):
        html_dump = lookup_online("senile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intervention(self):
        html_dump = lookup_online("intervention").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embezzlement(self):
        html_dump = lookup_online("embezzlement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bitters(self):
        html_dump = lookup_online("bitters").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vivisection(self):
        html_dump = lookup_online("vivisection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frothy(self):
        html_dump = lookup_online("frothy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amity(self):
        html_dump = lookup_online("amity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hussy(self):
        html_dump = lookup_online("hussy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virile(self):
        html_dump = lookup_online("virile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snoop(self):
        html_dump = lookup_online("snoop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abeyance(self):
        html_dump = lookup_online("abeyance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_raddled(self):
        html_dump = lookup_online("raddled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vacuous(self):
        html_dump = lookup_online("vacuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmuring(self):
        html_dump = lookup_online("murmuring").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kindling(self):
        html_dump = lookup_online("kindling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sweep(self):
        html_dump = lookup_online("sweep").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defect(self):
        html_dump = lookup_online("defect").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skid(self):
        html_dump = lookup_online("skid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interweave(self):
        html_dump = lookup_online("interweave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_egotism(self):
        html_dump = lookup_online("egotism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aerated(self):
        html_dump = lookup_online("aerated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_con(self):
        html_dump = lookup_online("con").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commence(self):
        html_dump = lookup_online("commence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_care(self):
        html_dump = lookup_online("care").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genteel(self):
        html_dump = lookup_online("genteel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disavow(self):
        html_dump = lookup_online("disavow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjecture(self):
        html_dump = lookup_online("conjecture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_skewer(self):
        html_dump = lookup_online("skewer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_consolidate(self):
        html_dump = lookup_online("consolidate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_remit(self):
        html_dump = lookup_online("remit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aging(self):
        html_dump = lookup_online("aging").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_badger(self):
        html_dump = lookup_online("badger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangible(self):
        html_dump = lookup_online("tangible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigil(self):
        html_dump = lookup_online("vigil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sag(self):
        html_dump = lookup_online("sag").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gerbil(self):
        html_dump = lookup_online("gerbil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fierceness(self):
        html_dump = lookup_online("fierceness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quiver(self):
        html_dump = lookup_online("quiver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_itinerary(self):
        html_dump = lookup_online("itinerary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presupposition(self):
        html_dump = lookup_online("presupposition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaol(self):
        html_dump = lookup_online("gaol").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ronin(self):
        html_dump = lookup_online("ronin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clatter(self):
        html_dump = lookup_online("clatter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eek(self):
        html_dump = lookup_online("eek").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaff(self):
        html_dump = lookup_online("quaff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shin(self):
        html_dump = lookup_online("shin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitation(self):
        html_dump = lookup_online("precipitation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flax(self):
        html_dump = lookup_online("flax").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quietude(self):
        html_dump = lookup_online("quietude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bohemian(self):
        html_dump = lookup_online("bohemian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palate(self):
        html_dump = lookup_online("palate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prolix(self):
        html_dump = lookup_online("prolix").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mink(self):
        html_dump = lookup_online("mink").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reconcile(self):
        html_dump = lookup_online("reconcile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_morass(self):
        html_dump = lookup_online("morass").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallible(self):
        html_dump = lookup_online("fallible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_centrifuge(self):
        html_dump = lookup_online("centrifuge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inculcate(self):
        html_dump = lookup_online("inculcate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fussy(self):
        html_dump = lookup_online("fussy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boozer(self):
        html_dump = lookup_online("boozer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cairn(self):
        html_dump = lookup_online("cairn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_auxilary(self):
        html_dump = lookup_online("auxilary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stele(self):
        html_dump = lookup_online("stele").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_restitution(self):
        html_dump = lookup_online("restitution").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fidgety(self):
        html_dump = lookup_online("fidgety").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contortion(self):
        html_dump = lookup_online("contortion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obscene(self):
        html_dump = lookup_online("obscene").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jeopardy(self):
        html_dump = lookup_online("jeopardy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_facetious(self):
        html_dump = lookup_online("facetious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chunky(self):
        html_dump = lookup_online("chunky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_osprey(self):
        html_dump = lookup_online("osprey").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rally(self):
        html_dump = lookup_online("rally").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foster(self):
        html_dump = lookup_online("foster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pace(self):
        html_dump = lookup_online("pace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bland(self):
        html_dump = lookup_online("bland").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sling(self):
        html_dump = lookup_online("sling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_posh(self):
        html_dump = lookup_online("posh").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsightly(self):
        html_dump = lookup_online("unsightly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bobcat(self):
        html_dump = lookup_online("bobcat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stricture(self):
        html_dump = lookup_online("stricture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blindsided(self):
        html_dump = lookup_online("blindsided").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unilateral(self):
        html_dump = lookup_online("unilateral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perseverance(self):
        html_dump = lookup_online("perseverance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_herbicide(self):
        html_dump = lookup_online("herbicide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adversity(self):
        html_dump = lookup_online("adversity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garble(self):
        html_dump = lookup_online("garble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strained(self):
        html_dump = lookup_online("strained").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meadow(self):
        html_dump = lookup_online("meadow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spleen(self):
        html_dump = lookup_online("spleen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vassalage(self):
        html_dump = lookup_online("vassalage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_violent(self):
        html_dump = lookup_online("violent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tenuous(self):
        html_dump = lookup_online("tenuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inhibit(self):
        html_dump = lookup_online("inhibit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untenable(self):
        html_dump = lookup_online("untenable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_equity(self):
        html_dump = lookup_online("equity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertinently(self):
        html_dump = lookup_online("pertinently").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gasket(self):
        html_dump = lookup_online("gasket").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neglect(self):
        html_dump = lookup_online("neglect").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruffled(self):
        html_dump = lookup_online("ruffled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inoculation(self):
        html_dump = lookup_online("inoculation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tough(self):
        html_dump = lookup_online("tough").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solidarity(self):
        html_dump = lookup_online("solidarity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sulking(self):
        html_dump = lookup_online("sulking").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brittle(self):
        html_dump = lookup_online("brittle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsavory(self):
        html_dump = lookup_online("unsavory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_altogether(self):
        html_dump = lookup_online("altogether").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disturbed(self):
        html_dump = lookup_online("disturbed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parish(self):
        html_dump = lookup_online("parish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fanny(self):
        html_dump = lookup_online("fanny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prolific(self):
        html_dump = lookup_online("prolific").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cater(self):
        html_dump = lookup_online("cater").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_punctilious(self):
        html_dump = lookup_online("punctilious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shaft(self):
        html_dump = lookup_online("shaft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jell(self):
        html_dump = lookup_online("jell").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acerbic(self):
        html_dump = lookup_online("acerbic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wicked(self):
        html_dump = lookup_online("wicked").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incarceration(self):
        html_dump = lookup_online("incarceration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chokehold(self):
        html_dump = lookup_online("chokehold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distressing(self):
        html_dump = lookup_online("distressing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clover(self):
        html_dump = lookup_online("clover").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teak(self):
        html_dump = lookup_online("teak").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pariah(self):
        html_dump = lookup_online("pariah").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pious(self):
        html_dump = lookup_online("pious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_homemaker(self):
        html_dump = lookup_online("homemaker").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rabble(self):
        html_dump = lookup_online("rabble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_millet(self):
        html_dump = lookup_online("millet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hieratic(self):
        html_dump = lookup_online("hieratic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pliable(self):
        html_dump = lookup_online("pliable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derived(self):
        html_dump = lookup_online("derived").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_surmise(self):
        html_dump = lookup_online("surmise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ominous(self):
        html_dump = lookup_online("ominous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whimsical(self):
        html_dump = lookup_online("whimsical").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indentured(self):
        html_dump = lookup_online("indentured").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_further(self):
        html_dump = lookup_online("further").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_argot(self):
        html_dump = lookup_online("argot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abode(self):
        html_dump = lookup_online("abode").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shed(self):
        html_dump = lookup_online("shed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chiefly(self):
        html_dump = lookup_online("chiefly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burden(self):
        html_dump = lookup_online("burden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placenta(self):
        html_dump = lookup_online("placenta").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hireling(self):
        html_dump = lookup_online("hireling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_saunter(self):
        html_dump = lookup_online("saunter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moniker(self):
        html_dump = lookup_online("moniker").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perseverative(self):
        html_dump = lookup_online("perseverative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tribunal(self):
        html_dump = lookup_online("tribunal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sputter(self):
        html_dump = lookup_online("sputter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_singular(self):
        html_dump = lookup_online("singular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_backhanded(self):
        html_dump = lookup_online("backhanded").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meld(self):
        html_dump = lookup_online("meld").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slim(self):
        html_dump = lookup_online("slim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_innuendo(self):
        html_dump = lookup_online("innuendo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brash(self):
        html_dump = lookup_online("brash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infirmary(self):
        html_dump = lookup_online("infirmary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eve(self):
        html_dump = lookup_online("eve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bullhorn(self):
        html_dump = lookup_online("bullhorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trepidation(self):
        html_dump = lookup_online("trepidation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clairvoyance(self):
        html_dump = lookup_online("clairvoyance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subversive(self):
        html_dump = lookup_online("subversive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bestow(self):
        html_dump = lookup_online("bestow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awash(self):
        html_dump = lookup_online("awash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tawdry(self):
        html_dump = lookup_online("tawdry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yield(self):
        html_dump = lookup_online("yield").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_molar(self):
        html_dump = lookup_online("molar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dispassionate(self):
        html_dump = lookup_online("dispassionate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unyielding(self):
        html_dump = lookup_online("unyielding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dull(self):
        html_dump = lookup_online("dull").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squish(self):
        html_dump = lookup_online("squish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dictum(self):
        html_dump = lookup_online("dictum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_musty(self):
        html_dump = lookup_online("musty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rigmarole(self):
        html_dump = lookup_online("rigmarole").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spasm(self):
        html_dump = lookup_online("spasm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_distress(self):
        html_dump = lookup_online("distress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stillborn(self):
        html_dump = lookup_online("stillborn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gloomy(self):
        html_dump = lookup_online("gloomy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incantatory(self):
        html_dump = lookup_online("incantatory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gutter(self):
        html_dump = lookup_online("gutter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fond(self):
        html_dump = lookup_online("fond").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_melanoma(self):
        html_dump = lookup_online("melanoma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tread(self):
        html_dump = lookup_online("tread").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acquit(self):
        html_dump = lookup_online("acquit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumigate(self):
        html_dump = lookup_online("fumigate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foil(self):
        html_dump = lookup_online("foil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bristle(self):
        html_dump = lookup_online("bristle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Fan(self):
        html_dump = lookup_online("Fan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stature(self):
        html_dump = lookup_online("stature").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abrasive(self):
        html_dump = lookup_online("abrasive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defy(self):
        html_dump = lookup_online("defy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminently(self):
        html_dump = lookup_online("eminently").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harken(self):
        html_dump = lookup_online("harken").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limper(self):
        html_dump = lookup_online("limper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disbarment(self):
        html_dump = lookup_online("disbarment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acrimonious(self):
        html_dump = lookup_online("acrimonious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recap(self):
        html_dump = lookup_online("recap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transient(self):
        html_dump = lookup_online("transient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forgo(self):
        html_dump = lookup_online("forgo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enamel(self):
        html_dump = lookup_online("enamel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_serenity(self):
        html_dump = lookup_online("serenity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soggy(self):
        html_dump = lookup_online("soggy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_binding(self):
        html_dump = lookup_online("binding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bulge(self):
        html_dump = lookup_online("bulge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loth(self):
        html_dump = lookup_online("loth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_salve(self):
        html_dump = lookup_online("salve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shawl(self):
        html_dump = lookup_online("shawl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manger(self):
        html_dump = lookup_online("manger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_festering(self):
        html_dump = lookup_online("festering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feisty(self):
        html_dump = lookup_online("feisty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barmy(self):
        html_dump = lookup_online("barmy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_qualm(self):
        html_dump = lookup_online("qualm").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_and(self):
        html_dump = lookup_online("and").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yelp(self):
        html_dump = lookup_online("yelp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prattle(self):
        html_dump = lookup_online("prattle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crow(self):
        html_dump = lookup_online("crow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jurisprudence(self):
        html_dump = lookup_online("jurisprudence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leach(self):
        html_dump = lookup_online("leach").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stencil(self):
        html_dump = lookup_online("stencil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cromulent(self):
        html_dump = lookup_online("cromulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_downtrodden(self):
        html_dump = lookup_online("downtrodden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_honeydew(self):
        html_dump = lookup_online("honeydew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cemetery(self):
        html_dump = lookup_online("cemetery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stippled(self):
        html_dump = lookup_online("stippled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_determinate(self):
        html_dump = lookup_online("determinate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shingles(self):
        html_dump = lookup_online("shingles").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edgy(self):
        html_dump = lookup_online("edgy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myopia(self):
        html_dump = lookup_online("myopia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obsequiousness(self):
        html_dump = lookup_online("obsequiousness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misappropriate(self):
        html_dump = lookup_online("misappropriate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meanly(self):
        html_dump = lookup_online("meanly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardent(self):
        html_dump = lookup_online("ardent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cranium(self):
        html_dump = lookup_online("cranium").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_comma(self):
        html_dump = lookup_online("comma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insolent(self):
        html_dump = lookup_online("insolent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ramrod(self):
        html_dump = lookup_online("ramrod").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stringent(self):
        html_dump = lookup_online("stringent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_baleful(self):
        html_dump = lookup_online("baleful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haven(self):
        html_dump = lookup_online("haven").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dregs(self):
        html_dump = lookup_online("dregs").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upend(self):
        html_dump = lookup_online("upend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conduit(self):
        html_dump = lookup_online("conduit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toddle(self):
        html_dump = lookup_online("toddle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malady(self):
        html_dump = lookup_online("malady").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_olfaction(self):
        html_dump = lookup_online("olfaction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accrue(self):
        html_dump = lookup_online("accrue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slather(self):
        html_dump = lookup_online("slather").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranquil(self):
        html_dump = lookup_online("tranquil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plummet(self):
        html_dump = lookup_online("plummet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bustard(self):
        html_dump = lookup_online("bustard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_somber(self):
        html_dump = lookup_online("somber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hitch(self):
        html_dump = lookup_online("hitch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tiller(self):
        html_dump = lookup_online("tiller").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_varsity(self):
        html_dump = lookup_online("varsity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outpace(self):
        html_dump = lookup_online("outpace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plow(self):
        html_dump = lookup_online("plow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limpid(self):
        html_dump = lookup_online("limpid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heap(self):
        html_dump = lookup_online("heap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_suite(self):
        html_dump = lookup_online("suite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harbinger(self):
        html_dump = lookup_online("harbinger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deft(self):
        html_dump = lookup_online("deft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ebb(self):
        html_dump = lookup_online("ebb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrewdness(self):
        html_dump = lookup_online("shrewdness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recant(self):
        html_dump = lookup_online("recant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exquisite(self):
        html_dump = lookup_online("exquisite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fiat(self):
        html_dump = lookup_online("fiat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_primacy(self):
        html_dump = lookup_online("primacy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tuff(self):
        html_dump = lookup_online("tuff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheen(self):
        html_dump = lookup_online("sheen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slope(self):
        html_dump = lookup_online("slope").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vigilantly(self):
        html_dump = lookup_online("vigilantly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kerfuffle(self):
        html_dump = lookup_online("kerfuffle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glare(self):
        html_dump = lookup_online("glare").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_permaculture(self):
        html_dump = lookup_online("permaculture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grunch(self):
        html_dump = lookup_online("grunch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rayon(self):
        html_dump = lookup_online("rayon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_effusive(self):
        html_dump = lookup_online("effusive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thine(self):
        html_dump = lookup_online("thine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_locus(self):
        html_dump = lookup_online("locus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aftermath(self):
        html_dump = lookup_online("aftermath").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savant(self):
        html_dump = lookup_online("savant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mongrel(self):
        html_dump = lookup_online("mongrel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_odometer(self):
        html_dump = lookup_online("odometer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_complacent(self):
        html_dump = lookup_online("complacent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crushed(self):
        html_dump = lookup_online("crushed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dimwit(self):
        html_dump = lookup_online("dimwit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concur(self):
        html_dump = lookup_online("concur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resentful(self):
        html_dump = lookup_online("resentful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_redundancy(self):
        html_dump = lookup_online("redundancy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eventually(self):
        html_dump = lookup_online("eventually").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sheaf(self):
        html_dump = lookup_online("sheaf").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrusive(self):
        html_dump = lookup_online("intrusive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_refusenik(self):
        html_dump = lookup_online("refusenik").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunk(self):
        html_dump = lookup_online("hunk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_camomile(self):
        html_dump = lookup_online("camomile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_veneration(self):
        html_dump = lookup_online("veneration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_seesaw(self):
        html_dump = lookup_online("seesaw").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reek(self):
        html_dump = lookup_online("reek").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pine(self):
        html_dump = lookup_online("pine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_digest(self):
        html_dump = lookup_online("digest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rave(self):
        html_dump = lookup_online("rave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gargantuan(self):
        html_dump = lookup_online("gargantuan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yon(self):
        html_dump = lookup_online("yon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_chaplain(self):
        html_dump = lookup_online("chaplain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atavistic(self):
        html_dump = lookup_online("atavistic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atone(self):
        html_dump = lookup_online("atone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aquiver(self):
        html_dump = lookup_online("aquiver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brisk(self):
        html_dump = lookup_online("brisk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestige(self):
        html_dump = lookup_online("vestige").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doubtless(self):
        html_dump = lookup_online("doubtless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exultant(self):
        html_dump = lookup_online("exultant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simp(self):
        html_dump = lookup_online("simp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forage(self):
        html_dump = lookup_online("forage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lofty(self):
        html_dump = lookup_online("lofty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acuity(self):
        html_dump = lookup_online("acuity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cop(self):
        html_dump = lookup_online("cop").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rawhide(self):
        html_dump = lookup_online("rawhide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unwind(self):
        html_dump = lookup_online("unwind").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferocity(self):
        html_dump = lookup_online("ferocity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vanguard(self):
        html_dump = lookup_online("vanguard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lattice(self):
        html_dump = lookup_online("lattice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curmudgeon(self):
        html_dump = lookup_online("curmudgeon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intractable(self):
        html_dump = lookup_online("intractable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_basking(self):
        html_dump = lookup_online("basking").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lackeys(self):
        html_dump = lookup_online("lackeys").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hunch(self):
        html_dump = lookup_online("hunch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapt(self):
        html_dump = lookup_online("rapt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incandescence(self):
        html_dump = lookup_online("incandescence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_behest(self):
        html_dump = lookup_online("behest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedate(self):
        html_dump = lookup_online("sedate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wilt(self):
        html_dump = lookup_online("wilt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_temerity(self):
        html_dump = lookup_online("temerity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humility(self):
        html_dump = lookup_online("humility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ripe(self):
        html_dump = lookup_online("ripe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncovered(self):
        html_dump = lookup_online("uncovered").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sweeping(self):
        html_dump = lookup_online("sweeping").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apperception(self):
        html_dump = lookup_online("apperception").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_destitution(self):
        html_dump = lookup_online("destitution").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_canny(self):
        html_dump = lookup_online("canny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voracious(self):
        html_dump = lookup_online("voracious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haggle(self):
        html_dump = lookup_online("haggle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overpass(self):
        html_dump = lookup_online("overpass").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disarray(self):
        html_dump = lookup_online("disarray").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unease(self):
        html_dump = lookup_online("unease").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alleviate(self):
        html_dump = lookup_online("alleviate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraction(self):
        html_dump = lookup_online("contraction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condone(self):
        html_dump = lookup_online("condone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tail(self):
        html_dump = lookup_online("tail").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unrelenting(self):
        html_dump = lookup_online("unrelenting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ditties(self):
        html_dump = lookup_online("ditties").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tacit(self):
        html_dump = lookup_online("tacit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lam(self):
        html_dump = lookup_online("lam").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_annoyed(self):
        html_dump = lookup_online("annoyed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lash(self):
        html_dump = lookup_online("lash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wage(self):
        html_dump = lookup_online("wage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unpalatable(self):
        html_dump = lookup_online("unpalatable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glossary(self):
        html_dump = lookup_online("glossary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_libel(self):
        html_dump = lookup_online("libel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teamster(self):
        html_dump = lookup_online("teamster").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repudiate(self):
        html_dump = lookup_online("repudiate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interwoven(self):
        html_dump = lookup_online("interwoven").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spate(self):
        html_dump = lookup_online("spate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pervasive(self):
        html_dump = lookup_online("pervasive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fusion(self):
        html_dump = lookup_online("fusion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abduct(self):
        html_dump = lookup_online("abduct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peccant(self):
        html_dump = lookup_online("peccant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outlandish(self):
        html_dump = lookup_online("outlandish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prudish(self):
        html_dump = lookup_online("prudish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scupper(self):
        html_dump = lookup_online("scupper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conciliation(self):
        html_dump = lookup_online("conciliation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disdain(self):
        html_dump = lookup_online("disdain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incendiary(self):
        html_dump = lookup_online("incendiary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deterrent(self):
        html_dump = lookup_online("deterrent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crippled(self):
        html_dump = lookup_online("crippled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arbitrage(self):
        html_dump = lookup_online("arbitrage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_same(self):
        html_dump = lookup_online("same").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_forecast(self):
        html_dump = lookup_online("forecast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exhilaration(self):
        html_dump = lookup_online("exhilaration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peregrination(self):
        html_dump = lookup_online("peregrination").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commune(self):
        html_dump = lookup_online("commune").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garishness(self):
        html_dump = lookup_online("garishness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_creeping(self):
        html_dump = lookup_online("creeping").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sinister(self):
        html_dump = lookup_online("sinister").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placating(self):
        html_dump = lookup_online("placating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_narrow(self):
        html_dump = lookup_online("narrow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nimble(self):
        html_dump = lookup_online("nimble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bandicoot(self):
        html_dump = lookup_online("bandicoot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_atrocious(self):
        html_dump = lookup_online("atrocious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garrulous(self):
        html_dump = lookup_online("garrulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bulk(self):
        html_dump = lookup_online("bulk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaundice(self):
        html_dump = lookup_online("jaundice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arguably(self):
        html_dump = lookup_online("arguably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleep(self):
        html_dump = lookup_online("sleep").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conciliatory(self):
        html_dump = lookup_online("conciliatory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gaze(self):
        html_dump = lookup_online("gaze").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aniseed(self):
        html_dump = lookup_online("aniseed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desiccate(self):
        html_dump = lookup_online("desiccate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dreadful(self):
        html_dump = lookup_online("dreadful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shimmer(self):
        html_dump = lookup_online("shimmer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vice(self):
        html_dump = lookup_online("vice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incinerator(self):
        html_dump = lookup_online("incinerator").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_delineate(self):
        html_dump = lookup_online("delineate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_alimony(self):
        html_dump = lookup_online("alimony").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_captivating(self):
        html_dump = lookup_online("captivating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hustle(self):
        html_dump = lookup_online("hustle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_endearment(self):
        html_dump = lookup_online("endearment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limp(self):
        html_dump = lookup_online("limp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phubbing(self):
        html_dump = lookup_online("phubbing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flay(self):
        html_dump = lookup_online("flay").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spoke(self):
        html_dump = lookup_online("spoke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbate(self):
        html_dump = lookup_online("exacerbate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hide(self):
        html_dump = lookup_online("hide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frankincense(self):
        html_dump = lookup_online("frankincense").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tale(self):
        html_dump = lookup_online("tale").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phalanx(self):
        html_dump = lookup_online("phalanx").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perfunctory(self):
        html_dump = lookup_online("perfunctory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sarcoma(self):
        html_dump = lookup_online("sarcoma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruntled(self):
        html_dump = lookup_online("gruntled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exasperated(self):
        html_dump = lookup_online("exasperated").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matron(self):
        html_dump = lookup_online("matron").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intrinsically(self):
        html_dump = lookup_online("intrinsically").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaint(self):
        html_dump = lookup_online("quaint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_medulla(self):
        html_dump = lookup_online("medulla").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rueful(self):
        html_dump = lookup_online("rueful").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_zealotry(self):
        html_dump = lookup_online("zealotry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_theorem(self):
        html_dump = lookup_online("theorem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affront(self):
        html_dump = lookup_online("affront").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eponymous(self):
        html_dump = lookup_online("eponymous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pending(self):
        html_dump = lookup_online("pending").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jilt(self):
        html_dump = lookup_online("jilt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hulk(self):
        html_dump = lookup_online("hulk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_languid(self):
        html_dump = lookup_online("languid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gammon(self):
        html_dump = lookup_online("gammon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heckle(self):
        html_dump = lookup_online("heckle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squabble(self):
        html_dump = lookup_online("squabble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corny(self):
        html_dump = lookup_online("corny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ridge(self):
        html_dump = lookup_online("ridge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inherent(self):
        html_dump = lookup_online("inherent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nebulous(self):
        html_dump = lookup_online("nebulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blimp(self):
        html_dump = lookup_online("blimp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ruddy(self):
        html_dump = lookup_online("ruddy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pulmonary(self):
        html_dump = lookup_online("pulmonary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caress(self):
        html_dump = lookup_online("caress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proliferation(self):
        html_dump = lookup_online("proliferation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excavation(self):
        html_dump = lookup_online("excavation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revile(self):
        html_dump = lookup_online("revile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affine(self):
        html_dump = lookup_online("affine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fraud(self):
        html_dump = lookup_online("fraud").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_midwife(self):
        html_dump = lookup_online("midwife").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rumpled(self):
        html_dump = lookup_online("rumpled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hone(self):
        html_dump = lookup_online("hone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_breadth(self):
        html_dump = lookup_online("breadth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dither(self):
        html_dump = lookup_online("dither").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paternalism(self):
        html_dump = lookup_online("paternalism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deference(self):
        html_dump = lookup_online("deference").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commission(self):
        html_dump = lookup_online("commission").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dejection(self):
        html_dump = lookup_online("dejection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ash(self):
        html_dump = lookup_online("ash").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_froth(self):
        html_dump = lookup_online("froth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_upon(self):
        html_dump = lookup_online("upon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miscreant(self):
        html_dump = lookup_online("miscreant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snide(self):
        html_dump = lookup_online("snide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sage(self):
        html_dump = lookup_online("sage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shriek(self):
        html_dump = lookup_online("shriek").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cronies(self):
        html_dump = lookup_online("cronies").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fumble(self):
        html_dump = lookup_online("fumble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spotless(self):
        html_dump = lookup_online("spotless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_umpteenth(self):
        html_dump = lookup_online("umpteenth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_service(self):
        html_dump = lookup_online("service").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abstruse(self):
        html_dump = lookup_online("abstruse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bout(self):
        html_dump = lookup_online("bout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lanky(self):
        html_dump = lookup_online("lanky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stifle(self):
        html_dump = lookup_online("stifle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_untrodden(self):
        html_dump = lookup_online("untrodden").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squint(self):
        html_dump = lookup_online("squint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slumber(self):
        html_dump = lookup_online("slumber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bemoan(self):
        html_dump = lookup_online("bemoan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shtick(self):
        html_dump = lookup_online("shtick").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contraband(self):
        html_dump = lookup_online("contraband").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catsup(self):
        html_dump = lookup_online("catsup").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reckoning(self):
        html_dump = lookup_online("reckoning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contain(self):
        html_dump = lookup_online("contain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peripheral(self):
        html_dump = lookup_online("peripheral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swagger(self):
        html_dump = lookup_online("swagger").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insular(self):
        html_dump = lookup_online("insular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sickle(self):
        html_dump = lookup_online("sickle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intertwine(self):
        html_dump = lookup_online("intertwine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fir(self):
        html_dump = lookup_online("fir").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gullet(self):
        html_dump = lookup_online("gullet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foliage(self):
        html_dump = lookup_online("foliage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fetter(self):
        html_dump = lookup_online("fetter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_malleable(self):
        html_dump = lookup_online("malleable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sylvan(self):
        html_dump = lookup_online("sylvan").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mock(self):
        html_dump = lookup_online("mock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cajole(self):
        html_dump = lookup_online("cajole").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nurture(self):
        html_dump = lookup_online("nurture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enjoin(self):
        html_dump = lookup_online("enjoin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reprehensible(self):
        html_dump = lookup_online("reprehensible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_folio(self):
        html_dump = lookup_online("folio").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prawn(self):
        html_dump = lookup_online("prawn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fern(self):
        html_dump = lookup_online("fern").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amicably(self):
        html_dump = lookup_online("amicably").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whig(self):
        html_dump = lookup_online("whig").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_listener(self):
        html_dump = lookup_online("listener").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitous(self):
        html_dump = lookup_online("precipitous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reticence(self):
        html_dump = lookup_online("reticence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardor(self):
        html_dump = lookup_online("ardor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dubious(self):
        html_dump = lookup_online("dubious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_limerick(self):
        html_dump = lookup_online("limerick").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_emerald(self):
        html_dump = lookup_online("emerald").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stalwart(self):
        html_dump = lookup_online("stalwart").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brazen(self):
        html_dump = lookup_online("brazen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gnat(self):
        html_dump = lookup_online("gnat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appendage(self):
        html_dump = lookup_online("appendage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_germane(self):
        html_dump = lookup_online("germane").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_preemptively(self):
        html_dump = lookup_online("preemptively").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cede(self):
        html_dump = lookup_online("cede").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cay(self):
        html_dump = lookup_online("cay").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_county(self):
        html_dump = lookup_online("county").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elation(self):
        html_dump = lookup_online("elation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curb(self):
        html_dump = lookup_online("curb").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_on(self):
        html_dump = lookup_online("on").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_portents(self):
        html_dump = lookup_online("portents").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abolish(self):
        html_dump = lookup_online("abolish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bejeezus(self):
        html_dump = lookup_online("bejeezus").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_torrefaction(self):
        html_dump = lookup_online("torrefaction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flaneur(self):
        html_dump = lookup_online("flaneur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ardour(self):
        html_dump = lookup_online("ardour").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_candid(self):
        html_dump = lookup_online("candid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proper(self):
        html_dump = lookup_online("proper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sprain(self):
        html_dump = lookup_online("sprain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_presuppose(self):
        html_dump = lookup_online("presuppose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hanker(self):
        html_dump = lookup_online("hanker").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_holler(self):
        html_dump = lookup_online("holler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prevarication(self):
        html_dump = lookup_online("prevarication").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_penitent(self):
        html_dump = lookup_online("penitent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garum(self):
        html_dump = lookup_online("garum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ilk(self):
        html_dump = lookup_online("ilk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pudgy(self):
        html_dump = lookup_online("pudgy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dismember(self):
        html_dump = lookup_online("dismember").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quit(self):
        html_dump = lookup_online("quit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miser(self):
        html_dump = lookup_online("miser").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_blight(self):
        html_dump = lookup_online("blight").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phthalates(self):
        html_dump = lookup_online("phthalates").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affidavit(self):
        html_dump = lookup_online("affidavit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relapse(self):
        html_dump = lookup_online("relapse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_character(self):
        html_dump = lookup_online("character").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slump(self):
        html_dump = lookup_online("slump").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_garner(self):
        html_dump = lookup_online("garner").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hum(self):
        html_dump = lookup_online("hum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unsound(self):
        html_dump = lookup_online("unsound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_condescending(self):
        html_dump = lookup_online("condescending").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ken(self):
        html_dump = lookup_online("ken").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bewilder(self):
        html_dump = lookup_online("bewilder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crust(self):
        html_dump = lookup_online("crust").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compassionate(self):
        html_dump = lookup_online("compassionate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_squid(self):
        html_dump = lookup_online("squid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reclusive(self):
        html_dump = lookup_online("reclusive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_are(self):
        html_dump = lookup_online("are").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gouge(self):
        html_dump = lookup_online("gouge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_satiate(self):
        html_dump = lookup_online("satiate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravage(self):
        html_dump = lookup_online("ravage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ecstatic(self):
        html_dump = lookup_online("ecstatic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mull(self):
        html_dump = lookup_online("mull").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_avowedly(self):
        html_dump = lookup_online("avowedly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lock(self):
        html_dump = lookup_online("lock").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fettle(self):
        html_dump = lookup_online("fettle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urchin(self):
        html_dump = lookup_online("urchin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ferocious(self):
        html_dump = lookup_online("ferocious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scrawl(self):
        html_dump = lookup_online("scrawl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_looey(self):
        html_dump = lookup_online("looey").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snitch(self):
        html_dump = lookup_online("snitch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmurs(self):
        html_dump = lookup_online("murmurs").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harness(self):
        html_dump = lookup_online("harness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rapture(self):
        html_dump = lookup_online("rapture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_debauchery(self):
        html_dump = lookup_online("debauchery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amelioration(self):
        html_dump = lookup_online("amelioration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incapacity(self):
        html_dump = lookup_online("incapacity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scallion(self):
        html_dump = lookup_online("scallion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prism(self):
        html_dump = lookup_online("prism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desolate(self):
        html_dump = lookup_online("desolate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_niggle(self):
        html_dump = lookup_online("niggle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_snap(self):
        html_dump = lookup_online("snap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lucent(self):
        html_dump = lookup_online("lucent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spurious(self):
        html_dump = lookup_online("spurious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pertain(self):
        html_dump = lookup_online("pertain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_allegiance(self):
        html_dump = lookup_online("allegiance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eminent(self):
        html_dump = lookup_online("eminent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_yore(self):
        html_dump = lookup_online("yore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dusk(self):
        html_dump = lookup_online("dusk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bondage(self):
        html_dump = lookup_online("bondage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_starch(self):
        html_dump = lookup_online("starch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fertile(self):
        html_dump = lookup_online("fertile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trump(self):
        html_dump = lookup_online("trump").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aggrieve(self):
        html_dump = lookup_online("aggrieve").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cogitate(self):
        html_dump = lookup_online("cogitate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_retrograde(self):
        html_dump = lookup_online("retrograde").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inchoate(self):
        html_dump = lookup_online("inchoate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quandary(self):
        html_dump = lookup_online("quandary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defenestration(self):
        html_dump = lookup_online("defenestration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vinegar(self):
        html_dump = lookup_online("vinegar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_greyhound(self):
        html_dump = lookup_online("greyhound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hem(self):
        html_dump = lookup_online("hem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_piety(self):
        html_dump = lookup_online("piety").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poof(self):
        html_dump = lookup_online("poof").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rue(self):
        html_dump = lookup_online("rue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_brawl(self):
        html_dump = lookup_online("brawl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_divest(self):
        html_dump = lookup_online("divest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hustings(self):
        html_dump = lookup_online("hustings").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lone(self):
        html_dump = lookup_online("lone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_countersink(self):
        html_dump = lookup_online("countersink").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_apposition(self):
        html_dump = lookup_online("apposition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_weep(self):
        html_dump = lookup_online("weep").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_parallelogram(self):
        html_dump = lookup_online("parallelogram").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_detain(self):
        html_dump = lookup_online("detain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extraneous(self):
        html_dump = lookup_online("extraneous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_overwrought(self):
        html_dump = lookup_online("overwrought").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gape(self):
        html_dump = lookup_online("gape").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insidious(self):
        html_dump = lookup_online("insidious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobblestone(self):
        html_dump = lookup_online("cobblestone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_puff(self):
        html_dump = lookup_online("puff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pestilence(self):
        html_dump = lookup_online("pestilence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crotchety(self):
        html_dump = lookup_online("crotchety").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tart(self):
        html_dump = lookup_online("tart").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_infallibility(self):
        html_dump = lookup_online("infallibility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fierce(self):
        html_dump = lookup_online("fierce").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_curate(self):
        html_dump = lookup_online("curate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glimpse(self):
        html_dump = lookup_online("glimpse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simular(self):
        html_dump = lookup_online("simular").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extoll(self):
        html_dump = lookup_online("extoll").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grit(self):
        html_dump = lookup_online("grit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_knead(self):
        html_dump = lookup_online("knead").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_meting(self):
        html_dump = lookup_online("meting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ballot(self):
        html_dump = lookup_online("ballot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conjugate(self):
        html_dump = lookup_online("conjugate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frolic(self):
        html_dump = lookup_online("frolic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_junction(self):
        html_dump = lookup_online("junction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hewing(self):
        html_dump = lookup_online("hewing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abscess(self):
        html_dump = lookup_online("abscess").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pinnace(self):
        html_dump = lookup_online("pinnace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recess(self):
        html_dump = lookup_online("recess").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recuperate(self):
        html_dump = lookup_online("recuperate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_progeny(self):
        html_dump = lookup_online("progeny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dissemination(self):
        html_dump = lookup_online("dissemination").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_specious(self):
        html_dump = lookup_online("specious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heath(self):
        html_dump = lookup_online("heath").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_foreshadow(self):
        html_dump = lookup_online("foreshadow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_conflate(self):
        html_dump = lookup_online("conflate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sumac(self):
        html_dump = lookup_online("sumac").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flagellating(self):
        html_dump = lookup_online("flagellating").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_address(self):
        html_dump = lookup_online("address").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_languish(self):
        html_dump = lookup_online("languish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amuse(self):
        html_dump = lookup_online("amuse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncanny(self):
        html_dump = lookup_online("uncanny").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_perpetuate(self):
        html_dump = lookup_online("perpetuate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heathen(self):
        html_dump = lookup_online("heathen").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_discernment(self):
        html_dump = lookup_online("discernment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abort(self):
        html_dump = lookup_online("abort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_iniquity(self):
        html_dump = lookup_online("iniquity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vary(self):
        html_dump = lookup_online("vary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_featureless(self):
        html_dump = lookup_online("featureless").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crave(self):
        html_dump = lookup_online("crave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glaze(self):
        html_dump = lookup_online("glaze").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cricket(self):
        html_dump = lookup_online("cricket").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_reify(self):
        html_dump = lookup_online("reify").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amorphous(self):
        html_dump = lookup_online("amorphous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intangible(self):
        html_dump = lookup_online("intangible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_daft(self):
        html_dump = lookup_online("daft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lesion(self):
        html_dump = lookup_online("lesion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rein(self):
        html_dump = lookup_online("rein").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teat(self):
        html_dump = lookup_online("teat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entice(self):
        html_dump = lookup_online("entice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_expound(self):
        html_dump = lookup_online("expound").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resent(self):
        html_dump = lookup_online("resent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fling(self):
        html_dump = lookup_online("fling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matricide(self):
        html_dump = lookup_online("matricide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aegis(self):
        html_dump = lookup_online("aegis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_egregious(self):
        html_dump = lookup_online("egregious").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scourge(self):
        html_dump = lookup_online("scourge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mould(self):
        html_dump = lookup_online("mould").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rad(self):
        html_dump = lookup_online("rad").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_extruding(self):
        html_dump = lookup_online("extruding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_drama(self):
        html_dump = lookup_online("drama").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murmur(self):
        html_dump = lookup_online("murmur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smug(self):
        html_dump = lookup_online("smug").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_toil(self):
        html_dump = lookup_online("toil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fungible(self):
        html_dump = lookup_online("fungible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plodding(self):
        html_dump = lookup_online("plodding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bustle(self):
        html_dump = lookup_online("bustle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acute(self):
        html_dump = lookup_online("acute").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pouty(self):
        html_dump = lookup_online("pouty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harass(self):
        html_dump = lookup_online("harass").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pram(self):
        html_dump = lookup_online("pram").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dilate(self):
        html_dump = lookup_online("dilate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sow(self):
        html_dump = lookup_online("sow").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_requisite(self):
        html_dump = lookup_online("requisite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wedge(self):
        html_dump = lookup_online("wedge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disjunction(self):
        html_dump = lookup_online("disjunction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_swell(self):
        html_dump = lookup_online("swell").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contempt(self):
        html_dump = lookup_online("contempt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_birch(self):
        html_dump = lookup_online("birch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stakeout(self):
        html_dump = lookup_online("stakeout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ibex(self):
        html_dump = lookup_online("ibex").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_submit(self):
        html_dump = lookup_online("submit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fowl(self):
        html_dump = lookup_online("fowl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ostensibly(self):
        html_dump = lookup_online("ostensibly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indignant(self):
        html_dump = lookup_online("indignant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbecoming(self):
        html_dump = lookup_online("unbecoming").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_insensate(self):
        html_dump = lookup_online("insensate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_influence(self):
        html_dump = lookup_online("influence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_noncommissioned(self):
        html_dump = lookup_online("noncommissioned").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_matronly(self):
        html_dump = lookup_online("matronly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nominal(self):
        html_dump = lookup_online("nominal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rife(self):
        html_dump = lookup_online("rife").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scuffed(self):
        html_dump = lookup_online("scuffed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unscathed(self):
        html_dump = lookup_online("unscathed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_roil(self):
        html_dump = lookup_online("roil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nadir(self):
        html_dump = lookup_online("nadir").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_coffer(self):
        html_dump = lookup_online("coffer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gout(self):
        html_dump = lookup_online("gout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leap(self):
        html_dump = lookup_online("leap").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indirection(self):
        html_dump = lookup_online("indirection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ambler(self):
        html_dump = lookup_online("ambler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supress(self):
        html_dump = lookup_online("supress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_helot(self):
        html_dump = lookup_online("helot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dapper(self):
        html_dump = lookup_online("dapper").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_erstwhile(self):
        html_dump = lookup_online("erstwhile").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_audacity(self):
        html_dump = lookup_online("audacity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trombone(self):
        html_dump = lookup_online("trombone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ascend(self):
        html_dump = lookup_online("ascend").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_voluptuous(self):
        html_dump = lookup_online("voluptuous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_transcendent(self):
        html_dump = lookup_online("transcendent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_corpulent(self):
        html_dump = lookup_online("corpulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haphazard(self):
        html_dump = lookup_online("haphazard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bowels(self):
        html_dump = lookup_online("bowels").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stem(self):
        html_dump = lookup_online("stem").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flaunt(self):
        html_dump = lookup_online("flaunt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_readily(self):
        html_dump = lookup_online("readily").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_peer(self):
        html_dump = lookup_online("peer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_despoil(self):
        html_dump = lookup_online("despoil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vex(self):
        html_dump = lookup_online("vex").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glibness(self):
        html_dump = lookup_online("glibness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_artifact(self):
        html_dump = lookup_online("artifact").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ord(self):
        html_dump = lookup_online("ord").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_utilitarian(self):
        html_dump = lookup_online("utilitarian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dolt(self):
        html_dump = lookup_online("dolt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stint(self):
        html_dump = lookup_online("stint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_estranged(self):
        html_dump = lookup_online("estranged").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succint(self):
        html_dump = lookup_online("succint").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hassle(self):
        html_dump = lookup_online("hassle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rivet(self):
        html_dump = lookup_online("rivet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_undertones(self):
        html_dump = lookup_online("undertones").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whiff(self):
        html_dump = lookup_online("whiff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unraveling(self):
        html_dump = lookup_online("unraveling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gruff(self):
        html_dump = lookup_online("gruff").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vocation(self):
        html_dump = lookup_online("vocation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_committ(self):
        html_dump = lookup_online("committ").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mince(self):
        html_dump = lookup_online("mince").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flimsy(self):
        html_dump = lookup_online("flimsy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bumble(self):
        html_dump = lookup_online("bumble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_whirling(self):
        html_dump = lookup_online("whirling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unbridle(self):
        html_dump = lookup_online("unbridle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gingerly(self):
        html_dump = lookup_online("gingerly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_twang(self):
        html_dump = lookup_online("twang").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_teeter(self):
        html_dump = lookup_online("teeter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_manatee(self):
        html_dump = lookup_online("manatee").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_succulent(self):
        html_dump = lookup_online("succulent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_centrifugal(self):
        html_dump = lookup_online("centrifugal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_edifice(self):
        html_dump = lookup_online("edifice").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tungsten(self):
        html_dump = lookup_online("tungsten").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_asphyxia(self):
        html_dump = lookup_online("asphyxia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obscurity(self):
        html_dump = lookup_online("obscurity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_unscrupulous(self):
        html_dump = lookup_online("unscrupulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_intercession(self):
        html_dump = lookup_online("intercession").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inexorable(self):
        html_dump = lookup_online("inexorable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fleeting(self):
        html_dump = lookup_online("fleeting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sounder(self):
        html_dump = lookup_online("sounder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disgruntled(self):
        html_dump = lookup_online("disgruntled").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_inducement(self):
        html_dump = lookup_online("inducement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_travois(self):
        html_dump = lookup_online("travois").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crankshaft(self):
        html_dump = lookup_online("crankshaft").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caraway(self):
        html_dump = lookup_online("caraway").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_awry(self):
        html_dump = lookup_online("awry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleuth(self):
        html_dump = lookup_online("sleuth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pellet(self):
        html_dump = lookup_online("pellet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_phlebotomy(self):
        html_dump = lookup_online("phlebotomy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_crackle(self):
        html_dump = lookup_online("crackle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incursion(self):
        html_dump = lookup_online("incursion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leeway(self):
        html_dump = lookup_online("leeway").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accessible(self):
        html_dump = lookup_online("accessible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contract(self):
        html_dump = lookup_online("contract").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_simplistic(self):
        html_dump = lookup_online("simplistic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_almanac(self):
        html_dump = lookup_online("almanac").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_desultory(self):
        html_dump = lookup_online("desultory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_outpatient(self):
        html_dump = lookup_online("outpatient").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_array(self):
        html_dump = lookup_online("array").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_neuroticism(self):
        html_dump = lookup_online("neuroticism").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_augur(self):
        html_dump = lookup_online("augur").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dyke(self):
        html_dump = lookup_online("dyke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_antsy(self):
        html_dump = lookup_online("antsy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_admission(self):
        html_dump = lookup_online("admission").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sleazy(self):
        html_dump = lookup_online("sleazy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_writ(self):
        html_dump = lookup_online("writ").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cauldron(self):
        html_dump = lookup_online("cauldron").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_withering(self):
        html_dump = lookup_online("withering").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cadence(self):
        html_dump = lookup_online("cadence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cavity(self):
        html_dump = lookup_online("cavity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_collateral(self):
        html_dump = lookup_online("collateral").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feature(self):
        html_dump = lookup_online("feature").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acorn(self):
        html_dump = lookup_online("acorn").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_murky(self):
        html_dump = lookup_online("murky").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jovial(self):
        html_dump = lookup_online("jovial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangent(self):
        html_dump = lookup_online("tangent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_enormity(self):
        html_dump = lookup_online("enormity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prostrate(self):
        html_dump = lookup_online("prostrate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sever(self):
        html_dump = lookup_online("sever").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_venereal(self):
        html_dump = lookup_online("venereal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_loiter(self):
        html_dump = lookup_online("loiter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accosted(self):
        html_dump = lookup_online("accosted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_adore(self):
        html_dump = lookup_online("adore").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_flexibility(self):
        html_dump = lookup_online("flexibility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_embroidery(self):
        html_dump = lookup_online("embroidery").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_juncture(self):
        html_dump = lookup_online("juncture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boast(self):
        html_dump = lookup_online("boast").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_longitude(self):
        html_dump = lookup_online("longitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ingot(self):
        html_dump = lookup_online("ingot").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_katydid(self):
        html_dump = lookup_online("katydid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Shia(self):
        html_dump = lookup_online("Shia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_actuary(self):
        html_dump = lookup_online("actuary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_throe(self):
        html_dump = lookup_online("throe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bifurcate(self):
        html_dump = lookup_online("bifurcate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_placate(self):
        html_dump = lookup_online("placate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_leek(self):
        html_dump = lookup_online("leek").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scurry(self):
        html_dump = lookup_online("scurry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excoriation(self):
        html_dump = lookup_online("excoriation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_primordial(self):
        html_dump = lookup_online("primordial").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_potty(self):
        html_dump = lookup_online("potty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_accentuate(self):
        html_dump = lookup_online("accentuate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_wholly(self):
        html_dump = lookup_online("wholly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tantalizing(self):
        html_dump = lookup_online("tantalizing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fossick(self):
        html_dump = lookup_online("fossick").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_gale(self):
        html_dump = lookup_online("gale").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_interlocutor(self):
        html_dump = lookup_online("interlocutor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_disparagement(self):
        html_dump = lookup_online("disparagement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quaver(self):
        html_dump = lookup_online("quaver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amiable(self):
        html_dump = lookup_online("amiable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harrowing(self):
        html_dump = lookup_online("harrowing").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subsist(self):
        html_dump = lookup_online("subsist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concede(self):
        html_dump = lookup_online("concede").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scanty(self):
        html_dump = lookup_online("scanty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_harbour(self):
        html_dump = lookup_online("harbour").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hideously(self):
        html_dump = lookup_online("hideously").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_canuck(self):
        html_dump = lookup_online("canuck").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lorry(self):
        html_dump = lookup_online("lorry").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fallout(self):
        html_dump = lookup_online("fallout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pineal(self):
        html_dump = lookup_online("pineal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigence(self):
        html_dump = lookup_online("indigence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ponder(self):
        html_dump = lookup_online("ponder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_doe(self):
        html_dump = lookup_online("doe").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deviant(self):
        html_dump = lookup_online("deviant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excerpt(self):
        html_dump = lookup_online("excerpt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_contractions(self):
        html_dump = lookup_online("contractions").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_beignet(self):
        html_dump = lookup_online("beignet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cellar(self):
        html_dump = lookup_online("cellar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pejorative(self):
        html_dump = lookup_online("pejorative").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_soar(self):
        html_dump = lookup_online("soar").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Formica(self):
        html_dump = lookup_online("Formica").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_prescriptive(self):
        html_dump = lookup_online("prescriptive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_switch(self):
        html_dump = lookup_online("switch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_miasma(self):
        html_dump = lookup_online("miasma").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mite(self):
        html_dump = lookup_online("mite").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ravenous(self):
        html_dump = lookup_online("ravenous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frame(self):
        html_dump = lookup_online("frame").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caustic(self):
        html_dump = lookup_online("caustic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_largesse(self):
        html_dump = lookup_online("largesse").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_trifle(self):
        html_dump = lookup_online("trifle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_resort(self):
        html_dump = lookup_online("resort").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_augment(self):
        html_dump = lookup_online("augment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_startling(self):
        html_dump = lookup_online("startling").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frugality(self):
        html_dump = lookup_online("frugality").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_introspective(self):
        html_dump = lookup_online("introspective").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_catalyze(self):
        html_dump = lookup_online("catalyze").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_benighted(self):
        html_dump = lookup_online("benighted").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sway(self):
        html_dump = lookup_online("sway").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_agency(self):
        html_dump = lookup_online("agency").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caption(self):
        html_dump = lookup_online("caption").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_horcrux(self):
        html_dump = lookup_online("horcrux").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aloof(self):
        html_dump = lookup_online("aloof").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_anguish(self):
        html_dump = lookup_online("anguish").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_menace(self):
        html_dump = lookup_online("menace").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_maudlin(self):
        html_dump = lookup_online("maudlin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_predator(self):
        html_dump = lookup_online("predator").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sown(self):
        html_dump = lookup_online("sown").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_den(self):
        html_dump = lookup_online("den").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_severance(self):
        html_dump = lookup_online("severance").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_recrudescence(self):
        html_dump = lookup_online("recrudescence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impeccable(self):
        html_dump = lookup_online("impeccable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barrage(self):
        html_dump = lookup_online("barrage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_urge(self):
        html_dump = lookup_online("urge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mild(self):
        html_dump = lookup_online("mild").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rectitude(self):
        html_dump = lookup_online("rectitude").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pledge(self):
        html_dump = lookup_online("pledge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tangential(self):
        html_dump = lookup_online("tangential").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tailgate(self):
        html_dump = lookup_online("tailgate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concierge(self):
        html_dump = lookup_online("concierge").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_didn_t(self):
        html_dump = lookup_online("didn't").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_moat(self):
        html_dump = lookup_online("moat").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_calamities(self):
        html_dump = lookup_online("calamities").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scag(self):
        html_dump = lookup_online("scag").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_commendable(self):
        html_dump = lookup_online("commendable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_defiant(self):
        html_dump = lookup_online("defiant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hawk(self):
        html_dump = lookup_online("hawk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_orthogonal(self):
        html_dump = lookup_online("orthogonal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nitwit(self):
        html_dump = lookup_online("nitwit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stain(self):
        html_dump = lookup_online("stain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_treacherous(self):
        html_dump = lookup_online("treacherous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lynchpin(self):
        html_dump = lookup_online("lynchpin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mainland(self):
        html_dump = lookup_online("mainland").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grope(self):
        html_dump = lookup_online("grope").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bloke(self):
        html_dump = lookup_online("bloke").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hemorrhage(self):
        html_dump = lookup_online("hemorrhage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_palpable(self):
        html_dump = lookup_online("palpable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_echelon(self):
        html_dump = lookup_online("echelon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hewer(self):
        html_dump = lookup_online("hewer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affliction(self):
        html_dump = lookup_online("affliction").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_glisten(self):
        html_dump = lookup_online("glisten").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obviate(self):
        html_dump = lookup_online("obviate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_playdate(self):
        html_dump = lookup_online("playdate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elide(self):
        html_dump = lookup_online("elide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_planter(self):
        html_dump = lookup_online("planter").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sabbatical(self):
        html_dump = lookup_online("sabbatical").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incongruous(self):
        html_dump = lookup_online("incongruous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_burl(self):
        html_dump = lookup_online("burl").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vitriolic(self):
        html_dump = lookup_online("vitriolic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ulterior(self):
        html_dump = lookup_online("ulterior").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abjure(self):
        html_dump = lookup_online("abjure").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_taxis(self):
        html_dump = lookup_online("taxis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_indigo(self):
        html_dump = lookup_online("indigo").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shone(self):
        html_dump = lookup_online("shone").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_Lapp(self):
        html_dump = lookup_online("Lapp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_deride(self):
        html_dump = lookup_online("deride").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eulogise(self):
        html_dump = lookup_online("eulogise").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hectic(self):
        html_dump = lookup_online("hectic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stave(self):
        html_dump = lookup_online("stave").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncouth(self):
        html_dump = lookup_online("uncouth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ordain(self):
        html_dump = lookup_online("ordain").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lynx(self):
        html_dump = lookup_online("lynx").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_genuflection(self):
        html_dump = lookup_online("genuflection").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liver(self):
        html_dump = lookup_online("liver").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_modest(self):
        html_dump = lookup_online("modest").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mooring(self):
        html_dump = lookup_online("mooring").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobbler(self):
        html_dump = lookup_online("cobbler").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_savor(self):
        html_dump = lookup_online("savor").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impunity(self):
        html_dump = lookup_online("impunity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_entrust(self):
        html_dump = lookup_online("entrust").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_judder(self):
        html_dump = lookup_online("judder").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clout(self):
        html_dump = lookup_online("clout").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cogent(self):
        html_dump = lookup_online("cogent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_derangement(self):
        html_dump = lookup_online("derangement").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_smiting(self):
        html_dump = lookup_online("smiting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_rummage(self):
        html_dump = lookup_online("rummage").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_noose(self):
        html_dump = lookup_online("noose").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amalgam(self):
        html_dump = lookup_online("amalgam").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_petit(self):
        html_dump = lookup_online("petit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_boilerplate(self):
        html_dump = lookup_online("boilerplate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_front(self):
        html_dump = lookup_online("front").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tremble(self):
        html_dump = lookup_online("tremble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_volition(self):
        html_dump = lookup_online("volition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proclivity(self):
        html_dump = lookup_online("proclivity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_waning(self):
        html_dump = lookup_online("waning").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jovially(self):
        html_dump = lookup_online("jovially").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hoary(self):
        html_dump = lookup_online("hoary").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_precipitate(self):
        html_dump = lookup_online("precipitate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_eschew(self):
        html_dump = lookup_online("eschew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_superstition(self):
        html_dump = lookup_online("superstition").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bold(self):
        html_dump = lookup_online("bold").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cobble(self):
        html_dump = lookup_online("cobble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sedation(self):
        html_dump = lookup_online("sedation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_belcher(self):
        html_dump = lookup_online("belcher").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cramp(self):
        html_dump = lookup_online("cramp").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_excessive(self):
        html_dump = lookup_online("excessive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_plainly(self):
        html_dump = lookup_online("plainly").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clandestine(self):
        html_dump = lookup_online("clandestine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bollard(self):
        html_dump = lookup_online("bollard").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_credulous(self):
        html_dump = lookup_online("credulous").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ante(self):
        html_dump = lookup_online("ante").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_futon(self):
        html_dump = lookup_online("futon").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_synesthesia(self):
        html_dump = lookup_online("synesthesia").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_single_out(self):
        html_dump = lookup_online("single out").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_mystical(self):
        html_dump = lookup_online("mystical").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_grouch(self):
        html_dump = lookup_online("grouch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_uncanniness(self):
        html_dump = lookup_online("uncanniness").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_epiphany(self):
        html_dump = lookup_online("epiphany").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cowed(self):
        html_dump = lookup_online("cowed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exonerate(self):
        html_dump = lookup_online("exonerate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_during(self):
        html_dump = lookup_online("during").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_affluence(self):
        html_dump = lookup_online("affluence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bucolic(self):
        html_dump = lookup_online("bucolic").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_feasible(self):
        html_dump = lookup_online("feasible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_comestible(self):
        html_dump = lookup_online("comestible").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_compulsion(self):
        html_dump = lookup_online("compulsion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bromide(self):
        html_dump = lookup_online("bromide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vestibule(self):
        html_dump = lookup_online("vestibule").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_relief(self):
        html_dump = lookup_online("relief").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_abrupt(self):
        html_dump = lookup_online("abrupt").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dapple(self):
        html_dump = lookup_online("dapple").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_stye(self):
        html_dump = lookup_online("stye").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_larks(self):
        html_dump = lookup_online("larks").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_exacerbation(self):
        html_dump = lookup_online("exacerbation").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_turgid(self):
        html_dump = lookup_online("turgid").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elk(self):
        html_dump = lookup_online("elk").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_paunch(self):
        html_dump = lookup_online("paunch").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hornbeam(self):
        html_dump = lookup_online("hornbeam").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_scaffolding(self):
        html_dump = lookup_online("scaffolding").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_obstruct(self):
        html_dump = lookup_online("obstruct").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_kestrel(self):
        html_dump = lookup_online("kestrel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_impertinent(self):
        html_dump = lookup_online("impertinent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concision(self):
        html_dump = lookup_online("concision").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_myelin(self):
        html_dump = lookup_online("myelin").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_possibility(self):
        html_dump = lookup_online("possibility").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_revel(self):
        html_dump = lookup_online("revel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supplicant(self):
        html_dump = lookup_online("supplicant").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_caldron(self):
        html_dump = lookup_online("caldron").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_amenity(self):
        html_dump = lookup_online("amenity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_supersede(self):
        html_dump = lookup_online("supersede").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_fracture(self):
        html_dump = lookup_online("fracture").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_nettle(self):
        html_dump = lookup_online("nettle").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_heed(self):
        html_dump = lookup_online("heed").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aproximate(self):
        html_dump = lookup_online("aproximate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_regicide(self):
        html_dump = lookup_online("regicide").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_cursory(self):
        html_dump = lookup_online("cursory").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_pamphlet(self):
        html_dump = lookup_online("pamphlet").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_duffer(self):
        html_dump = lookup_online("duffer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_thence(self):
        html_dump = lookup_online("thence").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humdrum(self):
        html_dump = lookup_online("humdrum").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_sanguine(self):
        html_dump = lookup_online("sanguine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_shrivel(self):
        html_dump = lookup_online("shrivel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_ermine(self):
        html_dump = lookup_online("ermine").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_repress(self):
        html_dump = lookup_online("repress").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_bruiser(self):
        html_dump = lookup_online("bruiser").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_acclaim(self):
        html_dump = lookup_online("acclaim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_poltergeist(self):
        html_dump = lookup_online("poltergeist").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_summit(self):
        html_dump = lookup_online("summit").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_quack(self):
        html_dump = lookup_online("quack").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_spiffy(self):
        html_dump = lookup_online("spiffy").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_dew(self):
        html_dump = lookup_online("dew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_aliment(self):
        html_dump = lookup_online("aliment").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_concussion(self):
        html_dump = lookup_online("concussion").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_septuagenarian(self):
        html_dump = lookup_online("septuagenarian").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_strew(self):
        html_dump = lookup_online("strew").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_slobber(self):
        html_dump = lookup_online("slobber").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_solvent(self):
        html_dump = lookup_online("solvent").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_frank(self):
        html_dump = lookup_online("frank").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_royal(self):
        html_dump = lookup_online("royal").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_barley(self):
        html_dump = lookup_online("barley").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_clench(self):
        html_dump = lookup_online("clench").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_imperturbable(self):
        html_dump = lookup_online("imperturbable").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_tranquilize(self):
        html_dump = lookup_online("tranquilize").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_virgil(self):
        html_dump = lookup_online("virgil").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_lentils(self):
        html_dump = lookup_online("lentils").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_incongruity(self):
        html_dump = lookup_online("incongruity").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_proclaim(self):
        html_dump = lookup_online("proclaim").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_appreciate(self):
        html_dump = lookup_online("appreciate").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_broth(self):
        html_dump = lookup_online("broth").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_humble(self):
        html_dump = lookup_online("humble").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vitriol(self):
        html_dump = lookup_online("vitriol").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_afflict(self):
        html_dump = lookup_online("afflict").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_subdue(self):
        html_dump = lookup_online("subdue").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_laceration(self):
        html_dump = lookup_online("laceration").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_arthritis(self):
        html_dump = lookup_online("arthritis").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_liason(self):
        html_dump = lookup_online("liason").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_vaporware(self):
        html_dump = lookup_online("vaporware").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_oust(self):
        html_dump = lookup_online("oust").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_jaunty(self):
        html_dump = lookup_online("jaunty").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_haunting(self):
        html_dump = lookup_online("haunting").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_misnomer(self):
        html_dump = lookup_online("misnomer").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_layman(self):
        html_dump = lookup_online("layman").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_elusive(self):
        html_dump = lookup_online("elusive").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

    def test_compare_hovel(self):
        html_dump = lookup_online("hovel").html
        result = parse_en_pl(html_dump)
        f_result = flatten(_parse_html(html_dump))
        assert result == f_result

