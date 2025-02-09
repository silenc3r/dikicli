import json
import pathlib

from dikicli.core import parse_en_pl

test_dir = pathlib.Path(__file__).resolve().parent
html_dir = test_dir / "htmldump_en"
json_dir = test_dir / "json_en"

html = {}
for filepath in html_dir.iterdir():
    word = filepath.stem
    with open(filepath) as f:
        html[word] = f.read()


def load_json(word):
    with open(json_dir / f"{word}.json") as f:
        content = json.load(f)
    return content


class TestAll:
    def test_parse_pawning(self):
        parsed = parse_en_pl(html["pawning"])
        cached = load_json("pawning")
        assert parsed == cached

    def test_parse_apparently(self):
        parsed = parse_en_pl(html["apparently"])
        cached = load_json("apparently")
        assert parsed == cached

    def test_parse_scathe(self):
        parsed = parse_en_pl(html["scathe"])
        cached = load_json("scathe")
        assert parsed == cached

    def test_parse_fecund(self):
        parsed = parse_en_pl(html["fecund"])
        cached = load_json("fecund")
        assert parsed == cached

    def test_parse_caucus(self):
        parsed = parse_en_pl(html["caucus"])
        cached = load_json("caucus")
        assert parsed == cached

    def test_parse_pamper(self):
        parsed = parse_en_pl(html["pamper"])
        cached = load_json("pamper")
        assert parsed == cached

    def test_parse_venerated(self):
        parsed = parse_en_pl(html["venerated"])
        cached = load_json("venerated")
        assert parsed == cached

    def test_parse_incisive(self):
        parsed = parse_en_pl(html["incisive"])
        cached = load_json("incisive")
        assert parsed == cached

    def test_parse_gospel(self):
        parsed = parse_en_pl(html["gospel"])
        cached = load_json("gospel")
        assert parsed == cached

    def test_parse_suppleness(self):
        parsed = parse_en_pl(html["suppleness"])
        cached = load_json("suppleness")
        assert parsed == cached

    def test_parse_mingle(self):
        parsed = parse_en_pl(html["mingle"])
        cached = load_json("mingle")
        assert parsed == cached

    def test_parse_blitheness(self):
        parsed = parse_en_pl(html["blitheness"])
        cached = load_json("blitheness")
        assert parsed == cached

    def test_parse_mulligan(self):
        parsed = parse_en_pl(html["mulligan"])
        cached = load_json("mulligan")
        assert parsed == cached

    def test_parse_ascent(self):
        parsed = parse_en_pl(html["ascent"])
        cached = load_json("ascent")
        assert parsed == cached

    def test_parse_nonchalant(self):
        parsed = parse_en_pl(html["nonchalant"])
        cached = load_json("nonchalant")
        assert parsed == cached

    def test_parse_pundit(self):
        parsed = parse_en_pl(html["pundit"])
        cached = load_json("pundit")
        assert parsed == cached

    def test_parse_cervical(self):
        parsed = parse_en_pl(html["cervical"])
        cached = load_json("cervical")
        assert parsed == cached

    def test_parse_aggravate(self):
        parsed = parse_en_pl(html["aggravate"])
        cached = load_json("aggravate")
        assert parsed == cached

    def test_parse_commissioner(self):
        parsed = parse_en_pl(html["commissioner"])
        cached = load_json("commissioner")
        assert parsed == cached

    def test_parse_oracular(self):
        parsed = parse_en_pl(html["oracular"])
        cached = load_json("oracular")
        assert parsed == cached

    def test_parse_giardia(self):
        parsed = parse_en_pl(html["giardia"])
        cached = load_json("giardia")
        assert parsed == cached

    def test_parse_swathe(self):
        parsed = parse_en_pl(html["swathe"])
        cached = load_json("swathe")
        assert parsed == cached

    def test_parse_daub(self):
        parsed = parse_en_pl(html["daub"])
        cached = load_json("daub")
        assert parsed == cached

    def test_parse_feline(self):
        parsed = parse_en_pl(html["feline"])
        cached = load_json("feline")
        assert parsed == cached

    def test_parse_ayahuasca(self):
        parsed = parse_en_pl(html["ayahuasca"])
        cached = load_json("ayahuasca")
        assert parsed == cached

    def test_parse_garret(self):
        parsed = parse_en_pl(html["garret"])
        cached = load_json("garret")
        assert parsed == cached

    def test_parse_Solidarity(self):
        parsed = parse_en_pl(html["Solidarity"])
        cached = load_json("Solidarity")
        assert parsed == cached

    def test_parse_drudgery(self):
        parsed = parse_en_pl(html["drudgery"])
        cached = load_json("drudgery")
        assert parsed == cached

    def test_parse_hosier(self):
        parsed = parse_en_pl(html["hosier"])
        cached = load_json("hosier")
        assert parsed == cached

    def test_parse_remarkable(self):
        parsed = parse_en_pl(html["remarkable"])
        cached = load_json("remarkable")
        assert parsed == cached

    def test_parse_snotty(self):
        parsed = parse_en_pl(html["snotty"])
        cached = load_json("snotty")
        assert parsed == cached

    def test_parse_cusp(self):
        parsed = parse_en_pl(html["cusp"])
        cached = load_json("cusp")
        assert parsed == cached

    def test_parse_endeavor(self):
        parsed = parse_en_pl(html["endeavor"])
        cached = load_json("endeavor")
        assert parsed == cached

    def test_parse_embellishment(self):
        parsed = parse_en_pl(html["embellishment"])
        cached = load_json("embellishment")
        assert parsed == cached

    def test_parse_commend(self):
        parsed = parse_en_pl(html["commend"])
        cached = load_json("commend")
        assert parsed == cached

    def test_parse_palliative(self):
        parsed = parse_en_pl(html["palliative"])
        cached = load_json("palliative")
        assert parsed == cached

    def test_parse_parishioner(self):
        parsed = parse_en_pl(html["parishioner"])
        cached = load_json("parishioner")
        assert parsed == cached

    def test_parse_millipede(self):
        parsed = parse_en_pl(html["millipede"])
        cached = load_json("millipede")
        assert parsed == cached

    def test_parse_kludge(self):
        parsed = parse_en_pl(html["kludge"])
        cached = load_json("kludge")
        assert parsed == cached

    def test_parse_introspection(self):
        parsed = parse_en_pl(html["introspection"])
        cached = load_json("introspection")
        assert parsed == cached

    def test_parse_pinnacle(self):
        parsed = parse_en_pl(html["pinnacle"])
        cached = load_json("pinnacle")
        assert parsed == cached

    def test_parse_ballpark(self):
        parsed = parse_en_pl(html["ballpark"])
        cached = load_json("ballpark")
        assert parsed == cached

    def test_parse_tantrum(self):
        parsed = parse_en_pl(html["tantrum"])
        cached = load_json("tantrum")
        assert parsed == cached

    def test_parse_disconcerting(self):
        parsed = parse_en_pl(html["disconcerting"])
        cached = load_json("disconcerting")
        assert parsed == cached

    def test_parse_missive(self):
        parsed = parse_en_pl(html["missive"])
        cached = load_json("missive")
        assert parsed == cached

    def test_parse_feigned(self):
        parsed = parse_en_pl(html["feigned"])
        cached = load_json("feigned")
        assert parsed == cached

    def test_parse_deferral(self):
        parsed = parse_en_pl(html["deferral"])
        cached = load_json("deferral")
        assert parsed == cached

    def test_parse_manure(self):
        parsed = parse_en_pl(html["manure"])
        cached = load_json("manure")
        assert parsed == cached

    def test_parse_penury(self):
        parsed = parse_en_pl(html["penury"])
        cached = load_json("penury")
        assert parsed == cached

    def test_parse_fringe(self):
        parsed = parse_en_pl(html["fringe"])
        cached = load_json("fringe")
        assert parsed == cached

    def test_parse_coincidence(self):
        parsed = parse_en_pl(html["coincidence"])
        cached = load_json("coincidence")
        assert parsed == cached

    def test_parse_surmount(self):
        parsed = parse_en_pl(html["surmount"])
        cached = load_json("surmount")
        assert parsed == cached

    def test_parse_succor(self):
        parsed = parse_en_pl(html["succor"])
        cached = load_json("succor")
        assert parsed == cached

    def test_parse_amatory(self):
        parsed = parse_en_pl(html["amatory"])
        cached = load_json("amatory")
        assert parsed == cached

    def test_parse_needlessly(self):
        parsed = parse_en_pl(html["needlessly"])
        cached = load_json("needlessly")
        assert parsed == cached

    def test_parse_yearn(self):
        parsed = parse_en_pl(html["yearn"])
        cached = load_json("yearn")
        assert parsed == cached

    def test_parse_dreary(self):
        parsed = parse_en_pl(html["dreary"])
        cached = load_json("dreary")
        assert parsed == cached

    def test_parse_upheaval(self):
        parsed = parse_en_pl(html["upheaval"])
        cached = load_json("upheaval")
        assert parsed == cached

    def test_parse_contented(self):
        parsed = parse_en_pl(html["contented"])
        cached = load_json("contented")
        assert parsed == cached

    def test_parse_snarly(self):
        parsed = parse_en_pl(html["snarly"])
        cached = load_json("snarly")
        assert parsed == cached

    def test_parse_transitively(self):
        parsed = parse_en_pl(html["transitively"])
        cached = load_json("transitively")
        assert parsed == cached

    def test_parse_tenable(self):
        parsed = parse_en_pl(html["tenable"])
        cached = load_json("tenable")
        assert parsed == cached

    def test_parse_klutz(self):
        parsed = parse_en_pl(html["klutz"])
        cached = load_json("klutz")
        assert parsed == cached

    def test_parse_hackney(self):
        parsed = parse_en_pl(html["hackney"])
        cached = load_json("hackney")
        assert parsed == cached

    def test_parse_chlamydia(self):
        parsed = parse_en_pl(html["chlamydia"])
        cached = load_json("chlamydia")
        assert parsed == cached

    def test_parse_cache(self):
        parsed = parse_en_pl(html["cache"])
        cached = load_json("cache")
        assert parsed == cached

    def test_parse_crude(self):
        parsed = parse_en_pl(html["crude"])
        cached = load_json("crude")
        assert parsed == cached

    def test_parse_bint(self):
        parsed = parse_en_pl(html["bint"])
        cached = load_json("bint")
        assert parsed == cached

    def test_parse_dour(self):
        parsed = parse_en_pl(html["dour"])
        cached = load_json("dour")
        assert parsed == cached

    def test_parse_pillock(self):
        parsed = parse_en_pl(html["pillock"])
        cached = load_json("pillock")
        assert parsed == cached

    def test_parse_crater(self):
        parsed = parse_en_pl(html["crater"])
        cached = load_json("crater")
        assert parsed == cached

    def test_parse_finagle(self):
        parsed = parse_en_pl(html["finagle"])
        cached = load_json("finagle")
        assert parsed == cached

    def test_parse_veer(self):
        parsed = parse_en_pl(html["veer"])
        cached = load_json("veer")
        assert parsed == cached

    def test_parse_boomlet(self):
        parsed = parse_en_pl(html["boomlet"])
        cached = load_json("boomlet")
        assert parsed == cached

    def test_parse_rose(self):
        parsed = parse_en_pl(html["rose"])
        cached = load_json("rose")
        assert parsed == cached

    def test_parse_mayhem(self):
        parsed = parse_en_pl(html["mayhem"])
        cached = load_json("mayhem")
        assert parsed == cached

    def test_parse_renowned(self):
        parsed = parse_en_pl(html["renowned"])
        cached = load_json("renowned")
        assert parsed == cached

    def test_parse_ephemeral(self):
        parsed = parse_en_pl(html["ephemeral"])
        cached = load_json("ephemeral")
        assert parsed == cached

    def test_parse_sickly(self):
        parsed = parse_en_pl(html["sickly"])
        cached = load_json("sickly")
        assert parsed == cached

    def test_parse_sensible(self):
        parsed = parse_en_pl(html["sensible"])
        cached = load_json("sensible")
        assert parsed == cached

    def test_parse_blustery(self):
        parsed = parse_en_pl(html["blustery"])
        cached = load_json("blustery")
        assert parsed == cached

    def test_parse_virulent(self):
        parsed = parse_en_pl(html["virulent"])
        cached = load_json("virulent")
        assert parsed == cached

    def test_parse_adrift(self):
        parsed = parse_en_pl(html["adrift"])
        cached = load_json("adrift")
        assert parsed == cached

    def test_parse_rascal(self):
        parsed = parse_en_pl(html["rascal"])
        cached = load_json("rascal")
        assert parsed == cached

    def test_parse_hodgepodge(self):
        parsed = parse_en_pl(html["hodgepodge"])
        cached = load_json("hodgepodge")
        assert parsed == cached

    def test_parse_humongous(self):
        parsed = parse_en_pl(html["humongous"])
        cached = load_json("humongous")
        assert parsed == cached

    def test_parse_stocky(self):
        parsed = parse_en_pl(html["stocky"])
        cached = load_json("stocky")
        assert parsed == cached

    def test_parse_reef(self):
        parsed = parse_en_pl(html["reef"])
        cached = load_json("reef")
        assert parsed == cached

    def test_parse_cervix(self):
        parsed = parse_en_pl(html["cervix"])
        cached = load_json("cervix")
        assert parsed == cached

    def test_parse_maroon(self):
        parsed = parse_en_pl(html["maroon"])
        cached = load_json("maroon")
        assert parsed == cached

    def test_parse_grubby(self):
        parsed = parse_en_pl(html["grubby"])
        cached = load_json("grubby")
        assert parsed == cached

    def test_parse_serendipitous(self):
        parsed = parse_en_pl(html["serendipitous"])
        cached = load_json("serendipitous")
        assert parsed == cached

    def test_parse_altercation(self):
        parsed = parse_en_pl(html["altercation"])
        cached = load_json("altercation")
        assert parsed == cached

    def test_parse_bravado(self):
        parsed = parse_en_pl(html["bravado"])
        cached = load_json("bravado")
        assert parsed == cached

    def test_parse_eerie(self):
        parsed = parse_en_pl(html["eerie"])
        cached = load_json("eerie")
        assert parsed == cached

    def test_parse_thaw(self):
        parsed = parse_en_pl(html["thaw"])
        cached = load_json("thaw")
        assert parsed == cached

    def test_parse_bewildering(self):
        parsed = parse_en_pl(html["bewildering"])
        cached = load_json("bewildering")
        assert parsed == cached

    def test_parse_taint(self):
        parsed = parse_en_pl(html["taint"])
        cached = load_json("taint")
        assert parsed == cached

    def test_parse_vie(self):
        parsed = parse_en_pl(html["vie"])
        cached = load_json("vie")
        assert parsed == cached

    def test_parse_agenda(self):
        parsed = parse_en_pl(html["agenda"])
        cached = load_json("agenda")
        assert parsed == cached

    def test_parse_midst(self):
        parsed = parse_en_pl(html["midst"])
        cached = load_json("midst")
        assert parsed == cached

    def test_parse_churn(self):
        parsed = parse_en_pl(html["churn"])
        cached = load_json("churn")
        assert parsed == cached

    def test_parse_nexus(self):
        parsed = parse_en_pl(html["nexus"])
        cached = load_json("nexus")
        assert parsed == cached

    def test_parse_oat(self):
        parsed = parse_en_pl(html["oat"])
        cached = load_json("oat")
        assert parsed == cached

    def test_parse_chastity(self):
        parsed = parse_en_pl(html["chastity"])
        cached = load_json("chastity")
        assert parsed == cached

    def test_parse_poplar(self):
        parsed = parse_en_pl(html["poplar"])
        cached = load_json("poplar")
        assert parsed == cached

    def test_parse_glazed(self):
        parsed = parse_en_pl(html["glazed"])
        cached = load_json("glazed")
        assert parsed == cached

    def test_parse_seethe(self):
        parsed = parse_en_pl(html["seethe"])
        cached = load_json("seethe")
        assert parsed == cached

    def test_parse_serene(self):
        parsed = parse_en_pl(html["serene"])
        cached = load_json("serene")
        assert parsed == cached

    def test_parse_tempestuous(self):
        parsed = parse_en_pl(html["tempestuous"])
        cached = load_json("tempestuous")
        assert parsed == cached

    def test_parse_stoked(self):
        parsed = parse_en_pl(html["stoked"])
        cached = load_json("stoked")
        assert parsed == cached

    def test_parse_tantalize(self):
        parsed = parse_en_pl(html["tantalize"])
        cached = load_json("tantalize")
        assert parsed == cached

    def test_parse_mesmerizing(self):
        parsed = parse_en_pl(html["mesmerizing"])
        cached = load_json("mesmerizing")
        assert parsed == cached

    def test_parse_gull(self):
        parsed = parse_en_pl(html["gull"])
        cached = load_json("gull")
        assert parsed == cached

    def test_parse_stratify(self):
        parsed = parse_en_pl(html["stratify"])
        cached = load_json("stratify")
        assert parsed == cached

    def test_parse_derive(self):
        parsed = parse_en_pl(html["derive"])
        cached = load_json("derive")
        assert parsed == cached

    def test_parse_absentminded(self):
        parsed = parse_en_pl(html["absentminded"])
        cached = load_json("absentminded")
        assert parsed == cached

    def test_parse_wiry(self):
        parsed = parse_en_pl(html["wiry"])
        cached = load_json("wiry")
        assert parsed == cached

    def test_parse_spoonful(self):
        parsed = parse_en_pl(html["spoonful"])
        cached = load_json("spoonful")
        assert parsed == cached

    def test_parse_munchkin(self):
        parsed = parse_en_pl(html["munchkin"])
        cached = load_json("munchkin")
        assert parsed == cached

    def test_parse_peppy(self):
        parsed = parse_en_pl(html["peppy"])
        cached = load_json("peppy")
        assert parsed == cached

    def test_parse_flummoxed(self):
        parsed = parse_en_pl(html["flummoxed"])
        cached = load_json("flummoxed")
        assert parsed == cached

    def test_parse_spurt(self):
        parsed = parse_en_pl(html["spurt"])
        cached = load_json("spurt")
        assert parsed == cached

    def test_parse_linger(self):
        parsed = parse_en_pl(html["linger"])
        cached = load_json("linger")
        assert parsed == cached

    def test_parse_crumple(self):
        parsed = parse_en_pl(html["crumple"])
        cached = load_json("crumple")
        assert parsed == cached

    def test_parse_inundate(self):
        parsed = parse_en_pl(html["inundate"])
        cached = load_json("inundate")
        assert parsed == cached

    def test_parse_smut(self):
        parsed = parse_en_pl(html["smut"])
        cached = load_json("smut")
        assert parsed == cached

    def test_parse_elicit(self):
        parsed = parse_en_pl(html["elicit"])
        cached = load_json("elicit")
        assert parsed == cached

    def test_parse_acme(self):
        parsed = parse_en_pl(html["acme"])
        cached = load_json("acme")
        assert parsed == cached

    def test_parse_neurotic(self):
        parsed = parse_en_pl(html["neurotic"])
        cached = load_json("neurotic")
        assert parsed == cached

    def test_parse_restless(self):
        parsed = parse_en_pl(html["restless"])
        cached = load_json("restless")
        assert parsed == cached

    def test_parse_exaltation(self):
        parsed = parse_en_pl(html["exaltation"])
        cached = load_json("exaltation")
        assert parsed == cached

    def test_parse_tether(self):
        parsed = parse_en_pl(html["tether"])
        cached = load_json("tether")
        assert parsed == cached

    def test_parse_communion(self):
        parsed = parse_en_pl(html["communion"])
        cached = load_json("communion")
        assert parsed == cached

    def test_parse_fuselage(self):
        parsed = parse_en_pl(html["fuselage"])
        cached = load_json("fuselage")
        assert parsed == cached

    def test_parse_plenitude(self):
        parsed = parse_en_pl(html["plenitude"])
        cached = load_json("plenitude")
        assert parsed == cached

    def test_parse_proxy(self):
        parsed = parse_en_pl(html["proxy"])
        cached = load_json("proxy")
        assert parsed == cached

    def test_parse_lucidity(self):
        parsed = parse_en_pl(html["lucidity"])
        cached = load_json("lucidity")
        assert parsed == cached

    def test_parse_navel(self):
        parsed = parse_en_pl(html["navel"])
        cached = load_json("navel")
        assert parsed == cached

    def test_parse_opulent(self):
        parsed = parse_en_pl(html["opulent"])
        cached = load_json("opulent")
        assert parsed == cached

    def test_parse_bijective(self):
        parsed = parse_en_pl(html["bijective"])
        cached = load_json("bijective")
        assert parsed == cached

    def test_parse_skewers(self):
        parsed = parse_en_pl(html["skewers"])
        cached = load_json("skewers")
        assert parsed == cached

    def test_parse_underpin(self):
        parsed = parse_en_pl(html["underpin"])
        cached = load_json("underpin")
        assert parsed == cached

    def test_parse_pneumonia(self):
        parsed = parse_en_pl(html["pneumonia"])
        cached = load_json("pneumonia")
        assert parsed == cached

    def test_parse_relentlessly(self):
        parsed = parse_en_pl(html["relentlessly"])
        cached = load_json("relentlessly")
        assert parsed == cached

    def test_parse_provost(self):
        parsed = parse_en_pl(html["provost"])
        cached = load_json("provost")
        assert parsed == cached

    def test_parse_spruce(self):
        parsed = parse_en_pl(html["spruce"])
        cached = load_json("spruce")
        assert parsed == cached

    def test_parse_nix(self):
        parsed = parse_en_pl(html["nix"])
        cached = load_json("nix")
        assert parsed == cached

    def test_parse_damsel(self):
        parsed = parse_en_pl(html["damsel"])
        cached = load_json("damsel")
        assert parsed == cached

    def test_parse_enthrall(self):
        parsed = parse_en_pl(html["enthrall"])
        cached = load_json("enthrall")
        assert parsed == cached

    def test_parse_glitzy(self):
        parsed = parse_en_pl(html["glitzy"])
        cached = load_json("glitzy")
        assert parsed == cached

    def test_parse_tithing(self):
        parsed = parse_en_pl(html["tithing"])
        cached = load_json("tithing")
        assert parsed == cached

    def test_parse_jettison(self):
        parsed = parse_en_pl(html["jettison"])
        cached = load_json("jettison")
        assert parsed == cached

    def test_parse_bugle(self):
        parsed = parse_en_pl(html["bugle"])
        cached = load_json("bugle")
        assert parsed == cached

    def test_parse_aspen(self):
        parsed = parse_en_pl(html["aspen"])
        cached = load_json("aspen")
        assert parsed == cached

    def test_parse_pang(self):
        parsed = parse_en_pl(html["pang"])
        cached = load_json("pang")
        assert parsed == cached

    def test_parse_limbo(self):
        parsed = parse_en_pl(html["limbo"])
        cached = load_json("limbo")
        assert parsed == cached

    def test_parse_opportunistic(self):
        parsed = parse_en_pl(html["opportunistic"])
        cached = load_json("opportunistic")
        assert parsed == cached

    def test_parse_platitude(self):
        parsed = parse_en_pl(html["platitude"])
        cached = load_json("platitude")
        assert parsed == cached

    def test_parse_kale(self):
        parsed = parse_en_pl(html["kale"])
        cached = load_json("kale")
        assert parsed == cached

    def test_parse_apricot(self):
        parsed = parse_en_pl(html["apricot"])
        cached = load_json("apricot")
        assert parsed == cached

    def test_parse_flak(self):
        parsed = parse_en_pl(html["flak"])
        cached = load_json("flak")
        assert parsed == cached

    def test_parse_dowry(self):
        parsed = parse_en_pl(html["dowry"])
        cached = load_json("dowry")
        assert parsed == cached

    def test_parse_concoct(self):
        parsed = parse_en_pl(html["concoct"])
        cached = load_json("concoct")
        assert parsed == cached

    def test_parse_mute(self):
        parsed = parse_en_pl(html["mute"])
        cached = load_json("mute")
        assert parsed == cached

    def test_parse_genuine(self):
        parsed = parse_en_pl(html["genuine"])
        cached = load_json("genuine")
        assert parsed == cached

    def test_parse_impartial(self):
        parsed = parse_en_pl(html["impartial"])
        cached = load_json("impartial")
        assert parsed == cached

    def test_parse_pliers(self):
        parsed = parse_en_pl(html["pliers"])
        cached = load_json("pliers")
        assert parsed == cached

    def test_parse_plod(self):
        parsed = parse_en_pl(html["plod"])
        cached = load_json("plod")
        assert parsed == cached

    def test_parse_vestigial(self):
        parsed = parse_en_pl(html["vestigial"])
        cached = load_json("vestigial")
        assert parsed == cached

    def test_parse_vest(self):
        parsed = parse_en_pl(html["vest"])
        cached = load_json("vest")
        assert parsed == cached

    def test_parse_cohesion(self):
        parsed = parse_en_pl(html["cohesion"])
        cached = load_json("cohesion")
        assert parsed == cached

    def test_parse_pauper(self):
        parsed = parse_en_pl(html["pauper"])
        cached = load_json("pauper")
        assert parsed == cached

    def test_parse_exhilarating(self):
        parsed = parse_en_pl(html["exhilarating"])
        cached = load_json("exhilarating")
        assert parsed == cached

    def test_parse_sumptuous(self):
        parsed = parse_en_pl(html["sumptuous"])
        cached = load_json("sumptuous")
        assert parsed == cached

    def test_parse_gratuitous(self):
        parsed = parse_en_pl(html["gratuitous"])
        cached = load_json("gratuitous")
        assert parsed == cached

    def test_parse_meddle(self):
        parsed = parse_en_pl(html["meddle"])
        cached = load_json("meddle")
        assert parsed == cached

    def test_parse_yam(self):
        parsed = parse_en_pl(html["yam"])
        cached = load_json("yam")
        assert parsed == cached

    def test_parse_deftly(self):
        parsed = parse_en_pl(html["deftly"])
        cached = load_json("deftly")
        assert parsed == cached

    def test_parse_fitful(self):
        parsed = parse_en_pl(html["fitful"])
        cached = load_json("fitful")
        assert parsed == cached

    def test_parse_rancid(self):
        parsed = parse_en_pl(html["rancid"])
        cached = load_json("rancid")
        assert parsed == cached

    def test_parse_stilted(self):
        parsed = parse_en_pl(html["stilted"])
        cached = load_json("stilted")
        assert parsed == cached

    def test_parse_unprepossessing(self):
        parsed = parse_en_pl(html["unprepossessing"])
        cached = load_json("unprepossessing")
        assert parsed == cached

    def test_parse_redemption(self):
        parsed = parse_en_pl(html["redemption"])
        cached = load_json("redemption")
        assert parsed == cached

    def test_parse_planer(self):
        parsed = parse_en_pl(html["planer"])
        cached = load_json("planer")
        assert parsed == cached

    def test_parse_wimpy(self):
        parsed = parse_en_pl(html["wimpy"])
        cached = load_json("wimpy")
        assert parsed == cached

    def test_parse_evocative(self):
        parsed = parse_en_pl(html["evocative"])
        cached = load_json("evocative")
        assert parsed == cached

    def test_parse_workhorse(self):
        parsed = parse_en_pl(html["workhorse"])
        cached = load_json("workhorse")
        assert parsed == cached

    def test_parse_predicate(self):
        parsed = parse_en_pl(html["predicate"])
        cached = load_json("predicate")
        assert parsed == cached

    def test_parse_sophistry(self):
        parsed = parse_en_pl(html["sophistry"])
        cached = load_json("sophistry")
        assert parsed == cached

    def test_parse_permanence(self):
        parsed = parse_en_pl(html["permanence"])
        cached = load_json("permanence")
        assert parsed == cached

    def test_parse_deranged(self):
        parsed = parse_en_pl(html["deranged"])
        cached = load_json("deranged")
        assert parsed == cached

    def test_parse_disingenuous(self):
        parsed = parse_en_pl(html["disingenuous"])
        cached = load_json("disingenuous")
        assert parsed == cached

    def test_parse_fizzle(self):
        parsed = parse_en_pl(html["fizzle"])
        cached = load_json("fizzle")
        assert parsed == cached

    def test_parse_dinky(self):
        parsed = parse_en_pl(html["dinky"])
        cached = load_json("dinky")
        assert parsed == cached

    def test_parse_stranglehold(self):
        parsed = parse_en_pl(html["stranglehold"])
        cached = load_json("stranglehold")
        assert parsed == cached

    def test_parse_yap(self):
        parsed = parse_en_pl(html["yap"])
        cached = load_json("yap")
        assert parsed == cached

    def test_parse_grogginess(self):
        parsed = parse_en_pl(html["grogginess"])
        cached = load_json("grogginess")
        assert parsed == cached

    def test_parse_exertion(self):
        parsed = parse_en_pl(html["exertion"])
        cached = load_json("exertion")
        assert parsed == cached

    def test_parse_solicite(self):
        parsed = parse_en_pl(html["solicite"])
        cached = load_json("solicite")
        assert parsed == cached

    def test_parse_custard(self):
        parsed = parse_en_pl(html["custard"])
        cached = load_json("custard")
        assert parsed == cached

    def test_parse_irreverence(self):
        parsed = parse_en_pl(html["irreverence"])
        cached = load_json("irreverence")
        assert parsed == cached

    def test_parse_gutted(self):
        parsed = parse_en_pl(html["gutted"])
        cached = load_json("gutted")
        assert parsed == cached

    def test_parse_cashew(self):
        parsed = parse_en_pl(html["cashew"])
        cached = load_json("cashew")
        assert parsed == cached

    def test_parse_gaff(self):
        parsed = parse_en_pl(html["gaff"])
        cached = load_json("gaff")
        assert parsed == cached

    def test_parse_seclude(self):
        parsed = parse_en_pl(html["seclude"])
        cached = load_json("seclude")
        assert parsed == cached

    def test_parse_seditious(self):
        parsed = parse_en_pl(html["seditious"])
        cached = load_json("seditious")
        assert parsed == cached

    def test_parse_sassy(self):
        parsed = parse_en_pl(html["sassy"])
        cached = load_json("sassy")
        assert parsed == cached

    def test_parse_botcher(self):
        parsed = parse_en_pl(html["botcher"])
        cached = load_json("botcher")
        assert parsed == cached

    def test_parse_endearing(self):
        parsed = parse_en_pl(html["endearing"])
        cached = load_json("endearing")
        assert parsed == cached

    def test_parse_maintainer(self):
        parsed = parse_en_pl(html["maintainer"])
        cached = load_json("maintainer")
        assert parsed == cached

    def test_parse_zealous(self):
        parsed = parse_en_pl(html["zealous"])
        cached = load_json("zealous")
        assert parsed == cached

    def test_parse_kiln(self):
        parsed = parse_en_pl(html["kiln"])
        cached = load_json("kiln")
        assert parsed == cached

    def test_parse_chagrin(self):
        parsed = parse_en_pl(html["chagrin"])
        cached = load_json("chagrin")
        assert parsed == cached

    def test_parse_oud(self):
        parsed = parse_en_pl(html["oud"])
        cached = load_json("oud")
        assert parsed == cached

    def test_parse_squalid(self):
        parsed = parse_en_pl(html["squalid"])
        cached = load_json("squalid")
        assert parsed == cached

    def test_parse_plaster(self):
        parsed = parse_en_pl(html["plaster"])
        cached = load_json("plaster")
        assert parsed == cached

    def test_parse_obnoxious(self):
        parsed = parse_en_pl(html["obnoxious"])
        cached = load_json("obnoxious")
        assert parsed == cached

    def test_parse_idem(self):
        parsed = parse_en_pl(html["idem"])
        cached = load_json("idem")
        assert parsed == cached

    def test_parse_realtor(self):
        parsed = parse_en_pl(html["realtor"])
        cached = load_json("realtor")
        assert parsed == cached

    def test_parse_chivalry(self):
        parsed = parse_en_pl(html["chivalry"])
        cached = load_json("chivalry")
        assert parsed == cached

    def test_parse_tussle(self):
        parsed = parse_en_pl(html["tussle"])
        cached = load_json("tussle")
        assert parsed == cached

    def test_parse_vile(self):
        parsed = parse_en_pl(html["vile"])
        cached = load_json("vile")
        assert parsed == cached

    def test_parse_clumsy(self):
        parsed = parse_en_pl(html["clumsy"])
        cached = load_json("clumsy")
        assert parsed == cached

    def test_parse_derelict(self):
        parsed = parse_en_pl(html["derelict"])
        cached = load_json("derelict")
        assert parsed == cached

    def test_parse_trite(self):
        parsed = parse_en_pl(html["trite"])
        cached = load_json("trite")
        assert parsed == cached

    def test_parse_procurement(self):
        parsed = parse_en_pl(html["procurement"])
        cached = load_json("procurement")
        assert parsed == cached

    def test_parse_cannily(self):
        parsed = parse_en_pl(html["cannily"])
        cached = load_json("cannily")
        assert parsed == cached

    def test_parse_femur(self):
        parsed = parse_en_pl(html["femur"])
        cached = load_json("femur")
        assert parsed == cached

    def test_parse_infibulate(self):
        parsed = parse_en_pl(html["infibulate"])
        cached = load_json("infibulate")
        assert parsed == cached

    def test_parse_rampage(self):
        parsed = parse_en_pl(html["rampage"])
        cached = load_json("rampage")
        assert parsed == cached

    def test_parse_ruinous(self):
        parsed = parse_en_pl(html["ruinous"])
        cached = load_json("ruinous")
        assert parsed == cached

    def test_parse_soliloquy(self):
        parsed = parse_en_pl(html["soliloquy"])
        cached = load_json("soliloquy")
        assert parsed == cached

    def test_parse_wreath(self):
        parsed = parse_en_pl(html["wreath"])
        cached = load_json("wreath")
        assert parsed == cached

    def test_parse_deceit(self):
        parsed = parse_en_pl(html["deceit"])
        cached = load_json("deceit")
        assert parsed == cached

    def test_parse_vermin(self):
        parsed = parse_en_pl(html["vermin"])
        cached = load_json("vermin")
        assert parsed == cached

    def test_parse_acrid(self):
        parsed = parse_en_pl(html["acrid"])
        cached = load_json("acrid")
        assert parsed == cached

    def test_parse_foreman(self):
        parsed = parse_en_pl(html["foreman"])
        cached = load_json("foreman")
        assert parsed == cached

    def test_parse_pep(self):
        parsed = parse_en_pl(html["pep"])
        cached = load_json("pep")
        assert parsed == cached

    def test_parse_meadowlark(self):
        parsed = parse_en_pl(html["meadowlark"])
        cached = load_json("meadowlark")
        assert parsed == cached

    def test_parse_petite(self):
        parsed = parse_en_pl(html["petite"])
        cached = load_json("petite")
        assert parsed == cached

    def test_parse_thistle(self):
        parsed = parse_en_pl(html["thistle"])
        cached = load_json("thistle")
        assert parsed == cached

    def test_parse_tenure(self):
        parsed = parse_en_pl(html["tenure"])
        cached = load_json("tenure")
        assert parsed == cached

    def test_parse_incense(self):
        parsed = parse_en_pl(html["incense"])
        cached = load_json("incense")
        assert parsed == cached

    def test_parse_easel(self):
        parsed = parse_en_pl(html["easel"])
        cached = load_json("easel")
        assert parsed == cached

    def test_parse_predicament(self):
        parsed = parse_en_pl(html["predicament"])
        cached = load_json("predicament")
        assert parsed == cached

    def test_parse_portly(self):
        parsed = parse_en_pl(html["portly"])
        cached = load_json("portly")
        assert parsed == cached

    def test_parse_exasperating(self):
        parsed = parse_en_pl(html["exasperating"])
        cached = load_json("exasperating")
        assert parsed == cached

    def test_parse_rancorous(self):
        parsed = parse_en_pl(html["rancorous"])
        cached = load_json("rancorous")
        assert parsed == cached

    def test_parse_punditry(self):
        parsed = parse_en_pl(html["punditry"])
        cached = load_json("punditry")
        assert parsed == cached

    def test_parse_notoriety(self):
        parsed = parse_en_pl(html["notoriety"])
        cached = load_json("notoriety")
        assert parsed == cached

    def test_parse_holster(self):
        parsed = parse_en_pl(html["holster"])
        cached = load_json("holster")
        assert parsed == cached

    def test_parse_pithy(self):
        parsed = parse_en_pl(html["pithy"])
        cached = load_json("pithy")
        assert parsed == cached

    def test_parse_ableism(self):
        parsed = parse_en_pl(html["ableism"])
        cached = load_json("ableism")
        assert parsed == cached

    def test_parse_congruence(self):
        parsed = parse_en_pl(html["congruence"])
        cached = load_json("congruence")
        assert parsed == cached

    def test_parse_pronounced(self):
        parsed = parse_en_pl(html["pronounced"])
        cached = load_json("pronounced")
        assert parsed == cached

    def test_parse_sequin(self):
        parsed = parse_en_pl(html["sequin"])
        cached = load_json("sequin")
        assert parsed == cached

    def test_parse_flounder(self):
        parsed = parse_en_pl(html["flounder"])
        cached = load_json("flounder")
        assert parsed == cached

    def test_parse_serendipity(self):
        parsed = parse_en_pl(html["serendipity"])
        cached = load_json("serendipity")
        assert parsed == cached

    def test_parse_coveted(self):
        parsed = parse_en_pl(html["coveted"])
        cached = load_json("coveted")
        assert parsed == cached

    def test_parse_revet(self):
        parsed = parse_en_pl(html["revet"])
        cached = load_json("revet")
        assert parsed == cached

    def test_parse_etch(self):
        parsed = parse_en_pl(html["etch"])
        cached = load_json("etch")
        assert parsed == cached

    def test_parse_sleight(self):
        parsed = parse_en_pl(html["sleight"])
        cached = load_json("sleight")
        assert parsed == cached

    def test_parse_poignant(self):
        parsed = parse_en_pl(html["poignant"])
        cached = load_json("poignant")
        assert parsed == cached

    def test_parse_chirality(self):
        parsed = parse_en_pl(html["chirality"])
        cached = load_json("chirality")
        assert parsed == cached

    def test_parse_assiduously(self):
        parsed = parse_en_pl(html["assiduously"])
        cached = load_json("assiduously")
        assert parsed == cached

    def test_parse_gait(self):
        parsed = parse_en_pl(html["gait"])
        cached = load_json("gait")
        assert parsed == cached

    def test_parse_blindside(self):
        parsed = parse_en_pl(html["blindside"])
        cached = load_json("blindside")
        assert parsed == cached

    def test_parse_putter(self):
        parsed = parse_en_pl(html["putter"])
        cached = load_json("putter")
        assert parsed == cached

    def test_parse_phony(self):
        parsed = parse_en_pl(html["phony"])
        cached = load_json("phony")
        assert parsed == cached

    def test_parse_fidelity(self):
        parsed = parse_en_pl(html["fidelity"])
        cached = load_json("fidelity")
        assert parsed == cached

    def test_parse_sore(self):
        parsed = parse_en_pl(html["sore"])
        cached = load_json("sore")
        assert parsed == cached

    def test_parse_splendid(self):
        parsed = parse_en_pl(html["splendid"])
        cached = load_json("splendid")
        assert parsed == cached

    def test_parse_hamlet(self):
        parsed = parse_en_pl(html["hamlet"])
        cached = load_json("hamlet")
        assert parsed == cached

    def test_parse_hoist(self):
        parsed = parse_en_pl(html["hoist"])
        cached = load_json("hoist")
        assert parsed == cached

    def test_parse_depress(self):
        parsed = parse_en_pl(html["depress"])
        cached = load_json("depress")
        assert parsed == cached

    def test_parse_felony(self):
        parsed = parse_en_pl(html["felony"])
        cached = load_json("felony")
        assert parsed == cached

    def test_parse_androgen(self):
        parsed = parse_en_pl(html["androgen"])
        cached = load_json("androgen")
        assert parsed == cached

    def test_parse_asset(self):
        parsed = parse_en_pl(html["asset"])
        cached = load_json("asset")
        assert parsed == cached

    def test_parse_auspicious(self):
        parsed = parse_en_pl(html["auspicious"])
        cached = load_json("auspicious")
        assert parsed == cached

    def test_parse_fallow(self):
        parsed = parse_en_pl(html["fallow"])
        cached = load_json("fallow")
        assert parsed == cached

    def test_parse_discord(self):
        parsed = parse_en_pl(html["discord"])
        cached = load_json("discord")
        assert parsed == cached

    def test_parse_gullible(self):
        parsed = parse_en_pl(html["gullible"])
        cached = load_json("gullible")
        assert parsed == cached

    def test_parse_enema(self):
        parsed = parse_en_pl(html["enema"])
        cached = load_json("enema")
        assert parsed == cached

    def test_parse_vindicate(self):
        parsed = parse_en_pl(html["vindicate"])
        cached = load_json("vindicate")
        assert parsed == cached

    def test_parse_kelp(self):
        parsed = parse_en_pl(html["kelp"])
        cached = load_json("kelp")
        assert parsed == cached

    def test_parse_grouse(self):
        parsed = parse_en_pl(html["grouse"])
        cached = load_json("grouse")
        assert parsed == cached

    def test_parse_lenient(self):
        parsed = parse_en_pl(html["lenient"])
        cached = load_json("lenient")
        assert parsed == cached

    def test_parse_esophagus(self):
        parsed = parse_en_pl(html["esophagus"])
        cached = load_json("esophagus")
        assert parsed == cached

    def test_parse_angst(self):
        parsed = parse_en_pl(html["angst"])
        cached = load_json("angst")
        assert parsed == cached

    def test_parse_fink(self):
        parsed = parse_en_pl(html["fink"])
        cached = load_json("fink")
        assert parsed == cached

    def test_parse_foo(self):
        parsed = parse_en_pl(html["foo"])
        cached = load_json("foo")
        assert parsed == cached

    def test_parse_congruent(self):
        parsed = parse_en_pl(html["congruent"])
        cached = load_json("congruent")
        assert parsed == cached

    def test_parse_cerebellum(self):
        parsed = parse_en_pl(html["cerebellum"])
        cached = load_json("cerebellum")
        assert parsed == cached

    def test_parse_creepy(self):
        parsed = parse_en_pl(html["creepy"])
        cached = load_json("creepy")
        assert parsed == cached

    def test_parse_cobweb(self):
        parsed = parse_en_pl(html["cobweb"])
        cached = load_json("cobweb")
        assert parsed == cached

    def test_parse_potent(self):
        parsed = parse_en_pl(html["potent"])
        cached = load_json("potent")
        assert parsed == cached

    def test_parse_inertia(self):
        parsed = parse_en_pl(html["inertia"])
        cached = load_json("inertia")
        assert parsed == cached

    def test_parse_legibility(self):
        parsed = parse_en_pl(html["legibility"])
        cached = load_json("legibility")
        assert parsed == cached

    def test_parse_flock(self):
        parsed = parse_en_pl(html["flock"])
        cached = load_json("flock")
        assert parsed == cached

    def test_parse_foray(self):
        parsed = parse_en_pl(html["foray"])
        cached = load_json("foray")
        assert parsed == cached

    def test_parse_tender(self):
        parsed = parse_en_pl(html["tender"])
        cached = load_json("tender")
        assert parsed == cached

    def test_parse_exude(self):
        parsed = parse_en_pl(html["exude"])
        cached = load_json("exude")
        assert parsed == cached

    def test_parse_fiefdom(self):
        parsed = parse_en_pl(html["fiefdom"])
        cached = load_json("fiefdom")
        assert parsed == cached

    def test_parse_inert(self):
        parsed = parse_en_pl(html["inert"])
        cached = load_json("inert")
        assert parsed == cached

    def test_parse_devise(self):
        parsed = parse_en_pl(html["devise"])
        cached = load_json("devise")
        assert parsed == cached

    def test_parse_knuckle(self):
        parsed = parse_en_pl(html["knuckle"])
        cached = load_json("knuckle")
        assert parsed == cached

    def test_parse_pulverize(self):
        parsed = parse_en_pl(html["pulverize"])
        cached = load_json("pulverize")
        assert parsed == cached

    def test_parse_tantamount(self):
        parsed = parse_en_pl(html["tantamount"])
        cached = load_json("tantamount")
        assert parsed == cached

    def test_parse_dole(self):
        parsed = parse_en_pl(html["dole"])
        cached = load_json("dole")
        assert parsed == cached

    def test_parse_attrit(self):
        parsed = parse_en_pl(html["attrit"])
        cached = load_json("attrit")
        assert parsed == cached

    def test_parse_battery(self):
        parsed = parse_en_pl(html["battery"])
        cached = load_json("battery")
        assert parsed == cached

    def test_parse_myopic(self):
        parsed = parse_en_pl(html["myopic"])
        cached = load_json("myopic")
        assert parsed == cached

    def test_parse_affectionate(self):
        parsed = parse_en_pl(html["affectionate"])
        cached = load_json("affectionate")
        assert parsed == cached

    def test_parse_malodorous(self):
        parsed = parse_en_pl(html["malodorous"])
        cached = load_json("malodorous")
        assert parsed == cached

    def test_parse_seaweed(self):
        parsed = parse_en_pl(html["seaweed"])
        cached = load_json("seaweed")
        assert parsed == cached

    def test_parse_resentment(self):
        parsed = parse_en_pl(html["resentment"])
        cached = load_json("resentment")
        assert parsed == cached

    def test_parse_causation(self):
        parsed = parse_en_pl(html["causation"])
        cached = load_json("causation")
        assert parsed == cached

    def test_parse_critic(self):
        parsed = parse_en_pl(html["critic"])
        cached = load_json("critic")
        assert parsed == cached

    def test_parse_stiffen(self):
        parsed = parse_en_pl(html["stiffen"])
        cached = load_json("stiffen")
        assert parsed == cached

    def test_parse_minimalist(self):
        parsed = parse_en_pl(html["minimalist"])
        cached = load_json("minimalist")
        assert parsed == cached

    def test_parse_deprecate(self):
        parsed = parse_en_pl(html["deprecate"])
        cached = load_json("deprecate")
        assert parsed == cached

    def test_parse_pet(self):
        parsed = parse_en_pl(html["pet"])
        cached = load_json("pet")
        assert parsed == cached

    def test_parse_dye(self):
        parsed = parse_en_pl(html["dye"])
        cached = load_json("dye")
        assert parsed == cached

    def test_parse_voluble(self):
        parsed = parse_en_pl(html["voluble"])
        cached = load_json("voluble")
        assert parsed == cached

    def test_parse_chisel(self):
        parsed = parse_en_pl(html["chisel"])
        cached = load_json("chisel")
        assert parsed == cached

    def test_parse_renounce(self):
        parsed = parse_en_pl(html["renounce"])
        cached = load_json("renounce")
        assert parsed == cached

    def test_parse_bereavement(self):
        parsed = parse_en_pl(html["bereavement"])
        cached = load_json("bereavement")
        assert parsed == cached

    def test_parse_sustain(self):
        parsed = parse_en_pl(html["sustain"])
        cached = load_json("sustain")
        assert parsed == cached

    def test_parse_carbohydrate(self):
        parsed = parse_en_pl(html["carbohydrate"])
        cached = load_json("carbohydrate")
        assert parsed == cached

    def test_parse_luddite(self):
        parsed = parse_en_pl(html["luddite"])
        cached = load_json("luddite")
        assert parsed == cached

    def test_parse_verbiage(self):
        parsed = parse_en_pl(html["verbiage"])
        cached = load_json("verbiage")
        assert parsed == cached

    def test_parse_diorama(self):
        parsed = parse_en_pl(html["diorama"])
        cached = load_json("diorama")
        assert parsed == cached

    def test_parse_anoint(self):
        parsed = parse_en_pl(html["anoint"])
        cached = load_json("anoint")
        assert parsed == cached

    def test_parse_mint(self):
        parsed = parse_en_pl(html["mint"])
        cached = load_json("mint")
        assert parsed == cached

    def test_parse_would(self):
        parsed = parse_en_pl(html["would"])
        cached = load_json("would")
        assert parsed == cached

    def test_parse_insinuate(self):
        parsed = parse_en_pl(html["insinuate"])
        cached = load_json("insinuate")
        assert parsed == cached

    def test_parse_malice(self):
        parsed = parse_en_pl(html["malice"])
        cached = load_json("malice")
        assert parsed == cached

    def test_parse_rescind(self):
        parsed = parse_en_pl(html["rescind"])
        cached = load_json("rescind")
        assert parsed == cached

    def test_parse_broil(self):
        parsed = parse_en_pl(html["broil"])
        cached = load_json("broil")
        assert parsed == cached

    def test_parse_stout(self):
        parsed = parse_en_pl(html["stout"])
        cached = load_json("stout")
        assert parsed == cached

    def test_parse_cobbles(self):
        parsed = parse_en_pl(html["cobbles"])
        cached = load_json("cobbles")
        assert parsed == cached

    def test_parse_parse(self):
        parsed = parse_en_pl(html["parse"])
        cached = load_json("parse")
        assert parsed == cached

    def test_parse_dysentery(self):
        parsed = parse_en_pl(html["dysentery"])
        cached = load_json("dysentery")
        assert parsed == cached

    def test_parse_abide(self):
        parsed = parse_en_pl(html["abide"])
        cached = load_json("abide")
        assert parsed == cached

    def test_parse_fraught(self):
        parsed = parse_en_pl(html["fraught"])
        cached = load_json("fraught")
        assert parsed == cached

    def test_parse_pastoral(self):
        parsed = parse_en_pl(html["pastoral"])
        cached = load_json("pastoral")
        assert parsed == cached

    def test_parse_quell(self):
        parsed = parse_en_pl(html["quell"])
        cached = load_json("quell")
        assert parsed == cached

    def test_parse_awl(self):
        parsed = parse_en_pl(html["awl"])
        cached = load_json("awl")
        assert parsed == cached

    def test_parse_paisley(self):
        parsed = parse_en_pl(html["paisley"])
        cached = load_json("paisley")
        assert parsed == cached

    def test_parse_darkly(self):
        parsed = parse_en_pl(html["darkly"])
        cached = load_json("darkly")
        assert parsed == cached

    def test_parse_viceroy(self):
        parsed = parse_en_pl(html["viceroy"])
        cached = load_json("viceroy")
        assert parsed == cached

    def test_parse_flagrant(self):
        parsed = parse_en_pl(html["flagrant"])
        cached = load_json("flagrant")
        assert parsed == cached

    def test_parse_could(self):
        parsed = parse_en_pl(html["could"])
        cached = load_json("could")
        assert parsed == cached

    def test_parse_trenchant(self):
        parsed = parse_en_pl(html["trenchant"])
        cached = load_json("trenchant")
        assert parsed == cached

    def test_parse_rupture(self):
        parsed = parse_en_pl(html["rupture"])
        cached = load_json("rupture")
        assert parsed == cached

    def test_parse_ulcer(self):
        parsed = parse_en_pl(html["ulcer"])
        cached = load_json("ulcer")
        assert parsed == cached

    def test_parse_vaguely(self):
        parsed = parse_en_pl(html["vaguely"])
        cached = load_json("vaguely")
        assert parsed == cached

    def test_parse_tumult(self):
        parsed = parse_en_pl(html["tumult"])
        cached = load_json("tumult")
        assert parsed == cached

    def test_parse_candor(self):
        parsed = parse_en_pl(html["candor"])
        cached = load_json("candor")
        assert parsed == cached

    def test_parse_conducive(self):
        parsed = parse_en_pl(html["conducive"])
        cached = load_json("conducive")
        assert parsed == cached

    def test_parse_subordinate(self):
        parsed = parse_en_pl(html["subordinate"])
        cached = load_json("subordinate")
        assert parsed == cached

    def test_parse_excoriate(self):
        parsed = parse_en_pl(html["excoriate"])
        cached = load_json("excoriate")
        assert parsed == cached

    def test_parse_merciless(self):
        parsed = parse_en_pl(html["merciless"])
        cached = load_json("merciless")
        assert parsed == cached

    def test_parse_abominable(self):
        parsed = parse_en_pl(html["abominable"])
        cached = load_json("abominable")
        assert parsed == cached

    def test_parse_turbulent(self):
        parsed = parse_en_pl(html["turbulent"])
        cached = load_json("turbulent")
        assert parsed == cached

    def test_parse_lambast(self):
        parsed = parse_en_pl(html["lambast"])
        cached = load_json("lambast")
        assert parsed == cached

    def test_parse_privileges(self):
        parsed = parse_en_pl(html["privileges"])
        cached = load_json("privileges")
        assert parsed == cached

    def test_parse_defiance(self):
        parsed = parse_en_pl(html["defiance"])
        cached = load_json("defiance")
        assert parsed == cached

    def test_parse_overcast(self):
        parsed = parse_en_pl(html["overcast"])
        cached = load_json("overcast")
        assert parsed == cached

    def test_parse_salient(self):
        parsed = parse_en_pl(html["salient"])
        cached = load_json("salient")
        assert parsed == cached

    def test_parse_these(self):
        parsed = parse_en_pl(html["these"])
        cached = load_json("these")
        assert parsed == cached

    def test_parse_valiantly(self):
        parsed = parse_en_pl(html["valiantly"])
        cached = load_json("valiantly")
        assert parsed == cached

    def test_parse_lucid(self):
        parsed = parse_en_pl(html["lucid"])
        cached = load_json("lucid")
        assert parsed == cached

    def test_parse_exacerbated(self):
        parsed = parse_en_pl(html["exacerbated"])
        cached = load_json("exacerbated")
        assert parsed == cached

    def test_parse_commutative(self):
        parsed = parse_en_pl(html["commutative"])
        cached = load_json("commutative")
        assert parsed == cached

    def test_parse_coarse(self):
        parsed = parse_en_pl(html["coarse"])
        cached = load_json("coarse")
        assert parsed == cached

    def test_parse_superficial(self):
        parsed = parse_en_pl(html["superficial"])
        cached = load_json("superficial")
        assert parsed == cached

    def test_parse_conscientious(self):
        parsed = parse_en_pl(html["conscientious"])
        cached = load_json("conscientious")
        assert parsed == cached

    def test_parse_hillock(self):
        parsed = parse_en_pl(html["hillock"])
        cached = load_json("hillock")
        assert parsed == cached

    def test_parse_alluvial(self):
        parsed = parse_en_pl(html["alluvial"])
        cached = load_json("alluvial")
        assert parsed == cached

    def test_parse_viscous(self):
        parsed = parse_en_pl(html["viscous"])
        cached = load_json("viscous")
        assert parsed == cached

    def test_parse_beguiling(self):
        parsed = parse_en_pl(html["beguiling"])
        cached = load_json("beguiling")
        assert parsed == cached

    def test_parse_manifold(self):
        parsed = parse_en_pl(html["manifold"])
        cached = load_json("manifold")
        assert parsed == cached

    def test_parse_scallop(self):
        parsed = parse_en_pl(html["scallop"])
        cached = load_json("scallop")
        assert parsed == cached

    def test_parse_recourse(self):
        parsed = parse_en_pl(html["recourse"])
        cached = load_json("recourse")
        assert parsed == cached

    def test_parse_whisked(self):
        parsed = parse_en_pl(html["whisked"])
        cached = load_json("whisked")
        assert parsed == cached

    def test_parse_feeble(self):
        parsed = parse_en_pl(html["feeble"])
        cached = load_json("feeble")
        assert parsed == cached

    def test_parse_swill(self):
        parsed = parse_en_pl(html["swill"])
        cached = load_json("swill")
        assert parsed == cached

    def test_parse_levy(self):
        parsed = parse_en_pl(html["levy"])
        cached = load_json("levy")
        assert parsed == cached

    def test_parse_corral(self):
        parsed = parse_en_pl(html["corral"])
        cached = load_json("corral")
        assert parsed == cached

    def test_parse_cluck(self):
        parsed = parse_en_pl(html["cluck"])
        cached = load_json("cluck")
        assert parsed == cached

    def test_parse_belligerence(self):
        parsed = parse_en_pl(html["belligerence"])
        cached = load_json("belligerence")
        assert parsed == cached

    def test_parse_chasm(self):
        parsed = parse_en_pl(html["chasm"])
        cached = load_json("chasm")
        assert parsed == cached

    def test_parse_latitude(self):
        parsed = parse_en_pl(html["latitude"])
        cached = load_json("latitude")
        assert parsed == cached

    def test_parse_incessant(self):
        parsed = parse_en_pl(html["incessant"])
        cached = load_json("incessant")
        assert parsed == cached

    def test_parse_mar(self):
        parsed = parse_en_pl(html["mar"])
        cached = load_json("mar")
        assert parsed == cached

    def test_parse_mandarin(self):
        parsed = parse_en_pl(html["mandarin"])
        cached = load_json("mandarin")
        assert parsed == cached

    def test_parse_tangy(self):
        parsed = parse_en_pl(html["tangy"])
        cached = load_json("tangy")
        assert parsed == cached

    def test_parse_palatable(self):
        parsed = parse_en_pl(html["palatable"])
        cached = load_json("palatable")
        assert parsed == cached

    def test_parse_avery(self):
        parsed = parse_en_pl(html["avery"])
        cached = load_json("avery")
        assert parsed == cached

    def test_parse_insidiously(self):
        parsed = parse_en_pl(html["insidiously"])
        cached = load_json("insidiously")
        assert parsed == cached

    def test_parse_grouchiness(self):
        parsed = parse_en_pl(html["grouchiness"])
        cached = load_json("grouchiness")
        assert parsed == cached

    def test_parse_traduce(self):
        parsed = parse_en_pl(html["traduce"])
        cached = load_json("traduce")
        assert parsed == cached

    def test_parse_rumble(self):
        parsed = parse_en_pl(html["rumble"])
        cached = load_json("rumble")
        assert parsed == cached

    def test_parse_timber(self):
        parsed = parse_en_pl(html["timber"])
        cached = load_json("timber")
        assert parsed == cached

    def test_parse_indulgence(self):
        parsed = parse_en_pl(html["indulgence"])
        cached = load_json("indulgence")
        assert parsed == cached

    def test_parse_yttria(self):
        parsed = parse_en_pl(html["yttria"])
        cached = load_json("yttria")
        assert parsed == cached

    def test_parse_crest(self):
        parsed = parse_en_pl(html["crest"])
        cached = load_json("crest")
        assert parsed == cached

    def test_parse_apple(self):
        parsed = parse_en_pl(html["apple"])
        cached = load_json("apple")
        assert parsed == cached

    def test_parse_whirl(self):
        parsed = parse_en_pl(html["whirl"])
        cached = load_json("whirl")
        assert parsed == cached

    def test_parse_scrutiny(self):
        parsed = parse_en_pl(html["scrutiny"])
        cached = load_json("scrutiny")
        assert parsed == cached

    def test_parse_abandon(self):
        parsed = parse_en_pl(html["abandon"])
        cached = load_json("abandon")
        assert parsed == cached

    def test_parse_hubris(self):
        parsed = parse_en_pl(html["hubris"])
        cached = load_json("hubris")
        assert parsed == cached

    def test_parse_creed(self):
        parsed = parse_en_pl(html["creed"])
        cached = load_json("creed")
        assert parsed == cached

    def test_parse_aghast(self):
        parsed = parse_en_pl(html["aghast"])
        cached = load_json("aghast")
        assert parsed == cached

    def test_parse_concession(self):
        parsed = parse_en_pl(html["concession"])
        cached = load_json("concession")
        assert parsed == cached

    def test_parse_contest(self):
        parsed = parse_en_pl(html["contest"])
        cached = load_json("contest")
        assert parsed == cached

    def test_parse_unravel(self):
        parsed = parse_en_pl(html["unravel"])
        cached = load_json("unravel")
        assert parsed == cached

    def test_parse_whimper(self):
        parsed = parse_en_pl(html["whimper"])
        cached = load_json("whimper")
        assert parsed == cached

    def test_parse_nigh(self):
        parsed = parse_en_pl(html["nigh"])
        cached = load_json("nigh")
        assert parsed == cached

    def test_parse_molasses(self):
        parsed = parse_en_pl(html["molasses"])
        cached = load_json("molasses")
        assert parsed == cached

    def test_parse_revered(self):
        parsed = parse_en_pl(html["revered"])
        cached = load_json("revered")
        assert parsed == cached

    def test_parse_captivity(self):
        parsed = parse_en_pl(html["captivity"])
        cached = load_json("captivity")
        assert parsed == cached

    def test_parse_unanimous(self):
        parsed = parse_en_pl(html["unanimous"])
        cached = load_json("unanimous")
        assert parsed == cached

    def test_parse_eminence(self):
        parsed = parse_en_pl(html["eminence"])
        cached = load_json("eminence")
        assert parsed == cached

    def test_parse_juggernaut(self):
        parsed = parse_en_pl(html["juggernaut"])
        cached = load_json("juggernaut")
        assert parsed == cached

    def test_parse_laudanum(self):
        parsed = parse_en_pl(html["laudanum"])
        cached = load_json("laudanum")
        assert parsed == cached

    def test_parse_interdict(self):
        parsed = parse_en_pl(html["interdict"])
        cached = load_json("interdict")
        assert parsed == cached

    def test_parse_fulfill(self):
        parsed = parse_en_pl(html["fulfill"])
        cached = load_json("fulfill")
        assert parsed == cached

    def test_parse_groggy(self):
        parsed = parse_en_pl(html["groggy"])
        cached = load_json("groggy")
        assert parsed == cached

    def test_parse_paucity(self):
        parsed = parse_en_pl(html["paucity"])
        cached = load_json("paucity")
        assert parsed == cached

    def test_parse_morrow(self):
        parsed = parse_en_pl(html["morrow"])
        cached = load_json("morrow")
        assert parsed == cached

    def test_parse_porous(self):
        parsed = parse_en_pl(html["porous"])
        cached = load_json("porous")
        assert parsed == cached

    def test_parse_sodding(self):
        parsed = parse_en_pl(html["sodding"])
        cached = load_json("sodding")
        assert parsed == cached

    def test_parse_beholden(self):
        parsed = parse_en_pl(html["beholden"])
        cached = load_json("beholden")
        assert parsed == cached

    def test_parse_eyesore(self):
        parsed = parse_en_pl(html["eyesore"])
        cached = load_json("eyesore")
        assert parsed == cached

    def test_parse_vainglory(self):
        parsed = parse_en_pl(html["vainglory"])
        cached = load_json("vainglory")
        assert parsed == cached

    def test_parse_coalesce(self):
        parsed = parse_en_pl(html["coalesce"])
        cached = load_json("coalesce")
        assert parsed == cached

    def test_parse_fester(self):
        parsed = parse_en_pl(html["fester"])
        cached = load_json("fester")
        assert parsed == cached

    def test_parse_petulance(self):
        parsed = parse_en_pl(html["petulance"])
        cached = load_json("petulance")
        assert parsed == cached

    def test_parse_leniency(self):
        parsed = parse_en_pl(html["leniency"])
        cached = load_json("leniency")
        assert parsed == cached

    def test_parse_debris(self):
        parsed = parse_en_pl(html["debris"])
        cached = load_json("debris")
        assert parsed == cached

    def test_parse_vanity(self):
        parsed = parse_en_pl(html["vanity"])
        cached = load_json("vanity")
        assert parsed == cached

    def test_parse_compel(self):
        parsed = parse_en_pl(html["compel"])
        cached = load_json("compel")
        assert parsed == cached

    def test_parse_solipsist(self):
        parsed = parse_en_pl(html["solipsist"])
        cached = load_json("solipsist")
        assert parsed == cached

    def test_parse_betide(self):
        parsed = parse_en_pl(html["betide"])
        cached = load_json("betide")
        assert parsed == cached

    def test_parse_ludicrous(self):
        parsed = parse_en_pl(html["ludicrous"])
        cached = load_json("ludicrous")
        assert parsed == cached

    def test_parse_chant(self):
        parsed = parse_en_pl(html["chant"])
        cached = load_json("chant")
        assert parsed == cached

    def test_parse_hound(self):
        parsed = parse_en_pl(html["hound"])
        cached = load_json("hound")
        assert parsed == cached

    def test_parse_ideation(self):
        parsed = parse_en_pl(html["ideation"])
        cached = load_json("ideation")
        assert parsed == cached

    def test_parse_infamy(self):
        parsed = parse_en_pl(html["infamy"])
        cached = load_json("infamy")
        assert parsed == cached

    def test_parse_leshy(self):
        parsed = parse_en_pl(html["leshy"])
        cached = load_json("leshy")
        assert parsed == cached

    def test_parse_contemporary(self):
        parsed = parse_en_pl(html["contemporary"])
        cached = load_json("contemporary")
        assert parsed == cached

    def test_parse_muck(self):
        parsed = parse_en_pl(html["muck"])
        cached = load_json("muck")
        assert parsed == cached

    def test_parse_abutting(self):
        parsed = parse_en_pl(html["abutting"])
        cached = load_json("abutting")
        assert parsed == cached

    def test_parse_gaunt(self):
        parsed = parse_en_pl(html["gaunt"])
        cached = load_json("gaunt")
        assert parsed == cached

    def test_parse_distaste(self):
        parsed = parse_en_pl(html["distaste"])
        cached = load_json("distaste")
        assert parsed == cached

    def test_parse_ecocide(self):
        parsed = parse_en_pl(html["ecocide"])
        cached = load_json("ecocide")
        assert parsed == cached

    def test_parse_conjugation(self):
        parsed = parse_en_pl(html["conjugation"])
        cached = load_json("conjugation")
        assert parsed == cached

    def test_parse_vicissitude(self):
        parsed = parse_en_pl(html["vicissitude"])
        cached = load_json("vicissitude")
        assert parsed == cached

    def test_parse_grouper(self):
        parsed = parse_en_pl(html["grouper"])
        cached = load_json("grouper")
        assert parsed == cached

    def test_parse_bespoke(self):
        parsed = parse_en_pl(html["bespoke"])
        cached = load_json("bespoke")
        assert parsed == cached

    def test_parse_protraction(self):
        parsed = parse_en_pl(html["protraction"])
        cached = load_json("protraction")
        assert parsed == cached

    def test_parse_aphasia(self):
        parsed = parse_en_pl(html["aphasia"])
        cached = load_json("aphasia")
        assert parsed == cached

    def test_parse_sluice(self):
        parsed = parse_en_pl(html["sluice"])
        cached = load_json("sluice")
        assert parsed == cached

    def test_parse_ivory(self):
        parsed = parse_en_pl(html["ivory"])
        cached = load_json("ivory")
        assert parsed == cached

    def test_parse_lichen(self):
        parsed = parse_en_pl(html["lichen"])
        cached = load_json("lichen")
        assert parsed == cached

    def test_parse_avon(self):
        parsed = parse_en_pl(html["avon"])
        cached = load_json("avon")
        assert parsed == cached

    def test_parse_conscientiousness(self):
        parsed = parse_en_pl(html["conscientiousness"])
        cached = load_json("conscientiousness")
        assert parsed == cached

    def test_parse_complex(self):
        parsed = parse_en_pl(html["complex"])
        cached = load_json("complex")
        assert parsed == cached

    def test_parse_pried(self):
        parsed = parse_en_pl(html["pried"])
        cached = load_json("pried")
        assert parsed == cached

    def test_parse_entail(self):
        parsed = parse_en_pl(html["entail"])
        cached = load_json("entail")
        assert parsed == cached

    def test_parse_unrepentant(self):
        parsed = parse_en_pl(html["unrepentant"])
        cached = load_json("unrepentant")
        assert parsed == cached

    def test_parse_plateau(self):
        parsed = parse_en_pl(html["plateau"])
        cached = load_json("plateau")
        assert parsed == cached

    def test_parse_pus(self):
        parsed = parse_en_pl(html["pus"])
        cached = load_json("pus")
        assert parsed == cached

    def test_parse_latent(self):
        parsed = parse_en_pl(html["latent"])
        cached = load_json("latent")
        assert parsed == cached

    def test_parse_vignette(self):
        parsed = parse_en_pl(html["vignette"])
        cached = load_json("vignette")
        assert parsed == cached

    def test_parse_tenet(self):
        parsed = parse_en_pl(html["tenet"])
        cached = load_json("tenet")
        assert parsed == cached

    def test_parse_sedition(self):
        parsed = parse_en_pl(html["sedition"])
        cached = load_json("sedition")
        assert parsed == cached

    def test_parse_snub(self):
        parsed = parse_en_pl(html["snub"])
        cached = load_json("snub")
        assert parsed == cached

    def test_parse_buoyant(self):
        parsed = parse_en_pl(html["buoyant"])
        cached = load_json("buoyant")
        assert parsed == cached

    def test_parse_pushy(self):
        parsed = parse_en_pl(html["pushy"])
        cached = load_json("pushy")
        assert parsed == cached

    def test_parse_walnut(self):
        parsed = parse_en_pl(html["walnut"])
        cached = load_json("walnut")
        assert parsed == cached

    def test_parse_stuffy(self):
        parsed = parse_en_pl(html["stuffy"])
        cached = load_json("stuffy")
        assert parsed == cached

    def test_parse_mace(self):
        parsed = parse_en_pl(html["mace"])
        cached = load_json("mace")
        assert parsed == cached

    def test_parse_perpetual(self):
        parsed = parse_en_pl(html["perpetual"])
        cached = load_json("perpetual")
        assert parsed == cached

    def test_parse_procurer(self):
        parsed = parse_en_pl(html["procurer"])
        cached = load_json("procurer")
        assert parsed == cached

    def test_parse_sander(self):
        parsed = parse_en_pl(html["sander"])
        cached = load_json("sander")
        assert parsed == cached

    def test_parse_assertive(self):
        parsed = parse_en_pl(html["assertive"])
        cached = load_json("assertive")
        assert parsed == cached

    def test_parse_wokeness(self):
        parsed = parse_en_pl(html["wokeness"])
        cached = load_json("wokeness")
        assert parsed == cached

    def test_parse_fluke(self):
        parsed = parse_en_pl(html["fluke"])
        cached = load_json("fluke")
        assert parsed == cached

    def test_parse_shrill(self):
        parsed = parse_en_pl(html["shrill"])
        cached = load_json("shrill")
        assert parsed == cached

    def test_parse_snubbed(self):
        parsed = parse_en_pl(html["snubbed"])
        cached = load_json("snubbed")
        assert parsed == cached

    def test_parse_orifice(self):
        parsed = parse_en_pl(html["orifice"])
        cached = load_json("orifice")
        assert parsed == cached

    def test_parse_ignoramus(self):
        parsed = parse_en_pl(html["ignoramus"])
        cached = load_json("ignoramus")
        assert parsed == cached

    def test_parse_remission(self):
        parsed = parse_en_pl(html["remission"])
        cached = load_json("remission")
        assert parsed == cached

    def test_parse_diligence(self):
        parsed = parse_en_pl(html["diligence"])
        cached = load_json("diligence")
        assert parsed == cached

    def test_parse_heredity(self):
        parsed = parse_en_pl(html["heredity"])
        cached = load_json("heredity")
        assert parsed == cached

    def test_parse_vertigo(self):
        parsed = parse_en_pl(html["vertigo"])
        cached = load_json("vertigo")
        assert parsed == cached

    def test_parse_vertebrate(self):
        parsed = parse_en_pl(html["vertebrate"])
        cached = load_json("vertebrate")
        assert parsed == cached

    def test_parse_pegboard(self):
        parsed = parse_en_pl(html["pegboard"])
        cached = load_json("pegboard")
        assert parsed == cached

    def test_parse_vainly(self):
        parsed = parse_en_pl(html["vainly"])
        cached = load_json("vainly")
        assert parsed == cached

    def test_parse_infringement(self):
        parsed = parse_en_pl(html["infringement"])
        cached = load_json("infringement")
        assert parsed == cached

    def test_parse_desolation(self):
        parsed = parse_en_pl(html["desolation"])
        cached = load_json("desolation")
        assert parsed == cached

    def test_parse_tend(self):
        parsed = parse_en_pl(html["tend"])
        cached = load_json("tend")
        assert parsed == cached

    def test_parse_adjourn(self):
        parsed = parse_en_pl(html["adjourn"])
        cached = load_json("adjourn")
        assert parsed == cached

    def test_parse_permeate(self):
        parsed = parse_en_pl(html["permeate"])
        cached = load_json("permeate")
        assert parsed == cached

    def test_parse_heft(self):
        parsed = parse_en_pl(html["heft"])
        cached = load_json("heft")
        assert parsed == cached

    def test_parse_utterance(self):
        parsed = parse_en_pl(html["utterance"])
        cached = load_json("utterance")
        assert parsed == cached

    def test_parse_careen(self):
        parsed = parse_en_pl(html["careen"])
        cached = load_json("careen")
        assert parsed == cached

    def test_parse_VAT(self):
        parsed = parse_en_pl(html["VAT"])
        cached = load_json("VAT")
        assert parsed == cached

    def test_parse_turnip(self):
        parsed = parse_en_pl(html["turnip"])
        cached = load_json("turnip")
        assert parsed == cached

    def test_parse_paragon(self):
        parsed = parse_en_pl(html["paragon"])
        cached = load_json("paragon")
        assert parsed == cached

    def test_parse_pecan(self):
        parsed = parse_en_pl(html["pecan"])
        cached = load_json("pecan")
        assert parsed == cached

    def test_parse_peruse(self):
        parsed = parse_en_pl(html["peruse"])
        cached = load_json("peruse")
        assert parsed == cached

    def test_parse_putty(self):
        parsed = parse_en_pl(html["putty"])
        cached = load_json("putty")
        assert parsed == cached

    def test_parse_cotton(self):
        parsed = parse_en_pl(html["cotton"])
        cached = load_json("cotton")
        assert parsed == cached

    def test_parse_fraternity(self):
        parsed = parse_en_pl(html["fraternity"])
        cached = load_json("fraternity")
        assert parsed == cached

    def test_parse_caldera(self):
        parsed = parse_en_pl(html["caldera"])
        cached = load_json("caldera")
        assert parsed == cached

    def test_parse_mellow(self):
        parsed = parse_en_pl(html["mellow"])
        cached = load_json("mellow")
        assert parsed == cached

    def test_parse_emasculate(self):
        parsed = parse_en_pl(html["emasculate"])
        cached = load_json("emasculate")
        assert parsed == cached

    def test_parse_stewardship(self):
        parsed = parse_en_pl(html["stewardship"])
        cached = load_json("stewardship")
        assert parsed == cached

    def test_parse_incontinence(self):
        parsed = parse_en_pl(html["incontinence"])
        cached = load_json("incontinence")
        assert parsed == cached

    def test_parse_gendarmerie(self):
        parsed = parse_en_pl(html["gendarmerie"])
        cached = load_json("gendarmerie")
        assert parsed == cached

    def test_parse_splurge(self):
        parsed = parse_en_pl(html["splurge"])
        cached = load_json("splurge")
        assert parsed == cached

    def test_parse_ebony(self):
        parsed = parse_en_pl(html["ebony"])
        cached = load_json("ebony")
        assert parsed == cached

    def test_parse_redeem(self):
        parsed = parse_en_pl(html["redeem"])
        cached = load_json("redeem")
        assert parsed == cached

    def test_parse_slut(self):
        parsed = parse_en_pl(html["slut"])
        cached = load_json("slut")
        assert parsed == cached

    def test_parse_invalidation(self):
        parsed = parse_en_pl(html["invalidation"])
        cached = load_json("invalidation")
        assert parsed == cached

    def test_parse_spoil(self):
        parsed = parse_en_pl(html["spoil"])
        cached = load_json("spoil")
        assert parsed == cached

    def test_parse_heinous(self):
        parsed = parse_en_pl(html["heinous"])
        cached = load_json("heinous")
        assert parsed == cached

    def test_parse_grazing(self):
        parsed = parse_en_pl(html["grazing"])
        cached = load_json("grazing")
        assert parsed == cached

    def test_parse_galore(self):
        parsed = parse_en_pl(html["galore"])
        cached = load_json("galore")
        assert parsed == cached

    def test_parse_brine(self):
        parsed = parse_en_pl(html["brine"])
        cached = load_json("brine")
        assert parsed == cached

    def test_parse_mirthless(self):
        parsed = parse_en_pl(html["mirthless"])
        cached = load_json("mirthless")
        assert parsed == cached

    def test_parse_fiefs(self):
        parsed = parse_en_pl(html["fiefs"])
        cached = load_json("fiefs")
        assert parsed == cached

    def test_parse_obstructive(self):
        parsed = parse_en_pl(html["obstructive"])
        cached = load_json("obstructive")
        assert parsed == cached

    def test_parse_ponderous(self):
        parsed = parse_en_pl(html["ponderous"])
        cached = load_json("ponderous")
        assert parsed == cached

    def test_parse_indispensable(self):
        parsed = parse_en_pl(html["indispensable"])
        cached = load_json("indispensable")
        assert parsed == cached

    def test_parse_sullen(self):
        parsed = parse_en_pl(html["sullen"])
        cached = load_json("sullen")
        assert parsed == cached

    def test_parse_prance(self):
        parsed = parse_en_pl(html["prance"])
        cached = load_json("prance")
        assert parsed == cached

    def test_parse_content(self):
        parsed = parse_en_pl(html["content"])
        cached = load_json("content")
        assert parsed == cached

    def test_parse_squander(self):
        parsed = parse_en_pl(html["squander"])
        cached = load_json("squander")
        assert parsed == cached

    def test_parse_bedridden(self):
        parsed = parse_en_pl(html["bedridden"])
        cached = load_json("bedridden")
        assert parsed == cached

    def test_parse_bore(self):
        parsed = parse_en_pl(html["bore"])
        cached = load_json("bore")
        assert parsed == cached

    def test_parse_pursuer(self):
        parsed = parse_en_pl(html["pursuer"])
        cached = load_json("pursuer")
        assert parsed == cached

    def test_parse_offspring(self):
        parsed = parse_en_pl(html["offspring"])
        cached = load_json("offspring")
        assert parsed == cached

    def test_parse_misfit(self):
        parsed = parse_en_pl(html["misfit"])
        cached = load_json("misfit")
        assert parsed == cached

    def test_parse_manacle(self):
        parsed = parse_en_pl(html["manacle"])
        cached = load_json("manacle")
        assert parsed == cached

    def test_parse_parochial(self):
        parsed = parse_en_pl(html["parochial"])
        cached = load_json("parochial")
        assert parsed == cached

    def test_parse_ribald(self):
        parsed = parse_en_pl(html["ribald"])
        cached = load_json("ribald")
        assert parsed == cached

    def test_parse_patronize(self):
        parsed = parse_en_pl(html["patronize"])
        cached = load_json("patronize")
        assert parsed == cached

    def test_parse_loaf(self):
        parsed = parse_en_pl(html["loaf"])
        cached = load_json("loaf")
        assert parsed == cached

    def test_parse_crevice(self):
        parsed = parse_en_pl(html["crevice"])
        cached = load_json("crevice")
        assert parsed == cached

    def test_parse_cow(self):
        parsed = parse_en_pl(html["cow"])
        cached = load_json("cow")
        assert parsed == cached

    def test_parse_cello(self):
        parsed = parse_en_pl(html["cello"])
        cached = load_json("cello")
        assert parsed == cached

    def test_parse_cuneiform(self):
        parsed = parse_en_pl(html["cuneiform"])
        cached = load_json("cuneiform")
        assert parsed == cached

    def test_parse_contort(self):
        parsed = parse_en_pl(html["contort"])
        cached = load_json("contort")
        assert parsed == cached

    def test_parse_prudent(self):
        parsed = parse_en_pl(html["prudent"])
        cached = load_json("prudent")
        assert parsed == cached

    def test_parse_riveting(self):
        parsed = parse_en_pl(html["riveting"])
        cached = load_json("riveting")
        assert parsed == cached

    def test_parse_wryly(self):
        parsed = parse_en_pl(html["wryly"])
        cached = load_json("wryly")
        assert parsed == cached

    def test_parse_protomartyr(self):
        parsed = parse_en_pl(html["protomartyr"])
        cached = load_json("protomartyr")
        assert parsed == cached

    def test_parse_taxidermist(self):
        parsed = parse_en_pl(html["taxidermist"])
        cached = load_json("taxidermist")
        assert parsed == cached

    def test_parse_addled(self):
        parsed = parse_en_pl(html["addled"])
        cached = load_json("addled")
        assert parsed == cached

    def test_parse_germinate(self):
        parsed = parse_en_pl(html["germinate"])
        cached = load_json("germinate")
        assert parsed == cached

    def test_parse_stipulate(self):
        parsed = parse_en_pl(html["stipulate"])
        cached = load_json("stipulate")
        assert parsed == cached

    def test_parse_anathema(self):
        parsed = parse_en_pl(html["anathema"])
        cached = load_json("anathema")
        assert parsed == cached

    def test_parse_feathered(self):
        parsed = parse_en_pl(html["feathered"])
        cached = load_json("feathered")
        assert parsed == cached

    def test_parse_rowan(self):
        parsed = parse_en_pl(html["rowan"])
        cached = load_json("rowan")
        assert parsed == cached

    def test_parse_rectifier(self):
        parsed = parse_en_pl(html["rectifier"])
        cached = load_json("rectifier")
        assert parsed == cached

    def test_parse_immediacy(self):
        parsed = parse_en_pl(html["immediacy"])
        cached = load_json("immediacy")
        assert parsed == cached

    def test_parse_batter(self):
        parsed = parse_en_pl(html["batter"])
        cached = load_json("batter")
        assert parsed == cached

    def test_parse_honky(self):
        parsed = parse_en_pl(html["honky"])
        cached = load_json("honky")
        assert parsed == cached

    def test_parse_ruthless(self):
        parsed = parse_en_pl(html["ruthless"])
        cached = load_json("ruthless")
        assert parsed == cached

    def test_parse_deliberation(self):
        parsed = parse_en_pl(html["deliberation"])
        cached = load_json("deliberation")
        assert parsed == cached

    def test_parse_squib(self):
        parsed = parse_en_pl(html["squib"])
        cached = load_json("squib")
        assert parsed == cached

    def test_parse_prophecy(self):
        parsed = parse_en_pl(html["prophecy"])
        cached = load_json("prophecy")
        assert parsed == cached

    def test_parse_slew(self):
        parsed = parse_en_pl(html["slew"])
        cached = load_json("slew")
        assert parsed == cached

    def test_parse_ravine(self):
        parsed = parse_en_pl(html["ravine"])
        cached = load_json("ravine")
        assert parsed == cached

    def test_parse_Levi(self):
        parsed = parse_en_pl(html["Levi"])
        cached = load_json("Levi")
        assert parsed == cached

    def test_parse_vapidity(self):
        parsed = parse_en_pl(html["vapidity"])
        cached = load_json("vapidity")
        assert parsed == cached

    def test_parse_stunt(self):
        parsed = parse_en_pl(html["stunt"])
        cached = load_json("stunt")
        assert parsed == cached

    def test_parse_inhibited(self):
        parsed = parse_en_pl(html["inhibited"])
        cached = load_json("inhibited")
        assert parsed == cached

    def test_parse_effusively(self):
        parsed = parse_en_pl(html["effusively"])
        cached = load_json("effusively")
        assert parsed == cached

    def test_parse_defer(self):
        parsed = parse_en_pl(html["defer"])
        cached = load_json("defer")
        assert parsed == cached

    def test_parse_coattail(self):
        parsed = parse_en_pl(html["coattail"])
        cached = load_json("coattail")
        assert parsed == cached

    def test_parse_incriminate(self):
        parsed = parse_en_pl(html["incriminate"])
        cached = load_json("incriminate")
        assert parsed == cached

    def test_parse_feast(self):
        parsed = parse_en_pl(html["feast"])
        cached = load_json("feast")
        assert parsed == cached

    def test_parse_heave(self):
        parsed = parse_en_pl(html["heave"])
        cached = load_json("heave")
        assert parsed == cached

    def test_parse_escalator(self):
        parsed = parse_en_pl(html["escalator"])
        cached = load_json("escalator")
        assert parsed == cached

    def test_parse_longshoreman(self):
        parsed = parse_en_pl(html["longshoreman"])
        cached = load_json("longshoreman")
        assert parsed == cached

    def test_parse_incinerate(self):
        parsed = parse_en_pl(html["incinerate"])
        cached = load_json("incinerate")
        assert parsed == cached

    def test_parse_glee(self):
        parsed = parse_en_pl(html["glee"])
        cached = load_json("glee")
        assert parsed == cached

    def test_parse_consign(self):
        parsed = parse_en_pl(html["consign"])
        cached = load_json("consign")
        assert parsed == cached

    def test_parse_coercion(self):
        parsed = parse_en_pl(html["coercion"])
        cached = load_json("coercion")
        assert parsed == cached

    def test_parse_procure(self):
        parsed = parse_en_pl(html["procure"])
        cached = load_json("procure")
        assert parsed == cached

    def test_parse_usher(self):
        parsed = parse_en_pl(html["usher"])
        cached = load_json("usher")
        assert parsed == cached

    def test_parse_protagonist(self):
        parsed = parse_en_pl(html["protagonist"])
        cached = load_json("protagonist")
        assert parsed == cached

    def test_parse_discernible(self):
        parsed = parse_en_pl(html["discernible"])
        cached = load_json("discernible")
        assert parsed == cached

    def test_parse_tropic(self):
        parsed = parse_en_pl(html["tropic"])
        cached = load_json("tropic")
        assert parsed == cached

    def test_parse_masonite(self):
        parsed = parse_en_pl(html["masonite"])
        cached = load_json("masonite")
        assert parsed == cached

    def test_parse_spun(self):
        parsed = parse_en_pl(html["spun"])
        cached = load_json("spun")
        assert parsed == cached

    def test_parse_penchant(self):
        parsed = parse_en_pl(html["penchant"])
        cached = load_json("penchant")
        assert parsed == cached

    def test_parse_sombre(self):
        parsed = parse_en_pl(html["sombre"])
        cached = load_json("sombre")
        assert parsed == cached

    def test_parse_graze(self):
        parsed = parse_en_pl(html["graze"])
        cached = load_json("graze")
        assert parsed == cached

    def test_parse_reeling(self):
        parsed = parse_en_pl(html["reeling"])
        cached = load_json("reeling")
        assert parsed == cached

    def test_parse_plaid(self):
        parsed = parse_en_pl(html["plaid"])
        cached = load_json("plaid")
        assert parsed == cached

    def test_parse_conscience(self):
        parsed = parse_en_pl(html["conscience"])
        cached = load_json("conscience")
        assert parsed == cached

    def test_parse_kindred(self):
        parsed = parse_en_pl(html["kindred"])
        cached = load_json("kindred")
        assert parsed == cached

    def test_parse_flatulence(self):
        parsed = parse_en_pl(html["flatulence"])
        cached = load_json("flatulence")
        assert parsed == cached

    def test_parse_adherent(self):
        parsed = parse_en_pl(html["adherent"])
        cached = load_json("adherent")
        assert parsed == cached

    def test_parse_sacrosanct(self):
        parsed = parse_en_pl(html["sacrosanct"])
        cached = load_json("sacrosanct")
        assert parsed == cached

    def test_parse_heartburn(self):
        parsed = parse_en_pl(html["heartburn"])
        cached = load_json("heartburn")
        assert parsed == cached

    def test_parse_arduous(self):
        parsed = parse_en_pl(html["arduous"])
        cached = load_json("arduous")
        assert parsed == cached

    def test_parse_specter(self):
        parsed = parse_en_pl(html["specter"])
        cached = load_json("specter")
        assert parsed == cached

    def test_parse_pretence(self):
        parsed = parse_en_pl(html["pretence"])
        cached = load_json("pretence")
        assert parsed == cached

    def test_parse_vain(self):
        parsed = parse_en_pl(html["vain"])
        cached = load_json("vain")
        assert parsed == cached

    def test_parse_permeable(self):
        parsed = parse_en_pl(html["permeable"])
        cached = load_json("permeable")
        assert parsed == cached

    def test_parse_rambunctious(self):
        parsed = parse_en_pl(html["rambunctious"])
        cached = load_json("rambunctious")
        assert parsed == cached

    def test_parse_emaciate(self):
        parsed = parse_en_pl(html["emaciate"])
        cached = load_json("emaciate")
        assert parsed == cached

    def test_parse_impediment(self):
        parsed = parse_en_pl(html["impediment"])
        cached = load_json("impediment")
        assert parsed == cached

    def test_parse_salience(self):
        parsed = parse_en_pl(html["salience"])
        cached = load_json("salience")
        assert parsed == cached

    def test_parse_klutzy(self):
        parsed = parse_en_pl(html["klutzy"])
        cached = load_json("klutzy")
        assert parsed == cached

    def test_parse_disclosure(self):
        parsed = parse_en_pl(html["disclosure"])
        cached = load_json("disclosure")
        assert parsed == cached

    def test_parse_arid(self):
        parsed = parse_en_pl(html["arid"])
        cached = load_json("arid")
        assert parsed == cached

    def test_parse_philander(self):
        parsed = parse_en_pl(html["philander"])
        cached = load_json("philander")
        assert parsed == cached

    def test_parse_tidbit(self):
        parsed = parse_en_pl(html["tidbit"])
        cached = load_json("tidbit")
        assert parsed == cached

    def test_parse_jostle(self):
        parsed = parse_en_pl(html["jostle"])
        cached = load_json("jostle")
        assert parsed == cached

    def test_parse_concord(self):
        parsed = parse_en_pl(html["concord"])
        cached = load_json("concord")
        assert parsed == cached

    def test_parse_residue(self):
        parsed = parse_en_pl(html["residue"])
        cached = load_json("residue")
        assert parsed == cached

    def test_parse_tumultuous(self):
        parsed = parse_en_pl(html["tumultuous"])
        cached = load_json("tumultuous")
        assert parsed == cached

    def test_parse_translucent(self):
        parsed = parse_en_pl(html["translucent"])
        cached = load_json("translucent")
        assert parsed == cached

    def test_parse_cooties(self):
        parsed = parse_en_pl(html["cooties"])
        cached = load_json("cooties")
        assert parsed == cached

    def test_parse_underlining(self):
        parsed = parse_en_pl(html["underlining"])
        cached = load_json("underlining")
        assert parsed == cached

    def test_parse_sog(self):
        parsed = parse_en_pl(html["sog"])
        cached = load_json("sog")
        assert parsed == cached

    def test_parse_moose(self):
        parsed = parse_en_pl(html["moose"])
        cached = load_json("moose")
        assert parsed == cached

    def test_parse_eke(self):
        parsed = parse_en_pl(html["eke"])
        cached = load_json("eke")
        assert parsed == cached

    def test_parse_hoggish(self):
        parsed = parse_en_pl(html["hoggish"])
        cached = load_json("hoggish")
        assert parsed == cached

    def test_parse_chafing(self):
        parsed = parse_en_pl(html["chafing"])
        cached = load_json("chafing")
        assert parsed == cached

    def test_parse_admonish(self):
        parsed = parse_en_pl(html["admonish"])
        cached = load_json("admonish")
        assert parsed == cached

    def test_parse_nitpick(self):
        parsed = parse_en_pl(html["nitpick"])
        cached = load_json("nitpick")
        assert parsed == cached

    def test_parse_clamp(self):
        parsed = parse_en_pl(html["clamp"])
        cached = load_json("clamp")
        assert parsed == cached

    def test_parse_usufruct(self):
        parsed = parse_en_pl(html["usufruct"])
        cached = load_json("usufruct")
        assert parsed == cached

    def test_parse_tuple(self):
        parsed = parse_en_pl(html["tuple"])
        cached = load_json("tuple")
        assert parsed == cached

    def test_parse_volatile(self):
        parsed = parse_en_pl(html["volatile"])
        cached = load_json("volatile")
        assert parsed == cached

    def test_parse_shrink(self):
        parsed = parse_en_pl(html["shrink"])
        cached = load_json("shrink")
        assert parsed == cached

    def test_parse_cleavage(self):
        parsed = parse_en_pl(html["cleavage"])
        cached = load_json("cleavage")
        assert parsed == cached

    def test_parse_dint(self):
        parsed = parse_en_pl(html["dint"])
        cached = load_json("dint")
        assert parsed == cached

    def test_parse_reckon(self):
        parsed = parse_en_pl(html["reckon"])
        cached = load_json("reckon")
        assert parsed == cached

    def test_parse_nausea(self):
        parsed = parse_en_pl(html["nausea"])
        cached = load_json("nausea")
        assert parsed == cached

    def test_parse_vixen(self):
        parsed = parse_en_pl(html["vixen"])
        cached = load_json("vixen")
        assert parsed == cached

    def test_parse_goop(self):
        parsed = parse_en_pl(html["goop"])
        cached = load_json("goop")
        assert parsed == cached

    def test_parse_strident(self):
        parsed = parse_en_pl(html["strident"])
        cached = load_json("strident")
        assert parsed == cached

    def test_parse_server(self):
        parsed = parse_en_pl(html["server"])
        cached = load_json("server")
        assert parsed == cached

    def test_parse_pebble(self):
        parsed = parse_en_pl(html["pebble"])
        cached = load_json("pebble")
        assert parsed == cached

    def test_parse_turtle(self):
        parsed = parse_en_pl(html["turtle"])
        cached = load_json("turtle")
        assert parsed == cached

    def test_parse_shard(self):
        parsed = parse_en_pl(html["shard"])
        cached = load_json("shard")
        assert parsed == cached

    def test_parse_smear(self):
        parsed = parse_en_pl(html["smear"])
        cached = load_json("smear")
        assert parsed == cached

    def test_parse_deterministic(self):
        parsed = parse_en_pl(html["deterministic"])
        cached = load_json("deterministic")
        assert parsed == cached

    def test_parse_chump(self):
        parsed = parse_en_pl(html["chump"])
        cached = load_json("chump")
        assert parsed == cached

    def test_parse_mortician(self):
        parsed = parse_en_pl(html["mortician"])
        cached = load_json("mortician")
        assert parsed == cached

    def test_parse_penance(self):
        parsed = parse_en_pl(html["penance"])
        cached = load_json("penance")
        assert parsed == cached

    def test_parse_placid(self):
        parsed = parse_en_pl(html["placid"])
        cached = load_json("placid")
        assert parsed == cached

    def test_parse_maven(self):
        parsed = parse_en_pl(html["maven"])
        cached = load_json("maven")
        assert parsed == cached

    def test_parse_pertinent(self):
        parsed = parse_en_pl(html["pertinent"])
        cached = load_json("pertinent")
        assert parsed == cached

    def test_parse_cornucopia(self):
        parsed = parse_en_pl(html["cornucopia"])
        cached = load_json("cornucopia")
        assert parsed == cached

    def test_parse_static(self):
        parsed = parse_en_pl(html["static"])
        cached = load_json("static")
        assert parsed == cached

    def test_parse_unmoored(self):
        parsed = parse_en_pl(html["unmoored"])
        cached = load_json("unmoored")
        assert parsed == cached

    def test_parse_larch(self):
        parsed = parse_en_pl(html["larch"])
        cached = load_json("larch")
        assert parsed == cached

    def test_parse_blistering(self):
        parsed = parse_en_pl(html["blistering"])
        cached = load_json("blistering")
        assert parsed == cached

    def test_parse_stride(self):
        parsed = parse_en_pl(html["stride"])
        cached = load_json("stride")
        assert parsed == cached

    def test_parse_nutmeg(self):
        parsed = parse_en_pl(html["nutmeg"])
        cached = load_json("nutmeg")
        assert parsed == cached

    def test_parse_posit(self):
        parsed = parse_en_pl(html["posit"])
        cached = load_json("posit")
        assert parsed == cached

    def test_parse_charter(self):
        parsed = parse_en_pl(html["charter"])
        cached = load_json("charter")
        assert parsed == cached

    def test_parse_oblivious(self):
        parsed = parse_en_pl(html["oblivious"])
        cached = load_json("oblivious")
        assert parsed == cached

    def test_parse_schist(self):
        parsed = parse_en_pl(html["schist"])
        cached = load_json("schist")
        assert parsed == cached

    def test_parse_predilection(self):
        parsed = parse_en_pl(html["predilection"])
        cached = load_json("predilection")
        assert parsed == cached

    def test_parse_solace(self):
        parsed = parse_en_pl(html["solace"])
        cached = load_json("solace")
        assert parsed == cached

    def test_parse_vaunt(self):
        parsed = parse_en_pl(html["vaunt"])
        cached = load_json("vaunt")
        assert parsed == cached

    def test_parse_pulchritude(self):
        parsed = parse_en_pl(html["pulchritude"])
        cached = load_json("pulchritude")
        assert parsed == cached

    def test_parse_cheapening(self):
        parsed = parse_en_pl(html["cheapening"])
        cached = load_json("cheapening")
        assert parsed == cached

    def test_parse_impalpable(self):
        parsed = parse_en_pl(html["impalpable"])
        cached = load_json("impalpable")
        assert parsed == cached

    def test_parse_severe(self):
        parsed = parse_en_pl(html["severe"])
        cached = load_json("severe")
        assert parsed == cached

    def test_parse_contingent(self):
        parsed = parse_en_pl(html["contingent"])
        cached = load_json("contingent")
        assert parsed == cached

    def test_parse_falter(self):
        parsed = parse_en_pl(html["falter"])
        cached = load_json("falter")
        assert parsed == cached

    def test_parse_swirl(self):
        parsed = parse_en_pl(html["swirl"])
        cached = load_json("swirl")
        assert parsed == cached

    def test_parse_cratering(self):
        parsed = parse_en_pl(html["cratering"])
        cached = load_json("cratering")
        assert parsed == cached

    def test_parse_industrious(self):
        parsed = parse_en_pl(html["industrious"])
        cached = load_json("industrious")
        assert parsed == cached

    def test_parse_crass(self):
        parsed = parse_en_pl(html["crass"])
        cached = load_json("crass")
        assert parsed == cached

    def test_parse_quibble(self):
        parsed = parse_en_pl(html["quibble"])
        cached = load_json("quibble")
        assert parsed == cached

    def test_parse_lacerate(self):
        parsed = parse_en_pl(html["lacerate"])
        cached = load_json("lacerate")
        assert parsed == cached

    def test_parse_arrear(self):
        parsed = parse_en_pl(html["arrear"])
        cached = load_json("arrear")
        assert parsed == cached

    def test_parse_wariness(self):
        parsed = parse_en_pl(html["wariness"])
        cached = load_json("wariness")
        assert parsed == cached

    def test_parse_parable(self):
        parsed = parse_en_pl(html["parable"])
        cached = load_json("parable")
        assert parsed == cached

    def test_parse_congenial(self):
        parsed = parse_en_pl(html["congenial"])
        cached = load_json("congenial")
        assert parsed == cached

    def test_parse_pusillanimity(self):
        parsed = parse_en_pl(html["pusillanimity"])
        cached = load_json("pusillanimity")
        assert parsed == cached

    def test_parse_grizzled(self):
        parsed = parse_en_pl(html["grizzled"])
        cached = load_json("grizzled")
        assert parsed == cached

    def test_parse_endorsement(self):
        parsed = parse_en_pl(html["endorsement"])
        cached = load_json("endorsement")
        assert parsed == cached

    def test_parse_upsell(self):
        parsed = parse_en_pl(html["upsell"])
        cached = load_json("upsell")
        assert parsed == cached

    def test_parse_blackened(self):
        parsed = parse_en_pl(html["blackened"])
        cached = load_json("blackened")
        assert parsed == cached

    def test_parse_sizzle(self):
        parsed = parse_en_pl(html["sizzle"])
        cached = load_json("sizzle")
        assert parsed == cached

    def test_parse_hawthorn(self):
        parsed = parse_en_pl(html["hawthorn"])
        cached = load_json("hawthorn")
        assert parsed == cached

    def test_parse_lotion(self):
        parsed = parse_en_pl(html["lotion"])
        cached = load_json("lotion")
        assert parsed == cached

    def test_parse_macaw(self):
        parsed = parse_en_pl(html["macaw"])
        cached = load_json("macaw")
        assert parsed == cached

    def test_parse_reprieve(self):
        parsed = parse_en_pl(html["reprieve"])
        cached = load_json("reprieve")
        assert parsed == cached

    def test_parse_gust(self):
        parsed = parse_en_pl(html["gust"])
        cached = load_json("gust")
        assert parsed == cached

    def test_parse_shank(self):
        parsed = parse_en_pl(html["shank"])
        cached = load_json("shank")
        assert parsed == cached

    def test_parse_bramble(self):
        parsed = parse_en_pl(html["bramble"])
        cached = load_json("bramble")
        assert parsed == cached

    def test_parse_corvid(self):
        parsed = parse_en_pl(html["corvid"])
        cached = load_json("corvid")
        assert parsed == cached

    def test_parse_stud(self):
        parsed = parse_en_pl(html["stud"])
        cached = load_json("stud")
        assert parsed == cached

    def test_parse_ceaselessly(self):
        parsed = parse_en_pl(html["ceaselessly"])
        cached = load_json("ceaselessly")
        assert parsed == cached

    def test_parse_crayfish(self):
        parsed = parse_en_pl(html["crayfish"])
        cached = load_json("crayfish")
        assert parsed == cached

    def test_parse_stern(self):
        parsed = parse_en_pl(html["stern"])
        cached = load_json("stern")
        assert parsed == cached

    def test_parse_sapient(self):
        parsed = parse_en_pl(html["sapient"])
        cached = load_json("sapient")
        assert parsed == cached

    def test_parse_arresting(self):
        parsed = parse_en_pl(html["arresting"])
        cached = load_json("arresting")
        assert parsed == cached

    def test_parse_tentatively(self):
        parsed = parse_en_pl(html["tentatively"])
        cached = load_json("tentatively")
        assert parsed == cached

    def test_parse_retain(self):
        parsed = parse_en_pl(html["retain"])
        cached = load_json("retain")
        assert parsed == cached

    def test_parse_posterity(self):
        parsed = parse_en_pl(html["posterity"])
        cached = load_json("posterity")
        assert parsed == cached

    def test_parse_lacklustre(self):
        parsed = parse_en_pl(html["lacklustre"])
        cached = load_json("lacklustre")
        assert parsed == cached

    def test_parse_grungy(self):
        parsed = parse_en_pl(html["grungy"])
        cached = load_json("grungy")
        assert parsed == cached

    def test_parse_establish(self):
        parsed = parse_en_pl(html["establish"])
        cached = load_json("establish")
        assert parsed == cached

    def test_parse_asinine(self):
        parsed = parse_en_pl(html["asinine"])
        cached = load_json("asinine")
        assert parsed == cached

    def test_parse_interdiction(self):
        parsed = parse_en_pl(html["interdiction"])
        cached = load_json("interdiction")
        assert parsed == cached

    def test_parse_clemency(self):
        parsed = parse_en_pl(html["clemency"])
        cached = load_json("clemency")
        assert parsed == cached

    def test_parse_circumvent(self):
        parsed = parse_en_pl(html["circumvent"])
        cached = load_json("circumvent")
        assert parsed == cached

    def test_parse_lark(self):
        parsed = parse_en_pl(html["lark"])
        cached = load_json("lark")
        assert parsed == cached

    def test_parse_adenoids(self):
        parsed = parse_en_pl(html["adenoids"])
        cached = load_json("adenoids")
        assert parsed == cached

    def test_parse_veracity(self):
        parsed = parse_en_pl(html["veracity"])
        cached = load_json("veracity")
        assert parsed == cached

    def test_parse_effuse(self):
        parsed = parse_en_pl(html["effuse"])
        cached = load_json("effuse")
        assert parsed == cached

    def test_parse_panache(self):
        parsed = parse_en_pl(html["panache"])
        cached = load_json("panache")
        assert parsed == cached

    def test_parse_isthmus(self):
        parsed = parse_en_pl(html["isthmus"])
        cached = load_json("isthmus")
        assert parsed == cached

    def test_parse_gestation(self):
        parsed = parse_en_pl(html["gestation"])
        cached = load_json("gestation")
        assert parsed == cached

    def test_parse_quinine(self):
        parsed = parse_en_pl(html["quinine"])
        cached = load_json("quinine")
        assert parsed == cached

    def test_parse_jugular(self):
        parsed = parse_en_pl(html["jugular"])
        cached = load_json("jugular")
        assert parsed == cached

    def test_parse_exuberant(self):
        parsed = parse_en_pl(html["exuberant"])
        cached = load_json("exuberant")
        assert parsed == cached

    def test_parse_pastry(self):
        parsed = parse_en_pl(html["pastry"])
        cached = load_json("pastry")
        assert parsed == cached

    def test_parse_rapscallion(self):
        parsed = parse_en_pl(html["rapscallion"])
        cached = load_json("rapscallion")
        assert parsed == cached

    def test_parse_exonym(self):
        parsed = parse_en_pl(html["exonym"])
        cached = load_json("exonym")
        assert parsed == cached

    def test_parse_ensconce(self):
        parsed = parse_en_pl(html["ensconce"])
        cached = load_json("ensconce")
        assert parsed == cached

    def test_parse_coherence(self):
        parsed = parse_en_pl(html["coherence"])
        cached = load_json("coherence")
        assert parsed == cached

    def test_parse_poised(self):
        parsed = parse_en_pl(html["poised"])
        cached = load_json("poised")
        assert parsed == cached

    def test_parse_pls(self):
        parsed = parse_en_pl(html["pls"])
        cached = load_json("pls")
        assert parsed == cached

    def test_parse_quirky(self):
        parsed = parse_en_pl(html["quirky"])
        cached = load_json("quirky")
        assert parsed == cached

    def test_parse_hopefully(self):
        parsed = parse_en_pl(html["hopefully"])
        cached = load_json("hopefully")
        assert parsed == cached

    def test_parse_mantle(self):
        parsed = parse_en_pl(html["mantle"])
        cached = load_json("mantle")
        assert parsed == cached

    def test_parse_tribulation(self):
        parsed = parse_en_pl(html["tribulation"])
        cached = load_json("tribulation")
        assert parsed == cached

    def test_parse_to(self):
        parsed = parse_en_pl(html["to"])
        cached = load_json("to")
        assert parsed == cached

    def test_parse_knoll(self):
        parsed = parse_en_pl(html["knoll"])
        cached = load_json("knoll")
        assert parsed == cached

    def test_parse_abhor(self):
        parsed = parse_en_pl(html["abhor"])
        cached = load_json("abhor")
        assert parsed == cached

    def test_parse_illegitimacy(self):
        parsed = parse_en_pl(html["illegitimacy"])
        cached = load_json("illegitimacy")
        assert parsed == cached

    def test_parse_juxtaposition(self):
        parsed = parse_en_pl(html["juxtaposition"])
        cached = load_json("juxtaposition")
        assert parsed == cached

    def test_parse_shag(self):
        parsed = parse_en_pl(html["shag"])
        cached = load_json("shag")
        assert parsed == cached

    def test_parse_immersion(self):
        parsed = parse_en_pl(html["immersion"])
        cached = load_json("immersion")
        assert parsed == cached

    def test_parse_tactile(self):
        parsed = parse_en_pl(html["tactile"])
        cached = load_json("tactile")
        assert parsed == cached

    def test_parse_haphazardly(self):
        parsed = parse_en_pl(html["haphazardly"])
        cached = load_json("haphazardly")
        assert parsed == cached

    def test_parse_turf(self):
        parsed = parse_en_pl(html["turf"])
        cached = load_json("turf")
        assert parsed == cached

    def test_parse_basswood(self):
        parsed = parse_en_pl(html["basswood"])
        cached = load_json("basswood")
        assert parsed == cached

    def test_parse_rowdy(self):
        parsed = parse_en_pl(html["rowdy"])
        cached = load_json("rowdy")
        assert parsed == cached

    def test_parse_outwardly(self):
        parsed = parse_en_pl(html["outwardly"])
        cached = load_json("outwardly")
        assert parsed == cached

    def test_parse_credible(self):
        parsed = parse_en_pl(html["credible"])
        cached = load_json("credible")
        assert parsed == cached

    def test_parse_fawning(self):
        parsed = parse_en_pl(html["fawning"])
        cached = load_json("fawning")
        assert parsed == cached

    def test_parse_closure(self):
        parsed = parse_en_pl(html["closure"])
        cached = load_json("closure")
        assert parsed == cached

    def test_parse_duplicitous(self):
        parsed = parse_en_pl(html["duplicitous"])
        cached = load_json("duplicitous")
        assert parsed == cached

    def test_parse_scald(self):
        parsed = parse_en_pl(html["scald"])
        cached = load_json("scald")
        assert parsed == cached

    def test_parse_disparate(self):
        parsed = parse_en_pl(html["disparate"])
        cached = load_json("disparate")
        assert parsed == cached

    def test_parse_endow(self):
        parsed = parse_en_pl(html["endow"])
        cached = load_json("endow")
        assert parsed == cached

    def test_parse_weasel(self):
        parsed = parse_en_pl(html["weasel"])
        cached = load_json("weasel")
        assert parsed == cached

    def test_parse_gravitas(self):
        parsed = parse_en_pl(html["gravitas"])
        cached = load_json("gravitas")
        assert parsed == cached

    def test_parse_casket(self):
        parsed = parse_en_pl(html["casket"])
        cached = load_json("casket")
        assert parsed == cached

    def test_parse_omniscient(self):
        parsed = parse_en_pl(html["omniscient"])
        cached = load_json("omniscient")
        assert parsed == cached

    def test_parse_rag(self):
        parsed = parse_en_pl(html["rag"])
        cached = load_json("rag")
        assert parsed == cached

    def test_parse_rod(self):
        parsed = parse_en_pl(html["rod"])
        cached = load_json("rod")
        assert parsed == cached

    def test_parse_suckle(self):
        parsed = parse_en_pl(html["suckle"])
        cached = load_json("suckle")
        assert parsed == cached

    def test_parse_oxblood(self):
        parsed = parse_en_pl(html["oxblood"])
        cached = load_json("oxblood")
        assert parsed == cached

    def test_parse_peckish(self):
        parsed = parse_en_pl(html["peckish"])
        cached = load_json("peckish")
        assert parsed == cached

    def test_parse_tableau(self):
        parsed = parse_en_pl(html["tableau"])
        cached = load_json("tableau")
        assert parsed == cached

    def test_parse_attrition(self):
        parsed = parse_en_pl(html["attrition"])
        cached = load_json("attrition")
        assert parsed == cached

    def test_parse_brawler(self):
        parsed = parse_en_pl(html["brawler"])
        cached = load_json("brawler")
        assert parsed == cached

    def test_parse_aggrieved(self):
        parsed = parse_en_pl(html["aggrieved"])
        cached = load_json("aggrieved")
        assert parsed == cached

    def test_parse_shawty(self):
        parsed = parse_en_pl(html["shawty"])
        cached = load_json("shawty")
        assert parsed == cached

    def test_parse_foible(self):
        parsed = parse_en_pl(html["foible"])
        cached = load_json("foible")
        assert parsed == cached

    def test_parse_slant(self):
        parsed = parse_en_pl(html["slant"])
        cached = load_json("slant")
        assert parsed == cached

    def test_parse_deer(self):
        parsed = parse_en_pl(html["deer"])
        cached = load_json("deer")
        assert parsed == cached

    def test_parse_flamboyant(self):
        parsed = parse_en_pl(html["flamboyant"])
        cached = load_json("flamboyant")
        assert parsed == cached

    def test_parse_pat(self):
        parsed = parse_en_pl(html["pat"])
        cached = load_json("pat")
        assert parsed == cached

    def test_parse_vine(self):
        parsed = parse_en_pl(html["vine"])
        cached = load_json("vine")
        assert parsed == cached

    def test_parse_iridescent(self):
        parsed = parse_en_pl(html["iridescent"])
        cached = load_json("iridescent")
        assert parsed == cached

    def test_parse_glean(self):
        parsed = parse_en_pl(html["glean"])
        cached = load_json("glean")
        assert parsed == cached

    def test_parse_dope(self):
        parsed = parse_en_pl(html["dope"])
        cached = load_json("dope")
        assert parsed == cached

    def test_parse_wanton(self):
        parsed = parse_en_pl(html["wanton"])
        cached = load_json("wanton")
        assert parsed == cached

    def test_parse_uppity(self):
        parsed = parse_en_pl(html["uppity"])
        cached = load_json("uppity")
        assert parsed == cached

    def test_parse_composure(self):
        parsed = parse_en_pl(html["composure"])
        cached = load_json("composure")
        assert parsed == cached

    def test_parse_pabulum(self):
        parsed = parse_en_pl(html["pabulum"])
        cached = load_json("pabulum")
        assert parsed == cached

    def test_parse_unremarkable(self):
        parsed = parse_en_pl(html["unremarkable"])
        cached = load_json("unremarkable")
        assert parsed == cached

    def test_parse_clark(self):
        parsed = parse_en_pl(html["clark"])
        cached = load_json("clark")
        assert parsed == cached

    def test_parse_bosom(self):
        parsed = parse_en_pl(html["bosom"])
        cached = load_json("bosom")
        assert parsed == cached

    def test_parse_discrete(self):
        parsed = parse_en_pl(html["discrete"])
        cached = load_json("discrete")
        assert parsed == cached

    def test_parse_sleet(self):
        parsed = parse_en_pl(html["sleet"])
        cached = load_json("sleet")
        assert parsed == cached

    def test_parse_rarefaction(self):
        parsed = parse_en_pl(html["rarefaction"])
        cached = load_json("rarefaction")
        assert parsed == cached

    def test_parse_hubcap(self):
        parsed = parse_en_pl(html["hubcap"])
        cached = load_json("hubcap")
        assert parsed == cached

    def test_parse_tatters(self):
        parsed = parse_en_pl(html["tatters"])
        cached = load_json("tatters")
        assert parsed == cached

    def test_parse_tack(self):
        parsed = parse_en_pl(html["tack"])
        cached = load_json("tack")
        assert parsed == cached

    def test_parse_crumpet(self):
        parsed = parse_en_pl(html["crumpet"])
        cached = load_json("crumpet")
        assert parsed == cached

    def test_parse_bawl(self):
        parsed = parse_en_pl(html["bawl"])
        cached = load_json("bawl")
        assert parsed == cached

    def test_parse_funnel(self):
        parsed = parse_en_pl(html["funnel"])
        cached = load_json("funnel")
        assert parsed == cached

    def test_parse_wail(self):
        parsed = parse_en_pl(html["wail"])
        cached = load_json("wail")
        assert parsed == cached

    def test_parse_leisure(self):
        parsed = parse_en_pl(html["leisure"])
        cached = load_json("leisure")
        assert parsed == cached

    def test_parse_rolodex(self):
        parsed = parse_en_pl(html["rolodex"])
        cached = load_json("rolodex")
        assert parsed == cached

    def test_parse_cupola(self):
        parsed = parse_en_pl(html["cupola"])
        cached = load_json("cupola")
        assert parsed == cached

    def test_parse_eczema(self):
        parsed = parse_en_pl(html["eczema"])
        cached = load_json("eczema")
        assert parsed == cached

    def test_parse_festoon(self):
        parsed = parse_en_pl(html["festoon"])
        cached = load_json("festoon")
        assert parsed == cached

    def test_parse_drivel(self):
        parsed = parse_en_pl(html["drivel"])
        cached = load_json("drivel")
        assert parsed == cached

    def test_parse_vicinity(self):
        parsed = parse_en_pl(html["vicinity"])
        cached = load_json("vicinity")
        assert parsed == cached

    def test_parse_starlight(self):
        parsed = parse_en_pl(html["starlight"])
        cached = load_json("starlight")
        assert parsed == cached

    def test_parse_decimate(self):
        parsed = parse_en_pl(html["decimate"])
        cached = load_json("decimate")
        assert parsed == cached

    def test_parse_astonished(self):
        parsed = parse_en_pl(html["astonished"])
        cached = load_json("astonished")
        assert parsed == cached

    def test_parse_impugning(self):
        parsed = parse_en_pl(html["impugning"])
        cached = load_json("impugning")
        assert parsed == cached

    def test_parse_stew(self):
        parsed = parse_en_pl(html["stew"])
        cached = load_json("stew")
        assert parsed == cached

    def test_parse_sensibly(self):
        parsed = parse_en_pl(html["sensibly"])
        cached = load_json("sensibly")
        assert parsed == cached

    def test_parse_dengue(self):
        parsed = parse_en_pl(html["dengue"])
        cached = load_json("dengue")
        assert parsed == cached

    def test_parse_convent(self):
        parsed = parse_en_pl(html["convent"])
        cached = load_json("convent")
        assert parsed == cached

    def test_parse_mendacious(self):
        parsed = parse_en_pl(html["mendacious"])
        cached = load_json("mendacious")
        assert parsed == cached

    def test_parse_allotment(self):
        parsed = parse_en_pl(html["allotment"])
        cached = load_json("allotment")
        assert parsed == cached

    def test_parse_bicentennial(self):
        parsed = parse_en_pl(html["bicentennial"])
        cached = load_json("bicentennial")
        assert parsed == cached

    def test_parse_astute(self):
        parsed = parse_en_pl(html["astute"])
        cached = load_json("astute")
        assert parsed == cached

    def test_parse_treacly(self):
        parsed = parse_en_pl(html["treacly"])
        cached = load_json("treacly")
        assert parsed == cached

    def test_parse_edification(self):
        parsed = parse_en_pl(html["edification"])
        cached = load_json("edification")
        assert parsed == cached

    def test_parse_ail(self):
        parsed = parse_en_pl(html["ail"])
        cached = load_json("ail")
        assert parsed == cached

    def test_parse_tally(self):
        parsed = parse_en_pl(html["tally"])
        cached = load_json("tally")
        assert parsed == cached

    def test_parse_cordial(self):
        parsed = parse_en_pl(html["cordial"])
        cached = load_json("cordial")
        assert parsed == cached

    def test_parse_racoon(self):
        parsed = parse_en_pl(html["racoon"])
        cached = load_json("racoon")
        assert parsed == cached

    def test_parse_tepid(self):
        parsed = parse_en_pl(html["tepid"])
        cached = load_json("tepid")
        assert parsed == cached

    def test_parse_detriment(self):
        parsed = parse_en_pl(html["detriment"])
        cached = load_json("detriment")
        assert parsed == cached

    def test_parse_mercurial(self):
        parsed = parse_en_pl(html["mercurial"])
        cached = load_json("mercurial")
        assert parsed == cached

    def test_parse_timbre(self):
        parsed = parse_en_pl(html["timbre"])
        cached = load_json("timbre")
        assert parsed == cached

    def test_parse_appalling(self):
        parsed = parse_en_pl(html["appalling"])
        cached = load_json("appalling")
        assert parsed == cached

    def test_parse_bewilderment(self):
        parsed = parse_en_pl(html["bewilderment"])
        cached = load_json("bewilderment")
        assert parsed == cached

    def test_parse_livid(self):
        parsed = parse_en_pl(html["livid"])
        cached = load_json("livid")
        assert parsed == cached

    def test_parse_wailing(self):
        parsed = parse_en_pl(html["wailing"])
        cached = load_json("wailing")
        assert parsed == cached

    def test_parse_devious(self):
        parsed = parse_en_pl(html["devious"])
        cached = load_json("devious")
        assert parsed == cached

    def test_parse_axiom(self):
        parsed = parse_en_pl(html["axiom"])
        cached = load_json("axiom")
        assert parsed == cached

    def test_parse_tarp(self):
        parsed = parse_en_pl(html["tarp"])
        cached = load_json("tarp")
        assert parsed == cached

    def test_parse_tacitly(self):
        parsed = parse_en_pl(html["tacitly"])
        cached = load_json("tacitly")
        assert parsed == cached

    def test_parse_tug(self):
        parsed = parse_en_pl(html["tug"])
        cached = load_json("tug")
        assert parsed == cached

    def test_parse_scrappy(self):
        parsed = parse_en_pl(html["scrappy"])
        cached = load_json("scrappy")
        assert parsed == cached

    def test_parse_payoff(self):
        parsed = parse_en_pl(html["payoff"])
        cached = load_json("payoff")
        assert parsed == cached

    def test_parse_animosity(self):
        parsed = parse_en_pl(html["animosity"])
        cached = load_json("animosity")
        assert parsed == cached

    def test_parse_lupine(self):
        parsed = parse_en_pl(html["lupine"])
        cached = load_json("lupine")
        assert parsed == cached

    def test_parse_asunder(self):
        parsed = parse_en_pl(html["asunder"])
        cached = load_json("asunder")
        assert parsed == cached

    def test_parse_unwitting(self):
        parsed = parse_en_pl(html["unwitting"])
        cached = load_json("unwitting")
        assert parsed == cached

    def test_parse_quisling(self):
        parsed = parse_en_pl(html["quisling"])
        cached = load_json("quisling")
        assert parsed == cached

    def test_parse_connoisseur(self):
        parsed = parse_en_pl(html["connoisseur"])
        cached = load_json("connoisseur")
        assert parsed == cached

    def test_parse_vaporous(self):
        parsed = parse_en_pl(html["vaporous"])
        cached = load_json("vaporous")
        assert parsed == cached

    def test_parse_harlot(self):
        parsed = parse_en_pl(html["harlot"])
        cached = load_json("harlot")
        assert parsed == cached

    def test_parse_blunderbuss(self):
        parsed = parse_en_pl(html["blunderbuss"])
        cached = load_json("blunderbuss")
        assert parsed == cached

    def test_parse_muddler(self):
        parsed = parse_en_pl(html["muddler"])
        cached = load_json("muddler")
        assert parsed == cached

    def test_parse_commotion(self):
        parsed = parse_en_pl(html["commotion"])
        cached = load_json("commotion")
        assert parsed == cached

    def test_parse_trout(self):
        parsed = parse_en_pl(html["trout"])
        cached = load_json("trout")
        assert parsed == cached

    def test_parse_extort(self):
        parsed = parse_en_pl(html["extort"])
        cached = load_json("extort")
        assert parsed == cached

    def test_parse_vernacular(self):
        parsed = parse_en_pl(html["vernacular"])
        cached = load_json("vernacular")
        assert parsed == cached

    def test_parse_queasy(self):
        parsed = parse_en_pl(html["queasy"])
        cached = load_json("queasy")
        assert parsed == cached

    def test_parse_pretentious(self):
        parsed = parse_en_pl(html["pretentious"])
        cached = load_json("pretentious")
        assert parsed == cached

    def test_parse_shrewd(self):
        parsed = parse_en_pl(html["shrewd"])
        cached = load_json("shrewd")
        assert parsed == cached

    def test_parse_mantel(self):
        parsed = parse_en_pl(html["mantel"])
        cached = load_json("mantel")
        assert parsed == cached

    def test_parse_onus(self):
        parsed = parse_en_pl(html["onus"])
        cached = load_json("onus")
        assert parsed == cached

    def test_parse_hypodermic(self):
        parsed = parse_en_pl(html["hypodermic"])
        cached = load_json("hypodermic")
        assert parsed == cached

    def test_parse_prophesying(self):
        parsed = parse_en_pl(html["prophesying"])
        cached = load_json("prophesying")
        assert parsed == cached

    def test_parse_pry(self):
        parsed = parse_en_pl(html["pry"])
        cached = load_json("pry")
        assert parsed == cached

    def test_parse_inundated(self):
        parsed = parse_en_pl(html["inundated"])
        cached = load_json("inundated")
        assert parsed == cached

    def test_parse_holistic(self):
        parsed = parse_en_pl(html["holistic"])
        cached = load_json("holistic")
        assert parsed == cached

    def test_parse_aperture(self):
        parsed = parse_en_pl(html["aperture"])
        cached = load_json("aperture")
        assert parsed == cached

    def test_parse_grasp(self):
        parsed = parse_en_pl(html["grasp"])
        cached = load_json("grasp")
        assert parsed == cached

    def test_parse_searing(self):
        parsed = parse_en_pl(html["searing"])
        cached = load_json("searing")
        assert parsed == cached

    def test_parse_recalcitrant(self):
        parsed = parse_en_pl(html["recalcitrant"])
        cached = load_json("recalcitrant")
        assert parsed == cached

    def test_parse_moribund(self):
        parsed = parse_en_pl(html["moribund"])
        cached = load_json("moribund")
        assert parsed == cached

    def test_parse_transitive(self):
        parsed = parse_en_pl(html["transitive"])
        cached = load_json("transitive")
        assert parsed == cached

    def test_parse_brat(self):
        parsed = parse_en_pl(html["brat"])
        cached = load_json("brat")
        assert parsed == cached

    def test_parse_mush(self):
        parsed = parse_en_pl(html["mush"])
        cached = load_json("mush")
        assert parsed == cached

    def test_parse_immerse(self):
        parsed = parse_en_pl(html["immerse"])
        cached = load_json("immerse")
        assert parsed == cached

    def test_parse_imbue(self):
        parsed = parse_en_pl(html["imbue"])
        cached = load_json("imbue")
        assert parsed == cached

    def test_parse_shutter(self):
        parsed = parse_en_pl(html["shutter"])
        cached = load_json("shutter")
        assert parsed == cached

    def test_parse_fingertip(self):
        parsed = parse_en_pl(html["fingertip"])
        cached = load_json("fingertip")
        assert parsed == cached

    def test_parse_spurn(self):
        parsed = parse_en_pl(html["spurn"])
        cached = load_json("spurn")
        assert parsed == cached

    def test_parse_curfew(self):
        parsed = parse_en_pl(html["curfew"])
        cached = load_json("curfew")
        assert parsed == cached

    def test_parse_subpoena(self):
        parsed = parse_en_pl(html["subpoena"])
        cached = load_json("subpoena")
        assert parsed == cached

    def test_parse_plunge(self):
        parsed = parse_en_pl(html["plunge"])
        cached = load_json("plunge")
        assert parsed == cached

    def test_parse_dissent(self):
        parsed = parse_en_pl(html["dissent"])
        cached = load_json("dissent")
        assert parsed == cached

    def test_parse_contagion(self):
        parsed = parse_en_pl(html["contagion"])
        cached = load_json("contagion")
        assert parsed == cached

    def test_parse_petty(self):
        parsed = parse_en_pl(html["petty"])
        cached = load_json("petty")
        assert parsed == cached

    def test_parse_preordain(self):
        parsed = parse_en_pl(html["preordain"])
        cached = load_json("preordain")
        assert parsed == cached

    def test_parse_revery(self):
        parsed = parse_en_pl(html["revery"])
        cached = load_json("revery")
        assert parsed == cached

    def test_parse_amygdala(self):
        parsed = parse_en_pl(html["amygdala"])
        cached = load_json("amygdala")
        assert parsed == cached

    def test_parse_rendition(self):
        parsed = parse_en_pl(html["rendition"])
        cached = load_json("rendition")
        assert parsed == cached

    def test_parse_incumbent(self):
        parsed = parse_en_pl(html["incumbent"])
        cached = load_json("incumbent")
        assert parsed == cached

    def test_parse_analgesic(self):
        parsed = parse_en_pl(html["analgesic"])
        cached = load_json("analgesic")
        assert parsed == cached

    def test_parse_prejudice(self):
        parsed = parse_en_pl(html["prejudice"])
        cached = load_json("prejudice")
        assert parsed == cached

    def test_parse_savage(self):
        parsed = parse_en_pl(html["savage"])
        cached = load_json("savage")
        assert parsed == cached

    def test_parse_marvellous(self):
        parsed = parse_en_pl(html["marvellous"])
        cached = load_json("marvellous")
        assert parsed == cached

    def test_parse_dulcimer(self):
        parsed = parse_en_pl(html["dulcimer"])
        cached = load_json("dulcimer")
        assert parsed == cached

    def test_parse_stupor(self):
        parsed = parse_en_pl(html["stupor"])
        cached = load_json("stupor")
        assert parsed == cached

    def test_parse_rickets(self):
        parsed = parse_en_pl(html["rickets"])
        cached = load_json("rickets")
        assert parsed == cached

    def test_parse_utensil(self):
        parsed = parse_en_pl(html["utensil"])
        cached = load_json("utensil")
        assert parsed == cached

    def test_parse_mollify(self):
        parsed = parse_en_pl(html["mollify"])
        cached = load_json("mollify")
        assert parsed == cached

    def test_parse_dot(self):
        parsed = parse_en_pl(html["dot"])
        cached = load_json("dot")
        assert parsed == cached

    def test_parse_mansion(self):
        parsed = parse_en_pl(html["mansion"])
        cached = load_json("mansion")
        assert parsed == cached

    def test_parse_corroborate(self):
        parsed = parse_en_pl(html["corroborate"])
        cached = load_json("corroborate")
        assert parsed == cached

    def test_parse_vapid(self):
        parsed = parse_en_pl(html["vapid"])
        cached = load_json("vapid")
        assert parsed == cached

    def test_parse_quixotic(self):
        parsed = parse_en_pl(html["quixotic"])
        cached = load_json("quixotic")
        assert parsed == cached

    def test_parse_effigy(self):
        parsed = parse_en_pl(html["effigy"])
        cached = load_json("effigy")
        assert parsed == cached

    def test_parse_bungle(self):
        parsed = parse_en_pl(html["bungle"])
        cached = load_json("bungle")
        assert parsed == cached

    def test_parse_wane(self):
        parsed = parse_en_pl(html["wane"])
        cached = load_json("wane")
        assert parsed == cached

    def test_parse_mend(self):
        parsed = parse_en_pl(html["mend"])
        cached = load_json("mend")
        assert parsed == cached

    def test_parse_ambient(self):
        parsed = parse_en_pl(html["ambient"])
        cached = load_json("ambient")
        assert parsed == cached

    def test_parse_gluttony(self):
        parsed = parse_en_pl(html["gluttony"])
        cached = load_json("gluttony")
        assert parsed == cached

    def test_parse_cheeky(self):
        parsed = parse_en_pl(html["cheeky"])
        cached = load_json("cheeky")
        assert parsed == cached

    def test_parse_lymphoma(self):
        parsed = parse_en_pl(html["lymphoma"])
        cached = load_json("lymphoma")
        assert parsed == cached

    def test_parse_affirm(self):
        parsed = parse_en_pl(html["affirm"])
        cached = load_json("affirm")
        assert parsed == cached

    def test_parse_confide(self):
        parsed = parse_en_pl(html["confide"])
        cached = load_json("confide")
        assert parsed == cached

    def test_parse_preternatural(self):
        parsed = parse_en_pl(html["preternatural"])
        cached = load_json("preternatural")
        assert parsed == cached

    def test_parse_evanescent(self):
        parsed = parse_en_pl(html["evanescent"])
        cached = load_json("evanescent")
        assert parsed == cached

    def test_parse_ineffectual(self):
        parsed = parse_en_pl(html["ineffectual"])
        cached = load_json("ineffectual")
        assert parsed == cached

    def test_parse_alacrity(self):
        parsed = parse_en_pl(html["alacrity"])
        cached = load_json("alacrity")
        assert parsed == cached

    def test_parse_marsupial(self):
        parsed = parse_en_pl(html["marsupial"])
        cached = load_json("marsupial")
        assert parsed == cached

    def test_parse_courting(self):
        parsed = parse_en_pl(html["courting"])
        cached = load_json("courting")
        assert parsed == cached

    def test_parse_balk(self):
        parsed = parse_en_pl(html["balk"])
        cached = load_json("balk")
        assert parsed == cached

    def test_parse_collate(self):
        parsed = parse_en_pl(html["collate"])
        cached = load_json("collate")
        assert parsed == cached

    def test_parse_denouement(self):
        parsed = parse_en_pl(html["denouement"])
        cached = load_json("denouement")
        assert parsed == cached

    def test_parse_oaf(self):
        parsed = parse_en_pl(html["oaf"])
        cached = load_json("oaf")
        assert parsed == cached

    def test_parse_riverine(self):
        parsed = parse_en_pl(html["riverine"])
        cached = load_json("riverine")
        assert parsed == cached

    def test_parse_tuberculosis(self):
        parsed = parse_en_pl(html["tuberculosis"])
        cached = load_json("tuberculosis")
        assert parsed == cached

    def test_parse_mottle(self):
        parsed = parse_en_pl(html["mottle"])
        cached = load_json("mottle")
        assert parsed == cached

    def test_parse_iffy(self):
        parsed = parse_en_pl(html["iffy"])
        cached = load_json("iffy")
        assert parsed == cached

    def test_parse_savory(self):
        parsed = parse_en_pl(html["savory"])
        cached = load_json("savory")
        assert parsed == cached

    def test_parse_sobriety(self):
        parsed = parse_en_pl(html["sobriety"])
        cached = load_json("sobriety")
        assert parsed == cached

    def test_parse_Mace(self):
        parsed = parse_en_pl(html["Mace"])
        cached = load_json("Mace")
        assert parsed == cached

    def test_parse_wrong_headed(self):
        parsed = parse_en_pl(html["wrong-headed"])
        cached = load_json("wrong-headed")
        assert parsed == cached

    def test_parse_reticent(self):
        parsed = parse_en_pl(html["reticent"])
        cached = load_json("reticent")
        assert parsed == cached

    def test_parse_abruptly(self):
        parsed = parse_en_pl(html["abruptly"])
        cached = load_json("abruptly")
        assert parsed == cached

    def test_parse_eulogy(self):
        parsed = parse_en_pl(html["eulogy"])
        cached = load_json("eulogy")
        assert parsed == cached

    def test_parse_slime(self):
        parsed = parse_en_pl(html["slime"])
        cached = load_json("slime")
        assert parsed == cached

    def test_parse_awning(self):
        parsed = parse_en_pl(html["awning"])
        cached = load_json("awning")
        assert parsed == cached

    def test_parse_bowled(self):
        parsed = parse_en_pl(html["bowled"])
        cached = load_json("bowled")
        assert parsed == cached

    def test_parse_glum(self):
        parsed = parse_en_pl(html["glum"])
        cached = load_json("glum")
        assert parsed == cached

    def test_parse_calcify(self):
        parsed = parse_en_pl(html["calcify"])
        cached = load_json("calcify")
        assert parsed == cached

    def test_parse_forthright(self):
        parsed = parse_en_pl(html["forthright"])
        cached = load_json("forthright")
        assert parsed == cached

    def test_parse_mischief(self):
        parsed = parse_en_pl(html["mischief"])
        cached = load_json("mischief")
        assert parsed == cached

    def test_parse_granadilla(self):
        parsed = parse_en_pl(html["granadilla"])
        cached = load_json("granadilla")
        assert parsed == cached

    def test_parse_garish(self):
        parsed = parse_en_pl(html["garish"])
        cached = load_json("garish")
        assert parsed == cached

    def test_parse_compulsory(self):
        parsed = parse_en_pl(html["compulsory"])
        cached = load_json("compulsory")
        assert parsed == cached

    def test_parse_lotus(self):
        parsed = parse_en_pl(html["lotus"])
        cached = load_json("lotus")
        assert parsed == cached

    def test_parse_quotidian(self):
        parsed = parse_en_pl(html["quotidian"])
        cached = load_json("quotidian")
        assert parsed == cached

    def test_parse_perch(self):
        parsed = parse_en_pl(html["perch"])
        cached = load_json("perch")
        assert parsed == cached

    def test_parse_segues(self):
        parsed = parse_en_pl(html["segues"])
        cached = load_json("segues")
        assert parsed == cached

    def test_parse_flirty(self):
        parsed = parse_en_pl(html["flirty"])
        cached = load_json("flirty")
        assert parsed == cached

    def test_parse_smugness(self):
        parsed = parse_en_pl(html["smugness"])
        cached = load_json("smugness")
        assert parsed == cached

    def test_parse_spic(self):
        parsed = parse_en_pl(html["spic"])
        cached = load_json("spic")
        assert parsed == cached

    def test_parse_mastic(self):
        parsed = parse_en_pl(html["mastic"])
        cached = load_json("mastic")
        assert parsed == cached

    def test_parse_pompous(self):
        parsed = parse_en_pl(html["pompous"])
        cached = load_json("pompous")
        assert parsed == cached

    def test_parse_admissible(self):
        parsed = parse_en_pl(html["admissible"])
        cached = load_json("admissible")
        assert parsed == cached

    def test_parse_minimalistic(self):
        parsed = parse_en_pl(html["minimalistic"])
        cached = load_json("minimalistic")
        assert parsed == cached

    def test_parse_hovercraft(self):
        parsed = parse_en_pl(html["hovercraft"])
        cached = load_json("hovercraft")
        assert parsed == cached

    def test_parse_compound(self):
        parsed = parse_en_pl(html["compound"])
        cached = load_json("compound")
        assert parsed == cached

    def test_parse_crusty(self):
        parsed = parse_en_pl(html["crusty"])
        cached = load_json("crusty")
        assert parsed == cached

    def test_parse_spite(self):
        parsed = parse_en_pl(html["spite"])
        cached = load_json("spite")
        assert parsed == cached

    def test_parse_buzzard(self):
        parsed = parse_en_pl(html["buzzard"])
        cached = load_json("buzzard")
        assert parsed == cached

    def test_parse_waver(self):
        parsed = parse_en_pl(html["waver"])
        cached = load_json("waver")
        assert parsed == cached

    def test_parse_ravel(self):
        parsed = parse_en_pl(html["ravel"])
        cached = load_json("ravel")
        assert parsed == cached

    def test_parse_dismal(self):
        parsed = parse_en_pl(html["dismal"])
        cached = load_json("dismal")
        assert parsed == cached

    def test_parse_impotence(self):
        parsed = parse_en_pl(html["impotence"])
        cached = load_json("impotence")
        assert parsed == cached

    def test_parse_assuage(self):
        parsed = parse_en_pl(html["assuage"])
        cached = load_json("assuage")
        assert parsed == cached

    def test_parse_conduct(self):
        parsed = parse_en_pl(html["conduct"])
        cached = load_json("conduct")
        assert parsed == cached

    def test_parse_indict(self):
        parsed = parse_en_pl(html["indict"])
        cached = load_json("indict")
        assert parsed == cached

    def test_parse_emaciated(self):
        parsed = parse_en_pl(html["emaciated"])
        cached = load_json("emaciated")
        assert parsed == cached

    def test_parse_solitude(self):
        parsed = parse_en_pl(html["solitude"])
        cached = load_json("solitude")
        assert parsed == cached

    def test_parse_brill(self):
        parsed = parse_en_pl(html["brill"])
        cached = load_json("brill")
        assert parsed == cached

    def test_parse_constraint(self):
        parsed = parse_en_pl(html["constraint"])
        cached = load_json("constraint")
        assert parsed == cached

    def test_parse_derogatory(self):
        parsed = parse_en_pl(html["derogatory"])
        cached = load_json("derogatory")
        assert parsed == cached

    def test_parse_gruesome(self):
        parsed = parse_en_pl(html["gruesome"])
        cached = load_json("gruesome")
        assert parsed == cached

    def test_parse_umpire(self):
        parsed = parse_en_pl(html["umpire"])
        cached = load_json("umpire")
        assert parsed == cached

    def test_parse_rout(self):
        parsed = parse_en_pl(html["rout"])
        cached = load_json("rout")
        assert parsed == cached

    def test_parse_runt(self):
        parsed = parse_en_pl(html["runt"])
        cached = load_json("runt")
        assert parsed == cached

    def test_parse_bovine(self):
        parsed = parse_en_pl(html["bovine"])
        cached = load_json("bovine")
        assert parsed == cached

    def test_parse_this(self):
        parsed = parse_en_pl(html["this"])
        cached = load_json("this")
        assert parsed == cached

    def test_parse_mold(self):
        parsed = parse_en_pl(html["mold"])
        cached = load_json("mold")
        assert parsed == cached

    def test_parse_vagaries(self):
        parsed = parse_en_pl(html["vagaries"])
        cached = load_json("vagaries")
        assert parsed == cached

    def test_parse_epiphanic(self):
        parsed = parse_en_pl(html["epiphanic"])
        cached = load_json("epiphanic")
        assert parsed == cached

    def test_parse_overhead(self):
        parsed = parse_en_pl(html["overhead"])
        cached = load_json("overhead")
        assert parsed == cached

    def test_parse_perennial(self):
        parsed = parse_en_pl(html["perennial"])
        cached = load_json("perennial")
        assert parsed == cached

    def test_parse_aptly(self):
        parsed = parse_en_pl(html["aptly"])
        cached = load_json("aptly")
        assert parsed == cached

    def test_parse_menacing(self):
        parsed = parse_en_pl(html["menacing"])
        cached = load_json("menacing")
        assert parsed == cached

    def test_parse_loon(self):
        parsed = parse_en_pl(html["loon"])
        cached = load_json("loon")
        assert parsed == cached

    def test_parse_satiable(self):
        parsed = parse_en_pl(html["satiable"])
        cached = load_json("satiable")
        assert parsed == cached

    def test_parse_callousness(self):
        parsed = parse_en_pl(html["callousness"])
        cached = load_json("callousness")
        assert parsed == cached

    def test_parse_huff(self):
        parsed = parse_en_pl(html["huff"])
        cached = load_json("huff")
        assert parsed == cached

    def test_parse_incidentally(self):
        parsed = parse_en_pl(html["incidentally"])
        cached = load_json("incidentally")
        assert parsed == cached

    def test_parse_brassiere(self):
        parsed = parse_en_pl(html["brassiere"])
        cached = load_json("brassiere")
        assert parsed == cached

    def test_parse_torpor(self):
        parsed = parse_en_pl(html["torpor"])
        cached = load_json("torpor")
        assert parsed == cached

    def test_parse_profane(self):
        parsed = parse_en_pl(html["profane"])
        cached = load_json("profane")
        assert parsed == cached

    def test_parse_calamity(self):
        parsed = parse_en_pl(html["calamity"])
        cached = load_json("calamity")
        assert parsed == cached

    def test_parse_hard_boiled(self):
        parsed = parse_en_pl(html["hard-boiled"])
        cached = load_json("hard-boiled")
        assert parsed == cached

    def test_parse_burly(self):
        parsed = parse_en_pl(html["burly"])
        cached = load_json("burly")
        assert parsed == cached

    def test_parse_epistemology(self):
        parsed = parse_en_pl(html["epistemology"])
        cached = load_json("epistemology")
        assert parsed == cached

    def test_parse_artisan(self):
        parsed = parse_en_pl(html["artisan"])
        cached = load_json("artisan")
        assert parsed == cached

    def test_parse_epitomize(self):
        parsed = parse_en_pl(html["epitomize"])
        cached = load_json("epitomize")
        assert parsed == cached

    def test_parse_culpably(self):
        parsed = parse_en_pl(html["culpably"])
        cached = load_json("culpably")
        assert parsed == cached

    def test_parse_mitten(self):
        parsed = parse_en_pl(html["mitten"])
        cached = load_json("mitten")
        assert parsed == cached

    def test_parse_bequeath(self):
        parsed = parse_en_pl(html["bequeath"])
        cached = load_json("bequeath")
        assert parsed == cached

    def test_parse_endowment(self):
        parsed = parse_en_pl(html["endowment"])
        cached = load_json("endowment")
        assert parsed == cached

    def test_parse_rebuke(self):
        parsed = parse_en_pl(html["rebuke"])
        cached = load_json("rebuke")
        assert parsed == cached

    def test_parse_refute(self):
        parsed = parse_en_pl(html["refute"])
        cached = load_json("refute")
        assert parsed == cached

    def test_parse_merit(self):
        parsed = parse_en_pl(html["merit"])
        cached = load_json("merit")
        assert parsed == cached

    def test_parse_vigilante(self):
        parsed = parse_en_pl(html["vigilante"])
        cached = load_json("vigilante")
        assert parsed == cached

    def test_parse_frontier(self):
        parsed = parse_en_pl(html["frontier"])
        cached = load_json("frontier")
        assert parsed == cached

    def test_parse_confidant(self):
        parsed = parse_en_pl(html["confidant"])
        cached = load_json("confidant")
        assert parsed == cached

    def test_parse_fallacy(self):
        parsed = parse_en_pl(html["fallacy"])
        cached = load_json("fallacy")
        assert parsed == cached

    def test_parse_preposterous(self):
        parsed = parse_en_pl(html["preposterous"])
        cached = load_json("preposterous")
        assert parsed == cached

    def test_parse_mockery(self):
        parsed = parse_en_pl(html["mockery"])
        cached = load_json("mockery")
        assert parsed == cached

    def test_parse_lugubrious(self):
        parsed = parse_en_pl(html["lugubrious"])
        cached = load_json("lugubrious")
        assert parsed == cached

    def test_parse_hemlock(self):
        parsed = parse_en_pl(html["hemlock"])
        cached = load_json("hemlock")
        assert parsed == cached

    def test_parse_discern(self):
        parsed = parse_en_pl(html["discern"])
        cached = load_json("discern")
        assert parsed == cached

    def test_parse_derisively(self):
        parsed = parse_en_pl(html["derisively"])
        cached = load_json("derisively")
        assert parsed == cached

    def test_parse_woe(self):
        parsed = parse_en_pl(html["woe"])
        cached = load_json("woe")
        assert parsed == cached

    def test_parse_conn(self):
        parsed = parse_en_pl(html["conn"])
        cached = load_json("conn")
        assert parsed == cached

    def test_parse_telltale(self):
        parsed = parse_en_pl(html["telltale"])
        cached = load_json("telltale")
        assert parsed == cached

    def test_parse_fawn(self):
        parsed = parse_en_pl(html["fawn"])
        cached = load_json("fawn")
        assert parsed == cached

    def test_parse_conclude(self):
        parsed = parse_en_pl(html["conclude"])
        cached = load_json("conclude")
        assert parsed == cached

    def test_parse_flinching(self):
        parsed = parse_en_pl(html["flinching"])
        cached = load_json("flinching")
        assert parsed == cached

    def test_parse_subpar(self):
        parsed = parse_en_pl(html["subpar"])
        cached = load_json("subpar")
        assert parsed == cached

    def test_parse_rosewood(self):
        parsed = parse_en_pl(html["rosewood"])
        cached = load_json("rosewood")
        assert parsed == cached

    def test_parse_fare(self):
        parsed = parse_en_pl(html["fare"])
        cached = load_json("fare")
        assert parsed == cached

    def test_parse_rumple(self):
        parsed = parse_en_pl(html["rumple"])
        cached = load_json("rumple")
        assert parsed == cached

    def test_parse_irascible(self):
        parsed = parse_en_pl(html["irascible"])
        cached = load_json("irascible")
        assert parsed == cached

    def test_parse_weld(self):
        parsed = parse_en_pl(html["weld"])
        cached = load_json("weld")
        assert parsed == cached

    def test_parse_lean(self):
        parsed = parse_en_pl(html["lean"])
        cached = load_json("lean")
        assert parsed == cached

    def test_parse_hither(self):
        parsed = parse_en_pl(html["hither"])
        cached = load_json("hither")
        assert parsed == cached

    def test_parse_lump(self):
        parsed = parse_en_pl(html["lump"])
        cached = load_json("lump")
        assert parsed == cached

    def test_parse_compunction(self):
        parsed = parse_en_pl(html["compunction"])
        cached = load_json("compunction")
        assert parsed == cached

    def test_parse_measles(self):
        parsed = parse_en_pl(html["measles"])
        cached = load_json("measles")
        assert parsed == cached

    def test_parse_trigger(self):
        parsed = parse_en_pl(html["trigger"])
        cached = load_json("trigger")
        assert parsed == cached

    def test_parse_wallaby(self):
        parsed = parse_en_pl(html["wallaby"])
        cached = load_json("wallaby")
        assert parsed == cached

    def test_parse_adamant(self):
        parsed = parse_en_pl(html["adamant"])
        cached = load_json("adamant")
        assert parsed == cached

    def test_parse_irritable(self):
        parsed = parse_en_pl(html["irritable"])
        cached = load_json("irritable")
        assert parsed == cached

    def test_parse_querulous(self):
        parsed = parse_en_pl(html["querulous"])
        cached = load_json("querulous")
        assert parsed == cached

    def test_parse_reciprocate(self):
        parsed = parse_en_pl(html["reciprocate"])
        cached = load_json("reciprocate")
        assert parsed == cached

    def test_parse_offal(self):
        parsed = parse_en_pl(html["offal"])
        cached = load_json("offal")
        assert parsed == cached

    def test_parse_coop(self):
        parsed = parse_en_pl(html["coop"])
        cached = load_json("coop")
        assert parsed == cached

    def test_parse_eerily(self):
        parsed = parse_en_pl(html["eerily"])
        cached = load_json("eerily")
        assert parsed == cached

    def test_parse_inane(self):
        parsed = parse_en_pl(html["inane"])
        cached = load_json("inane")
        assert parsed == cached

    def test_parse_inexorably(self):
        parsed = parse_en_pl(html["inexorably"])
        cached = load_json("inexorably")
        assert parsed == cached

    def test_parse_concave(self):
        parsed = parse_en_pl(html["concave"])
        cached = load_json("concave")
        assert parsed == cached

    def test_parse_retrieve(self):
        parsed = parse_en_pl(html["retrieve"])
        cached = load_json("retrieve")
        assert parsed == cached

    def test_parse_cadaver(self):
        parsed = parse_en_pl(html["cadaver"])
        cached = load_json("cadaver")
        assert parsed == cached

    def test_parse_dereliction(self):
        parsed = parse_en_pl(html["dereliction"])
        cached = load_json("dereliction")
        assert parsed == cached

    def test_parse_licorice(self):
        parsed = parse_en_pl(html["licorice"])
        cached = load_json("licorice")
        assert parsed == cached

    def test_parse_knapsack(self):
        parsed = parse_en_pl(html["knapsack"])
        cached = load_json("knapsack")
        assert parsed == cached

    def test_parse_overhaul(self):
        parsed = parse_en_pl(html["overhaul"])
        cached = load_json("overhaul")
        assert parsed == cached

    def test_parse_shill(self):
        parsed = parse_en_pl(html["shill"])
        cached = load_json("shill")
        assert parsed == cached

    def test_parse_hallmark(self):
        parsed = parse_en_pl(html["hallmark"])
        cached = load_json("hallmark")
        assert parsed == cached

    def test_parse_poise(self):
        parsed = parse_en_pl(html["poise"])
        cached = load_json("poise")
        assert parsed == cached

    def test_parse_affluent(self):
        parsed = parse_en_pl(html["affluent"])
        cached = load_json("affluent")
        assert parsed == cached

    def test_parse_verboten(self):
        parsed = parse_en_pl(html["verboten"])
        cached = load_json("verboten")
        assert parsed == cached

    def test_parse_refutation(self):
        parsed = parse_en_pl(html["refutation"])
        cached = load_json("refutation")
        assert parsed == cached

    def test_parse_fealty(self):
        parsed = parse_en_pl(html["fealty"])
        cached = load_json("fealty")
        assert parsed == cached

    def test_parse_minted(self):
        parsed = parse_en_pl(html["minted"])
        cached = load_json("minted")
        assert parsed == cached

    def test_parse_odious(self):
        parsed = parse_en_pl(html["odious"])
        cached = load_json("odious")
        assert parsed == cached

    def test_parse_blithely(self):
        parsed = parse_en_pl(html["blithely"])
        cached = load_json("blithely")
        assert parsed == cached

    def test_parse_trap(self):
        parsed = parse_en_pl(html["trap"])
        cached = load_json("trap")
        assert parsed == cached

    def test_parse_felt(self):
        parsed = parse_en_pl(html["felt"])
        cached = load_json("felt")
        assert parsed == cached

    def test_parse_spur(self):
        parsed = parse_en_pl(html["spur"])
        cached = load_json("spur")
        assert parsed == cached

    def test_parse_Bedouin(self):
        parsed = parse_en_pl(html["Bedouin"])
        cached = load_json("Bedouin")
        assert parsed == cached

    def test_parse_varnish(self):
        parsed = parse_en_pl(html["varnish"])
        cached = load_json("varnish")
        assert parsed == cached

    def test_parse_espouse(self):
        parsed = parse_en_pl(html["espouse"])
        cached = load_json("espouse")
        assert parsed == cached

    def test_parse_fecundity(self):
        parsed = parse_en_pl(html["fecundity"])
        cached = load_json("fecundity")
        assert parsed == cached

    def test_parse_gourd(self):
        parsed = parse_en_pl(html["gourd"])
        cached = load_json("gourd")
        assert parsed == cached

    def test_parse_adage(self):
        parsed = parse_en_pl(html["adage"])
        cached = load_json("adage")
        assert parsed == cached

    def test_parse_scotch(self):
        parsed = parse_en_pl(html["scotch"])
        cached = load_json("scotch")
        assert parsed == cached

    def test_parse_quark(self):
        parsed = parse_en_pl(html["quark"])
        cached = load_json("quark")
        assert parsed == cached

    def test_parse_ruse(self):
        parsed = parse_en_pl(html["ruse"])
        cached = load_json("ruse")
        assert parsed == cached

    def test_parse_vein(self):
        parsed = parse_en_pl(html["vein"])
        cached = load_json("vein")
        assert parsed == cached

    def test_parse_winch(self):
        parsed = parse_en_pl(html["winch"])
        cached = load_json("winch")
        assert parsed == cached

    def test_parse_ruminate(self):
        parsed = parse_en_pl(html["ruminate"])
        cached = load_json("ruminate")
        assert parsed == cached

    def test_parse_revelry(self):
        parsed = parse_en_pl(html["revelry"])
        cached = load_json("revelry")
        assert parsed == cached

    def test_parse_colon(self):
        parsed = parse_en_pl(html["colon"])
        cached = load_json("colon")
        assert parsed == cached

    def test_parse_scooped(self):
        parsed = parse_en_pl(html["scooped"])
        cached = load_json("scooped")
        assert parsed == cached

    def test_parse_itinerant(self):
        parsed = parse_en_pl(html["itinerant"])
        cached = load_json("itinerant")
        assert parsed == cached

    def test_parse_oeuvre(self):
        parsed = parse_en_pl(html["oeuvre"])
        cached = load_json("oeuvre")
        assert parsed == cached

    def test_parse_scion(self):
        parsed = parse_en_pl(html["scion"])
        cached = load_json("scion")
        assert parsed == cached

    def test_parse_exalted(self):
        parsed = parse_en_pl(html["exalted"])
        cached = load_json("exalted")
        assert parsed == cached

    def test_parse_playwright(self):
        parsed = parse_en_pl(html["playwright"])
        cached = load_json("playwright")
        assert parsed == cached

    def test_parse_liaison(self):
        parsed = parse_en_pl(html["liaison"])
        cached = load_json("liaison")
        assert parsed == cached

    def test_parse_abject(self):
        parsed = parse_en_pl(html["abject"])
        cached = load_json("abject")
        assert parsed == cached

    def test_parse_inexpressible(self):
        parsed = parse_en_pl(html["inexpressible"])
        cached = load_json("inexpressible")
        assert parsed == cached

    def test_parse_mound(self):
        parsed = parse_en_pl(html["mound"])
        cached = load_json("mound")
        assert parsed == cached

    def test_parse_despair(self):
        parsed = parse_en_pl(html["despair"])
        cached = load_json("despair")
        assert parsed == cached

    def test_parse_pettiness(self):
        parsed = parse_en_pl(html["pettiness"])
        cached = load_json("pettiness")
        assert parsed == cached

    def test_parse_portentous(self):
        parsed = parse_en_pl(html["portentous"])
        cached = load_json("portentous")
        assert parsed == cached

    def test_parse_stagger(self):
        parsed = parse_en_pl(html["stagger"])
        cached = load_json("stagger")
        assert parsed == cached

    def test_parse_hopeless(self):
        parsed = parse_en_pl(html["hopeless"])
        cached = load_json("hopeless")
        assert parsed == cached

    def test_parse_until(self):
        parsed = parse_en_pl(html["until"])
        cached = load_json("until")
        assert parsed == cached

    def test_parse_debonair(self):
        parsed = parse_en_pl(html["debonair"])
        cached = load_json("debonair")
        assert parsed == cached

    def test_parse_columnist(self):
        parsed = parse_en_pl(html["columnist"])
        cached = load_json("columnist")
        assert parsed == cached

    def test_parse_precarious(self):
        parsed = parse_en_pl(html["precarious"])
        cached = load_json("precarious")
        assert parsed == cached

    def test_parse_candidly(self):
        parsed = parse_en_pl(html["candidly"])
        cached = load_json("candidly")
        assert parsed == cached

    def test_parse_loom(self):
        parsed = parse_en_pl(html["loom"])
        cached = load_json("loom")
        assert parsed == cached

    def test_parse_bilateral(self):
        parsed = parse_en_pl(html["bilateral"])
        cached = load_json("bilateral")
        assert parsed == cached

    def test_parse_shellac(self):
        parsed = parse_en_pl(html["shellac"])
        cached = load_json("shellac")
        assert parsed == cached

    def test_parse_fennel(self):
        parsed = parse_en_pl(html["fennel"])
        cached = load_json("fennel")
        assert parsed == cached

    def test_parse_slavish(self):
        parsed = parse_en_pl(html["slavish"])
        cached = load_json("slavish")
        assert parsed == cached

    def test_parse_feckless(self):
        parsed = parse_en_pl(html["feckless"])
        cached = load_json("feckless")
        assert parsed == cached

    def test_parse_feral(self):
        parsed = parse_en_pl(html["feral"])
        cached = load_json("feral")
        assert parsed == cached

    def test_parse_fortitude(self):
        parsed = parse_en_pl(html["fortitude"])
        cached = load_json("fortitude")
        assert parsed == cached

    def test_parse_slantwise(self):
        parsed = parse_en_pl(html["slantwise"])
        cached = load_json("slantwise")
        assert parsed == cached

    def test_parse_convoluted(self):
        parsed = parse_en_pl(html["convoluted"])
        cached = load_json("convoluted")
        assert parsed == cached

    def test_parse_defector(self):
        parsed = parse_en_pl(html["defector"])
        cached = load_json("defector")
        assert parsed == cached

    def test_parse_cheekily(self):
        parsed = parse_en_pl(html["cheekily"])
        cached = load_json("cheekily")
        assert parsed == cached

    def test_parse_reciprocity(self):
        parsed = parse_en_pl(html["reciprocity"])
        cached = load_json("reciprocity")
        assert parsed == cached

    def test_parse_subliminal(self):
        parsed = parse_en_pl(html["subliminal"])
        cached = load_json("subliminal")
        assert parsed == cached

    def test_parse_furry(self):
        parsed = parse_en_pl(html["furry"])
        cached = load_json("furry")
        assert parsed == cached

    def test_parse_crayon(self):
        parsed = parse_en_pl(html["crayon"])
        cached = load_json("crayon")
        assert parsed == cached

    def test_parse_blotter(self):
        parsed = parse_en_pl(html["blotter"])
        cached = load_json("blotter")
        assert parsed == cached

    def test_parse_callous(self):
        parsed = parse_en_pl(html["callous"])
        cached = load_json("callous")
        assert parsed == cached

    def test_parse_prescient(self):
        parsed = parse_en_pl(html["prescient"])
        cached = load_json("prescient")
        assert parsed == cached

    def test_parse_pinch(self):
        parsed = parse_en_pl(html["pinch"])
        cached = load_json("pinch")
        assert parsed == cached

    def test_parse_equine(self):
        parsed = parse_en_pl(html["equine"])
        cached = load_json("equine")
        assert parsed == cached

    def test_parse_adamantine(self):
        parsed = parse_en_pl(html["adamantine"])
        cached = load_json("adamantine")
        assert parsed == cached

    def test_parse_indigent(self):
        parsed = parse_en_pl(html["indigent"])
        cached = load_json("indigent")
        assert parsed == cached

    def test_parse_musk(self):
        parsed = parse_en_pl(html["musk"])
        cached = load_json("musk")
        assert parsed == cached

    def test_parse_impugned(self):
        parsed = parse_en_pl(html["impugned"])
        cached = load_json("impugned")
        assert parsed == cached

    def test_parse_tumble(self):
        parsed = parse_en_pl(html["tumble"])
        cached = load_json("tumble")
        assert parsed == cached

    def test_parse_shim(self):
        parsed = parse_en_pl(html["shim"])
        cached = load_json("shim")
        assert parsed == cached

    def test_parse_billet(self):
        parsed = parse_en_pl(html["billet"])
        cached = load_json("billet")
        assert parsed == cached

    def test_parse_blossom(self):
        parsed = parse_en_pl(html["blossom"])
        cached = load_json("blossom")
        assert parsed == cached

    def test_parse_thrall(self):
        parsed = parse_en_pl(html["thrall"])
        cached = load_json("thrall")
        assert parsed == cached

    def test_parse_conifer(self):
        parsed = parse_en_pl(html["conifer"])
        cached = load_json("conifer")
        assert parsed == cached

    def test_parse_milter(self):
        parsed = parse_en_pl(html["milter"])
        cached = load_json("milter")
        assert parsed == cached

    def test_parse_scoop(self):
        parsed = parse_en_pl(html["scoop"])
        cached = load_json("scoop")
        assert parsed == cached

    def test_parse_scuttle(self):
        parsed = parse_en_pl(html["scuttle"])
        cached = load_json("scuttle")
        assert parsed == cached

    def test_parse_injunction(self):
        parsed = parse_en_pl(html["injunction"])
        cached = load_json("injunction")
        assert parsed == cached

    def test_parse_jot(self):
        parsed = parse_en_pl(html["jot"])
        cached = load_json("jot")
        assert parsed == cached

    def test_parse_lye(self):
        parsed = parse_en_pl(html["lye"])
        cached = load_json("lye")
        assert parsed == cached

    def test_parse_petulant(self):
        parsed = parse_en_pl(html["petulant"])
        cached = load_json("petulant")
        assert parsed == cached

    def test_parse_recriminate(self):
        parsed = parse_en_pl(html["recriminate"])
        cached = load_json("recriminate")
        assert parsed == cached

    def test_parse_inviolate(self):
        parsed = parse_en_pl(html["inviolate"])
        cached = load_json("inviolate")
        assert parsed == cached

    def test_parse_moderate(self):
        parsed = parse_en_pl(html["moderate"])
        cached = load_json("moderate")
        assert parsed == cached

    def test_parse_merle(self):
        parsed = parse_en_pl(html["merle"])
        cached = load_json("merle")
        assert parsed == cached

    def test_parse_streaked(self):
        parsed = parse_en_pl(html["streaked"])
        cached = load_json("streaked")
        assert parsed == cached

    def test_parse_valiance(self):
        parsed = parse_en_pl(html["valiance"])
        cached = load_json("valiance")
        assert parsed == cached

    def test_parse_disrobe(self):
        parsed = parse_en_pl(html["disrobe"])
        cached = load_json("disrobe")
        assert parsed == cached

    def test_parse_elm(self):
        parsed = parse_en_pl(html["elm"])
        cached = load_json("elm")
        assert parsed == cached

    def test_parse_descending(self):
        parsed = parse_en_pl(html["descending"])
        cached = load_json("descending")
        assert parsed == cached

    def test_parse_reverie(self):
        parsed = parse_en_pl(html["reverie"])
        cached = load_json("reverie")
        assert parsed == cached

    def test_parse_clot(self):
        parsed = parse_en_pl(html["clot"])
        cached = load_json("clot")
        assert parsed == cached

    def test_parse_trough(self):
        parsed = parse_en_pl(html["trough"])
        cached = load_json("trough")
        assert parsed == cached

    def test_parse_luster(self):
        parsed = parse_en_pl(html["luster"])
        cached = load_json("luster")
        assert parsed == cached

    def test_parse_rind(self):
        parsed = parse_en_pl(html["rind"])
        cached = load_json("rind")
        assert parsed == cached

    def test_parse_reserved(self):
        parsed = parse_en_pl(html["reserved"])
        cached = load_json("reserved")
        assert parsed == cached

    def test_parse_drizzle(self):
        parsed = parse_en_pl(html["drizzle"])
        cached = load_json("drizzle")
        assert parsed == cached

    def test_parse_tranquility(self):
        parsed = parse_en_pl(html["tranquility"])
        cached = load_json("tranquility")
        assert parsed == cached

    def test_parse_descendant(self):
        parsed = parse_en_pl(html["descendant"])
        cached = load_json("descendant")
        assert parsed == cached

    def test_parse_butch(self):
        parsed = parse_en_pl(html["butch"])
        cached = load_json("butch")
        assert parsed == cached

    def test_parse_court(self):
        parsed = parse_en_pl(html["court"])
        cached = load_json("court")
        assert parsed == cached

    def test_parse_duvet(self):
        parsed = parse_en_pl(html["duvet"])
        cached = load_json("duvet")
        assert parsed == cached

    def test_parse_discreet(self):
        parsed = parse_en_pl(html["discreet"])
        cached = load_json("discreet")
        assert parsed == cached

    def test_parse_ascertain(self):
        parsed = parse_en_pl(html["ascertain"])
        cached = load_json("ascertain")
        assert parsed == cached

    def test_parse_jacob(self):
        parsed = parse_en_pl(html["jacob"])
        cached = load_json("jacob")
        assert parsed == cached

    def test_parse_aneurysm(self):
        parsed = parse_en_pl(html["aneurysm"])
        cached = load_json("aneurysm")
        assert parsed == cached

    def test_parse_gaudy(self):
        parsed = parse_en_pl(html["gaudy"])
        cached = load_json("gaudy")
        assert parsed == cached

    def test_parse_bespectacled(self):
        parsed = parse_en_pl(html["bespectacled"])
        cached = load_json("bespectacled")
        assert parsed == cached

    def test_parse_placidity(self):
        parsed = parse_en_pl(html["placidity"])
        cached = load_json("placidity")
        assert parsed == cached

    def test_parse_zeal(self):
        parsed = parse_en_pl(html["zeal"])
        cached = load_json("zeal")
        assert parsed == cached

    def test_parse_flatter(self):
        parsed = parse_en_pl(html["flatter"])
        cached = load_json("flatter")
        assert parsed == cached

    def test_parse_pliability(self):
        parsed = parse_en_pl(html["pliability"])
        cached = load_json("pliability")
        assert parsed == cached

    def test_parse_flabbily(self):
        parsed = parse_en_pl(html["flabbily"])
        cached = load_json("flabbily")
        assert parsed == cached

    def test_parse_quadrilateral(self):
        parsed = parse_en_pl(html["quadrilateral"])
        cached = load_json("quadrilateral")
        assert parsed == cached

    def test_parse_snapshot(self):
        parsed = parse_en_pl(html["snapshot"])
        cached = load_json("snapshot")
        assert parsed == cached

    def test_parse_nephew(self):
        parsed = parse_en_pl(html["nephew"])
        cached = load_json("nephew")
        assert parsed == cached

    def test_parse_stymie(self):
        parsed = parse_en_pl(html["stymie"])
        cached = load_json("stymie")
        assert parsed == cached

    def test_parse_dreadnought(self):
        parsed = parse_en_pl(html["dreadnought"])
        cached = load_json("dreadnought")
        assert parsed == cached

    def test_parse_wizard(self):
        parsed = parse_en_pl(html["wizard"])
        cached = load_json("wizard")
        assert parsed == cached

    def test_parse_tertiary(self):
        parsed = parse_en_pl(html["tertiary"])
        cached = load_json("tertiary")
        assert parsed == cached

    def test_parse_amicable(self):
        parsed = parse_en_pl(html["amicable"])
        cached = load_json("amicable")
        assert parsed == cached

    def test_parse_unnerving(self):
        parsed = parse_en_pl(html["unnerving"])
        cached = load_json("unnerving")
        assert parsed == cached

    def test_parse_ordeal(self):
        parsed = parse_en_pl(html["ordeal"])
        cached = load_json("ordeal")
        assert parsed == cached

    def test_parse_peritonitis(self):
        parsed = parse_en_pl(html["peritonitis"])
        cached = load_json("peritonitis")
        assert parsed == cached

    def test_parse_profligate(self):
        parsed = parse_en_pl(html["profligate"])
        cached = load_json("profligate")
        assert parsed == cached

    def test_parse_industry(self):
        parsed = parse_en_pl(html["industry"])
        cached = load_json("industry")
        assert parsed == cached

    def test_parse_kith(self):
        parsed = parse_en_pl(html["kith"])
        cached = load_json("kith")
        assert parsed == cached

    def test_parse_conceal(self):
        parsed = parse_en_pl(html["conceal"])
        cached = load_json("conceal")
        assert parsed == cached

    def test_parse_antebellum(self):
        parsed = parse_en_pl(html["antebellum"])
        cached = load_json("antebellum")
        assert parsed == cached

    def test_parse_venerable(self):
        parsed = parse_en_pl(html["venerable"])
        cached = load_json("venerable")
        assert parsed == cached

    def test_parse_clarion(self):
        parsed = parse_en_pl(html["clarion"])
        cached = load_json("clarion")
        assert parsed == cached

    def test_parse_goldfinch(self):
        parsed = parse_en_pl(html["goldfinch"])
        cached = load_json("goldfinch")
        assert parsed == cached

    def test_parse_ornery(self):
        parsed = parse_en_pl(html["ornery"])
        cached = load_json("ornery")
        assert parsed == cached

    def test_parse_wart(self):
        parsed = parse_en_pl(html["wart"])
        cached = load_json("wart")
        assert parsed == cached

    def test_parse_precipitously(self):
        parsed = parse_en_pl(html["precipitously"])
        cached = load_json("precipitously")
        assert parsed == cached

    def test_parse_sly(self):
        parsed = parse_en_pl(html["sly"])
        cached = load_json("sly")
        assert parsed == cached

    def test_parse_deterred(self):
        parsed = parse_en_pl(html["deterred"])
        cached = load_json("deterred")
        assert parsed == cached

    def test_parse_acquiesce(self):
        parsed = parse_en_pl(html["acquiesce"])
        cached = load_json("acquiesce")
        assert parsed == cached

    def test_parse_deteriorate(self):
        parsed = parse_en_pl(html["deteriorate"])
        cached = load_json("deteriorate")
        assert parsed == cached

    def test_parse_strayed(self):
        parsed = parse_en_pl(html["strayed"])
        cached = load_json("strayed")
        assert parsed == cached

    def test_parse_fore(self):
        parsed = parse_en_pl(html["fore"])
        cached = load_json("fore")
        assert parsed == cached

    def test_parse_paulownia(self):
        parsed = parse_en_pl(html["paulownia"])
        cached = load_json("paulownia")
        assert parsed == cached

    def test_parse_apologetic(self):
        parsed = parse_en_pl(html["apologetic"])
        cached = load_json("apologetic")
        assert parsed == cached

    def test_parse_enticing(self):
        parsed = parse_en_pl(html["enticing"])
        cached = load_json("enticing")
        assert parsed == cached

    def test_parse_ensconced(self):
        parsed = parse_en_pl(html["ensconced"])
        cached = load_json("ensconced")
        assert parsed == cached

    def test_parse_lead(self):
        parsed = parse_en_pl(html["lead"])
        cached = load_json("lead")
        assert parsed == cached

    def test_parse_jilted(self):
        parsed = parse_en_pl(html["jilted"])
        cached = load_json("jilted")
        assert parsed == cached

    def test_parse_antecedent(self):
        parsed = parse_en_pl(html["antecedent"])
        cached = load_json("antecedent")
        assert parsed == cached

    def test_parse_meandering(self):
        parsed = parse_en_pl(html["meandering"])
        cached = load_json("meandering")
        assert parsed == cached

    def test_parse_zealot(self):
        parsed = parse_en_pl(html["zealot"])
        cached = load_json("zealot")
        assert parsed == cached

    def test_parse_rudderless(self):
        parsed = parse_en_pl(html["rudderless"])
        cached = load_json("rudderless")
        assert parsed == cached

    def test_parse_judicious(self):
        parsed = parse_en_pl(html["judicious"])
        cached = load_json("judicious")
        assert parsed == cached

    def test_parse_promiscuous(self):
        parsed = parse_en_pl(html["promiscuous"])
        cached = load_json("promiscuous")
        assert parsed == cached

    def test_parse_squirm(self):
        parsed = parse_en_pl(html["squirm"])
        cached = load_json("squirm")
        assert parsed == cached

    def test_parse_gallantry(self):
        parsed = parse_en_pl(html["gallantry"])
        cached = load_json("gallantry")
        assert parsed == cached

    def test_parse_forestall(self):
        parsed = parse_en_pl(html["forestall"])
        cached = load_json("forestall")
        assert parsed == cached

    def test_parse_incessantly(self):
        parsed = parse_en_pl(html["incessantly"])
        cached = load_json("incessantly")
        assert parsed == cached

    def test_parse_esoteric(self):
        parsed = parse_en_pl(html["esoteric"])
        cached = load_json("esoteric")
        assert parsed == cached

    def test_parse_banter(self):
        parsed = parse_en_pl(html["banter"])
        cached = load_json("banter")
        assert parsed == cached

    def test_parse_injective(self):
        parsed = parse_en_pl(html["injective"])
        cached = load_json("injective")
        assert parsed == cached

    def test_parse_environment(self):
        parsed = parse_en_pl(html["environment"])
        cached = load_json("environment")
        assert parsed == cached

    def test_parse_tentative(self):
        parsed = parse_en_pl(html["tentative"])
        cached = load_json("tentative")
        assert parsed == cached

    def test_parse_jarring(self):
        parsed = parse_en_pl(html["jarring"])
        cached = load_json("jarring")
        assert parsed == cached

    def test_parse_moot(self):
        parsed = parse_en_pl(html["moot"])
        cached = load_json("moot")
        assert parsed == cached

    def test_parse_faze(self):
        parsed = parse_en_pl(html["faze"])
        cached = load_json("faze")
        assert parsed == cached

    def test_parse_strain(self):
        parsed = parse_en_pl(html["strain"])
        cached = load_json("strain")
        assert parsed == cached

    def test_parse_lath(self):
        parsed = parse_en_pl(html["lath"])
        cached = load_json("lath")
        assert parsed == cached

    def test_parse_miscarry(self):
        parsed = parse_en_pl(html["miscarry"])
        cached = load_json("miscarry")
        assert parsed == cached

    def test_parse_contingency(self):
        parsed = parse_en_pl(html["contingency"])
        cached = load_json("contingency")
        assert parsed == cached

    def test_parse_conceit(self):
        parsed = parse_en_pl(html["conceit"])
        cached = load_json("conceit")
        assert parsed == cached

    def test_parse_invalidate(self):
        parsed = parse_en_pl(html["invalidate"])
        cached = load_json("invalidate")
        assert parsed == cached

    def test_parse_malaise(self):
        parsed = parse_en_pl(html["malaise"])
        cached = load_json("malaise")
        assert parsed == cached

    def test_parse_resolute(self):
        parsed = parse_en_pl(html["resolute"])
        cached = load_json("resolute")
        assert parsed == cached

    def test_parse_fidget(self):
        parsed = parse_en_pl(html["fidget"])
        cached = load_json("fidget")
        assert parsed == cached

    def test_parse_crux(self):
        parsed = parse_en_pl(html["crux"])
        cached = load_json("crux")
        assert parsed == cached

    def test_parse_flip(self):
        parsed = parse_en_pl(html["flip"])
        cached = load_json("flip")
        assert parsed == cached

    def test_parse_gorgeous(self):
        parsed = parse_en_pl(html["gorgeous"])
        cached = load_json("gorgeous")
        assert parsed == cached

    def test_parse_lupus(self):
        parsed = parse_en_pl(html["lupus"])
        cached = load_json("lupus")
        assert parsed == cached

    def test_parse_Mongoloid(self):
        parsed = parse_en_pl(html["Mongoloid"])
        cached = load_json("Mongoloid")
        assert parsed == cached

    def test_parse_serpentine(self):
        parsed = parse_en_pl(html["serpentine"])
        cached = load_json("serpentine")
        assert parsed == cached

    def test_parse_pancreas(self):
        parsed = parse_en_pl(html["pancreas"])
        cached = load_json("pancreas")
        assert parsed == cached

    def test_parse_poultry(self):
        parsed = parse_en_pl(html["poultry"])
        cached = load_json("poultry")
        assert parsed == cached

    def test_parse_explicit(self):
        parsed = parse_en_pl(html["explicit"])
        cached = load_json("explicit")
        assert parsed == cached

    def test_parse_gander(self):
        parsed = parse_en_pl(html["gander"])
        cached = load_json("gander")
        assert parsed == cached

    def test_parse_palliate(self):
        parsed = parse_en_pl(html["palliate"])
        cached = load_json("palliate")
        assert parsed == cached

    def test_parse_lay(self):
        parsed = parse_en_pl(html["lay"])
        cached = load_json("lay")
        assert parsed == cached

    def test_parse_deferential(self):
        parsed = parse_en_pl(html["deferential"])
        cached = load_json("deferential")
        assert parsed == cached

    def test_parse_interleaving(self):
        parsed = parse_en_pl(html["interleaving"])
        cached = load_json("interleaving")
        assert parsed == cached

    def test_parse_travesty(self):
        parsed = parse_en_pl(html["travesty"])
        cached = load_json("travesty")
        assert parsed == cached

    def test_parse_spindly(self):
        parsed = parse_en_pl(html["spindly"])
        cached = load_json("spindly")
        assert parsed == cached

    def test_parse_quail(self):
        parsed = parse_en_pl(html["quail"])
        cached = load_json("quail")
        assert parsed == cached

    def test_parse_southpaw(self):
        parsed = parse_en_pl(html["southpaw"])
        cached = load_json("southpaw")
        assert parsed == cached

    def test_parse_trampled(self):
        parsed = parse_en_pl(html["trampled"])
        cached = load_json("trampled")
        assert parsed == cached

    def test_parse_furlough(self):
        parsed = parse_en_pl(html["furlough"])
        cached = load_json("furlough")
        assert parsed == cached

    def test_parse_trifling(self):
        parsed = parse_en_pl(html["trifling"])
        cached = load_json("trifling")
        assert parsed == cached

    def test_parse_repudiation(self):
        parsed = parse_en_pl(html["repudiation"])
        cached = load_json("repudiation")
        assert parsed == cached

    def test_parse_implicit(self):
        parsed = parse_en_pl(html["implicit"])
        cached = load_json("implicit")
        assert parsed == cached

    def test_parse_recoil(self):
        parsed = parse_en_pl(html["recoil"])
        cached = load_json("recoil")
        assert parsed == cached

    def test_parse_provenance(self):
        parsed = parse_en_pl(html["provenance"])
        cached = load_json("provenance")
        assert parsed == cached

    def test_parse_overzealous(self):
        parsed = parse_en_pl(html["overzealous"])
        cached = load_json("overzealous")
        assert parsed == cached

    def test_parse_exhortation(self):
        parsed = parse_en_pl(html["exhortation"])
        cached = load_json("exhortation")
        assert parsed == cached

    def test_parse_implacable(self):
        parsed = parse_en_pl(html["implacable"])
        cached = load_json("implacable")
        assert parsed == cached

    def test_parse_mumble(self):
        parsed = parse_en_pl(html["mumble"])
        cached = load_json("mumble")
        assert parsed == cached

    def test_parse_rube(self):
        parsed = parse_en_pl(html["rube"])
        cached = load_json("rube")
        assert parsed == cached

    def test_parse_ennui(self):
        parsed = parse_en_pl(html["ennui"])
        cached = load_json("ennui")
        assert parsed == cached

    def test_parse_chastised(self):
        parsed = parse_en_pl(html["chastised"])
        cached = load_json("chastised")
        assert parsed == cached

    def test_parse_nous(self):
        parsed = parse_en_pl(html["nous"])
        cached = load_json("nous")
        assert parsed == cached

    def test_parse_elope(self):
        parsed = parse_en_pl(html["elope"])
        cached = load_json("elope")
        assert parsed == cached

    def test_parse_conch(self):
        parsed = parse_en_pl(html["conch"])
        cached = load_json("conch")
        assert parsed == cached

    def test_parse_nab(self):
        parsed = parse_en_pl(html["nab"])
        cached = load_json("nab")
        assert parsed == cached

    def test_parse_untether(self):
        parsed = parse_en_pl(html["untether"])
        cached = load_json("untether")
        assert parsed == cached

    def test_parse_septum(self):
        parsed = parse_en_pl(html["septum"])
        cached = load_json("septum")
        assert parsed == cached

    def test_parse_redress(self):
        parsed = parse_en_pl(html["redress"])
        cached = load_json("redress")
        assert parsed == cached

    def test_parse_weight(self):
        parsed = parse_en_pl(html["weight"])
        cached = load_json("weight")
        assert parsed == cached

    def test_parse_folly(self):
        parsed = parse_en_pl(html["folly"])
        cached = load_json("folly")
        assert parsed == cached

    def test_parse_hernia(self):
        parsed = parse_en_pl(html["hernia"])
        cached = load_json("hernia")
        assert parsed == cached

    def test_parse_brained(self):
        parsed = parse_en_pl(html["brained"])
        cached = load_json("brained")
        assert parsed == cached

    def test_parse_vexed(self):
        parsed = parse_en_pl(html["vexed"])
        cached = load_json("vexed")
        assert parsed == cached

    def test_parse_riff(self):
        parsed = parse_en_pl(html["riff"])
        cached = load_json("riff")
        assert parsed == cached

    def test_parse_maggot(self):
        parsed = parse_en_pl(html["maggot"])
        cached = load_json("maggot")
        assert parsed == cached

    def test_parse_serfdom(self):
        parsed = parse_en_pl(html["serfdom"])
        cached = load_json("serfdom")
        assert parsed == cached

    def test_parse_raunchy(self):
        parsed = parse_en_pl(html["raunchy"])
        cached = load_json("raunchy")
        assert parsed == cached

    def test_parse_impressively(self):
        parsed = parse_en_pl(html["impressively"])
        cached = load_json("impressively")
        assert parsed == cached

    def test_parse_rehearse(self):
        parsed = parse_en_pl(html["rehearse"])
        cached = load_json("rehearse")
        assert parsed == cached

    def test_parse_travail(self):
        parsed = parse_en_pl(html["travail"])
        cached = load_json("travail")
        assert parsed == cached

    def test_parse_propensity(self):
        parsed = parse_en_pl(html["propensity"])
        cached = load_json("propensity")
        assert parsed == cached

    def test_parse_influx(self):
        parsed = parse_en_pl(html["influx"])
        cached = load_json("influx")
        assert parsed == cached

    def test_parse_opaque(self):
        parsed = parse_en_pl(html["opaque"])
        cached = load_json("opaque")
        assert parsed == cached

    def test_parse_shibboleth(self):
        parsed = parse_en_pl(html["shibboleth"])
        cached = load_json("shibboleth")
        assert parsed == cached

    def test_parse_scorn(self):
        parsed = parse_en_pl(html["scorn"])
        cached = load_json("scorn")
        assert parsed == cached

    def test_parse_pilfer(self):
        parsed = parse_en_pl(html["pilfer"])
        cached = load_json("pilfer")
        assert parsed == cached

    def test_parse_asphyxiation(self):
        parsed = parse_en_pl(html["asphyxiation"])
        cached = load_json("asphyxiation")
        assert parsed == cached

    def test_parse_lethargy(self):
        parsed = parse_en_pl(html["lethargy"])
        cached = load_json("lethargy")
        assert parsed == cached

    def test_parse_unequivocal(self):
        parsed = parse_en_pl(html["unequivocal"])
        cached = load_json("unequivocal")
        assert parsed == cached

    def test_parse_converse(self):
        parsed = parse_en_pl(html["converse"])
        cached = load_json("converse")
        assert parsed == cached

    def test_parse_parlor(self):
        parsed = parse_en_pl(html["parlor"])
        cached = load_json("parlor")
        assert parsed == cached

    def test_parse_latch(self):
        parsed = parse_en_pl(html["latch"])
        cached = load_json("latch")
        assert parsed == cached

    def test_parse_expedient(self):
        parsed = parse_en_pl(html["expedient"])
        cached = load_json("expedient")
        assert parsed == cached

    def test_parse_reimburse(self):
        parsed = parse_en_pl(html["reimburse"])
        cached = load_json("reimburse")
        assert parsed == cached

    def test_parse_bruin(self):
        parsed = parse_en_pl(html["bruin"])
        cached = load_json("bruin")
        assert parsed == cached

    def test_parse_stepchild(self):
        parsed = parse_en_pl(html["stepchild"])
        cached = load_json("stepchild")
        assert parsed == cached

    def test_parse_lackey(self):
        parsed = parse_en_pl(html["lackey"])
        cached = load_json("lackey")
        assert parsed == cached

    def test_parse_rap(self):
        parsed = parse_en_pl(html["rap"])
        cached = load_json("rap")
        assert parsed == cached

    def test_parse_Melanoma(self):
        parsed = parse_en_pl(html["Melanoma"])
        cached = load_json("Melanoma")
        assert parsed == cached

    def test_parse_hefty(self):
        parsed = parse_en_pl(html["hefty"])
        cached = load_json("hefty")
        assert parsed == cached

    def test_parse_monosomy(self):
        parsed = parse_en_pl(html["monosomy"])
        cached = load_json("monosomy")
        assert parsed == cached

    def test_parse_penitence(self):
        parsed = parse_en_pl(html["penitence"])
        cached = load_json("penitence")
        assert parsed == cached

    def test_parse_backlash(self):
        parsed = parse_en_pl(html["backlash"])
        cached = load_json("backlash")
        assert parsed == cached

    def test_parse_onerous(self):
        parsed = parse_en_pl(html["onerous"])
        cached = load_json("onerous")
        assert parsed == cached

    def test_parse_ailing(self):
        parsed = parse_en_pl(html["ailing"])
        cached = load_json("ailing")
        assert parsed == cached

    def test_parse_sternum(self):
        parsed = parse_en_pl(html["sternum"])
        cached = load_json("sternum")
        assert parsed == cached

    def test_parse_chasten(self):
        parsed = parse_en_pl(html["chasten"])
        cached = load_json("chasten")
        assert parsed == cached

    def test_parse_beleaguer(self):
        parsed = parse_en_pl(html["beleaguer"])
        cached = load_json("beleaguer")
        assert parsed == cached

    def test_parse_genuinely(self):
        parsed = parse_en_pl(html["genuinely"])
        cached = load_json("genuinely")
        assert parsed == cached

    def test_parse_piteously(self):
        parsed = parse_en_pl(html["piteously"])
        cached = load_json("piteously")
        assert parsed == cached

    def test_parse_larceny(self):
        parsed = parse_en_pl(html["larceny"])
        cached = load_json("larceny")
        assert parsed == cached

    def test_parse_insurmountable(self):
        parsed = parse_en_pl(html["insurmountable"])
        cached = load_json("insurmountable")
        assert parsed == cached

    def test_parse_extirpation(self):
        parsed = parse_en_pl(html["extirpation"])
        cached = load_json("extirpation")
        assert parsed == cached

    def test_parse_ventriloquist(self):
        parsed = parse_en_pl(html["ventriloquist"])
        cached = load_json("ventriloquist")
        assert parsed == cached

    def test_parse_innocuous(self):
        parsed = parse_en_pl(html["innocuous"])
        cached = load_json("innocuous")
        assert parsed == cached

    def test_parse_remedial(self):
        parsed = parse_en_pl(html["remedial"])
        cached = load_json("remedial")
        assert parsed == cached

    def test_parse_bickering(self):
        parsed = parse_en_pl(html["bickering"])
        cached = load_json("bickering")
        assert parsed == cached

    def test_parse_unilaterally(self):
        parsed = parse_en_pl(html["unilaterally"])
        cached = load_json("unilaterally")
        assert parsed == cached

    def test_parse_attaboy(self):
        parsed = parse_en_pl(html["attaboy"])
        cached = load_json("attaboy")
        assert parsed == cached

    def test_parse_continuous(self):
        parsed = parse_en_pl(html["continuous"])
        cached = load_json("continuous")
        assert parsed == cached

    def test_parse_mullet(self):
        parsed = parse_en_pl(html["mullet"])
        cached = load_json("mullet")
        assert parsed == cached

    def test_parse_acrimony(self):
        parsed = parse_en_pl(html["acrimony"])
        cached = load_json("acrimony")
        assert parsed == cached

    def test_parse_glib(self):
        parsed = parse_en_pl(html["glib"])
        cached = load_json("glib")
        assert parsed == cached

    def test_parse_fray(self):
        parsed = parse_en_pl(html["fray"])
        cached = load_json("fray")
        assert parsed == cached

    def test_parse_mundane(self):
        parsed = parse_en_pl(html["mundane"])
        cached = load_json("mundane")
        assert parsed == cached

    def test_parse_haptic(self):
        parsed = parse_en_pl(html["haptic"])
        cached = load_json("haptic")
        assert parsed == cached

    def test_parse_relenting(self):
        parsed = parse_en_pl(html["relenting"])
        cached = load_json("relenting")
        assert parsed == cached

    def test_parse_grandiose(self):
        parsed = parse_en_pl(html["grandiose"])
        cached = load_json("grandiose")
        assert parsed == cached

    def test_parse_wacky(self):
        parsed = parse_en_pl(html["wacky"])
        cached = load_json("wacky")
        assert parsed == cached

    def test_parse_engender(self):
        parsed = parse_en_pl(html["engender"])
        cached = load_json("engender")
        assert parsed == cached

    def test_parse_nowt(self):
        parsed = parse_en_pl(html["nowt"])
        cached = load_json("nowt")
        assert parsed == cached

    def test_parse_wispy(self):
        parsed = parse_en_pl(html["wispy"])
        cached = load_json("wispy")
        assert parsed == cached

    def test_parse_left(self):
        parsed = parse_en_pl(html["left"])
        cached = load_json("left")
        assert parsed == cached

    def test_parse_hip(self):
        parsed = parse_en_pl(html["hip"])
        cached = load_json("hip")
        assert parsed == cached

    def test_parse_transience(self):
        parsed = parse_en_pl(html["transience"])
        cached = load_json("transience")
        assert parsed == cached

    def test_parse_parsnips(self):
        parsed = parse_en_pl(html["parsnips"])
        cached = load_json("parsnips")
        assert parsed == cached

    def test_parse_work(self):
        parsed = parse_en_pl(html["work"])
        cached = load_json("work")
        assert parsed == cached

    def test_parse_shoddy(self):
        parsed = parse_en_pl(html["shoddy"])
        cached = load_json("shoddy")
        assert parsed == cached

    def test_parse_ochre(self):
        parsed = parse_en_pl(html["ochre"])
        cached = load_json("ochre")
        assert parsed == cached

    def test_parse_coerce(self):
        parsed = parse_en_pl(html["coerce"])
        cached = load_json("coerce")
        assert parsed == cached

    def test_parse_castigate(self):
        parsed = parse_en_pl(html["castigate"])
        cached = load_json("castigate")
        assert parsed == cached

    def test_parse_loftiness(self):
        parsed = parse_en_pl(html["loftiness"])
        cached = load_json("loftiness")
        assert parsed == cached

    def test_parse_wand(self):
        parsed = parse_en_pl(html["wand"])
        cached = load_json("wand")
        assert parsed == cached

    def test_parse_barren(self):
        parsed = parse_en_pl(html["barren"])
        cached = load_json("barren")
        assert parsed == cached

    def test_parse_bras(self):
        parsed = parse_en_pl(html["bras"])
        cached = load_json("bras")
        assert parsed == cached

    def test_parse_recondite(self):
        parsed = parse_en_pl(html["recondite"])
        cached = load_json("recondite")
        assert parsed == cached

    def test_parse_derision(self):
        parsed = parse_en_pl(html["derision"])
        cached = load_json("derision")
        assert parsed == cached

    def test_parse_pelvis(self):
        parsed = parse_en_pl(html["pelvis"])
        cached = load_json("pelvis")
        assert parsed == cached

    def test_parse_tacky(self):
        parsed = parse_en_pl(html["tacky"])
        cached = load_json("tacky")
        assert parsed == cached

    def test_parse_pail(self):
        parsed = parse_en_pl(html["pail"])
        cached = load_json("pail")
        assert parsed == cached

    def test_parse_pernicious(self):
        parsed = parse_en_pl(html["pernicious"])
        cached = load_json("pernicious")
        assert parsed == cached

    def test_parse_flagrantly(self):
        parsed = parse_en_pl(html["flagrantly"])
        cached = load_json("flagrantly")
        assert parsed == cached

    def test_parse_emphysema(self):
        parsed = parse_en_pl(html["emphysema"])
        cached = load_json("emphysema")
        assert parsed == cached

    def test_parse_streak(self):
        parsed = parse_en_pl(html["streak"])
        cached = load_json("streak")
        assert parsed == cached

    def test_parse_yttrium(self):
        parsed = parse_en_pl(html["yttrium"])
        cached = load_json("yttrium")
        assert parsed == cached

    def test_parse_jocular(self):
        parsed = parse_en_pl(html["jocular"])
        cached = load_json("jocular")
        assert parsed == cached

    def test_parse_obstinate(self):
        parsed = parse_en_pl(html["obstinate"])
        cached = load_json("obstinate")
        assert parsed == cached

    def test_parse_protruding(self):
        parsed = parse_en_pl(html["protruding"])
        cached = load_json("protruding")
        assert parsed == cached

    def test_parse_nudge(self):
        parsed = parse_en_pl(html["nudge"])
        cached = load_json("nudge")
        assert parsed == cached

    def test_parse_apprehensive(self):
        parsed = parse_en_pl(html["apprehensive"])
        cached = load_json("apprehensive")
        assert parsed == cached

    def test_parse_squash(self):
        parsed = parse_en_pl(html["squash"])
        cached = load_json("squash")
        assert parsed == cached

    def test_parse_udder(self):
        parsed = parse_en_pl(html["udder"])
        cached = load_json("udder")
        assert parsed == cached

    def test_parse_prevalent(self):
        parsed = parse_en_pl(html["prevalent"])
        cached = load_json("prevalent")
        assert parsed == cached

    def test_parse_eal(self):
        parsed = parse_en_pl(html["eal"])
        cached = load_json("eal")
        assert parsed == cached

    def test_parse_scholarly(self):
        parsed = parse_en_pl(html["scholarly"])
        cached = load_json("scholarly")
        assert parsed == cached

    def test_parse_rye(self):
        parsed = parse_en_pl(html["rye"])
        cached = load_json("rye")
        assert parsed == cached

    def test_parse_belligerent(self):
        parsed = parse_en_pl(html["belligerent"])
        cached = load_json("belligerent")
        assert parsed == cached

    def test_parse_loquacious(self):
        parsed = parse_en_pl(html["loquacious"])
        cached = load_json("loquacious")
        assert parsed == cached

    def test_parse_extracurricular(self):
        parsed = parse_en_pl(html["extracurricular"])
        cached = load_json("extracurricular")
        assert parsed == cached

    def test_parse_inextricably(self):
        parsed = parse_en_pl(html["inextricably"])
        cached = load_json("inextricably")
        assert parsed == cached

    def test_parse_graceful(self):
        parsed = parse_en_pl(html["graceful"])
        cached = load_json("graceful")
        assert parsed == cached

    def test_parse_sybaritic(self):
        parsed = parse_en_pl(html["sybaritic"])
        cached = load_json("sybaritic")
        assert parsed == cached

    def test_parse_broad(self):
        parsed = parse_en_pl(html["broad"])
        cached = load_json("broad")
        assert parsed == cached

    def test_parse_inconvenience(self):
        parsed = parse_en_pl(html["inconvenience"])
        cached = load_json("inconvenience")
        assert parsed == cached

    def test_parse_rejoice(self):
        parsed = parse_en_pl(html["rejoice"])
        cached = load_json("rejoice")
        assert parsed == cached

    def test_parse_vagrancy(self):
        parsed = parse_en_pl(html["vagrancy"])
        cached = load_json("vagrancy")
        assert parsed == cached

    def test_parse_vexatious(self):
        parsed = parse_en_pl(html["vexatious"])
        cached = load_json("vexatious")
        assert parsed == cached

    def test_parse_spook(self):
        parsed = parse_en_pl(html["spook"])
        cached = load_json("spook")
        assert parsed == cached

    def test_parse_glimpsing(self):
        parsed = parse_en_pl(html["glimpsing"])
        cached = load_json("glimpsing")
        assert parsed == cached

    def test_parse_wallow(self):
        parsed = parse_en_pl(html["wallow"])
        cached = load_json("wallow")
        assert parsed == cached

    def test_parse_strife(self):
        parsed = parse_en_pl(html["strife"])
        cached = load_json("strife")
        assert parsed == cached

    def test_parse_tone_deaf(self):
        parsed = parse_en_pl(html["tone-deaf"])
        cached = load_json("tone-deaf")
        assert parsed == cached

    def test_parse_triage(self):
        parsed = parse_en_pl(html["triage"])
        cached = load_json("triage")
        assert parsed == cached

    def test_parse_heiress(self):
        parsed = parse_en_pl(html["heiress"])
        cached = load_json("heiress")
        assert parsed == cached

    def test_parse_slither(self):
        parsed = parse_en_pl(html["slither"])
        cached = load_json("slither")
        assert parsed == cached

    def test_parse_sanctity(self):
        parsed = parse_en_pl(html["sanctity"])
        cached = load_json("sanctity")
        assert parsed == cached

    def test_parse_penultimate(self):
        parsed = parse_en_pl(html["penultimate"])
        cached = load_json("penultimate")
        assert parsed == cached

    def test_parse_gimpy(self):
        parsed = parse_en_pl(html["gimpy"])
        cached = load_json("gimpy")
        assert parsed == cached

    def test_parse_neural(self):
        parsed = parse_en_pl(html["neural"])
        cached = load_json("neural")
        assert parsed == cached

    def test_parse_preserve(self):
        parsed = parse_en_pl(html["preserve"])
        cached = load_json("preserve")
        assert parsed == cached

    def test_parse_prodigious(self):
        parsed = parse_en_pl(html["prodigious"])
        cached = load_json("prodigious")
        assert parsed == cached

    def test_parse_inept(self):
        parsed = parse_en_pl(html["inept"])
        cached = load_json("inept")
        assert parsed == cached

    def test_parse_oedipal(self):
        parsed = parse_en_pl(html["oedipal"])
        cached = load_json("oedipal")
        assert parsed == cached

    def test_parse_coifs(self):
        parsed = parse_en_pl(html["coifs"])
        cached = load_json("coifs")
        assert parsed == cached

    def test_parse_astray(self):
        parsed = parse_en_pl(html["astray"])
        cached = load_json("astray")
        assert parsed == cached

    def test_parse_gawp(self):
        parsed = parse_en_pl(html["gawp"])
        cached = load_json("gawp")
        assert parsed == cached

    def test_parse_escarpment(self):
        parsed = parse_en_pl(html["escarpment"])
        cached = load_json("escarpment")
        assert parsed == cached

    def test_parse_acrimoniously(self):
        parsed = parse_en_pl(html["acrimoniously"])
        cached = load_json("acrimoniously")
        assert parsed == cached

    def test_parse_muppet(self):
        parsed = parse_en_pl(html["muppet"])
        cached = load_json("muppet")
        assert parsed == cached

    def test_parse_unwavering(self):
        parsed = parse_en_pl(html["unwavering"])
        cached = load_json("unwavering")
        assert parsed == cached

    def test_parse_reciprocal(self):
        parsed = parse_en_pl(html["reciprocal"])
        cached = load_json("reciprocal")
        assert parsed == cached

    def test_parse_mediocre(self):
        parsed = parse_en_pl(html["mediocre"])
        cached = load_json("mediocre")
        assert parsed == cached

    def test_parse_jubilee(self):
        parsed = parse_en_pl(html["jubilee"])
        cached = load_json("jubilee")
        assert parsed == cached

    def test_parse_culpable(self):
        parsed = parse_en_pl(html["culpable"])
        cached = load_json("culpable")
        assert parsed == cached

    def test_parse_obsequious(self):
        parsed = parse_en_pl(html["obsequious"])
        cached = load_json("obsequious")
        assert parsed == cached

    def test_parse_doldrums(self):
        parsed = parse_en_pl(html["doldrums"])
        cached = load_json("doldrums")
        assert parsed == cached

    def test_parse_jeremiad(self):
        parsed = parse_en_pl(html["jeremiad"])
        cached = load_json("jeremiad")
        assert parsed == cached

    def test_parse_extortion(self):
        parsed = parse_en_pl(html["extortion"])
        cached = load_json("extortion")
        assert parsed == cached

    def test_parse_willy_nilly(self):
        parsed = parse_en_pl(html["willy-nilly"])
        cached = load_json("willy-nilly")
        assert parsed == cached

    def test_parse_condescend(self):
        parsed = parse_en_pl(html["condescend"])
        cached = load_json("condescend")
        assert parsed == cached

    def test_parse_shingle(self):
        parsed = parse_en_pl(html["shingle"])
        cached = load_json("shingle")
        assert parsed == cached

    def test_parse_lisp(self):
        parsed = parse_en_pl(html["lisp"])
        cached = load_json("lisp")
        assert parsed == cached

    def test_parse_turmoil(self):
        parsed = parse_en_pl(html["turmoil"])
        cached = load_json("turmoil")
        assert parsed == cached

    def test_parse_stillbirth(self):
        parsed = parse_en_pl(html["stillbirth"])
        cached = load_json("stillbirth")
        assert parsed == cached

    def test_parse_knurled(self):
        parsed = parse_en_pl(html["knurled"])
        cached = load_json("knurled")
        assert parsed == cached

    def test_parse_foul(self):
        parsed = parse_en_pl(html["foul"])
        cached = load_json("foul")
        assert parsed == cached

    def test_parse_verbose(self):
        parsed = parse_en_pl(html["verbose"])
        cached = load_json("verbose")
        assert parsed == cached

    def test_parse_pander(self):
        parsed = parse_en_pl(html["pander"])
        cached = load_json("pander")
        assert parsed == cached

    def test_parse_eclectic(self):
        parsed = parse_en_pl(html["eclectic"])
        cached = load_json("eclectic")
        assert parsed == cached

    def test_parse_catering(self):
        parsed = parse_en_pl(html["catering"])
        cached = load_json("catering")
        assert parsed == cached

    def test_parse_limber(self):
        parsed = parse_en_pl(html["limber"])
        cached = load_json("limber")
        assert parsed == cached

    def test_parse_lateral(self):
        parsed = parse_en_pl(html["lateral"])
        cached = load_json("lateral")
        assert parsed == cached

    def test_parse_gland(self):
        parsed = parse_en_pl(html["gland"])
        cached = load_json("gland")
        assert parsed == cached

    def test_parse_implicated(self):
        parsed = parse_en_pl(html["implicated"])
        cached = load_json("implicated")
        assert parsed == cached

    def test_parse_vigilant(self):
        parsed = parse_en_pl(html["vigilant"])
        cached = load_json("vigilant")
        assert parsed == cached

    def test_parse_urea(self):
        parsed = parse_en_pl(html["urea"])
        cached = load_json("urea")
        assert parsed == cached

    def test_parse_thoroughfare(self):
        parsed = parse_en_pl(html["thoroughfare"])
        cached = load_json("thoroughfare")
        assert parsed == cached

    def test_parse_slavishly(self):
        parsed = parse_en_pl(html["slavishly"])
        cached = load_json("slavishly")
        assert parsed == cached

    def test_parse_famine(self):
        parsed = parse_en_pl(html["famine"])
        cached = load_json("famine")
        assert parsed == cached

    def test_parse_expedite(self):
        parsed = parse_en_pl(html["expedite"])
        cached = load_json("expedite")
        assert parsed == cached

    def test_parse_meticulous(self):
        parsed = parse_en_pl(html["meticulous"])
        cached = load_json("meticulous")
        assert parsed == cached

    def test_parse_maple(self):
        parsed = parse_en_pl(html["maple"])
        cached = load_json("maple")
        assert parsed == cached

    def test_parse_rank(self):
        parsed = parse_en_pl(html["rank"])
        cached = load_json("rank")
        assert parsed == cached

    def test_parse_contraption(self):
        parsed = parse_en_pl(html["contraption"])
        cached = load_json("contraption")
        assert parsed == cached

    def test_parse_clutter(self):
        parsed = parse_en_pl(html["clutter"])
        cached = load_json("clutter")
        assert parsed == cached

    def test_parse_now(self):
        parsed = parse_en_pl(html["now"])
        cached = load_json("now")
        assert parsed == cached

    def test_parse_grower(self):
        parsed = parse_en_pl(html["grower"])
        cached = load_json("grower")
        assert parsed == cached

    def test_parse_lectern(self):
        parsed = parse_en_pl(html["lectern"])
        cached = load_json("lectern")
        assert parsed == cached

    def test_parse_solemnity(self):
        parsed = parse_en_pl(html["solemnity"])
        cached = load_json("solemnity")
        assert parsed == cached

    def test_parse_heckler(self):
        parsed = parse_en_pl(html["heckler"])
        cached = load_json("heckler")
        assert parsed == cached

    def test_parse_ensue(self):
        parsed = parse_en_pl(html["ensue"])
        cached = load_json("ensue")
        assert parsed == cached

    def test_parse_encumber(self):
        parsed = parse_en_pl(html["encumber"])
        cached = load_json("encumber")
        assert parsed == cached

    def test_parse_swamped(self):
        parsed = parse_en_pl(html["swamped"])
        cached = load_json("swamped")
        assert parsed == cached

    def test_parse_futilely(self):
        parsed = parse_en_pl(html["futilely"])
        cached = load_json("futilely")
        assert parsed == cached

    def test_parse_angler(self):
        parsed = parse_en_pl(html["angler"])
        cached = load_json("angler")
        assert parsed == cached

    def test_parse_medicore(self):
        parsed = parse_en_pl(html["medicore"])
        cached = load_json("medicore")
        assert parsed == cached

    def test_parse_wean(self):
        parsed = parse_en_pl(html["wean"])
        cached = load_json("wean")
        assert parsed == cached

    def test_parse_fusillade(self):
        parsed = parse_en_pl(html["fusillade"])
        cached = load_json("fusillade")
        assert parsed == cached

    def test_parse_slender(self):
        parsed = parse_en_pl(html["slender"])
        cached = load_json("slender")
        assert parsed == cached

    def test_parse_kismet(self):
        parsed = parse_en_pl(html["kismet"])
        cached = load_json("kismet")
        assert parsed == cached

    def test_parse_nunnery(self):
        parsed = parse_en_pl(html["nunnery"])
        cached = load_json("nunnery")
        assert parsed == cached

    def test_parse_truce(self):
        parsed = parse_en_pl(html["truce"])
        cached = load_json("truce")
        assert parsed == cached

    def test_parse_dismay(self):
        parsed = parse_en_pl(html["dismay"])
        cached = load_json("dismay")
        assert parsed == cached

    def test_parse_intercede(self):
        parsed = parse_en_pl(html["intercede"])
        cached = load_json("intercede")
        assert parsed == cached

    def test_parse_accolade(self):
        parsed = parse_en_pl(html["accolade"])
        cached = load_json("accolade")
        assert parsed == cached

    def test_parse_ladle(self):
        parsed = parse_en_pl(html["ladle"])
        cached = load_json("ladle")
        assert parsed == cached

    def test_parse_assess(self):
        parsed = parse_en_pl(html["assess"])
        cached = load_json("assess")
        assert parsed == cached

    def test_parse_intricate(self):
        parsed = parse_en_pl(html["intricate"])
        cached = load_json("intricate")
        assert parsed == cached

    def test_parse_satchel(self):
        parsed = parse_en_pl(html["satchel"])
        cached = load_json("satchel")
        assert parsed == cached

    def test_parse_virility(self):
        parsed = parse_en_pl(html["virility"])
        cached = load_json("virility")
        assert parsed == cached

    def test_parse_rakish(self):
        parsed = parse_en_pl(html["rakish"])
        cached = load_json("rakish")
        assert parsed == cached

    def test_parse_abscond(self):
        parsed = parse_en_pl(html["abscond"])
        cached = load_json("abscond")
        assert parsed == cached

    def test_parse_sartorial(self):
        parsed = parse_en_pl(html["sartorial"])
        cached = load_json("sartorial")
        assert parsed == cached

    def test_parse_venison(self):
        parsed = parse_en_pl(html["venison"])
        cached = load_json("venison")
        assert parsed == cached

    def test_parse_litigate(self):
        parsed = parse_en_pl(html["litigate"])
        cached = load_json("litigate")
        assert parsed == cached

    def test_parse_vagrant(self):
        parsed = parse_en_pl(html["vagrant"])
        cached = load_json("vagrant")
        assert parsed == cached

    def test_parse_staid(self):
        parsed = parse_en_pl(html["staid"])
        cached = load_json("staid")
        assert parsed == cached

    def test_parse_superlative(self):
        parsed = parse_en_pl(html["superlative"])
        cached = load_json("superlative")
        assert parsed == cached

    def test_parse_dotage(self):
        parsed = parse_en_pl(html["dotage"])
        cached = load_json("dotage")
        assert parsed == cached

    def test_parse_gobble(self):
        parsed = parse_en_pl(html["gobble"])
        cached = load_json("gobble")
        assert parsed == cached

    def test_parse_procession(self):
        parsed = parse_en_pl(html["procession"])
        cached = load_json("procession")
        assert parsed == cached

    def test_parse_snarky(self):
        parsed = parse_en_pl(html["snarky"])
        cached = load_json("snarky")
        assert parsed == cached

    def test_parse_adherence(self):
        parsed = parse_en_pl(html["adherence"])
        cached = load_json("adherence")
        assert parsed == cached

    def test_parse_fledgling(self):
        parsed = parse_en_pl(html["fledgling"])
        cached = load_json("fledgling")
        assert parsed == cached

    def test_parse_pastie(self):
        parsed = parse_en_pl(html["pastie"])
        cached = load_json("pastie")
        assert parsed == cached

    def test_parse_peril(self):
        parsed = parse_en_pl(html["peril"])
        cached = load_json("peril")
        assert parsed == cached

    def test_parse_inhibitor(self):
        parsed = parse_en_pl(html["inhibitor"])
        cached = load_json("inhibitor")
        assert parsed == cached

    def test_parse_shunt(self):
        parsed = parse_en_pl(html["shunt"])
        cached = load_json("shunt")
        assert parsed == cached

    def test_parse_skirt(self):
        parsed = parse_en_pl(html["skirt"])
        cached = load_json("skirt")
        assert parsed == cached

    def test_parse_winging(self):
        parsed = parse_en_pl(html["winging"])
        cached = load_json("winging")
        assert parsed == cached

    def test_parse_brusque(self):
        parsed = parse_en_pl(html["brusque"])
        cached = load_json("brusque")
        assert parsed == cached

    def test_parse_stretch(self):
        parsed = parse_en_pl(html["stretch"])
        cached = load_json("stretch")
        assert parsed == cached

    def test_parse_scrawny(self):
        parsed = parse_en_pl(html["scrawny"])
        cached = load_json("scrawny")
        assert parsed == cached

    def test_parse_dowery(self):
        parsed = parse_en_pl(html["dowery"])
        cached = load_json("dowery")
        assert parsed == cached

    def test_parse_dyspraxia(self):
        parsed = parse_en_pl(html["dyspraxia"])
        cached = load_json("dyspraxia")
        assert parsed == cached

    def test_parse_gallbladder(self):
        parsed = parse_en_pl(html["gallbladder"])
        cached = load_json("gallbladder")
        assert parsed == cached

    def test_parse_slapdash(self):
        parsed = parse_en_pl(html["slapdash"])
        cached = load_json("slapdash")
        assert parsed == cached

    def test_parse_continence(self):
        parsed = parse_en_pl(html["continence"])
        cached = load_json("continence")
        assert parsed == cached

    def test_parse_unfazed(self):
        parsed = parse_en_pl(html["unfazed"])
        cached = load_json("unfazed")
        assert parsed == cached

    def test_parse_orneriness(self):
        parsed = parse_en_pl(html["orneriness"])
        cached = load_json("orneriness")
        assert parsed == cached

    def test_parse_enmity(self):
        parsed = parse_en_pl(html["enmity"])
        cached = load_json("enmity")
        assert parsed == cached

    def test_parse_garrote(self):
        parsed = parse_en_pl(html["garrote"])
        cached = load_json("garrote")
        assert parsed == cached

    def test_parse_mussels(self):
        parsed = parse_en_pl(html["mussels"])
        cached = load_json("mussels")
        assert parsed == cached

    def test_parse_meek(self):
        parsed = parse_en_pl(html["meek"])
        cached = load_json("meek")
        assert parsed == cached

    def test_parse_sift(self):
        parsed = parse_en_pl(html["sift"])
        cached = load_json("sift")
        assert parsed == cached

    def test_parse_blanket(self):
        parsed = parse_en_pl(html["blanket"])
        cached = load_json("blanket")
        assert parsed == cached

    def test_parse_coax(self):
        parsed = parse_en_pl(html["coax"])
        cached = load_json("coax")
        assert parsed == cached

    def test_parse_glaucoma(self):
        parsed = parse_en_pl(html["glaucoma"])
        cached = load_json("glaucoma")
        assert parsed == cached

    def test_parse_charade(self):
        parsed = parse_en_pl(html["charade"])
        cached = load_json("charade")
        assert parsed == cached

    def test_parse_audacious(self):
        parsed = parse_en_pl(html["audacious"])
        cached = load_json("audacious")
        assert parsed == cached

    def test_parse_disfunctional(self):
        parsed = parse_en_pl(html["disfunctional"])
        cached = load_json("disfunctional")
        assert parsed == cached

    def test_parse_sordid(self):
        parsed = parse_en_pl(html["sordid"])
        cached = load_json("sordid")
        assert parsed == cached

    def test_parse_respite(self):
        parsed = parse_en_pl(html["respite"])
        cached = load_json("respite")
        assert parsed == cached

    def test_parse_adulterate(self):
        parsed = parse_en_pl(html["adulterate"])
        cached = load_json("adulterate")
        assert parsed == cached

    def test_parse_blinkered(self):
        parsed = parse_en_pl(html["blinkered"])
        cached = load_json("blinkered")
        assert parsed == cached

    def test_parse_trebuchet(self):
        parsed = parse_en_pl(html["trebuchet"])
        cached = load_json("trebuchet")
        assert parsed == cached

    def test_parse_quixotically(self):
        parsed = parse_en_pl(html["quixotically"])
        cached = load_json("quixotically")
        assert parsed == cached

    def test_parse_resolve(self):
        parsed = parse_en_pl(html["resolve"])
        cached = load_json("resolve")
        assert parsed == cached

    def test_parse_oppressed(self):
        parsed = parse_en_pl(html["oppressed"])
        cached = load_json("oppressed")
        assert parsed == cached

    def test_parse_lesions(self):
        parsed = parse_en_pl(html["lesions"])
        cached = load_json("lesions")
        assert parsed == cached

    def test_parse_bough(self):
        parsed = parse_en_pl(html["bough"])
        cached = load_json("bough")
        assert parsed == cached

    def test_parse_hue(self):
        parsed = parse_en_pl(html["hue"])
        cached = load_json("hue")
        assert parsed == cached

    def test_parse_farrier(self):
        parsed = parse_en_pl(html["farrier"])
        cached = load_json("farrier")
        assert parsed == cached

    def test_parse_stash(self):
        parsed = parse_en_pl(html["stash"])
        cached = load_json("stash")
        assert parsed == cached

    def test_parse_vicious(self):
        parsed = parse_en_pl(html["vicious"])
        cached = load_json("vicious")
        assert parsed == cached

    def test_parse_tortoise(self):
        parsed = parse_en_pl(html["tortoise"])
        cached = load_json("tortoise")
        assert parsed == cached

    def test_parse_bewitched(self):
        parsed = parse_en_pl(html["bewitched"])
        cached = load_json("bewitched")
        assert parsed == cached

    def test_parse_quip(self):
        parsed = parse_en_pl(html["quip"])
        cached = load_json("quip")
        assert parsed == cached

    def test_parse_ancillary(self):
        parsed = parse_en_pl(html["ancillary"])
        cached = load_json("ancillary")
        assert parsed == cached

    def test_parse_congregant(self):
        parsed = parse_en_pl(html["congregant"])
        cached = load_json("congregant")
        assert parsed == cached

    def test_parse_punter(self):
        parsed = parse_en_pl(html["punter"])
        cached = load_json("punter")
        assert parsed == cached

    def test_parse_wreathe(self):
        parsed = parse_en_pl(html["wreathe"])
        cached = load_json("wreathe")
        assert parsed == cached

    def test_parse_durian(self):
        parsed = parse_en_pl(html["durian"])
        cached = load_json("durian")
        assert parsed == cached

    def test_parse_spigot(self):
        parsed = parse_en_pl(html["spigot"])
        cached = load_json("spigot")
        assert parsed == cached

    def test_parse_patch(self):
        parsed = parse_en_pl(html["patch"])
        cached = load_json("patch")
        assert parsed == cached

    def test_parse_diligent(self):
        parsed = parse_en_pl(html["diligent"])
        cached = load_json("diligent")
        assert parsed == cached

    def test_parse_filial(self):
        parsed = parse_en_pl(html["filial"])
        cached = load_json("filial")
        assert parsed == cached

    def test_parse_implacably(self):
        parsed = parse_en_pl(html["implacably"])
        cached = load_json("implacably")
        assert parsed == cached

    def test_parse_prediction(self):
        parsed = parse_en_pl(html["prediction"])
        cached = load_json("prediction")
        assert parsed == cached

    def test_parse_rabies(self):
        parsed = parse_en_pl(html["rabies"])
        cached = load_json("rabies")
        assert parsed == cached

    def test_parse_ado(self):
        parsed = parse_en_pl(html["ado"])
        cached = load_json("ado")
        assert parsed == cached

    def test_parse_prudence(self):
        parsed = parse_en_pl(html["prudence"])
        cached = load_json("prudence")
        assert parsed == cached

    def test_parse_vista(self):
        parsed = parse_en_pl(html["vista"])
        cached = load_json("vista")
        assert parsed == cached

    def test_parse_benignly(self):
        parsed = parse_en_pl(html["benignly"])
        cached = load_json("benignly")
        assert parsed == cached

    def test_parse_hog(self):
        parsed = parse_en_pl(html["hog"])
        cached = load_json("hog")
        assert parsed == cached

    def test_parse_tempest(self):
        parsed = parse_en_pl(html["tempest"])
        cached = load_json("tempest")
        assert parsed == cached

    def test_parse_vim(self):
        parsed = parse_en_pl(html["vim"])
        cached = load_json("vim")
        assert parsed == cached

    def test_parse_mead(self):
        parsed = parse_en_pl(html["mead"])
        cached = load_json("mead")
        assert parsed == cached

    def test_parse_spendthrift(self):
        parsed = parse_en_pl(html["spendthrift"])
        cached = load_json("spendthrift")
        assert parsed == cached

    def test_parse_panopticon(self):
        parsed = parse_en_pl(html["panopticon"])
        cached = load_json("panopticon")
        assert parsed == cached

    def test_parse_gaggle(self):
        parsed = parse_en_pl(html["gaggle"])
        cached = load_json("gaggle")
        assert parsed == cached

    def test_parse_voluminous(self):
        parsed = parse_en_pl(html["voluminous"])
        cached = load_json("voluminous")
        assert parsed == cached

    def test_parse_outline(self):
        parsed = parse_en_pl(html["outline"])
        cached = load_json("outline")
        assert parsed == cached

    def test_parse_wharve(self):
        parsed = parse_en_pl(html["wharve"])
        cached = load_json("wharve")
        assert parsed == cached

    def test_parse_expediency(self):
        parsed = parse_en_pl(html["expediency"])
        cached = load_json("expediency")
        assert parsed == cached

    def test_parse_trivial(self):
        parsed = parse_en_pl(html["trivial"])
        cached = load_json("trivial")
        assert parsed == cached

    def test_parse_bluff(self):
        parsed = parse_en_pl(html["bluff"])
        cached = load_json("bluff")
        assert parsed == cached

    def test_parse_forlorn(self):
        parsed = parse_en_pl(html["forlorn"])
        cached = load_json("forlorn")
        assert parsed == cached

    def test_parse_agrarian(self):
        parsed = parse_en_pl(html["agrarian"])
        cached = load_json("agrarian")
        assert parsed == cached

    def test_parse_tinnitus(self):
        parsed = parse_en_pl(html["tinnitus"])
        cached = load_json("tinnitus")
        assert parsed == cached

    def test_parse_exult(self):
        parsed = parse_en_pl(html["exult"])
        cached = load_json("exult")
        assert parsed == cached

    def test_parse_ornate(self):
        parsed = parse_en_pl(html["ornate"])
        cached = load_json("ornate")
        assert parsed == cached

    def test_parse_peon(self):
        parsed = parse_en_pl(html["peon"])
        cached = load_json("peon")
        assert parsed == cached

    def test_parse_unhinged(self):
        parsed = parse_en_pl(html["unhinged"])
        cached = load_json("unhinged")
        assert parsed == cached

    def test_parse_selfishness(self):
        parsed = parse_en_pl(html["selfishness"])
        cached = load_json("selfishness")
        assert parsed == cached

    def test_parse_precarity(self):
        parsed = parse_en_pl(html["precarity"])
        cached = load_json("precarity")
        assert parsed == cached

    def test_parse_perpetrator(self):
        parsed = parse_en_pl(html["perpetrator"])
        cached = load_json("perpetrator")
        assert parsed == cached

    def test_parse_luminary(self):
        parsed = parse_en_pl(html["luminary"])
        cached = load_json("luminary")
        assert parsed == cached

    def test_parse_convex(self):
        parsed = parse_en_pl(html["convex"])
        cached = load_json("convex")
        assert parsed == cached

    def test_parse_begat(self):
        parsed = parse_en_pl(html["begat"])
        cached = load_json("begat")
        assert parsed == cached

    def test_parse_indolence(self):
        parsed = parse_en_pl(html["indolence"])
        cached = load_json("indolence")
        assert parsed == cached

    def test_parse_vying(self):
        parsed = parse_en_pl(html["vying"])
        cached = load_json("vying")
        assert parsed == cached

    def test_parse_husbandry(self):
        parsed = parse_en_pl(html["husbandry"])
        cached = load_json("husbandry")
        assert parsed == cached

    def test_parse_quadriplegic(self):
        parsed = parse_en_pl(html["quadriplegic"])
        cached = load_json("quadriplegic")
        assert parsed == cached

    def test_parse_acquaint(self):
        parsed = parse_en_pl(html["acquaint"])
        cached = load_json("acquaint")
        assert parsed == cached

    def test_parse_rattle(self):
        parsed = parse_en_pl(html["rattle"])
        cached = load_json("rattle")
        assert parsed == cached

    def test_parse_corporeal(self):
        parsed = parse_en_pl(html["corporeal"])
        cached = load_json("corporeal")
        assert parsed == cached

    def test_parse_artifice(self):
        parsed = parse_en_pl(html["artifice"])
        cached = load_json("artifice")
        assert parsed == cached

    def test_parse_crooked(self):
        parsed = parse_en_pl(html["crooked"])
        cached = load_json("crooked")
        assert parsed == cached

    def test_parse_eaves(self):
        parsed = parse_en_pl(html["eaves"])
        cached = load_json("eaves")
        assert parsed == cached

    def test_parse_sentient(self):
        parsed = parse_en_pl(html["sentient"])
        cached = load_json("sentient")
        assert parsed == cached

    def test_parse_instigate(self):
        parsed = parse_en_pl(html["instigate"])
        cached = load_json("instigate")
        assert parsed == cached

    def test_parse_wizened(self):
        parsed = parse_en_pl(html["wizened"])
        cached = load_json("wizened")
        assert parsed == cached

    def test_parse_rising(self):
        parsed = parse_en_pl(html["rising"])
        cached = load_json("rising")
        assert parsed == cached

    def test_parse_inimical(self):
        parsed = parse_en_pl(html["inimical"])
        cached = load_json("inimical")
        assert parsed == cached

    def test_parse_acumen(self):
        parsed = parse_en_pl(html["acumen"])
        cached = load_json("acumen")
        assert parsed == cached

    def test_parse_discontent(self):
        parsed = parse_en_pl(html["discontent"])
        cached = load_json("discontent")
        assert parsed == cached

    def test_parse_exuberance(self):
        parsed = parse_en_pl(html["exuberance"])
        cached = load_json("exuberance")
        assert parsed == cached

    def test_parse_discrepancy(self):
        parsed = parse_en_pl(html["discrepancy"])
        cached = load_json("discrepancy")
        assert parsed == cached

    def test_parse_solicitor(self):
        parsed = parse_en_pl(html["solicitor"])
        cached = load_json("solicitor")
        assert parsed == cached

    def test_parse_parochialism(self):
        parsed = parse_en_pl(html["parochialism"])
        cached = load_json("parochialism")
        assert parsed == cached

    def test_parse_adulation(self):
        parsed = parse_en_pl(html["adulation"])
        cached = load_json("adulation")
        assert parsed == cached

    def test_parse_Kowloon(self):
        parsed = parse_en_pl(html["Kowloon"])
        cached = load_json("Kowloon")
        assert parsed == cached

    def test_parse_warring(self):
        parsed = parse_en_pl(html["warring"])
        cached = load_json("warring")
        assert parsed == cached

    def test_parse_conjunction(self):
        parsed = parse_en_pl(html["conjunction"])
        cached = load_json("conjunction")
        assert parsed == cached

    def test_parse_arcane(self):
        parsed = parse_en_pl(html["arcane"])
        cached = load_json("arcane")
        assert parsed == cached

    def test_parse_refurbish(self):
        parsed = parse_en_pl(html["refurbish"])
        cached = load_json("refurbish")
        assert parsed == cached

    def test_parse_negligent(self):
        parsed = parse_en_pl(html["negligent"])
        cached = load_json("negligent")
        assert parsed == cached

    def test_parse_whilist(self):
        parsed = parse_en_pl(html["whilist"])
        cached = load_json("whilist")
        assert parsed == cached

    def test_parse_lien(self):
        parsed = parse_en_pl(html["lien"])
        cached = load_json("lien")
        assert parsed == cached

    def test_parse_watercress(self):
        parsed = parse_en_pl(html["watercress"])
        cached = load_json("watercress")
        assert parsed == cached

    def test_parse_dash(self):
        parsed = parse_en_pl(html["dash"])
        cached = load_json("dash")
        assert parsed == cached

    def test_parse_cherish(self):
        parsed = parse_en_pl(html["cherish"])
        cached = load_json("cherish")
        assert parsed == cached

    def test_parse_indignation(self):
        parsed = parse_en_pl(html["indignation"])
        cached = load_json("indignation")
        assert parsed == cached

    def test_parse_loft(self):
        parsed = parse_en_pl(html["loft"])
        cached = load_json("loft")
        assert parsed == cached

    def test_parse_disregard(self):
        parsed = parse_en_pl(html["disregard"])
        cached = load_json("disregard")
        assert parsed == cached

    def test_parse_furor(self):
        parsed = parse_en_pl(html["furor"])
        cached = load_json("furor")
        assert parsed == cached

    def test_parse_betrothed(self):
        parsed = parse_en_pl(html["betrothed"])
        cached = load_json("betrothed")
        assert parsed == cached

    def test_parse_sheer(self):
        parsed = parse_en_pl(html["sheer"])
        cached = load_json("sheer")
        assert parsed == cached

    def test_parse_maw(self):
        parsed = parse_en_pl(html["maw"])
        cached = load_json("maw")
        assert parsed == cached

    def test_parse_influenza(self):
        parsed = parse_en_pl(html["influenza"])
        cached = load_json("influenza")
        assert parsed == cached

    def test_parse_affectation(self):
        parsed = parse_en_pl(html["affectation"])
        cached = load_json("affectation")
        assert parsed == cached

    def test_parse_précis(self):
        parsed = parse_en_pl(html["précis"])
        cached = load_json("précis")
        assert parsed == cached

    def test_parse_freight(self):
        parsed = parse_en_pl(html["freight"])
        cached = load_json("freight")
        assert parsed == cached

    def test_parse_frigid(self):
        parsed = parse_en_pl(html["frigid"])
        cached = load_json("frigid")
        assert parsed == cached

    def test_parse_remorse(self):
        parsed = parse_en_pl(html["remorse"])
        cached = load_json("remorse")
        assert parsed == cached

    def test_parse_headstrong(self):
        parsed = parse_en_pl(html["headstrong"])
        cached = load_json("headstrong")
        assert parsed == cached

    def test_parse_bobbin(self):
        parsed = parse_en_pl(html["bobbin"])
        cached = load_json("bobbin")
        assert parsed == cached

    def test_parse_wonk(self):
        parsed = parse_en_pl(html["wonk"])
        cached = load_json("wonk")
        assert parsed == cached

    def test_parse_poaching(self):
        parsed = parse_en_pl(html["poaching"])
        cached = load_json("poaching")
        assert parsed == cached

    def test_parse_eldritch(self):
        parsed = parse_en_pl(html["eldritch"])
        cached = load_json("eldritch")
        assert parsed == cached

    def test_parse_tomcat(self):
        parsed = parse_en_pl(html["tomcat"])
        cached = load_json("tomcat")
        assert parsed == cached

    def test_parse_tranny(self):
        parsed = parse_en_pl(html["tranny"])
        cached = load_json("tranny")
        assert parsed == cached

    def test_parse_thimble(self):
        parsed = parse_en_pl(html["thimble"])
        cached = load_json("thimble")
        assert parsed == cached

    def test_parse_jeremiads(self):
        parsed = parse_en_pl(html["jeremiads"])
        cached = load_json("jeremiads")
        assert parsed == cached

    def test_parse_quarry(self):
        parsed = parse_en_pl(html["quarry"])
        cached = load_json("quarry")
        assert parsed == cached

    def test_parse_intrepid(self):
        parsed = parse_en_pl(html["intrepid"])
        cached = load_json("intrepid")
        assert parsed == cached

    def test_parse_jerk(self):
        parsed = parse_en_pl(html["jerk"])
        cached = load_json("jerk")
        assert parsed == cached

    def test_parse_salutatory(self):
        parsed = parse_en_pl(html["salutatory"])
        cached = load_json("salutatory")
        assert parsed == cached

    def test_parse_feud(self):
        parsed = parse_en_pl(html["feud"])
        cached = load_json("feud")
        assert parsed == cached

    def test_parse_progenitor(self):
        parsed = parse_en_pl(html["progenitor"])
        cached = load_json("progenitor")
        assert parsed == cached

    def test_parse_suppurate(self):
        parsed = parse_en_pl(html["suppurate"])
        cached = load_json("suppurate")
        assert parsed == cached

    def test_parse_duress(self):
        parsed = parse_en_pl(html["duress"])
        cached = load_json("duress")
        assert parsed == cached

    def test_parse_proximal(self):
        parsed = parse_en_pl(html["proximal"])
        cached = load_json("proximal")
        assert parsed == cached

    def test_parse_risible(self):
        parsed = parse_en_pl(html["risible"])
        cached = load_json("risible")
        assert parsed == cached

    def test_parse_mendacity(self):
        parsed = parse_en_pl(html["mendacity"])
        cached = load_json("mendacity")
        assert parsed == cached

    def test_parse_cole(self):
        parsed = parse_en_pl(html["cole"])
        cached = load_json("cole")
        assert parsed == cached

    def test_parse_dignified(self):
        parsed = parse_en_pl(html["dignified"])
        cached = load_json("dignified")
        assert parsed == cached

    def test_parse_while(self):
        parsed = parse_en_pl(html["while"])
        cached = load_json("while")
        assert parsed == cached

    def test_parse_sap(self):
        parsed = parse_en_pl(html["sap"])
        cached = load_json("sap")
        assert parsed == cached

    def test_parse_abound(self):
        parsed = parse_en_pl(html["abound"])
        cached = load_json("abound")
        assert parsed == cached

    def test_parse_belie(self):
        parsed = parse_en_pl(html["belie"])
        cached = load_json("belie")
        assert parsed == cached

    def test_parse_diminishing(self):
        parsed = parse_en_pl(html["diminishing"])
        cached = load_json("diminishing")
        assert parsed == cached

    def test_parse_mutiny(self):
        parsed = parse_en_pl(html["mutiny"])
        cached = load_json("mutiny")
        assert parsed == cached

    def test_parse_throb(self):
        parsed = parse_en_pl(html["throb"])
        cached = load_json("throb")
        assert parsed == cached

    def test_parse_bareness(self):
        parsed = parse_en_pl(html["bareness"])
        cached = load_json("bareness")
        assert parsed == cached

    def test_parse_stow(self):
        parsed = parse_en_pl(html["stow"])
        cached = load_json("stow")
        assert parsed == cached

    def test_parse_eddying(self):
        parsed = parse_en_pl(html["eddying"])
        cached = load_json("eddying")
        assert parsed == cached

    def test_parse_dory(self):
        parsed = parse_en_pl(html["dory"])
        cached = load_json("dory")
        assert parsed == cached

    def test_parse_distract(self):
        parsed = parse_en_pl(html["distract"])
        cached = load_json("distract")
        assert parsed == cached

    def test_parse_for(self):
        parsed = parse_en_pl(html["for"])
        cached = load_json("for")
        assert parsed == cached

    def test_parse_stultify(self):
        parsed = parse_en_pl(html["stultify"])
        cached = load_json("stultify")
        assert parsed == cached

    def test_parse_detractor(self):
        parsed = parse_en_pl(html["detractor"])
        cached = load_json("detractor")
        assert parsed == cached

    def test_parse_magpie(self):
        parsed = parse_en_pl(html["magpie"])
        cached = load_json("magpie")
        assert parsed == cached

    def test_parse_indigenous(self):
        parsed = parse_en_pl(html["indigenous"])
        cached = load_json("indigenous")
        assert parsed == cached

    def test_parse_hereditary(self):
        parsed = parse_en_pl(html["hereditary"])
        cached = load_json("hereditary")
        assert parsed == cached

    def test_parse_miscegenation(self):
        parsed = parse_en_pl(html["miscegenation"])
        cached = load_json("miscegenation")
        assert parsed == cached

    def test_parse_splinter(self):
        parsed = parse_en_pl(html["splinter"])
        cached = load_json("splinter")
        assert parsed == cached

    def test_parse_curt(self):
        parsed = parse_en_pl(html["curt"])
        cached = load_json("curt")
        assert parsed == cached

    def test_parse_casserole(self):
        parsed = parse_en_pl(html["casserole"])
        cached = load_json("casserole")
        assert parsed == cached

    def test_parse_accord(self):
        parsed = parse_en_pl(html["accord"])
        cached = load_json("accord")
        assert parsed == cached

    def test_parse_corollary(self):
        parsed = parse_en_pl(html["corollary"])
        cached = load_json("corollary")
        assert parsed == cached

    def test_parse_excruciating(self):
        parsed = parse_en_pl(html["excruciating"])
        cached = load_json("excruciating")
        assert parsed == cached

    def test_parse_wistfully(self):
        parsed = parse_en_pl(html["wistfully"])
        cached = load_json("wistfully")
        assert parsed == cached

    def test_parse_despondence(self):
        parsed = parse_en_pl(html["despondence"])
        cached = load_json("despondence")
        assert parsed == cached

    def test_parse_age(self):
        parsed = parse_en_pl(html["age"])
        cached = load_json("age")
        assert parsed == cached

    def test_parse_diverge(self):
        parsed = parse_en_pl(html["diverge"])
        cached = load_json("diverge")
        assert parsed == cached

    def test_parse_ferment(self):
        parsed = parse_en_pl(html["ferment"])
        cached = load_json("ferment")
        assert parsed == cached

    def test_parse_fetch(self):
        parsed = parse_en_pl(html["fetch"])
        cached = load_json("fetch")
        assert parsed == cached

    def test_parse_facsimile(self):
        parsed = parse_en_pl(html["facsimile"])
        cached = load_json("facsimile")
        assert parsed == cached

    def test_parse_maim(self):
        parsed = parse_en_pl(html["maim"])
        cached = load_json("maim")
        assert parsed == cached

    def test_parse_mercantile(self):
        parsed = parse_en_pl(html["mercantile"])
        cached = load_json("mercantile")
        assert parsed == cached

    def test_parse_tendentious(self):
        parsed = parse_en_pl(html["tendentious"])
        cached = load_json("tendentious")
        assert parsed == cached

    def test_parse_hepatitis(self):
        parsed = parse_en_pl(html["hepatitis"])
        cached = load_json("hepatitis")
        assert parsed == cached

    def test_parse_fret(self):
        parsed = parse_en_pl(html["fret"])
        cached = load_json("fret")
        assert parsed == cached

    def test_parse_admonition(self):
        parsed = parse_en_pl(html["admonition"])
        cached = load_json("admonition")
        assert parsed == cached

    def test_parse_ingenuity(self):
        parsed = parse_en_pl(html["ingenuity"])
        cached = load_json("ingenuity")
        assert parsed == cached

    def test_parse_carb(self):
        parsed = parse_en_pl(html["carb"])
        cached = load_json("carb")
        assert parsed == cached

    def test_parse_brisant(self):
        parsed = parse_en_pl(html["brisant"])
        cached = load_json("brisant")
        assert parsed == cached

    def test_parse_gutters(self):
        parsed = parse_en_pl(html["gutters"])
        cached = load_json("gutters")
        assert parsed == cached

    def test_parse_spat(self):
        parsed = parse_en_pl(html["spat"])
        cached = load_json("spat")
        assert parsed == cached

    def test_parse_testing(self):
        parsed = parse_en_pl(html["testing"])
        cached = load_json("testing")
        assert parsed == cached

    def test_parse_apathy(self):
        parsed = parse_en_pl(html["apathy"])
        cached = load_json("apathy")
        assert parsed == cached

    def test_parse_trickster(self):
        parsed = parse_en_pl(html["trickster"])
        cached = load_json("trickster")
        assert parsed == cached

    def test_parse_furtive(self):
        parsed = parse_en_pl(html["furtive"])
        cached = load_json("furtive")
        assert parsed == cached

    def test_parse_rack(self):
        parsed = parse_en_pl(html["rack"])
        cached = load_json("rack")
        assert parsed == cached

    def test_parse_lime(self):
        parsed = parse_en_pl(html["lime"])
        cached = load_json("lime")
        assert parsed == cached

    def test_parse_tawdriness(self):
        parsed = parse_en_pl(html["tawdriness"])
        cached = load_json("tawdriness")
        assert parsed == cached

    def test_parse_limestone(self):
        parsed = parse_en_pl(html["limestone"])
        cached = load_json("limestone")
        assert parsed == cached

    def test_parse_brim(self):
        parsed = parse_en_pl(html["brim"])
        cached = load_json("brim")
        assert parsed == cached

    def test_parse_berth(self):
        parsed = parse_en_pl(html["berth"])
        cached = load_json("berth")
        assert parsed == cached

    def test_parse_bacillus(self):
        parsed = parse_en_pl(html["bacillus"])
        cached = load_json("bacillus")
        assert parsed == cached

    def test_parse_blunder(self):
        parsed = parse_en_pl(html["blunder"])
        cached = load_json("blunder")
        assert parsed == cached

    def test_parse_stowaway(self):
        parsed = parse_en_pl(html["stowaway"])
        cached = load_json("stowaway")
        assert parsed == cached

    def test_parse_coy(self):
        parsed = parse_en_pl(html["coy"])
        cached = load_json("coy")
        assert parsed == cached

    def test_parse_porridge(self):
        parsed = parse_en_pl(html["porridge"])
        cached = load_json("porridge")
        assert parsed == cached

    def test_parse_puttering(self):
        parsed = parse_en_pl(html["puttering"])
        cached = load_json("puttering")
        assert parsed == cached

    def test_parse_unencumbered(self):
        parsed = parse_en_pl(html["unencumbered"])
        cached = load_json("unencumbered")
        assert parsed == cached

    def test_parse_narc(self):
        parsed = parse_en_pl(html["narc"])
        cached = load_json("narc")
        assert parsed == cached

    def test_parse_slander(self):
        parsed = parse_en_pl(html["slander"])
        cached = load_json("slander")
        assert parsed == cached

    def test_parse_homicide(self):
        parsed = parse_en_pl(html["homicide"])
        cached = load_json("homicide")
        assert parsed == cached

    def test_parse_rued(self):
        parsed = parse_en_pl(html["rued"])
        cached = load_json("rued")
        assert parsed == cached

    def test_parse_vested(self):
        parsed = parse_en_pl(html["vested"])
        cached = load_json("vested")
        assert parsed == cached

    def test_parse_immaculate(self):
        parsed = parse_en_pl(html["immaculate"])
        cached = load_json("immaculate")
        assert parsed == cached

    def test_parse_ulceration(self):
        parsed = parse_en_pl(html["ulceration"])
        cached = load_json("ulceration")
        assert parsed == cached

    def test_parse_lumber(self):
        parsed = parse_en_pl(html["lumber"])
        cached = load_json("lumber")
        assert parsed == cached

    def test_parse_containable(self):
        parsed = parse_en_pl(html["containable"])
        cached = load_json("containable")
        assert parsed == cached

    def test_parse_snag(self):
        parsed = parse_en_pl(html["snag"])
        cached = load_json("snag")
        assert parsed == cached

    def test_parse_forfeit(self):
        parsed = parse_en_pl(html["forfeit"])
        cached = load_json("forfeit")
        assert parsed == cached

    def test_parse_inordinate(self):
        parsed = parse_en_pl(html["inordinate"])
        cached = load_json("inordinate")
        assert parsed == cached

    def test_parse_afterbirth(self):
        parsed = parse_en_pl(html["afterbirth"])
        cached = load_json("afterbirth")
        assert parsed == cached

    def test_parse_deter(self):
        parsed = parse_en_pl(html["deter"])
        cached = load_json("deter")
        assert parsed == cached

    def test_parse_adorn(self):
        parsed = parse_en_pl(html["adorn"])
        cached = load_json("adorn")
        assert parsed == cached

    def test_parse_adversarial(self):
        parsed = parse_en_pl(html["adversarial"])
        cached = load_json("adversarial")
        assert parsed == cached

    def test_parse_parchment(self):
        parsed = parse_en_pl(html["parchment"])
        cached = load_json("parchment")
        assert parsed == cached

    def test_parse_demeanor(self):
        parsed = parse_en_pl(html["demeanor"])
        cached = load_json("demeanor")
        assert parsed == cached

    def test_parse_damp(self):
        parsed = parse_en_pl(html["damp"])
        cached = load_json("damp")
        assert parsed == cached

    def test_parse_efficacy(self):
        parsed = parse_en_pl(html["efficacy"])
        cached = load_json("efficacy")
        assert parsed == cached

    def test_parse_garment(self):
        parsed = parse_en_pl(html["garment"])
        cached = load_json("garment")
        assert parsed == cached

    def test_parse_insofar(self):
        parsed = parse_en_pl(html["insofar"])
        cached = load_json("insofar")
        assert parsed == cached

    def test_parse_triplet(self):
        parsed = parse_en_pl(html["triplet"])
        cached = load_json("triplet")
        assert parsed == cached

    def test_parse_straddle(self):
        parsed = parse_en_pl(html["straddle"])
        cached = load_json("straddle")
        assert parsed == cached

    def test_parse_beseech(self):
        parsed = parse_en_pl(html["beseech"])
        cached = load_json("beseech")
        assert parsed == cached

    def test_parse_frugally(self):
        parsed = parse_en_pl(html["frugally"])
        cached = load_json("frugally")
        assert parsed == cached

    def test_parse_hifalutin(self):
        parsed = parse_en_pl(html["hifalutin"])
        cached = load_json("hifalutin")
        assert parsed == cached

    def test_parse_alloy(self):
        parsed = parse_en_pl(html["alloy"])
        cached = load_json("alloy")
        assert parsed == cached

    def test_parse_gregarious(self):
        parsed = parse_en_pl(html["gregarious"])
        cached = load_json("gregarious")
        assert parsed == cached

    def test_parse_pontificate(self):
        parsed = parse_en_pl(html["pontificate"])
        cached = load_json("pontificate")
        assert parsed == cached

    def test_parse_impel(self):
        parsed = parse_en_pl(html["impel"])
        cached = load_json("impel")
        assert parsed == cached

    def test_parse_amusing(self):
        parsed = parse_en_pl(html["amusing"])
        cached = load_json("amusing")
        assert parsed == cached

    def test_parse_alteration(self):
        parsed = parse_en_pl(html["alteration"])
        cached = load_json("alteration")
        assert parsed == cached

    def test_parse_hew(self):
        parsed = parse_en_pl(html["hew"])
        cached = load_json("hew")
        assert parsed == cached

    def test_parse_convivial(self):
        parsed = parse_en_pl(html["convivial"])
        cached = load_json("convivial")
        assert parsed == cached

    def test_parse_docile(self):
        parsed = parse_en_pl(html["docile"])
        cached = load_json("docile")
        assert parsed == cached

    def test_parse_pewter(self):
        parsed = parse_en_pl(html["pewter"])
        cached = load_json("pewter")
        assert parsed == cached

    def test_parse_manila(self):
        parsed = parse_en_pl(html["manila"])
        cached = load_json("manila")
        assert parsed == cached

    def test_parse_notional(self):
        parsed = parse_en_pl(html["notional"])
        cached = load_json("notional")
        assert parsed == cached

    def test_parse_jeer(self):
        parsed = parse_en_pl(html["jeer"])
        cached = load_json("jeer")
        assert parsed == cached

    def test_parse_figuratively(self):
        parsed = parse_en_pl(html["figuratively"])
        cached = load_json("figuratively")
        assert parsed == cached

    def test_parse_rut(self):
        parsed = parse_en_pl(html["rut"])
        cached = load_json("rut")
        assert parsed == cached

    def test_parse_preclude(self):
        parsed = parse_en_pl(html["preclude"])
        cached = load_json("preclude")
        assert parsed == cached

    def test_parse_hussle(self):
        parsed = parse_en_pl(html["hussle"])
        cached = load_json("hussle")
        assert parsed == cached

    def test_parse_assent(self):
        parsed = parse_en_pl(html["assent"])
        cached = load_json("assent")
        assert parsed == cached

    def test_parse_unadorned(self):
        parsed = parse_en_pl(html["unadorned"])
        cached = load_json("unadorned")
        assert parsed == cached

    def test_parse_gorge(self):
        parsed = parse_en_pl(html["gorge"])
        cached = load_json("gorge")
        assert parsed == cached

    def test_parse_appropriate(self):
        parsed = parse_en_pl(html["appropriate"])
        cached = load_json("appropriate")
        assert parsed == cached

    def test_parse_coo(self):
        parsed = parse_en_pl(html["coo"])
        cached = load_json("coo")
        assert parsed == cached

    def test_parse_minnow(self):
        parsed = parse_en_pl(html["minnow"])
        cached = load_json("minnow")
        assert parsed == cached

    def test_parse_carping(self):
        parsed = parse_en_pl(html["carping"])
        cached = load_json("carping")
        assert parsed == cached

    def test_parse_chad(self):
        parsed = parse_en_pl(html["chad"])
        cached = load_json("chad")
        assert parsed == cached

    def test_parse_dowel(self):
        parsed = parse_en_pl(html["dowel"])
        cached = load_json("dowel")
        assert parsed == cached

    def test_parse_auger(self):
        parsed = parse_en_pl(html["auger"])
        cached = load_json("auger")
        assert parsed == cached

    def test_parse_prenuptial(self):
        parsed = parse_en_pl(html["prenuptial"])
        cached = load_json("prenuptial")
        assert parsed == cached

    def test_parse_tic(self):
        parsed = parse_en_pl(html["tic"])
        cached = load_json("tic")
        assert parsed == cached

    def test_parse_malleability(self):
        parsed = parse_en_pl(html["malleability"])
        cached = load_json("malleability")
        assert parsed == cached

    def test_parse_shagging(self):
        parsed = parse_en_pl(html["shagging"])
        cached = load_json("shagging")
        assert parsed == cached

    def test_parse_discombobulated(self):
        parsed = parse_en_pl(html["discombobulated"])
        cached = load_json("discombobulated")
        assert parsed == cached

    def test_parse_lavish(self):
        parsed = parse_en_pl(html["lavish"])
        cached = load_json("lavish")
        assert parsed == cached

    def test_parse_vehemently(self):
        parsed = parse_en_pl(html["vehemently"])
        cached = load_json("vehemently")
        assert parsed == cached

    def test_parse_unfettered(self):
        parsed = parse_en_pl(html["unfettered"])
        cached = load_json("unfettered")
        assert parsed == cached

    def test_parse_onwards(self):
        parsed = parse_en_pl(html["onwards"])
        cached = load_json("onwards")
        assert parsed == cached

    def test_parse_racketeer(self):
        parsed = parse_en_pl(html["racketeer"])
        cached = load_json("racketeer")
        assert parsed == cached

    def test_parse_chide(self):
        parsed = parse_en_pl(html["chide"])
        cached = load_json("chide")
        assert parsed == cached

    def test_parse_prowess(self):
        parsed = parse_en_pl(html["prowess"])
        cached = load_json("prowess")
        assert parsed == cached

    def test_parse_hump(self):
        parsed = parse_en_pl(html["hump"])
        cached = load_json("hump")
        assert parsed == cached

    def test_parse_purge(self):
        parsed = parse_en_pl(html["purge"])
        cached = load_json("purge")
        assert parsed == cached

    def test_parse_diatribe(self):
        parsed = parse_en_pl(html["diatribe"])
        cached = load_json("diatribe")
        assert parsed == cached

    def test_parse_digress(self):
        parsed = parse_en_pl(html["digress"])
        cached = load_json("digress")
        assert parsed == cached

    def test_parse_scaffold(self):
        parsed = parse_en_pl(html["scaffold"])
        cached = load_json("scaffold")
        assert parsed == cached

    def test_parse_renunciations(self):
        parsed = parse_en_pl(html["renunciations"])
        cached = load_json("renunciations")
        assert parsed == cached

    def test_parse_elated(self):
        parsed = parse_en_pl(html["elated"])
        cached = load_json("elated")
        assert parsed == cached

    def test_parse_marshal(self):
        parsed = parse_en_pl(html["marshal"])
        cached = load_json("marshal")
        assert parsed == cached

    def test_parse_snivelling(self):
        parsed = parse_en_pl(html["snivelling"])
        cached = load_json("snivelling")
        assert parsed == cached

    def test_parse_strap(self):
        parsed = parse_en_pl(html["strap"])
        cached = load_json("strap")
        assert parsed == cached

    def test_parse_sucker(self):
        parsed = parse_en_pl(html["sucker"])
        cached = load_json("sucker")
        assert parsed == cached

    def test_parse_renunciation(self):
        parsed = parse_en_pl(html["renunciation"])
        cached = load_json("renunciation")
        assert parsed == cached

    def test_parse_visceral(self):
        parsed = parse_en_pl(html["visceral"])
        cached = load_json("visceral")
        assert parsed == cached

    def test_parse_sound(self):
        parsed = parse_en_pl(html["sound"])
        cached = load_json("sound")
        assert parsed == cached

    def test_parse_conceivably(self):
        parsed = parse_en_pl(html["conceivably"])
        cached = load_json("conceivably")
        assert parsed == cached

    def test_parse_corduroy(self):
        parsed = parse_en_pl(html["corduroy"])
        cached = load_json("corduroy")
        assert parsed == cached

    def test_parse_frisky(self):
        parsed = parse_en_pl(html["frisky"])
        cached = load_json("frisky")
        assert parsed == cached

    def test_parse_deprivation(self):
        parsed = parse_en_pl(html["deprivation"])
        cached = load_json("deprivation")
        assert parsed == cached

    def test_parse_proprietor(self):
        parsed = parse_en_pl(html["proprietor"])
        cached = load_json("proprietor")
        assert parsed == cached

    def test_parse_contiguous(self):
        parsed = parse_en_pl(html["contiguous"])
        cached = load_json("contiguous")
        assert parsed == cached

    def test_parse_disappointing(self):
        parsed = parse_en_pl(html["disappointing"])
        cached = load_json("disappointing")
        assert parsed == cached

    def test_parse_gush(self):
        parsed = parse_en_pl(html["gush"])
        cached = load_json("gush")
        assert parsed == cached

    def test_parse_impish(self):
        parsed = parse_en_pl(html["impish"])
        cached = load_json("impish")
        assert parsed == cached

    def test_parse_residence(self):
        parsed = parse_en_pl(html["residence"])
        cached = load_json("residence")
        assert parsed == cached

    def test_parse_unruffled(self):
        parsed = parse_en_pl(html["unruffled"])
        cached = load_json("unruffled")
        assert parsed == cached

    def test_parse_carnal(self):
        parsed = parse_en_pl(html["carnal"])
        cached = load_json("carnal")
        assert parsed == cached

    def test_parse_regency(self):
        parsed = parse_en_pl(html["regency"])
        cached = load_json("regency")
        assert parsed == cached

    def test_parse_churlish(self):
        parsed = parse_en_pl(html["churlish"])
        cached = load_json("churlish")
        assert parsed == cached

    def test_parse_pulchritudinous(self):
        parsed = parse_en_pl(html["pulchritudinous"])
        cached = load_json("pulchritudinous")
        assert parsed == cached

    def test_parse_beech(self):
        parsed = parse_en_pl(html["beech"])
        cached = load_json("beech")
        assert parsed == cached

    def test_parse_alder(self):
        parsed = parse_en_pl(html["alder"])
        cached = load_json("alder")
        assert parsed == cached

    def test_parse_quote(self):
        parsed = parse_en_pl(html["quote"])
        cached = load_json("quote")
        assert parsed == cached

    def test_parse_confound(self):
        parsed = parse_en_pl(html["confound"])
        cached = load_json("confound")
        assert parsed == cached

    def test_parse_pitilessly(self):
        parsed = parse_en_pl(html["pitilessly"])
        cached = load_json("pitilessly")
        assert parsed == cached

    def test_parse_hick(self):
        parsed = parse_en_pl(html["hick"])
        cached = load_json("hick")
        assert parsed == cached

    def test_parse_excruciatingly(self):
        parsed = parse_en_pl(html["excruciatingly"])
        cached = load_json("excruciatingly")
        assert parsed == cached

    def test_parse_punitive(self):
        parsed = parse_en_pl(html["punitive"])
        cached = load_json("punitive")
        assert parsed == cached

    def test_parse_patter(self):
        parsed = parse_en_pl(html["patter"])
        cached = load_json("patter")
        assert parsed == cached

    def test_parse_darkness(self):
        parsed = parse_en_pl(html["darkness"])
        cached = load_json("darkness")
        assert parsed == cached

    def test_parse_succumb(self):
        parsed = parse_en_pl(html["succumb"])
        cached = load_json("succumb")
        assert parsed == cached

    def test_parse_lend(self):
        parsed = parse_en_pl(html["lend"])
        cached = load_json("lend")
        assert parsed == cached

    def test_parse_affinity(self):
        parsed = parse_en_pl(html["affinity"])
        cached = load_json("affinity")
        assert parsed == cached

    def test_parse_supposition(self):
        parsed = parse_en_pl(html["supposition"])
        cached = load_json("supposition")
        assert parsed == cached

    def test_parse_ulcers(self):
        parsed = parse_en_pl(html["ulcers"])
        cached = load_json("ulcers")
        assert parsed == cached

    def test_parse_notch(self):
        parsed = parse_en_pl(html["notch"])
        cached = load_json("notch")
        assert parsed == cached

    def test_parse_perspicaciously(self):
        parsed = parse_en_pl(html["perspicaciously"])
        cached = load_json("perspicaciously")
        assert parsed == cached

    def test_parse_exegesis(self):
        parsed = parse_en_pl(html["exegesis"])
        cached = load_json("exegesis")
        assert parsed == cached

    def test_parse_chubby(self):
        parsed = parse_en_pl(html["chubby"])
        cached = load_json("chubby")
        assert parsed == cached

    def test_parse_tenacious(self):
        parsed = parse_en_pl(html["tenacious"])
        cached = load_json("tenacious")
        assert parsed == cached

    def test_parse_console(self):
        parsed = parse_en_pl(html["console"])
        cached = load_json("console")
        assert parsed == cached

    def test_parse_dispatch(self):
        parsed = parse_en_pl(html["dispatch"])
        cached = load_json("dispatch")
        assert parsed == cached

    def test_parse_marred(self):
        parsed = parse_en_pl(html["marred"])
        cached = load_json("marred")
        assert parsed == cached

    def test_parse_unassailable(self):
        parsed = parse_en_pl(html["unassailable"])
        cached = load_json("unassailable")
        assert parsed == cached

    def test_parse_dissuade(self):
        parsed = parse_en_pl(html["dissuade"])
        cached = load_json("dissuade")
        assert parsed == cached

    def test_parse_conjure(self):
        parsed = parse_en_pl(html["conjure"])
        cached = load_json("conjure")
        assert parsed == cached

    def test_parse_sagacity(self):
        parsed = parse_en_pl(html["sagacity"])
        cached = load_json("sagacity")
        assert parsed == cached

    def test_parse_reed(self):
        parsed = parse_en_pl(html["reed"])
        cached = load_json("reed")
        assert parsed == cached

    def test_parse_plight(self):
        parsed = parse_en_pl(html["plight"])
        cached = load_json("plight")
        assert parsed == cached

    def test_parse_taciturn(self):
        parsed = parse_en_pl(html["taciturn"])
        cached = load_json("taciturn")
        assert parsed == cached

    def test_parse_brass(self):
        parsed = parse_en_pl(html["brass"])
        cached = load_json("brass")
        assert parsed == cached

    def test_parse_proselyte(self):
        parsed = parse_en_pl(html["proselyte"])
        cached = load_json("proselyte")
        assert parsed == cached

    def test_parse_cringe(self):
        parsed = parse_en_pl(html["cringe"])
        cached = load_json("cringe")
        assert parsed == cached

    def test_parse_morsel(self):
        parsed = parse_en_pl(html["morsel"])
        cached = load_json("morsel")
        assert parsed == cached

    def test_parse_squeal(self):
        parsed = parse_en_pl(html["squeal"])
        cached = load_json("squeal")
        assert parsed == cached

    def test_parse_aggravating(self):
        parsed = parse_en_pl(html["aggravating"])
        cached = load_json("aggravating")
        assert parsed == cached

    def test_parse_intermittent(self):
        parsed = parse_en_pl(html["intermittent"])
        cached = load_json("intermittent")
        assert parsed == cached

    def test_parse_mezzanine(self):
        parsed = parse_en_pl(html["mezzanine"])
        cached = load_json("mezzanine")
        assert parsed == cached

    def test_parse_meekness(self):
        parsed = parse_en_pl(html["meekness"])
        cached = load_json("meekness")
        assert parsed == cached

    def test_parse_brawn(self):
        parsed = parse_en_pl(html["brawn"])
        cached = load_json("brawn")
        assert parsed == cached

    def test_parse_crufty(self):
        parsed = parse_en_pl(html["crufty"])
        cached = load_json("crufty")
        assert parsed == cached

    def test_parse_coven(self):
        parsed = parse_en_pl(html["coven"])
        cached = load_json("coven")
        assert parsed == cached

    def test_parse_jolt(self):
        parsed = parse_en_pl(html["jolt"])
        cached = load_json("jolt")
        assert parsed == cached

    def test_parse_disparage(self):
        parsed = parse_en_pl(html["disparage"])
        cached = load_json("disparage")
        assert parsed == cached

    def test_parse_parlance(self):
        parsed = parse_en_pl(html["parlance"])
        cached = load_json("parlance")
        assert parsed == cached

    def test_parse_confine(self):
        parsed = parse_en_pl(html["confine"])
        cached = load_json("confine")
        assert parsed == cached

    def test_parse_distributed(self):
        parsed = parse_en_pl(html["distributed"])
        cached = load_json("distributed")
        assert parsed == cached

    def test_parse_leonine(self):
        parsed = parse_en_pl(html["leonine"])
        cached = load_json("leonine")
        assert parsed == cached

    def test_parse_spain(self):
        parsed = parse_en_pl(html["spain"])
        cached = load_json("spain")
        assert parsed == cached

    def test_parse_slyly(self):
        parsed = parse_en_pl(html["slyly"])
        cached = load_json("slyly")
        assert parsed == cached

    def test_parse_seminal(self):
        parsed = parse_en_pl(html["seminal"])
        cached = load_json("seminal")
        assert parsed == cached

    def test_parse_culpability(self):
        parsed = parse_en_pl(html["culpability"])
        cached = load_json("culpability")
        assert parsed == cached

    def test_parse_mediocrity(self):
        parsed = parse_en_pl(html["mediocrity"])
        cached = load_json("mediocrity")
        assert parsed == cached

    def test_parse_auspice(self):
        parsed = parse_en_pl(html["auspice"])
        cached = load_json("auspice")
        assert parsed == cached

    def test_parse_grandee(self):
        parsed = parse_en_pl(html["grandee"])
        cached = load_json("grandee")
        assert parsed == cached

    def test_parse_frankness(self):
        parsed = parse_en_pl(html["frankness"])
        cached = load_json("frankness")
        assert parsed == cached

    def test_parse_wily(self):
        parsed = parse_en_pl(html["wily"])
        cached = load_json("wily")
        assert parsed == cached

    def test_parse_gored(self):
        parsed = parse_en_pl(html["gored"])
        cached = load_json("gored")
        assert parsed == cached

    def test_parse_plonk(self):
        parsed = parse_en_pl(html["plonk"])
        cached = load_json("plonk")
        assert parsed == cached

    def test_parse_unbridled(self):
        parsed = parse_en_pl(html["unbridled"])
        cached = load_json("unbridled")
        assert parsed == cached

    def test_parse_spunk(self):
        parsed = parse_en_pl(html["spunk"])
        cached = load_json("spunk")
        assert parsed == cached

    def test_parse_rile(self):
        parsed = parse_en_pl(html["rile"])
        cached = load_json("rile")
        assert parsed == cached

    def test_parse_titter(self):
        parsed = parse_en_pl(html["titter"])
        cached = load_json("titter")
        assert parsed == cached

    def test_parse_writhe(self):
        parsed = parse_en_pl(html["writhe"])
        cached = load_json("writhe")
        assert parsed == cached

    def test_parse_crummy(self):
        parsed = parse_en_pl(html["crummy"])
        cached = load_json("crummy")
        assert parsed == cached

    def test_parse_sob(self):
        parsed = parse_en_pl(html["sob"])
        cached = load_json("sob")
        assert parsed == cached

    def test_parse_remedy(self):
        parsed = parse_en_pl(html["remedy"])
        cached = load_json("remedy")
        assert parsed == cached

    def test_parse_disparaging(self):
        parsed = parse_en_pl(html["disparaging"])
        cached = load_json("disparaging")
        assert parsed == cached

    def test_parse_keef(self):
        parsed = parse_en_pl(html["keef"])
        cached = load_json("keef")
        assert parsed == cached

    def test_parse_lint(self):
        parsed = parse_en_pl(html["lint"])
        cached = load_json("lint")
        assert parsed == cached

    def test_parse_relieved(self):
        parsed = parse_en_pl(html["relieved"])
        cached = load_json("relieved")
        assert parsed == cached

    def test_parse_tits(self):
        parsed = parse_en_pl(html["tits"])
        cached = load_json("tits")
        assert parsed == cached

    def test_parse_sorority(self):
        parsed = parse_en_pl(html["sorority"])
        cached = load_json("sorority")
        assert parsed == cached

    def test_parse_oleander(self):
        parsed = parse_en_pl(html["oleander"])
        cached = load_json("oleander")
        assert parsed == cached

    def test_parse_mulberry(self):
        parsed = parse_en_pl(html["mulberry"])
        cached = load_json("mulberry")
        assert parsed == cached

    def test_parse_incredulity(self):
        parsed = parse_en_pl(html["incredulity"])
        cached = load_json("incredulity")
        assert parsed == cached

    def test_parse_boon(self):
        parsed = parse_en_pl(html["boon"])
        cached = load_json("boon")
        assert parsed == cached

    def test_parse_freckle(self):
        parsed = parse_en_pl(html["freckle"])
        cached = load_json("freckle")
        assert parsed == cached

    def test_parse_beget(self):
        parsed = parse_en_pl(html["beget"])
        cached = load_json("beget")
        assert parsed == cached

    def test_parse_curtail(self):
        parsed = parse_en_pl(html["curtail"])
        cached = load_json("curtail")
        assert parsed == cached

    def test_parse_sack(self):
        parsed = parse_en_pl(html["sack"])
        cached = load_json("sack")
        assert parsed == cached

    def test_parse_amalgamation(self):
        parsed = parse_en_pl(html["amalgamation"])
        cached = load_json("amalgamation")
        assert parsed == cached

    def test_parse_slandering(self):
        parsed = parse_en_pl(html["slandering"])
        cached = load_json("slandering")
        assert parsed == cached

    def test_parse_malt(self):
        parsed = parse_en_pl(html["malt"])
        cached = load_json("malt")
        assert parsed == cached

    def test_parse_allusive(self):
        parsed = parse_en_pl(html["allusive"])
        cached = load_json("allusive")
        assert parsed == cached

    def test_parse_mewl(self):
        parsed = parse_en_pl(html["mewl"])
        cached = load_json("mewl")
        assert parsed == cached

    def test_parse_tinny(self):
        parsed = parse_en_pl(html["tinny"])
        cached = load_json("tinny")
        assert parsed == cached

    def test_parse_curl(self):
        parsed = parse_en_pl(html["curl"])
        cached = load_json("curl")
        assert parsed == cached

    def test_parse_liability(self):
        parsed = parse_en_pl(html["liability"])
        cached = load_json("liability")
        assert parsed == cached

    def test_parse_consort(self):
        parsed = parse_en_pl(html["consort"])
        cached = load_json("consort")
        assert parsed == cached

    def test_parse_tar(self):
        parsed = parse_en_pl(html["tar"])
        cached = load_json("tar")
        assert parsed == cached

    def test_parse_vantage(self):
        parsed = parse_en_pl(html["vantage"])
        cached = load_json("vantage")
        assert parsed == cached

    def test_parse_moped(self):
        parsed = parse_en_pl(html["moped"])
        cached = load_json("moped")
        assert parsed == cached

    def test_parse_sludge(self):
        parsed = parse_en_pl(html["sludge"])
        cached = load_json("sludge")
        assert parsed == cached

    def test_parse_gurney(self):
        parsed = parse_en_pl(html["gurney"])
        cached = load_json("gurney")
        assert parsed == cached

    def test_parse_nascent(self):
        parsed = parse_en_pl(html["nascent"])
        cached = load_json("nascent")
        assert parsed == cached

    def test_parse_fender(self):
        parsed = parse_en_pl(html["fender"])
        cached = load_json("fender")
        assert parsed == cached

    def test_parse_hunker(self):
        parsed = parse_en_pl(html["hunker"])
        cached = load_json("hunker")
        assert parsed == cached

    def test_parse_adroitness(self):
        parsed = parse_en_pl(html["adroitness"])
        cached = load_json("adroitness")
        assert parsed == cached

    def test_parse_litmus(self):
        parsed = parse_en_pl(html["litmus"])
        cached = load_json("litmus")
        assert parsed == cached

    def test_parse_salmon(self):
        parsed = parse_en_pl(html["salmon"])
        cached = load_json("salmon")
        assert parsed == cached

    def test_parse_jessamine(self):
        parsed = parse_en_pl(html["jessamine"])
        cached = load_json("jessamine")
        assert parsed == cached

    def test_parse_gnarly(self):
        parsed = parse_en_pl(html["gnarly"])
        cached = load_json("gnarly")
        assert parsed == cached

    def test_parse_verge(self):
        parsed = parse_en_pl(html["verge"])
        cached = load_json("verge")
        assert parsed == cached

    def test_parse_destitute(self):
        parsed = parse_en_pl(html["destitute"])
        cached = load_json("destitute")
        assert parsed == cached

    def test_parse_refrain(self):
        parsed = parse_en_pl(html["refrain"])
        cached = load_json("refrain")
        assert parsed == cached

    def test_parse_derange(self):
        parsed = parse_en_pl(html["derange"])
        cached = load_json("derange")
        assert parsed == cached

    def test_parse_equestrian(self):
        parsed = parse_en_pl(html["equestrian"])
        cached = load_json("equestrian")
        assert parsed == cached

    def test_parse_grovel(self):
        parsed = parse_en_pl(html["grovel"])
        cached = load_json("grovel")
        assert parsed == cached

    def test_parse_articulate(self):
        parsed = parse_en_pl(html["articulate"])
        cached = load_json("articulate")
        assert parsed == cached

    def test_parse_vigilance(self):
        parsed = parse_en_pl(html["vigilance"])
        cached = load_json("vigilance")
        assert parsed == cached

    def test_parse_dumb(self):
        parsed = parse_en_pl(html["dumb"])
        cached = load_json("dumb")
        assert parsed == cached

    def test_parse_tutelage(self):
        parsed = parse_en_pl(html["tutelage"])
        cached = load_json("tutelage")
        assert parsed == cached

    def test_parse_toehold(self):
        parsed = parse_en_pl(html["toehold"])
        cached = load_json("toehold")
        assert parsed == cached

    def test_parse_rapacious(self):
        parsed = parse_en_pl(html["rapacious"])
        cached = load_json("rapacious")
        assert parsed == cached

    def test_parse_puppet(self):
        parsed = parse_en_pl(html["puppet"])
        cached = load_json("puppet")
        assert parsed == cached

    def test_parse_brute(self):
        parsed = parse_en_pl(html["brute"])
        cached = load_json("brute")
        assert parsed == cached

    def test_parse_briskly(self):
        parsed = parse_en_pl(html["briskly"])
        cached = load_json("briskly")
        assert parsed == cached

    def test_parse_guile(self):
        parsed = parse_en_pl(html["guile"])
        cached = load_json("guile")
        assert parsed == cached

    def test_parse_chestnut(self):
        parsed = parse_en_pl(html["chestnut"])
        cached = load_json("chestnut")
        assert parsed == cached

    def test_parse_tort(self):
        parsed = parse_en_pl(html["tort"])
        cached = load_json("tort")
        assert parsed == cached

    def test_parse_frenetic(self):
        parsed = parse_en_pl(html["frenetic"])
        cached = load_json("frenetic")
        assert parsed == cached

    def test_parse_shambles(self):
        parsed = parse_en_pl(html["shambles"])
        cached = load_json("shambles")
        assert parsed == cached

    def test_parse_yoke(self):
        parsed = parse_en_pl(html["yoke"])
        cached = load_json("yoke")
        assert parsed == cached

    def test_parse_lentil(self):
        parsed = parse_en_pl(html["lentil"])
        cached = load_json("lentil")
        assert parsed == cached

    def test_parse_clobber(self):
        parsed = parse_en_pl(html["clobber"])
        cached = load_json("clobber")
        assert parsed == cached

    def test_parse_appendix(self):
        parsed = parse_en_pl(html["appendix"])
        cached = load_json("appendix")
        assert parsed == cached

    def test_parse_conspicuous(self):
        parsed = parse_en_pl(html["conspicuous"])
        cached = load_json("conspicuous")
        assert parsed == cached

    def test_parse_covet(self):
        parsed = parse_en_pl(html["covet"])
        cached = load_json("covet")
        assert parsed == cached

    def test_parse_repossess(self):
        parsed = parse_en_pl(html["repossess"])
        cached = load_json("repossess")
        assert parsed == cached

    def test_parse_baffle(self):
        parsed = parse_en_pl(html["baffle"])
        cached = load_json("baffle")
        assert parsed == cached

    def test_parse_henchman(self):
        parsed = parse_en_pl(html["henchman"])
        cached = load_json("henchman")
        assert parsed == cached

    def test_parse_regurgitate(self):
        parsed = parse_en_pl(html["regurgitate"])
        cached = load_json("regurgitate")
        assert parsed == cached

    def test_parse_fabricated(self):
        parsed = parse_en_pl(html["fabricated"])
        cached = load_json("fabricated")
        assert parsed == cached

    def test_parse_leatherette(self):
        parsed = parse_en_pl(html["leatherette"])
        cached = load_json("leatherette")
        assert parsed == cached

    def test_parse_inauspicious(self):
        parsed = parse_en_pl(html["inauspicious"])
        cached = load_json("inauspicious")
        assert parsed == cached

    def test_parse_chattel(self):
        parsed = parse_en_pl(html["chattel"])
        cached = load_json("chattel")
        assert parsed == cached

    def test_parse_imbibe(self):
        parsed = parse_en_pl(html["imbibe"])
        cached = load_json("imbibe")
        assert parsed == cached

    def test_parse_unclench(self):
        parsed = parse_en_pl(html["unclench"])
        cached = load_json("unclench")
        assert parsed == cached

    def test_parse_incidence(self):
        parsed = parse_en_pl(html["incidence"])
        cached = load_json("incidence")
        assert parsed == cached

    def test_parse_flaky(self):
        parsed = parse_en_pl(html["flaky"])
        cached = load_json("flaky")
        assert parsed == cached

    def test_parse_wager(self):
        parsed = parse_en_pl(html["wager"])
        cached = load_json("wager")
        assert parsed == cached

    def test_parse_curdled(self):
        parsed = parse_en_pl(html["curdled"])
        cached = load_json("curdled")
        assert parsed == cached

    def test_parse_insipid(self):
        parsed = parse_en_pl(html["insipid"])
        cached = load_json("insipid")
        assert parsed == cached

    def test_parse_presumptuousness(self):
        parsed = parse_en_pl(html["presumptuousness"])
        cached = load_json("presumptuousness")
        assert parsed == cached

    def test_parse_menacingly(self):
        parsed = parse_en_pl(html["menacingly"])
        cached = load_json("menacingly")
        assert parsed == cached

    def test_parse_lousy(self):
        parsed = parse_en_pl(html["lousy"])
        cached = load_json("lousy")
        assert parsed == cached

    def test_parse_metonymy(self):
        parsed = parse_en_pl(html["metonymy"])
        cached = load_json("metonymy")
        assert parsed == cached

    def test_parse_parsimonious(self):
        parsed = parse_en_pl(html["parsimonious"])
        cached = load_json("parsimonious")
        assert parsed == cached

    def test_parse_denounce(self):
        parsed = parse_en_pl(html["denounce"])
        cached = load_json("denounce")
        assert parsed == cached

    def test_parse_exert(self):
        parsed = parse_en_pl(html["exert"])
        cached = load_json("exert")
        assert parsed == cached

    def test_parse_bumbling(self):
        parsed = parse_en_pl(html["bumbling"])
        cached = load_json("bumbling")
        assert parsed == cached

    def test_parse_whim(self):
        parsed = parse_en_pl(html["whim"])
        cached = load_json("whim")
        assert parsed == cached

    def test_parse_transgression(self):
        parsed = parse_en_pl(html["transgression"])
        cached = load_json("transgression")
        assert parsed == cached

    def test_parse_sanction(self):
        parsed = parse_en_pl(html["sanction"])
        cached = load_json("sanction")
        assert parsed == cached

    def test_parse_theory(self):
        parsed = parse_en_pl(html["theory"])
        cached = load_json("theory")
        assert parsed == cached

    def test_parse_faciliate(self):
        parsed = parse_en_pl(html["faciliate"])
        cached = load_json("faciliate")
        assert parsed == cached

    def test_parse_fugue(self):
        parsed = parse_en_pl(html["fugue"])
        cached = load_json("fugue")
        assert parsed == cached

    def test_parse_bronchitis(self):
        parsed = parse_en_pl(html["bronchitis"])
        cached = load_json("bronchitis")
        assert parsed == cached

    def test_parse_cockeyed(self):
        parsed = parse_en_pl(html["cockeyed"])
        cached = load_json("cockeyed")
        assert parsed == cached

    def test_parse_pallor(self):
        parsed = parse_en_pl(html["pallor"])
        cached = load_json("pallor")
        assert parsed == cached

    def test_parse_cliche(self):
        parsed = parse_en_pl(html["cliche"])
        cached = load_json("cliche")
        assert parsed == cached

    def test_parse_fleece(self):
        parsed = parse_en_pl(html["fleece"])
        cached = load_json("fleece")
        assert parsed == cached

    def test_parse_embellished(self):
        parsed = parse_en_pl(html["embellished"])
        cached = load_json("embellished")
        assert parsed == cached

    def test_parse_evokes(self):
        parsed = parse_en_pl(html["evokes"])
        cached = load_json("evokes")
        assert parsed == cached

    def test_parse_hedge(self):
        parsed = parse_en_pl(html["hedge"])
        cached = load_json("hedge")
        assert parsed == cached

    def test_parse_pique(self):
        parsed = parse_en_pl(html["pique"])
        cached = load_json("pique")
        assert parsed == cached

    def test_parse_topiary(self):
        parsed = parse_en_pl(html["topiary"])
        cached = load_json("topiary")
        assert parsed == cached

    def test_parse_slack(self):
        parsed = parse_en_pl(html["slack"])
        cached = load_json("slack")
        assert parsed == cached

    def test_parse_prune(self):
        parsed = parse_en_pl(html["prune"])
        cached = load_json("prune")
        assert parsed == cached

    def test_parse_bleak(self):
        parsed = parse_en_pl(html["bleak"])
        cached = load_json("bleak")
        assert parsed == cached

    def test_parse_oxbow(self):
        parsed = parse_en_pl(html["oxbow"])
        cached = load_json("oxbow")
        assert parsed == cached

    def test_parse_coitus(self):
        parsed = parse_en_pl(html["coitus"])
        cached = load_json("coitus")
        assert parsed == cached

    def test_parse_lightning(self):
        parsed = parse_en_pl(html["lightning"])
        cached = load_json("lightning")
        assert parsed == cached

    def test_parse_morose(self):
        parsed = parse_en_pl(html["morose"])
        cached = load_json("morose")
        assert parsed == cached

    def test_parse_assiduous(self):
        parsed = parse_en_pl(html["assiduous"])
        cached = load_json("assiduous")
        assert parsed == cached

    def test_parse_legitimate(self):
        parsed = parse_en_pl(html["legitimate"])
        cached = load_json("legitimate")
        assert parsed == cached

    def test_parse_nether(self):
        parsed = parse_en_pl(html["nether"])
        cached = load_json("nether")
        assert parsed == cached

    def test_parse_valiant(self):
        parsed = parse_en_pl(html["valiant"])
        cached = load_json("valiant")
        assert parsed == cached

    def test_parse_fissure(self):
        parsed = parse_en_pl(html["fissure"])
        cached = load_json("fissure")
        assert parsed == cached

    def test_parse_jaded(self):
        parsed = parse_en_pl(html["jaded"])
        cached = load_json("jaded")
        assert parsed == cached

    def test_parse_demean(self):
        parsed = parse_en_pl(html["demean"])
        cached = load_json("demean")
        assert parsed == cached

    def test_parse_zest(self):
        parsed = parse_en_pl(html["zest"])
        cached = load_json("zest")
        assert parsed == cached

    def test_parse_preen(self):
        parsed = parse_en_pl(html["preen"])
        cached = load_json("preen")
        assert parsed == cached

    def test_parse_amanuensis(self):
        parsed = parse_en_pl(html["amanuensis"])
        cached = load_json("amanuensis")
        assert parsed == cached

    def test_parse_raucous(self):
        parsed = parse_en_pl(html["raucous"])
        cached = load_json("raucous")
        assert parsed == cached

    def test_parse_insatiable(self):
        parsed = parse_en_pl(html["insatiable"])
        cached = load_json("insatiable")
        assert parsed == cached

    def test_parse_litigious(self):
        parsed = parse_en_pl(html["litigious"])
        cached = load_json("litigious")
        assert parsed == cached

    def test_parse_lucre(self):
        parsed = parse_en_pl(html["lucre"])
        cached = load_json("lucre")
        assert parsed == cached

    def test_parse_sunset(self):
        parsed = parse_en_pl(html["sunset"])
        cached = load_json("sunset")
        assert parsed == cached

    def test_parse_abet(self):
        parsed = parse_en_pl(html["abet"])
        cached = load_json("abet")
        assert parsed == cached

    def test_parse_quench(self):
        parsed = parse_en_pl(html["quench"])
        cached = load_json("quench")
        assert parsed == cached

    def test_parse_grueling(self):
        parsed = parse_en_pl(html["grueling"])
        cached = load_json("grueling")
        assert parsed == cached

    def test_parse_ulcerate(self):
        parsed = parse_en_pl(html["ulcerate"])
        cached = load_json("ulcerate")
        assert parsed == cached

    def test_parse_vogue(self):
        parsed = parse_en_pl(html["vogue"])
        cached = load_json("vogue")
        assert parsed == cached

    def test_parse_fad(self):
        parsed = parse_en_pl(html["fad"])
        cached = load_json("fad")
        assert parsed == cached

    def test_parse_benign(self):
        parsed = parse_en_pl(html["benign"])
        cached = load_json("benign")
        assert parsed == cached

    def test_parse_grout(self):
        parsed = parse_en_pl(html["grout"])
        cached = load_json("grout")
        assert parsed == cached

    def test_parse_lard(self):
        parsed = parse_en_pl(html["lard"])
        cached = load_json("lard")
        assert parsed == cached

    def test_parse_labour(self):
        parsed = parse_en_pl(html["labour"])
        cached = load_json("labour")
        assert parsed == cached

    def test_parse_barnacle(self):
        parsed = parse_en_pl(html["barnacle"])
        cached = load_json("barnacle")
        assert parsed == cached

    def test_parse_agitate(self):
        parsed = parse_en_pl(html["agitate"])
        cached = load_json("agitate")
        assert parsed == cached

    def test_parse_soldier(self):
        parsed = parse_en_pl(html["soldier"])
        cached = load_json("soldier")
        assert parsed == cached

    def test_parse_infamous(self):
        parsed = parse_en_pl(html["infamous"])
        cached = load_json("infamous")
        assert parsed == cached

    def test_parse_evince(self):
        parsed = parse_en_pl(html["evince"])
        cached = load_json("evince")
        assert parsed == cached

    def test_parse_pungent(self):
        parsed = parse_en_pl(html["pungent"])
        cached = load_json("pungent")
        assert parsed == cached

    def test_parse_bereft(self):
        parsed = parse_en_pl(html["bereft"])
        cached = load_json("bereft")
        assert parsed == cached

    def test_parse_trailing(self):
        parsed = parse_en_pl(html["trailing"])
        cached = load_json("trailing")
        assert parsed == cached

    def test_parse_husky(self):
        parsed = parse_en_pl(html["husky"])
        cached = load_json("husky")
        assert parsed == cached

    def test_parse_miff(self):
        parsed = parse_en_pl(html["miff"])
        cached = load_json("miff")
        assert parsed == cached

    def test_parse_ointment(self):
        parsed = parse_en_pl(html["ointment"])
        cached = load_json("ointment")
        assert parsed == cached

    def test_parse_disrupt(self):
        parsed = parse_en_pl(html["disrupt"])
        cached = load_json("disrupt")
        assert parsed == cached

    def test_parse_later(self):
        parsed = parse_en_pl(html["later"])
        cached = load_json("later")
        assert parsed == cached

    def test_parse_gossamer(self):
        parsed = parse_en_pl(html["gossamer"])
        cached = load_json("gossamer")
        assert parsed == cached

    def test_parse_courtship(self):
        parsed = parse_en_pl(html["courtship"])
        cached = load_json("courtship")
        assert parsed == cached

    def test_parse_appall(self):
        parsed = parse_en_pl(html["appall"])
        cached = load_json("appall")
        assert parsed == cached

    def test_parse_wither(self):
        parsed = parse_en_pl(html["wither"])
        cached = load_json("wither")
        assert parsed == cached

    def test_parse_despatch(self):
        parsed = parse_en_pl(html["despatch"])
        cached = load_json("despatch")
        assert parsed == cached

    def test_parse_stooge(self):
        parsed = parse_en_pl(html["stooge"])
        cached = load_json("stooge")
        assert parsed == cached

    def test_parse_arboretum(self):
        parsed = parse_en_pl(html["arboretum"])
        cached = load_json("arboretum")
        assert parsed == cached

    def test_parse_infraction(self):
        parsed = parse_en_pl(html["infraction"])
        cached = load_json("infraction")
        assert parsed == cached

    def test_parse_flout(self):
        parsed = parse_en_pl(html["flout"])
        cached = load_json("flout")
        assert parsed == cached

    def test_parse_bunion(self):
        parsed = parse_en_pl(html["bunion"])
        cached = load_json("bunion")
        assert parsed == cached

    def test_parse_promiscuity(self):
        parsed = parse_en_pl(html["promiscuity"])
        cached = load_json("promiscuity")
        assert parsed == cached

    def test_parse_fraying(self):
        parsed = parse_en_pl(html["fraying"])
        cached = load_json("fraying")
        assert parsed == cached

    def test_parse_irate(self):
        parsed = parse_en_pl(html["irate"])
        cached = load_json("irate")
        assert parsed == cached

    def test_parse_loggerhead(self):
        parsed = parse_en_pl(html["loggerhead"])
        cached = load_json("loggerhead")
        assert parsed == cached

    def test_parse_strive(self):
        parsed = parse_en_pl(html["strive"])
        cached = load_json("strive")
        assert parsed == cached

    def test_parse_loony(self):
        parsed = parse_en_pl(html["loony"])
        cached = load_json("loony")
        assert parsed == cached

    def test_parse_midden(self):
        parsed = parse_en_pl(html["midden"])
        cached = load_json("midden")
        assert parsed == cached

    def test_parse_desultorily(self):
        parsed = parse_en_pl(html["desultorily"])
        cached = load_json("desultorily")
        assert parsed == cached

    def test_parse_motley(self):
        parsed = parse_en_pl(html["motley"])
        cached = load_json("motley")
        assert parsed == cached

    def test_parse_longing(self):
        parsed = parse_en_pl(html["longing"])
        cached = load_json("longing")
        assert parsed == cached

    def test_parse_bifurcation(self):
        parsed = parse_en_pl(html["bifurcation"])
        cached = load_json("bifurcation")
        assert parsed == cached

    def test_parse_groan(self):
        parsed = parse_en_pl(html["groan"])
        cached = load_json("groan")
        assert parsed == cached

    def test_parse_bile(self):
        parsed = parse_en_pl(html["bile"])
        cached = load_json("bile")
        assert parsed == cached

    def test_parse_pheasant(self):
        parsed = parse_en_pl(html["pheasant"])
        cached = load_json("pheasant")
        assert parsed == cached

    def test_parse_afoul(self):
        parsed = parse_en_pl(html["afoul"])
        cached = load_json("afoul")
        assert parsed == cached

    def test_parse_despondency(self):
        parsed = parse_en_pl(html["despondency"])
        cached = load_json("despondency")
        assert parsed == cached

    def test_parse_tetanus(self):
        parsed = parse_en_pl(html["tetanus"])
        cached = load_json("tetanus")
        assert parsed == cached

    def test_parse_perpetuity(self):
        parsed = parse_en_pl(html["perpetuity"])
        cached = load_json("perpetuity")
        assert parsed == cached

    def test_parse_pilfering(self):
        parsed = parse_en_pl(html["pilfering"])
        cached = load_json("pilfering")
        assert parsed == cached

    def test_parse_substitute(self):
        parsed = parse_en_pl(html["substitute"])
        cached = load_json("substitute")
        assert parsed == cached

    def test_parse_prowl(self):
        parsed = parse_en_pl(html["prowl"])
        cached = load_json("prowl")
        assert parsed == cached

    def test_parse_grue(self):
        parsed = parse_en_pl(html["grue"])
        cached = load_json("grue")
        assert parsed == cached

    def test_parse_bole(self):
        parsed = parse_en_pl(html["bole"])
        cached = load_json("bole")
        assert parsed == cached

    def test_parse_duende(self):
        parsed = parse_en_pl(html["duende"])
        cached = load_json("duende")
        assert parsed == cached

    def test_parse_token(self):
        parsed = parse_en_pl(html["token"])
        cached = load_json("token")
        assert parsed == cached

    def test_parse_condescension(self):
        parsed = parse_en_pl(html["condescension"])
        cached = load_json("condescension")
        assert parsed == cached

    def test_parse_indenture(self):
        parsed = parse_en_pl(html["indenture"])
        cached = load_json("indenture")
        assert parsed == cached

    def test_parse_sham(self):
        parsed = parse_en_pl(html["sham"])
        cached = load_json("sham")
        assert parsed == cached

    def test_parse_effluent(self):
        parsed = parse_en_pl(html["effluent"])
        cached = load_json("effluent")
        assert parsed == cached

    def test_parse_infantry(self):
        parsed = parse_en_pl(html["infantry"])
        cached = load_json("infantry")
        assert parsed == cached

    def test_parse_nematode(self):
        parsed = parse_en_pl(html["nematode"])
        cached = load_json("nematode")
        assert parsed == cached

    def test_parse_alopecia(self):
        parsed = parse_en_pl(html["alopecia"])
        cached = load_json("alopecia")
        assert parsed == cached

    def test_parse_bop(self):
        parsed = parse_en_pl(html["bop"])
        cached = load_json("bop")
        assert parsed == cached

    def test_parse_gamin(self):
        parsed = parse_en_pl(html["gamin"])
        cached = load_json("gamin")
        assert parsed == cached

    def test_parse_relent(self):
        parsed = parse_en_pl(html["relent"])
        cached = load_json("relent")
        assert parsed == cached

    def test_parse_fiddly(self):
        parsed = parse_en_pl(html["fiddly"])
        cached = load_json("fiddly")
        assert parsed == cached

    def test_parse_protein(self):
        parsed = parse_en_pl(html["protein"])
        cached = load_json("protein")
        assert parsed == cached

    def test_parse_trailblazing(self):
        parsed = parse_en_pl(html["trailblazing"])
        cached = load_json("trailblazing")
        assert parsed == cached

    def test_parse_exigency(self):
        parsed = parse_en_pl(html["exigency"])
        cached = load_json("exigency")
        assert parsed == cached

    def test_parse_perilous(self):
        parsed = parse_en_pl(html["perilous"])
        cached = load_json("perilous")
        assert parsed == cached

    def test_parse_gimp(self):
        parsed = parse_en_pl(html["gimp"])
        cached = load_json("gimp")
        assert parsed == cached

    def test_parse_precipice(self):
        parsed = parse_en_pl(html["precipice"])
        cached = load_json("precipice")
        assert parsed == cached

    def test_parse_imperil(self):
        parsed = parse_en_pl(html["imperil"])
        cached = load_json("imperil")
        assert parsed == cached

    def test_parse_quagmire(self):
        parsed = parse_en_pl(html["quagmire"])
        cached = load_json("quagmire")
        assert parsed == cached

    def test_parse_cull(self):
        parsed = parse_en_pl(html["cull"])
        cached = load_json("cull")
        assert parsed == cached

    def test_parse_litigator(self):
        parsed = parse_en_pl(html["litigator"])
        cached = load_json("litigator")
        assert parsed == cached

    def test_parse_indeterminate(self):
        parsed = parse_en_pl(html["indeterminate"])
        cached = load_json("indeterminate")
        assert parsed == cached

    def test_parse_uncharitable(self):
        parsed = parse_en_pl(html["uncharitable"])
        cached = load_json("uncharitable")
        assert parsed == cached

    def test_parse_trope(self):
        parsed = parse_en_pl(html["trope"])
        cached = load_json("trope")
        assert parsed == cached

    def test_parse_roundel(self):
        parsed = parse_en_pl(html["roundel"])
        cached = load_json("roundel")
        assert parsed == cached

    def test_parse_inveterate(self):
        parsed = parse_en_pl(html["inveterate"])
        cached = load_json("inveterate")
        assert parsed == cached

    def test_parse_heedlessly(self):
        parsed = parse_en_pl(html["heedlessly"])
        cached = load_json("heedlessly")
        assert parsed == cached

    def test_parse_littoral(self):
        parsed = parse_en_pl(html["littoral"])
        cached = load_json("littoral")
        assert parsed == cached

    def test_parse_spuriously(self):
        parsed = parse_en_pl(html["spuriously"])
        cached = load_json("spuriously")
        assert parsed == cached

    def test_parse_readability(self):
        parsed = parse_en_pl(html["readability"])
        cached = load_json("readability")
        assert parsed == cached

    def test_parse_sunder(self):
        parsed = parse_en_pl(html["sunder"])
        cached = load_json("sunder")
        assert parsed == cached

    def test_parse_curbing(self):
        parsed = parse_en_pl(html["curbing"])
        cached = load_json("curbing")
        assert parsed == cached

    def test_parse_fumes(self):
        parsed = parse_en_pl(html["fumes"])
        cached = load_json("fumes")
        assert parsed == cached

    def test_parse_congenital(self):
        parsed = parse_en_pl(html["congenital"])
        cached = load_json("congenital")
        assert parsed == cached

    def test_parse_rumination(self):
        parsed = parse_en_pl(html["rumination"])
        cached = load_json("rumination")
        assert parsed == cached

    def test_parse_drape(self):
        parsed = parse_en_pl(html["drape"])
        cached = load_json("drape")
        assert parsed == cached

    def test_parse_fulguration(self):
        parsed = parse_en_pl(html["fulguration"])
        cached = load_json("fulguration")
        assert parsed == cached

    def test_parse_pancreatitis(self):
        parsed = parse_en_pl(html["pancreatitis"])
        cached = load_json("pancreatitis")
        assert parsed == cached

    def test_parse_repugnance(self):
        parsed = parse_en_pl(html["repugnance"])
        cached = load_json("repugnance")
        assert parsed == cached

    def test_parse_bushel(self):
        parsed = parse_en_pl(html["bushel"])
        cached = load_json("bushel")
        assert parsed == cached

    def test_parse_wayward(self):
        parsed = parse_en_pl(html["wayward"])
        cached = load_json("wayward")
        assert parsed == cached

    def test_parse_sedulity(self):
        parsed = parse_en_pl(html["sedulity"])
        cached = load_json("sedulity")
        assert parsed == cached

    def test_parse_elision(self):
        parsed = parse_en_pl(html["elision"])
        cached = load_json("elision")
        assert parsed == cached

    def test_parse_paltry(self):
        parsed = parse_en_pl(html["paltry"])
        cached = load_json("paltry")
        assert parsed == cached

    def test_parse_friar(self):
        parsed = parse_en_pl(html["friar"])
        cached = load_json("friar")
        assert parsed == cached

    def test_parse_flue(self):
        parsed = parse_en_pl(html["flue"])
        cached = load_json("flue")
        assert parsed == cached

    def test_parse_fluff(self):
        parsed = parse_en_pl(html["fluff"])
        cached = load_json("fluff")
        assert parsed == cached

    def test_parse_deciduous(self):
        parsed = parse_en_pl(html["deciduous"])
        cached = load_json("deciduous")
        assert parsed == cached

    def test_parse_invalid(self):
        parsed = parse_en_pl(html["invalid"])
        cached = load_json("invalid")
        assert parsed == cached

    def test_parse_shrimp(self):
        parsed = parse_en_pl(html["shrimp"])
        cached = load_json("shrimp")
        assert parsed == cached

    def test_parse_vapor(self):
        parsed = parse_en_pl(html["vapor"])
        cached = load_json("vapor")
        assert parsed == cached

    def test_parse_vacation(self):
        parsed = parse_en_pl(html["vacation"])
        cached = load_json("vacation")
        assert parsed == cached

    def test_parse_gritty(self):
        parsed = parse_en_pl(html["gritty"])
        cached = load_json("gritty")
        assert parsed == cached

    def test_parse_crony(self):
        parsed = parse_en_pl(html["crony"])
        cached = load_json("crony")
        assert parsed == cached

    def test_parse_yarn(self):
        parsed = parse_en_pl(html["yarn"])
        cached = load_json("yarn")
        assert parsed == cached

    def test_parse_gypsy(self):
        parsed = parse_en_pl(html["gypsy"])
        cached = load_json("gypsy")
        assert parsed == cached

    def test_parse_sulk(self):
        parsed = parse_en_pl(html["sulk"])
        cached = load_json("sulk")
        assert parsed == cached

    def test_parse_eager(self):
        parsed = parse_en_pl(html["eager"])
        cached = load_json("eager")
        assert parsed == cached

    def test_parse_savvy(self):
        parsed = parse_en_pl(html["savvy"])
        cached = load_json("savvy")
        assert parsed == cached

    def test_parse_thrush(self):
        parsed = parse_en_pl(html["thrush"])
        cached = load_json("thrush")
        assert parsed == cached

    def test_parse_famished(self):
        parsed = parse_en_pl(html["famished"])
        cached = load_json("famished")
        assert parsed == cached

    def test_parse_wayfare(self):
        parsed = parse_en_pl(html["wayfare"])
        cached = load_json("wayfare")
        assert parsed == cached

    def test_parse_bargain(self):
        parsed = parse_en_pl(html["bargain"])
        cached = load_json("bargain")
        assert parsed == cached

    def test_parse_sinewy(self):
        parsed = parse_en_pl(html["sinewy"])
        cached = load_json("sinewy")
        assert parsed == cached

    def test_parse_inexplicably(self):
        parsed = parse_en_pl(html["inexplicably"])
        cached = load_json("inexplicably")
        assert parsed == cached

    def test_parse_beset(self):
        parsed = parse_en_pl(html["beset"])
        cached = load_json("beset")
        assert parsed == cached

    def test_parse_unhinge(self):
        parsed = parse_en_pl(html["unhinge"])
        cached = load_json("unhinge")
        assert parsed == cached

    def test_parse_immane(self):
        parsed = parse_en_pl(html["immane"])
        cached = load_json("immane")
        assert parsed == cached

    def test_parse_eking(self):
        parsed = parse_en_pl(html["eking"])
        cached = load_json("eking")
        assert parsed == cached

    def test_parse_sanctimonious(self):
        parsed = parse_en_pl(html["sanctimonious"])
        cached = load_json("sanctimonious")
        assert parsed == cached

    def test_parse_speakeasy(self):
        parsed = parse_en_pl(html["speakeasy"])
        cached = load_json("speakeasy")
        assert parsed == cached

    def test_parse_raspy(self):
        parsed = parse_en_pl(html["raspy"])
        cached = load_json("raspy")
        assert parsed == cached

    def test_parse_cattle(self):
        parsed = parse_en_pl(html["cattle"])
        cached = load_json("cattle")
        assert parsed == cached

    def test_parse_marmite(self):
        parsed = parse_en_pl(html["marmite"])
        cached = load_json("marmite")
        assert parsed == cached

    def test_parse_screwup(self):
        parsed = parse_en_pl(html["screwup"])
        cached = load_json("screwup")
        assert parsed == cached

    def test_parse_reckless(self):
        parsed = parse_en_pl(html["reckless"])
        cached = load_json("reckless")
        assert parsed == cached

    def test_parse_thicket(self):
        parsed = parse_en_pl(html["thicket"])
        cached = load_json("thicket")
        assert parsed == cached

    def test_parse_halter(self):
        parsed = parse_en_pl(html["halter"])
        cached = load_json("halter")
        assert parsed == cached

    def test_parse_goldilocks(self):
        parsed = parse_en_pl(html["goldilocks"])
        cached = load_json("goldilocks")
        assert parsed == cached

    def test_parse_yeoman(self):
        parsed = parse_en_pl(html["yeoman"])
        cached = load_json("yeoman")
        assert parsed == cached

    def test_parse_gumption(self):
        parsed = parse_en_pl(html["gumption"])
        cached = load_json("gumption")
        assert parsed == cached

    def test_parse_harmonious(self):
        parsed = parse_en_pl(html["harmonious"])
        cached = load_json("harmonious")
        assert parsed == cached

    def test_parse_guest(self):
        parsed = parse_en_pl(html["guest"])
        cached = load_json("guest")
        assert parsed == cached

    def test_parse_butler(self):
        parsed = parse_en_pl(html["butler"])
        cached = load_json("butler")
        assert parsed == cached

    def test_parse_tenacity(self):
        parsed = parse_en_pl(html["tenacity"])
        cached = load_json("tenacity")
        assert parsed == cached

    def test_parse_salacious(self):
        parsed = parse_en_pl(html["salacious"])
        cached = load_json("salacious")
        assert parsed == cached

    def test_parse_sentience(self):
        parsed = parse_en_pl(html["sentience"])
        cached = load_json("sentience")
        assert parsed == cached

    def test_parse_peddle(self):
        parsed = parse_en_pl(html["peddle"])
        cached = load_json("peddle")
        assert parsed == cached

    def test_parse_disbar(self):
        parsed = parse_en_pl(html["disbar"])
        cached = load_json("disbar")
        assert parsed == cached

    def test_parse_equanimity(self):
        parsed = parse_en_pl(html["equanimity"])
        cached = load_json("equanimity")
        assert parsed == cached

    def test_parse_catamite(self):
        parsed = parse_en_pl(html["catamite"])
        cached = load_json("catamite")
        assert parsed == cached

    def test_parse_taper(self):
        parsed = parse_en_pl(html["taper"])
        cached = load_json("taper")
        assert parsed == cached

    def test_parse_veneer(self):
        parsed = parse_en_pl(html["veneer"])
        cached = load_json("veneer")
        assert parsed == cached

    def test_parse_effect(self):
        parsed = parse_en_pl(html["effect"])
        cached = load_json("effect")
        assert parsed == cached

    def test_parse_hazmat(self):
        parsed = parse_en_pl(html["hazmat"])
        cached = load_json("hazmat")
        assert parsed == cached

    def test_parse_sobriquet(self):
        parsed = parse_en_pl(html["sobriquet"])
        cached = load_json("sobriquet")
        assert parsed == cached

    def test_parse_integrity(self):
        parsed = parse_en_pl(html["integrity"])
        cached = load_json("integrity")
        assert parsed == cached

    def test_parse_avarice(self):
        parsed = parse_en_pl(html["avarice"])
        cached = load_json("avarice")
        assert parsed == cached

    def test_parse_abate(self):
        parsed = parse_en_pl(html["abate"])
        cached = load_json("abate")
        assert parsed == cached

    def test_parse_salubrious(self):
        parsed = parse_en_pl(html["salubrious"])
        cached = load_json("salubrious")
        assert parsed == cached

    def test_parse_jocose(self):
        parsed = parse_en_pl(html["jocose"])
        cached = load_json("jocose")
        assert parsed == cached

    def test_parse_dilation(self):
        parsed = parse_en_pl(html["dilation"])
        cached = load_json("dilation")
        assert parsed == cached

    def test_parse_lemma(self):
        parsed = parse_en_pl(html["lemma"])
        cached = load_json("lemma")
        assert parsed == cached

    def test_parse_denigrate(self):
        parsed = parse_en_pl(html["denigrate"])
        cached = load_json("denigrate")
        assert parsed == cached

    def test_parse_beet(self):
        parsed = parse_en_pl(html["beet"])
        cached = load_json("beet")
        assert parsed == cached

    def test_parse_savour(self):
        parsed = parse_en_pl(html["savour"])
        cached = load_json("savour")
        assert parsed == cached

    def test_parse_martyr(self):
        parsed = parse_en_pl(html["martyr"])
        cached = load_json("martyr")
        assert parsed == cached

    def test_parse_laryngitis(self):
        parsed = parse_en_pl(html["laryngitis"])
        cached = load_json("laryngitis")
        assert parsed == cached

    def test_parse_ignominious(self):
        parsed = parse_en_pl(html["ignominious"])
        cached = load_json("ignominious")
        assert parsed == cached

    def test_parse_senile(self):
        parsed = parse_en_pl(html["senile"])
        cached = load_json("senile")
        assert parsed == cached

    def test_parse_intervention(self):
        parsed = parse_en_pl(html["intervention"])
        cached = load_json("intervention")
        assert parsed == cached

    def test_parse_embezzlement(self):
        parsed = parse_en_pl(html["embezzlement"])
        cached = load_json("embezzlement")
        assert parsed == cached

    def test_parse_bitters(self):
        parsed = parse_en_pl(html["bitters"])
        cached = load_json("bitters")
        assert parsed == cached

    def test_parse_vivisection(self):
        parsed = parse_en_pl(html["vivisection"])
        cached = load_json("vivisection")
        assert parsed == cached

    def test_parse_frothy(self):
        parsed = parse_en_pl(html["frothy"])
        cached = load_json("frothy")
        assert parsed == cached

    def test_parse_amity(self):
        parsed = parse_en_pl(html["amity"])
        cached = load_json("amity")
        assert parsed == cached

    def test_parse_hussy(self):
        parsed = parse_en_pl(html["hussy"])
        cached = load_json("hussy")
        assert parsed == cached

    def test_parse_virile(self):
        parsed = parse_en_pl(html["virile"])
        cached = load_json("virile")
        assert parsed == cached

    def test_parse_snoop(self):
        parsed = parse_en_pl(html["snoop"])
        cached = load_json("snoop")
        assert parsed == cached

    def test_parse_abeyance(self):
        parsed = parse_en_pl(html["abeyance"])
        cached = load_json("abeyance")
        assert parsed == cached

    def test_parse_raddled(self):
        parsed = parse_en_pl(html["raddled"])
        cached = load_json("raddled")
        assert parsed == cached

    def test_parse_vacuous(self):
        parsed = parse_en_pl(html["vacuous"])
        cached = load_json("vacuous")
        assert parsed == cached

    def test_parse_murmuring(self):
        parsed = parse_en_pl(html["murmuring"])
        cached = load_json("murmuring")
        assert parsed == cached

    def test_parse_kindling(self):
        parsed = parse_en_pl(html["kindling"])
        cached = load_json("kindling")
        assert parsed == cached

    def test_parse_sweep(self):
        parsed = parse_en_pl(html["sweep"])
        cached = load_json("sweep")
        assert parsed == cached

    def test_parse_defect(self):
        parsed = parse_en_pl(html["defect"])
        cached = load_json("defect")
        assert parsed == cached

    def test_parse_skid(self):
        parsed = parse_en_pl(html["skid"])
        cached = load_json("skid")
        assert parsed == cached

    def test_parse_interweave(self):
        parsed = parse_en_pl(html["interweave"])
        cached = load_json("interweave")
        assert parsed == cached

    def test_parse_beading(self):
        parsed = parse_en_pl(html["beading"])
        cached = load_json("beading")
        assert parsed == cached

    def test_parse_egotism(self):
        parsed = parse_en_pl(html["egotism"])
        cached = load_json("egotism")
        assert parsed == cached

    def test_parse_aerated(self):
        parsed = parse_en_pl(html["aerated"])
        cached = load_json("aerated")
        assert parsed == cached

    def test_parse_con(self):
        parsed = parse_en_pl(html["con"])
        cached = load_json("con")
        assert parsed == cached

    def test_parse_commence(self):
        parsed = parse_en_pl(html["commence"])
        cached = load_json("commence")
        assert parsed == cached

    def test_parse_care(self):
        parsed = parse_en_pl(html["care"])
        cached = load_json("care")
        assert parsed == cached

    def test_parse_genteel(self):
        parsed = parse_en_pl(html["genteel"])
        cached = load_json("genteel")
        assert parsed == cached

    def test_parse_disavow(self):
        parsed = parse_en_pl(html["disavow"])
        cached = load_json("disavow")
        assert parsed == cached

    def test_parse_conjecture(self):
        parsed = parse_en_pl(html["conjecture"])
        cached = load_json("conjecture")
        assert parsed == cached

    def test_parse_skewer(self):
        parsed = parse_en_pl(html["skewer"])
        cached = load_json("skewer")
        assert parsed == cached

    def test_parse_consolidate(self):
        parsed = parse_en_pl(html["consolidate"])
        cached = load_json("consolidate")
        assert parsed == cached

    def test_parse_remit(self):
        parsed = parse_en_pl(html["remit"])
        cached = load_json("remit")
        assert parsed == cached

    def test_parse_aging(self):
        parsed = parse_en_pl(html["aging"])
        cached = load_json("aging")
        assert parsed == cached

    def test_parse_badger(self):
        parsed = parse_en_pl(html["badger"])
        cached = load_json("badger")
        assert parsed == cached

    def test_parse_tangible(self):
        parsed = parse_en_pl(html["tangible"])
        cached = load_json("tangible")
        assert parsed == cached

    def test_parse_vigil(self):
        parsed = parse_en_pl(html["vigil"])
        cached = load_json("vigil")
        assert parsed == cached

    def test_parse_sag(self):
        parsed = parse_en_pl(html["sag"])
        cached = load_json("sag")
        assert parsed == cached

    def test_parse_gerbil(self):
        parsed = parse_en_pl(html["gerbil"])
        cached = load_json("gerbil")
        assert parsed == cached

    def test_parse_fierceness(self):
        parsed = parse_en_pl(html["fierceness"])
        cached = load_json("fierceness")
        assert parsed == cached

    def test_parse_quiver(self):
        parsed = parse_en_pl(html["quiver"])
        cached = load_json("quiver")
        assert parsed == cached

    def test_parse_itinerary(self):
        parsed = parse_en_pl(html["itinerary"])
        cached = load_json("itinerary")
        assert parsed == cached

    def test_parse_presupposition(self):
        parsed = parse_en_pl(html["presupposition"])
        cached = load_json("presupposition")
        assert parsed == cached

    def test_parse_gaol(self):
        parsed = parse_en_pl(html["gaol"])
        cached = load_json("gaol")
        assert parsed == cached

    def test_parse_ronin(self):
        parsed = parse_en_pl(html["ronin"])
        cached = load_json("ronin")
        assert parsed == cached

    def test_parse_clatter(self):
        parsed = parse_en_pl(html["clatter"])
        cached = load_json("clatter")
        assert parsed == cached

    def test_parse_eek(self):
        parsed = parse_en_pl(html["eek"])
        cached = load_json("eek")
        assert parsed == cached

    def test_parse_quaff(self):
        parsed = parse_en_pl(html["quaff"])
        cached = load_json("quaff")
        assert parsed == cached

    def test_parse_shin(self):
        parsed = parse_en_pl(html["shin"])
        cached = load_json("shin")
        assert parsed == cached

    def test_parse_precipitation(self):
        parsed = parse_en_pl(html["precipitation"])
        cached = load_json("precipitation")
        assert parsed == cached

    def test_parse_flax(self):
        parsed = parse_en_pl(html["flax"])
        cached = load_json("flax")
        assert parsed == cached

    def test_parse_quietude(self):
        parsed = parse_en_pl(html["quietude"])
        cached = load_json("quietude")
        assert parsed == cached

    def test_parse_bohemian(self):
        parsed = parse_en_pl(html["bohemian"])
        cached = load_json("bohemian")
        assert parsed == cached

    def test_parse_palate(self):
        parsed = parse_en_pl(html["palate"])
        cached = load_json("palate")
        assert parsed == cached

    def test_parse_prolix(self):
        parsed = parse_en_pl(html["prolix"])
        cached = load_json("prolix")
        assert parsed == cached

    def test_parse_mink(self):
        parsed = parse_en_pl(html["mink"])
        cached = load_json("mink")
        assert parsed == cached

    def test_parse_reconcile(self):
        parsed = parse_en_pl(html["reconcile"])
        cached = load_json("reconcile")
        assert parsed == cached

    def test_parse_morass(self):
        parsed = parse_en_pl(html["morass"])
        cached = load_json("morass")
        assert parsed == cached

    def test_parse_fallible(self):
        parsed = parse_en_pl(html["fallible"])
        cached = load_json("fallible")
        assert parsed == cached

    def test_parse_centrifuge(self):
        parsed = parse_en_pl(html["centrifuge"])
        cached = load_json("centrifuge")
        assert parsed == cached

    def test_parse_inculcate(self):
        parsed = parse_en_pl(html["inculcate"])
        cached = load_json("inculcate")
        assert parsed == cached

    def test_parse_fussy(self):
        parsed = parse_en_pl(html["fussy"])
        cached = load_json("fussy")
        assert parsed == cached

    def test_parse_boozer(self):
        parsed = parse_en_pl(html["boozer"])
        cached = load_json("boozer")
        assert parsed == cached

    def test_parse_cairn(self):
        parsed = parse_en_pl(html["cairn"])
        cached = load_json("cairn")
        assert parsed == cached

    def test_parse_cleft(self):
        parsed = parse_en_pl(html["cleft"])
        cached = load_json("cleft")
        assert parsed == cached

    def test_parse_auxilary(self):
        parsed = parse_en_pl(html["auxilary"])
        cached = load_json("auxilary")
        assert parsed == cached

    def test_parse_stele(self):
        parsed = parse_en_pl(html["stele"])
        cached = load_json("stele")
        assert parsed == cached

    def test_parse_restitution(self):
        parsed = parse_en_pl(html["restitution"])
        cached = load_json("restitution")
        assert parsed == cached

    def test_parse_flippant(self):
        parsed = parse_en_pl(html["flippant"])
        cached = load_json("flippant")
        assert parsed == cached

    def test_parse_fidgety(self):
        parsed = parse_en_pl(html["fidgety"])
        cached = load_json("fidgety")
        assert parsed == cached

    def test_parse_contortion(self):
        parsed = parse_en_pl(html["contortion"])
        cached = load_json("contortion")
        assert parsed == cached

    def test_parse_obscene(self):
        parsed = parse_en_pl(html["obscene"])
        cached = load_json("obscene")
        assert parsed == cached

    def test_parse_jeopardy(self):
        parsed = parse_en_pl(html["jeopardy"])
        cached = load_json("jeopardy")
        assert parsed == cached

    def test_parse_facetious(self):
        parsed = parse_en_pl(html["facetious"])
        cached = load_json("facetious")
        assert parsed == cached

    def test_parse_venerate(self):
        parsed = parse_en_pl(html["venerate"])
        cached = load_json("venerate")
        assert parsed == cached

    def test_parse_chunky(self):
        parsed = parse_en_pl(html["chunky"])
        cached = load_json("chunky")
        assert parsed == cached

    def test_parse_osprey(self):
        parsed = parse_en_pl(html["osprey"])
        cached = load_json("osprey")
        assert parsed == cached

    def test_parse_rally(self):
        parsed = parse_en_pl(html["rally"])
        cached = load_json("rally")
        assert parsed == cached

    def test_parse_foster(self):
        parsed = parse_en_pl(html["foster"])
        cached = load_json("foster")
        assert parsed == cached

    def test_parse_pace(self):
        parsed = parse_en_pl(html["pace"])
        cached = load_json("pace")
        assert parsed == cached

    def test_parse_bland(self):
        parsed = parse_en_pl(html["bland"])
        cached = load_json("bland")
        assert parsed == cached

    def test_parse_sling(self):
        parsed = parse_en_pl(html["sling"])
        cached = load_json("sling")
        assert parsed == cached

    def test_parse_posh(self):
        parsed = parse_en_pl(html["posh"])
        cached = load_json("posh")
        assert parsed == cached

    def test_parse_unsightly(self):
        parsed = parse_en_pl(html["unsightly"])
        cached = load_json("unsightly")
        assert parsed == cached

    def test_parse_bobcat(self):
        parsed = parse_en_pl(html["bobcat"])
        cached = load_json("bobcat")
        assert parsed == cached

    def test_parse_stricture(self):
        parsed = parse_en_pl(html["stricture"])
        cached = load_json("stricture")
        assert parsed == cached

    def test_parse_blindsided(self):
        parsed = parse_en_pl(html["blindsided"])
        cached = load_json("blindsided")
        assert parsed == cached

    def test_parse_unilateral(self):
        parsed = parse_en_pl(html["unilateral"])
        cached = load_json("unilateral")
        assert parsed == cached

    def test_parse_perseverance(self):
        parsed = parse_en_pl(html["perseverance"])
        cached = load_json("perseverance")
        assert parsed == cached

    def test_parse_herbicide(self):
        parsed = parse_en_pl(html["herbicide"])
        cached = load_json("herbicide")
        assert parsed == cached

    def test_parse_adversity(self):
        parsed = parse_en_pl(html["adversity"])
        cached = load_json("adversity")
        assert parsed == cached

    def test_parse_garble(self):
        parsed = parse_en_pl(html["garble"])
        cached = load_json("garble")
        assert parsed == cached

    def test_parse_strained(self):
        parsed = parse_en_pl(html["strained"])
        cached = load_json("strained")
        assert parsed == cached

    def test_parse_meadow(self):
        parsed = parse_en_pl(html["meadow"])
        cached = load_json("meadow")
        assert parsed == cached

    def test_parse_spleen(self):
        parsed = parse_en_pl(html["spleen"])
        cached = load_json("spleen")
        assert parsed == cached

    def test_parse_vassalage(self):
        parsed = parse_en_pl(html["vassalage"])
        cached = load_json("vassalage")
        assert parsed == cached

    def test_parse_violent(self):
        parsed = parse_en_pl(html["violent"])
        cached = load_json("violent")
        assert parsed == cached

    def test_parse_tenuous(self):
        parsed = parse_en_pl(html["tenuous"])
        cached = load_json("tenuous")
        assert parsed == cached

    def test_parse_inhibit(self):
        parsed = parse_en_pl(html["inhibit"])
        cached = load_json("inhibit")
        assert parsed == cached

    def test_parse_untenable(self):
        parsed = parse_en_pl(html["untenable"])
        cached = load_json("untenable")
        assert parsed == cached

    def test_parse_equity(self):
        parsed = parse_en_pl(html["equity"])
        cached = load_json("equity")
        assert parsed == cached

    def test_parse_pertinently(self):
        parsed = parse_en_pl(html["pertinently"])
        cached = load_json("pertinently")
        assert parsed == cached

    def test_parse_gasket(self):
        parsed = parse_en_pl(html["gasket"])
        cached = load_json("gasket")
        assert parsed == cached

    def test_parse_neglect(self):
        parsed = parse_en_pl(html["neglect"])
        cached = load_json("neglect")
        assert parsed == cached

    def test_parse_ruffled(self):
        parsed = parse_en_pl(html["ruffled"])
        cached = load_json("ruffled")
        assert parsed == cached

    def test_parse_inoculation(self):
        parsed = parse_en_pl(html["inoculation"])
        cached = load_json("inoculation")
        assert parsed == cached

    def test_parse_tough(self):
        parsed = parse_en_pl(html["tough"])
        cached = load_json("tough")
        assert parsed == cached

    def test_parse_solidarity(self):
        parsed = parse_en_pl(html["solidarity"])
        cached = load_json("solidarity")
        assert parsed == cached

    def test_parse_sulking(self):
        parsed = parse_en_pl(html["sulking"])
        cached = load_json("sulking")
        assert parsed == cached

    def test_parse_brittle(self):
        parsed = parse_en_pl(html["brittle"])
        cached = load_json("brittle")
        assert parsed == cached

    def test_parse_unsavory(self):
        parsed = parse_en_pl(html["unsavory"])
        cached = load_json("unsavory")
        assert parsed == cached

    def test_parse_altogether(self):
        parsed = parse_en_pl(html["altogether"])
        cached = load_json("altogether")
        assert parsed == cached

    def test_parse_disturbed(self):
        parsed = parse_en_pl(html["disturbed"])
        cached = load_json("disturbed")
        assert parsed == cached

    def test_parse_parish(self):
        parsed = parse_en_pl(html["parish"])
        cached = load_json("parish")
        assert parsed == cached

    def test_parse_fanny(self):
        parsed = parse_en_pl(html["fanny"])
        cached = load_json("fanny")
        assert parsed == cached

    def test_parse_prolific(self):
        parsed = parse_en_pl(html["prolific"])
        cached = load_json("prolific")
        assert parsed == cached

    def test_parse_cater(self):
        parsed = parse_en_pl(html["cater"])
        cached = load_json("cater")
        assert parsed == cached

    def test_parse_punctilious(self):
        parsed = parse_en_pl(html["punctilious"])
        cached = load_json("punctilious")
        assert parsed == cached

    def test_parse_shaft(self):
        parsed = parse_en_pl(html["shaft"])
        cached = load_json("shaft")
        assert parsed == cached

    def test_parse_jell(self):
        parsed = parse_en_pl(html["jell"])
        cached = load_json("jell")
        assert parsed == cached

    def test_parse_acerbic(self):
        parsed = parse_en_pl(html["acerbic"])
        cached = load_json("acerbic")
        assert parsed == cached

    def test_parse_wicked(self):
        parsed = parse_en_pl(html["wicked"])
        cached = load_json("wicked")
        assert parsed == cached

    def test_parse_incarceration(self):
        parsed = parse_en_pl(html["incarceration"])
        cached = load_json("incarceration")
        assert parsed == cached

    def test_parse_chokehold(self):
        parsed = parse_en_pl(html["chokehold"])
        cached = load_json("chokehold")
        assert parsed == cached

    def test_parse_distressing(self):
        parsed = parse_en_pl(html["distressing"])
        cached = load_json("distressing")
        assert parsed == cached

    def test_parse_clover(self):
        parsed = parse_en_pl(html["clover"])
        cached = load_json("clover")
        assert parsed == cached

    def test_parse_teak(self):
        parsed = parse_en_pl(html["teak"])
        cached = load_json("teak")
        assert parsed == cached

    def test_parse_pariah(self):
        parsed = parse_en_pl(html["pariah"])
        cached = load_json("pariah")
        assert parsed == cached

    def test_parse_pious(self):
        parsed = parse_en_pl(html["pious"])
        cached = load_json("pious")
        assert parsed == cached

    def test_parse_homemaker(self):
        parsed = parse_en_pl(html["homemaker"])
        cached = load_json("homemaker")
        assert parsed == cached

    def test_parse_rabble(self):
        parsed = parse_en_pl(html["rabble"])
        cached = load_json("rabble")
        assert parsed == cached

    def test_parse_repugnant(self):
        parsed = parse_en_pl(html["repugnant"])
        cached = load_json("repugnant")
        assert parsed == cached

    def test_parse_millet(self):
        parsed = parse_en_pl(html["millet"])
        cached = load_json("millet")
        assert parsed == cached

    def test_parse_hieratic(self):
        parsed = parse_en_pl(html["hieratic"])
        cached = load_json("hieratic")
        assert parsed == cached

    def test_parse_pliable(self):
        parsed = parse_en_pl(html["pliable"])
        cached = load_json("pliable")
        assert parsed == cached

    def test_parse_derived(self):
        parsed = parse_en_pl(html["derived"])
        cached = load_json("derived")
        assert parsed == cached

    def test_parse_surmise(self):
        parsed = parse_en_pl(html["surmise"])
        cached = load_json("surmise")
        assert parsed == cached

    def test_parse_ominous(self):
        parsed = parse_en_pl(html["ominous"])
        cached = load_json("ominous")
        assert parsed == cached

    def test_parse_whimsical(self):
        parsed = parse_en_pl(html["whimsical"])
        cached = load_json("whimsical")
        assert parsed == cached

    def test_parse_indentured(self):
        parsed = parse_en_pl(html["indentured"])
        cached = load_json("indentured")
        assert parsed == cached

    def test_parse_further(self):
        parsed = parse_en_pl(html["further"])
        cached = load_json("further")
        assert parsed == cached

    def test_parse_argot(self):
        parsed = parse_en_pl(html["argot"])
        cached = load_json("argot")
        assert parsed == cached

    def test_parse_abode(self):
        parsed = parse_en_pl(html["abode"])
        cached = load_json("abode")
        assert parsed == cached

    def test_parse_shed(self):
        parsed = parse_en_pl(html["shed"])
        cached = load_json("shed")
        assert parsed == cached

    def test_parse_chiefly(self):
        parsed = parse_en_pl(html["chiefly"])
        cached = load_json("chiefly")
        assert parsed == cached

    def test_parse_burden(self):
        parsed = parse_en_pl(html["burden"])
        cached = load_json("burden")
        assert parsed == cached

    def test_parse_placenta(self):
        parsed = parse_en_pl(html["placenta"])
        cached = load_json("placenta")
        assert parsed == cached

    def test_parse_hireling(self):
        parsed = parse_en_pl(html["hireling"])
        cached = load_json("hireling")
        assert parsed == cached

    def test_parse_saunter(self):
        parsed = parse_en_pl(html["saunter"])
        cached = load_json("saunter")
        assert parsed == cached

    def test_parse_moniker(self):
        parsed = parse_en_pl(html["moniker"])
        cached = load_json("moniker")
        assert parsed == cached

    def test_parse_perseverative(self):
        parsed = parse_en_pl(html["perseverative"])
        cached = load_json("perseverative")
        assert parsed == cached

    def test_parse_tribunal(self):
        parsed = parse_en_pl(html["tribunal"])
        cached = load_json("tribunal")
        assert parsed == cached

    def test_parse_sputter(self):
        parsed = parse_en_pl(html["sputter"])
        cached = load_json("sputter")
        assert parsed == cached

    def test_parse_singular(self):
        parsed = parse_en_pl(html["singular"])
        cached = load_json("singular")
        assert parsed == cached

    def test_parse_backhanded(self):
        parsed = parse_en_pl(html["backhanded"])
        cached = load_json("backhanded")
        assert parsed == cached

    def test_parse_meld(self):
        parsed = parse_en_pl(html["meld"])
        cached = load_json("meld")
        assert parsed == cached

    def test_parse_slim(self):
        parsed = parse_en_pl(html["slim"])
        cached = load_json("slim")
        assert parsed == cached

    def test_parse_innuendo(self):
        parsed = parse_en_pl(html["innuendo"])
        cached = load_json("innuendo")
        assert parsed == cached

    def test_parse_brash(self):
        parsed = parse_en_pl(html["brash"])
        cached = load_json("brash")
        assert parsed == cached

    def test_parse_infirmary(self):
        parsed = parse_en_pl(html["infirmary"])
        cached = load_json("infirmary")
        assert parsed == cached

    def test_parse_eve(self):
        parsed = parse_en_pl(html["eve"])
        cached = load_json("eve")
        assert parsed == cached

    def test_parse_bullhorn(self):
        parsed = parse_en_pl(html["bullhorn"])
        cached = load_json("bullhorn")
        assert parsed == cached

    def test_parse_trepidation(self):
        parsed = parse_en_pl(html["trepidation"])
        cached = load_json("trepidation")
        assert parsed == cached

    def test_parse_clairvoyance(self):
        parsed = parse_en_pl(html["clairvoyance"])
        cached = load_json("clairvoyance")
        assert parsed == cached

    def test_parse_subversive(self):
        parsed = parse_en_pl(html["subversive"])
        cached = load_json("subversive")
        assert parsed == cached

    def test_parse_bestow(self):
        parsed = parse_en_pl(html["bestow"])
        cached = load_json("bestow")
        assert parsed == cached

    def test_parse_awash(self):
        parsed = parse_en_pl(html["awash"])
        cached = load_json("awash")
        assert parsed == cached

    def test_parse_tawdry(self):
        parsed = parse_en_pl(html["tawdry"])
        cached = load_json("tawdry")
        assert parsed == cached

    def test_parse_yield(self):
        parsed = parse_en_pl(html["yield"])
        cached = load_json("yield")
        assert parsed == cached

    def test_parse_molar(self):
        parsed = parse_en_pl(html["molar"])
        cached = load_json("molar")
        assert parsed == cached

    def test_parse_dispassionate(self):
        parsed = parse_en_pl(html["dispassionate"])
        cached = load_json("dispassionate")
        assert parsed == cached

    def test_parse_unyielding(self):
        parsed = parse_en_pl(html["unyielding"])
        cached = load_json("unyielding")
        assert parsed == cached

    def test_parse_dull(self):
        parsed = parse_en_pl(html["dull"])
        cached = load_json("dull")
        assert parsed == cached

    def test_parse_squish(self):
        parsed = parse_en_pl(html["squish"])
        cached = load_json("squish")
        assert parsed == cached

    def test_parse_dictum(self):
        parsed = parse_en_pl(html["dictum"])
        cached = load_json("dictum")
        assert parsed == cached

    def test_parse_comatose(self):
        parsed = parse_en_pl(html["comatose"])
        cached = load_json("comatose")
        assert parsed == cached

    def test_parse_musty(self):
        parsed = parse_en_pl(html["musty"])
        cached = load_json("musty")
        assert parsed == cached

    def test_parse_rigmarole(self):
        parsed = parse_en_pl(html["rigmarole"])
        cached = load_json("rigmarole")
        assert parsed == cached

    def test_parse_spasm(self):
        parsed = parse_en_pl(html["spasm"])
        cached = load_json("spasm")
        assert parsed == cached

    def test_parse_distress(self):
        parsed = parse_en_pl(html["distress"])
        cached = load_json("distress")
        assert parsed == cached

    def test_parse_stillborn(self):
        parsed = parse_en_pl(html["stillborn"])
        cached = load_json("stillborn")
        assert parsed == cached

    def test_parse_gloomy(self):
        parsed = parse_en_pl(html["gloomy"])
        cached = load_json("gloomy")
        assert parsed == cached

    def test_parse_incantatory(self):
        parsed = parse_en_pl(html["incantatory"])
        cached = load_json("incantatory")
        assert parsed == cached

    def test_parse_gutter(self):
        parsed = parse_en_pl(html["gutter"])
        cached = load_json("gutter")
        assert parsed == cached

    def test_parse_fond(self):
        parsed = parse_en_pl(html["fond"])
        cached = load_json("fond")
        assert parsed == cached

    def test_parse_melanoma(self):
        parsed = parse_en_pl(html["melanoma"])
        cached = load_json("melanoma")
        assert parsed == cached

    def test_parse_tread(self):
        parsed = parse_en_pl(html["tread"])
        cached = load_json("tread")
        assert parsed == cached

    def test_parse_acquit(self):
        parsed = parse_en_pl(html["acquit"])
        cached = load_json("acquit")
        assert parsed == cached

    def test_parse_fumigate(self):
        parsed = parse_en_pl(html["fumigate"])
        cached = load_json("fumigate")
        assert parsed == cached

    def test_parse_foil(self):
        parsed = parse_en_pl(html["foil"])
        cached = load_json("foil")
        assert parsed == cached

    def test_parse_bristle(self):
        parsed = parse_en_pl(html["bristle"])
        cached = load_json("bristle")
        assert parsed == cached

    def test_parse_Fan(self):
        parsed = parse_en_pl(html["Fan"])
        cached = load_json("Fan")
        assert parsed == cached

    def test_parse_stature(self):
        parsed = parse_en_pl(html["stature"])
        cached = load_json("stature")
        assert parsed == cached

    def test_parse_baulk(self):
        parsed = parse_en_pl(html["baulk"])
        cached = load_json("baulk")
        assert parsed == cached

    def test_parse_apprehension(self):
        parsed = parse_en_pl(html["apprehension"])
        cached = load_json("apprehension")
        assert parsed == cached

    def test_parse_abrasive(self):
        parsed = parse_en_pl(html["abrasive"])
        cached = load_json("abrasive")
        assert parsed == cached

    def test_parse_defy(self):
        parsed = parse_en_pl(html["defy"])
        cached = load_json("defy")
        assert parsed == cached

    def test_parse_eminently(self):
        parsed = parse_en_pl(html["eminently"])
        cached = load_json("eminently")
        assert parsed == cached

    def test_parse_harken(self):
        parsed = parse_en_pl(html["harken"])
        cached = load_json("harken")
        assert parsed == cached

    def test_parse_limper(self):
        parsed = parse_en_pl(html["limper"])
        cached = load_json("limper")
        assert parsed == cached

    def test_parse_disbarment(self):
        parsed = parse_en_pl(html["disbarment"])
        cached = load_json("disbarment")
        assert parsed == cached

    def test_parse_acrimonious(self):
        parsed = parse_en_pl(html["acrimonious"])
        cached = load_json("acrimonious")
        assert parsed == cached

    def test_parse_enduring(self):
        parsed = parse_en_pl(html["enduring"])
        cached = load_json("enduring")
        assert parsed == cached

    def test_parse_recap(self):
        parsed = parse_en_pl(html["recap"])
        cached = load_json("recap")
        assert parsed == cached

    def test_parse_transient(self):
        parsed = parse_en_pl(html["transient"])
        cached = load_json("transient")
        assert parsed == cached

    def test_parse_forgo(self):
        parsed = parse_en_pl(html["forgo"])
        cached = load_json("forgo")
        assert parsed == cached

    def test_parse_enamel(self):
        parsed = parse_en_pl(html["enamel"])
        cached = load_json("enamel")
        assert parsed == cached

    def test_parse_serenity(self):
        parsed = parse_en_pl(html["serenity"])
        cached = load_json("serenity")
        assert parsed == cached

    def test_parse_soggy(self):
        parsed = parse_en_pl(html["soggy"])
        cached = load_json("soggy")
        assert parsed == cached

    def test_parse_binding(self):
        parsed = parse_en_pl(html["binding"])
        cached = load_json("binding")
        assert parsed == cached

    def test_parse_bulge(self):
        parsed = parse_en_pl(html["bulge"])
        cached = load_json("bulge")
        assert parsed == cached

    def test_parse_loth(self):
        parsed = parse_en_pl(html["loth"])
        cached = load_json("loth")
        assert parsed == cached

    def test_parse_salve(self):
        parsed = parse_en_pl(html["salve"])
        cached = load_json("salve")
        assert parsed == cached

    def test_parse_shawl(self):
        parsed = parse_en_pl(html["shawl"])
        cached = load_json("shawl")
        assert parsed == cached

    def test_parse_manger(self):
        parsed = parse_en_pl(html["manger"])
        cached = load_json("manger")
        assert parsed == cached

    def test_parse_festering(self):
        parsed = parse_en_pl(html["festering"])
        cached = load_json("festering")
        assert parsed == cached

    def test_parse_feisty(self):
        parsed = parse_en_pl(html["feisty"])
        cached = load_json("feisty")
        assert parsed == cached

    def test_parse_barmy(self):
        parsed = parse_en_pl(html["barmy"])
        cached = load_json("barmy")
        assert parsed == cached

    def test_parse_qualm(self):
        parsed = parse_en_pl(html["qualm"])
        cached = load_json("qualm")
        assert parsed == cached

    def test_parse_and(self):
        parsed = parse_en_pl(html["and"])
        cached = load_json("and")
        assert parsed == cached

    def test_parse_patrimony(self):
        parsed = parse_en_pl(html["patrimony"])
        cached = load_json("patrimony")
        assert parsed == cached

    def test_parse_yelp(self):
        parsed = parse_en_pl(html["yelp"])
        cached = load_json("yelp")
        assert parsed == cached

    def test_parse_prattle(self):
        parsed = parse_en_pl(html["prattle"])
        cached = load_json("prattle")
        assert parsed == cached

    def test_parse_crow(self):
        parsed = parse_en_pl(html["crow"])
        cached = load_json("crow")
        assert parsed == cached

    def test_parse_jurisprudence(self):
        parsed = parse_en_pl(html["jurisprudence"])
        cached = load_json("jurisprudence")
        assert parsed == cached

    def test_parse_leach(self):
        parsed = parse_en_pl(html["leach"])
        cached = load_json("leach")
        assert parsed == cached

    def test_parse_stencil(self):
        parsed = parse_en_pl(html["stencil"])
        cached = load_json("stencil")
        assert parsed == cached

    def test_parse_cromulent(self):
        parsed = parse_en_pl(html["cromulent"])
        cached = load_json("cromulent")
        assert parsed == cached

    def test_parse_downtrodden(self):
        parsed = parse_en_pl(html["downtrodden"])
        cached = load_json("downtrodden")
        assert parsed == cached

    def test_parse_honeydew(self):
        parsed = parse_en_pl(html["honeydew"])
        cached = load_json("honeydew")
        assert parsed == cached

    def test_parse_cemetery(self):
        parsed = parse_en_pl(html["cemetery"])
        cached = load_json("cemetery")
        assert parsed == cached

    def test_parse_stippled(self):
        parsed = parse_en_pl(html["stippled"])
        cached = load_json("stippled")
        assert parsed == cached

    def test_parse_solicitation(self):
        parsed = parse_en_pl(html["solicitation"])
        cached = load_json("solicitation")
        assert parsed == cached

    def test_parse_determinate(self):
        parsed = parse_en_pl(html["determinate"])
        cached = load_json("determinate")
        assert parsed == cached

    def test_parse_shingles(self):
        parsed = parse_en_pl(html["shingles"])
        cached = load_json("shingles")
        assert parsed == cached

    def test_parse_edgy(self):
        parsed = parse_en_pl(html["edgy"])
        cached = load_json("edgy")
        assert parsed == cached

    def test_parse_myopia(self):
        parsed = parse_en_pl(html["myopia"])
        cached = load_json("myopia")
        assert parsed == cached

    def test_parse_obsequiousness(self):
        parsed = parse_en_pl(html["obsequiousness"])
        cached = load_json("obsequiousness")
        assert parsed == cached

    def test_parse_misappropriate(self):
        parsed = parse_en_pl(html["misappropriate"])
        cached = load_json("misappropriate")
        assert parsed == cached

    def test_parse_meanly(self):
        parsed = parse_en_pl(html["meanly"])
        cached = load_json("meanly")
        assert parsed == cached

    def test_parse_ardent(self):
        parsed = parse_en_pl(html["ardent"])
        cached = load_json("ardent")
        assert parsed == cached

    def test_parse_cranium(self):
        parsed = parse_en_pl(html["cranium"])
        cached = load_json("cranium")
        assert parsed == cached

    def test_parse_comma(self):
        parsed = parse_en_pl(html["comma"])
        cached = load_json("comma")
        assert parsed == cached

    def test_parse_insolent(self):
        parsed = parse_en_pl(html["insolent"])
        cached = load_json("insolent")
        assert parsed == cached

    def test_parse_ramrod(self):
        parsed = parse_en_pl(html["ramrod"])
        cached = load_json("ramrod")
        assert parsed == cached

    def test_parse_stringent(self):
        parsed = parse_en_pl(html["stringent"])
        cached = load_json("stringent")
        assert parsed == cached

    def test_parse_baleful(self):
        parsed = parse_en_pl(html["baleful"])
        cached = load_json("baleful")
        assert parsed == cached

    def test_parse_haven(self):
        parsed = parse_en_pl(html["haven"])
        cached = load_json("haven")
        assert parsed == cached

    def test_parse_dregs(self):
        parsed = parse_en_pl(html["dregs"])
        cached = load_json("dregs")
        assert parsed == cached

    def test_parse_upend(self):
        parsed = parse_en_pl(html["upend"])
        cached = load_json("upend")
        assert parsed == cached

    def test_parse_conduit(self):
        parsed = parse_en_pl(html["conduit"])
        cached = load_json("conduit")
        assert parsed == cached

    def test_parse_toddle(self):
        parsed = parse_en_pl(html["toddle"])
        cached = load_json("toddle")
        assert parsed == cached

    def test_parse_malady(self):
        parsed = parse_en_pl(html["malady"])
        cached = load_json("malady")
        assert parsed == cached

    def test_parse_olfaction(self):
        parsed = parse_en_pl(html["olfaction"])
        cached = load_json("olfaction")
        assert parsed == cached

    def test_parse_accrue(self):
        parsed = parse_en_pl(html["accrue"])
        cached = load_json("accrue")
        assert parsed == cached

    def test_parse_slather(self):
        parsed = parse_en_pl(html["slather"])
        cached = load_json("slather")
        assert parsed == cached

    def test_parse_tranquil(self):
        parsed = parse_en_pl(html["tranquil"])
        cached = load_json("tranquil")
        assert parsed == cached

    def test_parse_plummet(self):
        parsed = parse_en_pl(html["plummet"])
        cached = load_json("plummet")
        assert parsed == cached

    def test_parse_bustard(self):
        parsed = parse_en_pl(html["bustard"])
        cached = load_json("bustard")
        assert parsed == cached

    def test_parse_somber(self):
        parsed = parse_en_pl(html["somber"])
        cached = load_json("somber")
        assert parsed == cached

    def test_parse_hitch(self):
        parsed = parse_en_pl(html["hitch"])
        cached = load_json("hitch")
        assert parsed == cached

    def test_parse_tiller(self):
        parsed = parse_en_pl(html["tiller"])
        cached = load_json("tiller")
        assert parsed == cached

    def test_parse_varsity(self):
        parsed = parse_en_pl(html["varsity"])
        cached = load_json("varsity")
        assert parsed == cached

    def test_parse_outpace(self):
        parsed = parse_en_pl(html["outpace"])
        cached = load_json("outpace")
        assert parsed == cached

    def test_parse_plow(self):
        parsed = parse_en_pl(html["plow"])
        cached = load_json("plow")
        assert parsed == cached

    def test_parse_limpid(self):
        parsed = parse_en_pl(html["limpid"])
        cached = load_json("limpid")
        assert parsed == cached

    def test_parse_heap(self):
        parsed = parse_en_pl(html["heap"])
        cached = load_json("heap")
        assert parsed == cached

    def test_parse_suite(self):
        parsed = parse_en_pl(html["suite"])
        cached = load_json("suite")
        assert parsed == cached

    def test_parse_harbinger(self):
        parsed = parse_en_pl(html["harbinger"])
        cached = load_json("harbinger")
        assert parsed == cached

    def test_parse_deft(self):
        parsed = parse_en_pl(html["deft"])
        cached = load_json("deft")
        assert parsed == cached

    def test_parse_ebb(self):
        parsed = parse_en_pl(html["ebb"])
        cached = load_json("ebb")
        assert parsed == cached

    def test_parse_shrewdness(self):
        parsed = parse_en_pl(html["shrewdness"])
        cached = load_json("shrewdness")
        assert parsed == cached

    def test_parse_recant(self):
        parsed = parse_en_pl(html["recant"])
        cached = load_json("recant")
        assert parsed == cached

    def test_parse_exquisite(self):
        parsed = parse_en_pl(html["exquisite"])
        cached = load_json("exquisite")
        assert parsed == cached

    def test_parse_fiat(self):
        parsed = parse_en_pl(html["fiat"])
        cached = load_json("fiat")
        assert parsed == cached

    def test_parse_primacy(self):
        parsed = parse_en_pl(html["primacy"])
        cached = load_json("primacy")
        assert parsed == cached

    def test_parse_tuff(self):
        parsed = parse_en_pl(html["tuff"])
        cached = load_json("tuff")
        assert parsed == cached

    def test_parse_sheen(self):
        parsed = parse_en_pl(html["sheen"])
        cached = load_json("sheen")
        assert parsed == cached

    def test_parse_slope(self):
        parsed = parse_en_pl(html["slope"])
        cached = load_json("slope")
        assert parsed == cached

    def test_parse_vigilantly(self):
        parsed = parse_en_pl(html["vigilantly"])
        cached = load_json("vigilantly")
        assert parsed == cached

    def test_parse_kerfuffle(self):
        parsed = parse_en_pl(html["kerfuffle"])
        cached = load_json("kerfuffle")
        assert parsed == cached

    def test_parse_glare(self):
        parsed = parse_en_pl(html["glare"])
        cached = load_json("glare")
        assert parsed == cached

    def test_parse_permaculture(self):
        parsed = parse_en_pl(html["permaculture"])
        cached = load_json("permaculture")
        assert parsed == cached

    def test_parse_grunch(self):
        parsed = parse_en_pl(html["grunch"])
        cached = load_json("grunch")
        assert parsed == cached

    def test_parse_rayon(self):
        parsed = parse_en_pl(html["rayon"])
        cached = load_json("rayon")
        assert parsed == cached

    def test_parse_effusive(self):
        parsed = parse_en_pl(html["effusive"])
        cached = load_json("effusive")
        assert parsed == cached

    def test_parse_thine(self):
        parsed = parse_en_pl(html["thine"])
        cached = load_json("thine")
        assert parsed == cached

    def test_parse_locus(self):
        parsed = parse_en_pl(html["locus"])
        cached = load_json("locus")
        assert parsed == cached

    def test_parse_aftermath(self):
        parsed = parse_en_pl(html["aftermath"])
        cached = load_json("aftermath")
        assert parsed == cached

    def test_parse_savant(self):
        parsed = parse_en_pl(html["savant"])
        cached = load_json("savant")
        assert parsed == cached

    def test_parse_mongrel(self):
        parsed = parse_en_pl(html["mongrel"])
        cached = load_json("mongrel")
        assert parsed == cached

    def test_parse_odometer(self):
        parsed = parse_en_pl(html["odometer"])
        cached = load_json("odometer")
        assert parsed == cached

    def test_parse_complacent(self):
        parsed = parse_en_pl(html["complacent"])
        cached = load_json("complacent")
        assert parsed == cached

    def test_parse_crushed(self):
        parsed = parse_en_pl(html["crushed"])
        cached = load_json("crushed")
        assert parsed == cached

    def test_parse_dimwit(self):
        parsed = parse_en_pl(html["dimwit"])
        cached = load_json("dimwit")
        assert parsed == cached

    def test_parse_circumscribe(self):
        parsed = parse_en_pl(html["circumscribe"])
        cached = load_json("circumscribe")
        assert parsed == cached

    def test_parse_concur(self):
        parsed = parse_en_pl(html["concur"])
        cached = load_json("concur")
        assert parsed == cached

    def test_parse_resentful(self):
        parsed = parse_en_pl(html["resentful"])
        cached = load_json("resentful")
        assert parsed == cached

    def test_parse_redundancy(self):
        parsed = parse_en_pl(html["redundancy"])
        cached = load_json("redundancy")
        assert parsed == cached

    def test_parse_eventually(self):
        parsed = parse_en_pl(html["eventually"])
        cached = load_json("eventually")
        assert parsed == cached

    def test_parse_sheaf(self):
        parsed = parse_en_pl(html["sheaf"])
        cached = load_json("sheaf")
        assert parsed == cached

    def test_parse_intrusive(self):
        parsed = parse_en_pl(html["intrusive"])
        cached = load_json("intrusive")
        assert parsed == cached

    def test_parse_refusenik(self):
        parsed = parse_en_pl(html["refusenik"])
        cached = load_json("refusenik")
        assert parsed == cached

    def test_parse_hunk(self):
        parsed = parse_en_pl(html["hunk"])
        cached = load_json("hunk")
        assert parsed == cached

    def test_parse_camomile(self):
        parsed = parse_en_pl(html["camomile"])
        cached = load_json("camomile")
        assert parsed == cached

    def test_parse_veneration(self):
        parsed = parse_en_pl(html["veneration"])
        cached = load_json("veneration")
        assert parsed == cached

    def test_parse_seesaw(self):
        parsed = parse_en_pl(html["seesaw"])
        cached = load_json("seesaw")
        assert parsed == cached

    def test_parse_reek(self):
        parsed = parse_en_pl(html["reek"])
        cached = load_json("reek")
        assert parsed == cached

    def test_parse_pine(self):
        parsed = parse_en_pl(html["pine"])
        cached = load_json("pine")
        assert parsed == cached

    def test_parse_egress(self):
        parsed = parse_en_pl(html["egress"])
        cached = load_json("egress")
        assert parsed == cached

    def test_parse_digest(self):
        parsed = parse_en_pl(html["digest"])
        cached = load_json("digest")
        assert parsed == cached

    def test_parse_rave(self):
        parsed = parse_en_pl(html["rave"])
        cached = load_json("rave")
        assert parsed == cached

    def test_parse_gargantuan(self):
        parsed = parse_en_pl(html["gargantuan"])
        cached = load_json("gargantuan")
        assert parsed == cached

    def test_parse_yon(self):
        parsed = parse_en_pl(html["yon"])
        cached = load_json("yon")
        assert parsed == cached

    def test_parse_chaplain(self):
        parsed = parse_en_pl(html["chaplain"])
        cached = load_json("chaplain")
        assert parsed == cached

    def test_parse_atavistic(self):
        parsed = parse_en_pl(html["atavistic"])
        cached = load_json("atavistic")
        assert parsed == cached

    def test_parse_atone(self):
        parsed = parse_en_pl(html["atone"])
        cached = load_json("atone")
        assert parsed == cached

    def test_parse_aquiver(self):
        parsed = parse_en_pl(html["aquiver"])
        cached = load_json("aquiver")
        assert parsed == cached

    def test_parse_brisk(self):
        parsed = parse_en_pl(html["brisk"])
        cached = load_json("brisk")
        assert parsed == cached

    def test_parse_vestige(self):
        parsed = parse_en_pl(html["vestige"])
        cached = load_json("vestige")
        assert parsed == cached

    def test_parse_doubtless(self):
        parsed = parse_en_pl(html["doubtless"])
        cached = load_json("doubtless")
        assert parsed == cached

    def test_parse_exultant(self):
        parsed = parse_en_pl(html["exultant"])
        cached = load_json("exultant")
        assert parsed == cached

    def test_parse_post(self):
        parsed = parse_en_pl(html["post"])
        cached = load_json("post")
        assert parsed == cached

    def test_parse_simp(self):
        parsed = parse_en_pl(html["simp"])
        cached = load_json("simp")
        assert parsed == cached

    def test_parse_forage(self):
        parsed = parse_en_pl(html["forage"])
        cached = load_json("forage")
        assert parsed == cached

    def test_parse_lofty(self):
        parsed = parse_en_pl(html["lofty"])
        cached = load_json("lofty")
        assert parsed == cached

    def test_parse_acuity(self):
        parsed = parse_en_pl(html["acuity"])
        cached = load_json("acuity")
        assert parsed == cached

    def test_parse_cop(self):
        parsed = parse_en_pl(html["cop"])
        cached = load_json("cop")
        assert parsed == cached

    def test_parse_rawhide(self):
        parsed = parse_en_pl(html["rawhide"])
        cached = load_json("rawhide")
        assert parsed == cached

    def test_parse_unwind(self):
        parsed = parse_en_pl(html["unwind"])
        cached = load_json("unwind")
        assert parsed == cached

    def test_parse_ferocity(self):
        parsed = parse_en_pl(html["ferocity"])
        cached = load_json("ferocity")
        assert parsed == cached

    def test_parse_vanguard(self):
        parsed = parse_en_pl(html["vanguard"])
        cached = load_json("vanguard")
        assert parsed == cached

    def test_parse_lattice(self):
        parsed = parse_en_pl(html["lattice"])
        cached = load_json("lattice")
        assert parsed == cached

    def test_parse_curmudgeon(self):
        parsed = parse_en_pl(html["curmudgeon"])
        cached = load_json("curmudgeon")
        assert parsed == cached

    def test_parse_intractable(self):
        parsed = parse_en_pl(html["intractable"])
        cached = load_json("intractable")
        assert parsed == cached

    def test_parse_basking(self):
        parsed = parse_en_pl(html["basking"])
        cached = load_json("basking")
        assert parsed == cached

    def test_parse_lackeys(self):
        parsed = parse_en_pl(html["lackeys"])
        cached = load_json("lackeys")
        assert parsed == cached

    def test_parse_grazer(self):
        parsed = parse_en_pl(html["grazer"])
        cached = load_json("grazer")
        assert parsed == cached

    def test_parse_hunch(self):
        parsed = parse_en_pl(html["hunch"])
        cached = load_json("hunch")
        assert parsed == cached

    def test_parse_rapt(self):
        parsed = parse_en_pl(html["rapt"])
        cached = load_json("rapt")
        assert parsed == cached

    def test_parse_incandescence(self):
        parsed = parse_en_pl(html["incandescence"])
        cached = load_json("incandescence")
        assert parsed == cached

    def test_parse_behest(self):
        parsed = parse_en_pl(html["behest"])
        cached = load_json("behest")
        assert parsed == cached

    def test_parse_sedate(self):
        parsed = parse_en_pl(html["sedate"])
        cached = load_json("sedate")
        assert parsed == cached

    def test_parse_wilt(self):
        parsed = parse_en_pl(html["wilt"])
        cached = load_json("wilt")
        assert parsed == cached

    def test_parse_temerity(self):
        parsed = parse_en_pl(html["temerity"])
        cached = load_json("temerity")
        assert parsed == cached

    def test_parse_humility(self):
        parsed = parse_en_pl(html["humility"])
        cached = load_json("humility")
        assert parsed == cached

    def test_parse_ripe(self):
        parsed = parse_en_pl(html["ripe"])
        cached = load_json("ripe")
        assert parsed == cached

    def test_parse_uncovered(self):
        parsed = parse_en_pl(html["uncovered"])
        cached = load_json("uncovered")
        assert parsed == cached

    def test_parse_sweeping(self):
        parsed = parse_en_pl(html["sweeping"])
        cached = load_json("sweeping")
        assert parsed == cached

    def test_parse_apperception(self):
        parsed = parse_en_pl(html["apperception"])
        cached = load_json("apperception")
        assert parsed == cached

    def test_parse_destitution(self):
        parsed = parse_en_pl(html["destitution"])
        cached = load_json("destitution")
        assert parsed == cached

    def test_parse_canny(self):
        parsed = parse_en_pl(html["canny"])
        cached = load_json("canny")
        assert parsed == cached

    def test_parse_voracious(self):
        parsed = parse_en_pl(html["voracious"])
        cached = load_json("voracious")
        assert parsed == cached

    def test_parse_haggle(self):
        parsed = parse_en_pl(html["haggle"])
        cached = load_json("haggle")
        assert parsed == cached

    def test_parse_overpass(self):
        parsed = parse_en_pl(html["overpass"])
        cached = load_json("overpass")
        assert parsed == cached

    def test_parse_disarray(self):
        parsed = parse_en_pl(html["disarray"])
        cached = load_json("disarray")
        assert parsed == cached

    def test_parse_unease(self):
        parsed = parse_en_pl(html["unease"])
        cached = load_json("unease")
        assert parsed == cached

    def test_parse_alleviate(self):
        parsed = parse_en_pl(html["alleviate"])
        cached = load_json("alleviate")
        assert parsed == cached

    def test_parse_contraction(self):
        parsed = parse_en_pl(html["contraction"])
        cached = load_json("contraction")
        assert parsed == cached

    def test_parse_condone(self):
        parsed = parse_en_pl(html["condone"])
        cached = load_json("condone")
        assert parsed == cached

    def test_parse_tail(self):
        parsed = parse_en_pl(html["tail"])
        cached = load_json("tail")
        assert parsed == cached

    def test_parse_unrelenting(self):
        parsed = parse_en_pl(html["unrelenting"])
        cached = load_json("unrelenting")
        assert parsed == cached

    def test_parse_ditties(self):
        parsed = parse_en_pl(html["ditties"])
        cached = load_json("ditties")
        assert parsed == cached

    def test_parse_tacit(self):
        parsed = parse_en_pl(html["tacit"])
        cached = load_json("tacit")
        assert parsed == cached

    def test_parse_lam(self):
        parsed = parse_en_pl(html["lam"])
        cached = load_json("lam")
        assert parsed == cached

    def test_parse_annoyed(self):
        parsed = parse_en_pl(html["annoyed"])
        cached = load_json("annoyed")
        assert parsed == cached

    def test_parse_lash(self):
        parsed = parse_en_pl(html["lash"])
        cached = load_json("lash")
        assert parsed == cached

    def test_parse_wage(self):
        parsed = parse_en_pl(html["wage"])
        cached = load_json("wage")
        assert parsed == cached

    def test_parse_unpalatable(self):
        parsed = parse_en_pl(html["unpalatable"])
        cached = load_json("unpalatable")
        assert parsed == cached

    def test_parse_glossary(self):
        parsed = parse_en_pl(html["glossary"])
        cached = load_json("glossary")
        assert parsed == cached

    def test_parse_barge(self):
        parsed = parse_en_pl(html["barge"])
        cached = load_json("barge")
        assert parsed == cached

    def test_parse_libel(self):
        parsed = parse_en_pl(html["libel"])
        cached = load_json("libel")
        assert parsed == cached

    def test_parse_teamster(self):
        parsed = parse_en_pl(html["teamster"])
        cached = load_json("teamster")
        assert parsed == cached

    def test_parse_repudiate(self):
        parsed = parse_en_pl(html["repudiate"])
        cached = load_json("repudiate")
        assert parsed == cached

    def test_parse_interwoven(self):
        parsed = parse_en_pl(html["interwoven"])
        cached = load_json("interwoven")
        assert parsed == cached

    def test_parse_spate(self):
        parsed = parse_en_pl(html["spate"])
        cached = load_json("spate")
        assert parsed == cached

    def test_parse_pervasive(self):
        parsed = parse_en_pl(html["pervasive"])
        cached = load_json("pervasive")
        assert parsed == cached

    def test_parse_fusion(self):
        parsed = parse_en_pl(html["fusion"])
        cached = load_json("fusion")
        assert parsed == cached

    def test_parse_abduct(self):
        parsed = parse_en_pl(html["abduct"])
        cached = load_json("abduct")
        assert parsed == cached

    def test_parse_peccant(self):
        parsed = parse_en_pl(html["peccant"])
        cached = load_json("peccant")
        assert parsed == cached

    def test_parse_outlandish(self):
        parsed = parse_en_pl(html["outlandish"])
        cached = load_json("outlandish")
        assert parsed == cached

    def test_parse_prudish(self):
        parsed = parse_en_pl(html["prudish"])
        cached = load_json("prudish")
        assert parsed == cached

    def test_parse_scupper(self):
        parsed = parse_en_pl(html["scupper"])
        cached = load_json("scupper")
        assert parsed == cached

    def test_parse_conciliation(self):
        parsed = parse_en_pl(html["conciliation"])
        cached = load_json("conciliation")
        assert parsed == cached

    def test_parse_disdain(self):
        parsed = parse_en_pl(html["disdain"])
        cached = load_json("disdain")
        assert parsed == cached

    def test_parse_incendiary(self):
        parsed = parse_en_pl(html["incendiary"])
        cached = load_json("incendiary")
        assert parsed == cached

    def test_parse_deterrent(self):
        parsed = parse_en_pl(html["deterrent"])
        cached = load_json("deterrent")
        assert parsed == cached

    def test_parse_crippled(self):
        parsed = parse_en_pl(html["crippled"])
        cached = load_json("crippled")
        assert parsed == cached

    def test_parse_arbitrage(self):
        parsed = parse_en_pl(html["arbitrage"])
        cached = load_json("arbitrage")
        assert parsed == cached

    def test_parse_same(self):
        parsed = parse_en_pl(html["same"])
        cached = load_json("same")
        assert parsed == cached

    def test_parse_forecast(self):
        parsed = parse_en_pl(html["forecast"])
        cached = load_json("forecast")
        assert parsed == cached

    def test_parse_exhilaration(self):
        parsed = parse_en_pl(html["exhilaration"])
        cached = load_json("exhilaration")
        assert parsed == cached

    def test_parse_peregrination(self):
        parsed = parse_en_pl(html["peregrination"])
        cached = load_json("peregrination")
        assert parsed == cached

    def test_parse_commune(self):
        parsed = parse_en_pl(html["commune"])
        cached = load_json("commune")
        assert parsed == cached

    def test_parse_garishness(self):
        parsed = parse_en_pl(html["garishness"])
        cached = load_json("garishness")
        assert parsed == cached

    def test_parse_creeping(self):
        parsed = parse_en_pl(html["creeping"])
        cached = load_json("creeping")
        assert parsed == cached

    def test_parse_sinister(self):
        parsed = parse_en_pl(html["sinister"])
        cached = load_json("sinister")
        assert parsed == cached

    def test_parse_placating(self):
        parsed = parse_en_pl(html["placating"])
        cached = load_json("placating")
        assert parsed == cached

    def test_parse_narrow(self):
        parsed = parse_en_pl(html["narrow"])
        cached = load_json("narrow")
        assert parsed == cached

    def test_parse_nimble(self):
        parsed = parse_en_pl(html["nimble"])
        cached = load_json("nimble")
        assert parsed == cached

    def test_parse_bandicoot(self):
        parsed = parse_en_pl(html["bandicoot"])
        cached = load_json("bandicoot")
        assert parsed == cached

    def test_parse_atrocious(self):
        parsed = parse_en_pl(html["atrocious"])
        cached = load_json("atrocious")
        assert parsed == cached

    def test_parse_garrulous(self):
        parsed = parse_en_pl(html["garrulous"])
        cached = load_json("garrulous")
        assert parsed == cached

    def test_parse_bulk(self):
        parsed = parse_en_pl(html["bulk"])
        cached = load_json("bulk")
        assert parsed == cached

    def test_parse_jaundice(self):
        parsed = parse_en_pl(html["jaundice"])
        cached = load_json("jaundice")
        assert parsed == cached

    def test_parse_arguably(self):
        parsed = parse_en_pl(html["arguably"])
        cached = load_json("arguably")
        assert parsed == cached

    def test_parse_sleep(self):
        parsed = parse_en_pl(html["sleep"])
        cached = load_json("sleep")
        assert parsed == cached

    def test_parse_conciliatory(self):
        parsed = parse_en_pl(html["conciliatory"])
        cached = load_json("conciliatory")
        assert parsed == cached

    def test_parse_gaze(self):
        parsed = parse_en_pl(html["gaze"])
        cached = load_json("gaze")
        assert parsed == cached

    def test_parse_aniseed(self):
        parsed = parse_en_pl(html["aniseed"])
        cached = load_json("aniseed")
        assert parsed == cached

    def test_parse_desiccate(self):
        parsed = parse_en_pl(html["desiccate"])
        cached = load_json("desiccate")
        assert parsed == cached

    def test_parse_dreadful(self):
        parsed = parse_en_pl(html["dreadful"])
        cached = load_json("dreadful")
        assert parsed == cached

    def test_parse_shimmer(self):
        parsed = parse_en_pl(html["shimmer"])
        cached = load_json("shimmer")
        assert parsed == cached

    def test_parse_vice(self):
        parsed = parse_en_pl(html["vice"])
        cached = load_json("vice")
        assert parsed == cached

    def test_parse_incinerator(self):
        parsed = parse_en_pl(html["incinerator"])
        cached = load_json("incinerator")
        assert parsed == cached

    def test_parse_delineate(self):
        parsed = parse_en_pl(html["delineate"])
        cached = load_json("delineate")
        assert parsed == cached

    def test_parse_alimony(self):
        parsed = parse_en_pl(html["alimony"])
        cached = load_json("alimony")
        assert parsed == cached

    def test_parse_captivating(self):
        parsed = parse_en_pl(html["captivating"])
        cached = load_json("captivating")
        assert parsed == cached

    def test_parse_hustle(self):
        parsed = parse_en_pl(html["hustle"])
        cached = load_json("hustle")
        assert parsed == cached

    def test_parse_endearment(self):
        parsed = parse_en_pl(html["endearment"])
        cached = load_json("endearment")
        assert parsed == cached

    def test_parse_limp(self):
        parsed = parse_en_pl(html["limp"])
        cached = load_json("limp")
        assert parsed == cached

    def test_parse_phubbing(self):
        parsed = parse_en_pl(html["phubbing"])
        cached = load_json("phubbing")
        assert parsed == cached

    def test_parse_flay(self):
        parsed = parse_en_pl(html["flay"])
        cached = load_json("flay")
        assert parsed == cached

    def test_parse_spoke(self):
        parsed = parse_en_pl(html["spoke"])
        cached = load_json("spoke")
        assert parsed == cached

    def test_parse_exacerbate(self):
        parsed = parse_en_pl(html["exacerbate"])
        cached = load_json("exacerbate")
        assert parsed == cached

    def test_parse_hide(self):
        parsed = parse_en_pl(html["hide"])
        cached = load_json("hide")
        assert parsed == cached

    def test_parse_frankincense(self):
        parsed = parse_en_pl(html["frankincense"])
        cached = load_json("frankincense")
        assert parsed == cached

    def test_parse_tale(self):
        parsed = parse_en_pl(html["tale"])
        cached = load_json("tale")
        assert parsed == cached

    def test_parse_phalanx(self):
        parsed = parse_en_pl(html["phalanx"])
        cached = load_json("phalanx")
        assert parsed == cached

    def test_parse_bellicose(self):
        parsed = parse_en_pl(html["bellicose"])
        cached = load_json("bellicose")
        assert parsed == cached

    def test_parse_perfunctory(self):
        parsed = parse_en_pl(html["perfunctory"])
        cached = load_json("perfunctory")
        assert parsed == cached

    def test_parse_sarcoma(self):
        parsed = parse_en_pl(html["sarcoma"])
        cached = load_json("sarcoma")
        assert parsed == cached

    def test_parse_gruntled(self):
        parsed = parse_en_pl(html["gruntled"])
        cached = load_json("gruntled")
        assert parsed == cached

    def test_parse_exasperated(self):
        parsed = parse_en_pl(html["exasperated"])
        cached = load_json("exasperated")
        assert parsed == cached

    def test_parse_matron(self):
        parsed = parse_en_pl(html["matron"])
        cached = load_json("matron")
        assert parsed == cached

    def test_parse_intrinsically(self):
        parsed = parse_en_pl(html["intrinsically"])
        cached = load_json("intrinsically")
        assert parsed == cached

    def test_parse_quaint(self):
        parsed = parse_en_pl(html["quaint"])
        cached = load_json("quaint")
        assert parsed == cached

    def test_parse_medulla(self):
        parsed = parse_en_pl(html["medulla"])
        cached = load_json("medulla")
        assert parsed == cached

    def test_parse_rueful(self):
        parsed = parse_en_pl(html["rueful"])
        cached = load_json("rueful")
        assert parsed == cached

    def test_parse_zealotry(self):
        parsed = parse_en_pl(html["zealotry"])
        cached = load_json("zealotry")
        assert parsed == cached

    def test_parse_foraging(self):
        parsed = parse_en_pl(html["foraging"])
        cached = load_json("foraging")
        assert parsed == cached

    def test_parse_theorem(self):
        parsed = parse_en_pl(html["theorem"])
        cached = load_json("theorem")
        assert parsed == cached

    def test_parse_affront(self):
        parsed = parse_en_pl(html["affront"])
        cached = load_json("affront")
        assert parsed == cached

    def test_parse_eponymous(self):
        parsed = parse_en_pl(html["eponymous"])
        cached = load_json("eponymous")
        assert parsed == cached

    def test_parse_pending(self):
        parsed = parse_en_pl(html["pending"])
        cached = load_json("pending")
        assert parsed == cached

    def test_parse_jilt(self):
        parsed = parse_en_pl(html["jilt"])
        cached = load_json("jilt")
        assert parsed == cached

    def test_parse_hulk(self):
        parsed = parse_en_pl(html["hulk"])
        cached = load_json("hulk")
        assert parsed == cached

    def test_parse_languid(self):
        parsed = parse_en_pl(html["languid"])
        cached = load_json("languid")
        assert parsed == cached

    def test_parse_gammon(self):
        parsed = parse_en_pl(html["gammon"])
        cached = load_json("gammon")
        assert parsed == cached

    def test_parse_heckle(self):
        parsed = parse_en_pl(html["heckle"])
        cached = load_json("heckle")
        assert parsed == cached

    def test_parse_squabble(self):
        parsed = parse_en_pl(html["squabble"])
        cached = load_json("squabble")
        assert parsed == cached

    def test_parse_corny(self):
        parsed = parse_en_pl(html["corny"])
        cached = load_json("corny")
        assert parsed == cached

    def test_parse_ridge(self):
        parsed = parse_en_pl(html["ridge"])
        cached = load_json("ridge")
        assert parsed == cached

    def test_parse_inherent(self):
        parsed = parse_en_pl(html["inherent"])
        cached = load_json("inherent")
        assert parsed == cached

    def test_parse_nebulous(self):
        parsed = parse_en_pl(html["nebulous"])
        cached = load_json("nebulous")
        assert parsed == cached

    def test_parse_blimp(self):
        parsed = parse_en_pl(html["blimp"])
        cached = load_json("blimp")
        assert parsed == cached

    def test_parse_ruddy(self):
        parsed = parse_en_pl(html["ruddy"])
        cached = load_json("ruddy")
        assert parsed == cached

    def test_parse_pulmonary(self):
        parsed = parse_en_pl(html["pulmonary"])
        cached = load_json("pulmonary")
        assert parsed == cached

    def test_parse_caress(self):
        parsed = parse_en_pl(html["caress"])
        cached = load_json("caress")
        assert parsed == cached

    def test_parse_proliferation(self):
        parsed = parse_en_pl(html["proliferation"])
        cached = load_json("proliferation")
        assert parsed == cached

    def test_parse_excavation(self):
        parsed = parse_en_pl(html["excavation"])
        cached = load_json("excavation")
        assert parsed == cached

    def test_parse_revile(self):
        parsed = parse_en_pl(html["revile"])
        cached = load_json("revile")
        assert parsed == cached

    def test_parse_affine(self):
        parsed = parse_en_pl(html["affine"])
        cached = load_json("affine")
        assert parsed == cached

    def test_parse_fraud(self):
        parsed = parse_en_pl(html["fraud"])
        cached = load_json("fraud")
        assert parsed == cached

    def test_parse_midwife(self):
        parsed = parse_en_pl(html["midwife"])
        cached = load_json("midwife")
        assert parsed == cached

    def test_parse_rumpled(self):
        parsed = parse_en_pl(html["rumpled"])
        cached = load_json("rumpled")
        assert parsed == cached

    def test_parse_hone(self):
        parsed = parse_en_pl(html["hone"])
        cached = load_json("hone")
        assert parsed == cached

    def test_parse_breadth(self):
        parsed = parse_en_pl(html["breadth"])
        cached = load_json("breadth")
        assert parsed == cached

    def test_parse_dither(self):
        parsed = parse_en_pl(html["dither"])
        cached = load_json("dither")
        assert parsed == cached

    def test_parse_paternalism(self):
        parsed = parse_en_pl(html["paternalism"])
        cached = load_json("paternalism")
        assert parsed == cached

    def test_parse_deference(self):
        parsed = parse_en_pl(html["deference"])
        cached = load_json("deference")
        assert parsed == cached

    def test_parse_commission(self):
        parsed = parse_en_pl(html["commission"])
        cached = load_json("commission")
        assert parsed == cached

    def test_parse_dejection(self):
        parsed = parse_en_pl(html["dejection"])
        cached = load_json("dejection")
        assert parsed == cached

    def test_parse_ash(self):
        parsed = parse_en_pl(html["ash"])
        cached = load_json("ash")
        assert parsed == cached

    def test_parse_froth(self):
        parsed = parse_en_pl(html["froth"])
        cached = load_json("froth")
        assert parsed == cached

    def test_parse_upon(self):
        parsed = parse_en_pl(html["upon"])
        cached = load_json("upon")
        assert parsed == cached

    def test_parse_miscreant(self):
        parsed = parse_en_pl(html["miscreant"])
        cached = load_json("miscreant")
        assert parsed == cached

    def test_parse_snide(self):
        parsed = parse_en_pl(html["snide"])
        cached = load_json("snide")
        assert parsed == cached

    def test_parse_sage(self):
        parsed = parse_en_pl(html["sage"])
        cached = load_json("sage")
        assert parsed == cached

    def test_parse_shriek(self):
        parsed = parse_en_pl(html["shriek"])
        cached = load_json("shriek")
        assert parsed == cached

    def test_parse_cronies(self):
        parsed = parse_en_pl(html["cronies"])
        cached = load_json("cronies")
        assert parsed == cached

    def test_parse_fumble(self):
        parsed = parse_en_pl(html["fumble"])
        cached = load_json("fumble")
        assert parsed == cached

    def test_parse_spotless(self):
        parsed = parse_en_pl(html["spotless"])
        cached = load_json("spotless")
        assert parsed == cached

    def test_parse_umpteenth(self):
        parsed = parse_en_pl(html["umpteenth"])
        cached = load_json("umpteenth")
        assert parsed == cached

    def test_parse_service(self):
        parsed = parse_en_pl(html["service"])
        cached = load_json("service")
        assert parsed == cached

    def test_parse_harried(self):
        parsed = parse_en_pl(html["harried"])
        cached = load_json("harried")
        assert parsed == cached

    def test_parse_abstruse(self):
        parsed = parse_en_pl(html["abstruse"])
        cached = load_json("abstruse")
        assert parsed == cached

    def test_parse_bout(self):
        parsed = parse_en_pl(html["bout"])
        cached = load_json("bout")
        assert parsed == cached

    def test_parse_lanky(self):
        parsed = parse_en_pl(html["lanky"])
        cached = load_json("lanky")
        assert parsed == cached

    def test_parse_stifle(self):
        parsed = parse_en_pl(html["stifle"])
        cached = load_json("stifle")
        assert parsed == cached

    def test_parse_untrodden(self):
        parsed = parse_en_pl(html["untrodden"])
        cached = load_json("untrodden")
        assert parsed == cached

    def test_parse_squint(self):
        parsed = parse_en_pl(html["squint"])
        cached = load_json("squint")
        assert parsed == cached

    def test_parse_slumber(self):
        parsed = parse_en_pl(html["slumber"])
        cached = load_json("slumber")
        assert parsed == cached

    def test_parse_bemoan(self):
        parsed = parse_en_pl(html["bemoan"])
        cached = load_json("bemoan")
        assert parsed == cached

    def test_parse_shtick(self):
        parsed = parse_en_pl(html["shtick"])
        cached = load_json("shtick")
        assert parsed == cached

    def test_parse_contraband(self):
        parsed = parse_en_pl(html["contraband"])
        cached = load_json("contraband")
        assert parsed == cached

    def test_parse_catsup(self):
        parsed = parse_en_pl(html["catsup"])
        cached = load_json("catsup")
        assert parsed == cached

    def test_parse_reckoning(self):
        parsed = parse_en_pl(html["reckoning"])
        cached = load_json("reckoning")
        assert parsed == cached

    def test_parse_contain(self):
        parsed = parse_en_pl(html["contain"])
        cached = load_json("contain")
        assert parsed == cached

    def test_parse_peripheral(self):
        parsed = parse_en_pl(html["peripheral"])
        cached = load_json("peripheral")
        assert parsed == cached

    def test_parse_swagger(self):
        parsed = parse_en_pl(html["swagger"])
        cached = load_json("swagger")
        assert parsed == cached

    def test_parse_insular(self):
        parsed = parse_en_pl(html["insular"])
        cached = load_json("insular")
        assert parsed == cached

    def test_parse_sickle(self):
        parsed = parse_en_pl(html["sickle"])
        cached = load_json("sickle")
        assert parsed == cached

    def test_parse_intertwine(self):
        parsed = parse_en_pl(html["intertwine"])
        cached = load_json("intertwine")
        assert parsed == cached

    def test_parse_extraordinary(self):
        parsed = parse_en_pl(html["extraordinary"])
        cached = load_json("extraordinary")
        assert parsed == cached

    def test_parse_fir(self):
        parsed = parse_en_pl(html["fir"])
        cached = load_json("fir")
        assert parsed == cached

    def test_parse_gullet(self):
        parsed = parse_en_pl(html["gullet"])
        cached = load_json("gullet")
        assert parsed == cached

    def test_parse_foliage(self):
        parsed = parse_en_pl(html["foliage"])
        cached = load_json("foliage")
        assert parsed == cached

    def test_parse_fetter(self):
        parsed = parse_en_pl(html["fetter"])
        cached = load_json("fetter")
        assert parsed == cached

    def test_parse_malleable(self):
        parsed = parse_en_pl(html["malleable"])
        cached = load_json("malleable")
        assert parsed == cached

    def test_parse_sylvan(self):
        parsed = parse_en_pl(html["sylvan"])
        cached = load_json("sylvan")
        assert parsed == cached

    def test_parse_mock(self):
        parsed = parse_en_pl(html["mock"])
        cached = load_json("mock")
        assert parsed == cached

    def test_parse_cajole(self):
        parsed = parse_en_pl(html["cajole"])
        cached = load_json("cajole")
        assert parsed == cached

    def test_parse_nurture(self):
        parsed = parse_en_pl(html["nurture"])
        cached = load_json("nurture")
        assert parsed == cached

    def test_parse_enjoin(self):
        parsed = parse_en_pl(html["enjoin"])
        cached = load_json("enjoin")
        assert parsed == cached

    def test_parse_reprehensible(self):
        parsed = parse_en_pl(html["reprehensible"])
        cached = load_json("reprehensible")
        assert parsed == cached

    def test_parse_folio(self):
        parsed = parse_en_pl(html["folio"])
        cached = load_json("folio")
        assert parsed == cached

    def test_parse_prawn(self):
        parsed = parse_en_pl(html["prawn"])
        cached = load_json("prawn")
        assert parsed == cached

    def test_parse_fern(self):
        parsed = parse_en_pl(html["fern"])
        cached = load_json("fern")
        assert parsed == cached

    def test_parse_amicably(self):
        parsed = parse_en_pl(html["amicably"])
        cached = load_json("amicably")
        assert parsed == cached

    def test_parse_whig(self):
        parsed = parse_en_pl(html["whig"])
        cached = load_json("whig")
        assert parsed == cached

    def test_parse_listener(self):
        parsed = parse_en_pl(html["listener"])
        cached = load_json("listener")
        assert parsed == cached

    def test_parse_bungler(self):
        parsed = parse_en_pl(html["bungler"])
        cached = load_json("bungler")
        assert parsed == cached

    def test_parse_precipitous(self):
        parsed = parse_en_pl(html["precipitous"])
        cached = load_json("precipitous")
        assert parsed == cached

    def test_parse_reticence(self):
        parsed = parse_en_pl(html["reticence"])
        cached = load_json("reticence")
        assert parsed == cached

    def test_parse_ardor(self):
        parsed = parse_en_pl(html["ardor"])
        cached = load_json("ardor")
        assert parsed == cached

    def test_parse_dubious(self):
        parsed = parse_en_pl(html["dubious"])
        cached = load_json("dubious")
        assert parsed == cached

    def test_parse_limerick(self):
        parsed = parse_en_pl(html["limerick"])
        cached = load_json("limerick")
        assert parsed == cached

    def test_parse_emerald(self):
        parsed = parse_en_pl(html["emerald"])
        cached = load_json("emerald")
        assert parsed == cached

    def test_parse_stalwart(self):
        parsed = parse_en_pl(html["stalwart"])
        cached = load_json("stalwart")
        assert parsed == cached

    def test_parse_brazen(self):
        parsed = parse_en_pl(html["brazen"])
        cached = load_json("brazen")
        assert parsed == cached

    def test_parse_gnat(self):
        parsed = parse_en_pl(html["gnat"])
        cached = load_json("gnat")
        assert parsed == cached

    def test_parse_appendage(self):
        parsed = parse_en_pl(html["appendage"])
        cached = load_json("appendage")
        assert parsed == cached

    def test_parse_germane(self):
        parsed = parse_en_pl(html["germane"])
        cached = load_json("germane")
        assert parsed == cached

    def test_parse_preemptively(self):
        parsed = parse_en_pl(html["preemptively"])
        cached = load_json("preemptively")
        assert parsed == cached

    def test_parse_cede(self):
        parsed = parse_en_pl(html["cede"])
        cached = load_json("cede")
        assert parsed == cached

    def test_parse_cay(self):
        parsed = parse_en_pl(html["cay"])
        cached = load_json("cay")
        assert parsed == cached

    def test_parse_county(self):
        parsed = parse_en_pl(html["county"])
        cached = load_json("county")
        assert parsed == cached

    def test_parse_elation(self):
        parsed = parse_en_pl(html["elation"])
        cached = load_json("elation")
        assert parsed == cached

    def test_parse_curb(self):
        parsed = parse_en_pl(html["curb"])
        cached = load_json("curb")
        assert parsed == cached

    def test_parse_on(self):
        parsed = parse_en_pl(html["on"])
        cached = load_json("on")
        assert parsed == cached

    def test_parse_glam(self):
        parsed = parse_en_pl(html["glam"])
        cached = load_json("glam")
        assert parsed == cached

    def test_parse_portents(self):
        parsed = parse_en_pl(html["portents"])
        cached = load_json("portents")
        assert parsed == cached

    def test_parse_abolish(self):
        parsed = parse_en_pl(html["abolish"])
        cached = load_json("abolish")
        assert parsed == cached

    def test_parse_bejeezus(self):
        parsed = parse_en_pl(html["bejeezus"])
        cached = load_json("bejeezus")
        assert parsed == cached

    def test_parse_torrefaction(self):
        parsed = parse_en_pl(html["torrefaction"])
        cached = load_json("torrefaction")
        assert parsed == cached

    def test_parse_flaneur(self):
        parsed = parse_en_pl(html["flaneur"])
        cached = load_json("flaneur")
        assert parsed == cached

    def test_parse_ardour(self):
        parsed = parse_en_pl(html["ardour"])
        cached = load_json("ardour")
        assert parsed == cached

    def test_parse_candid(self):
        parsed = parse_en_pl(html["candid"])
        cached = load_json("candid")
        assert parsed == cached

    def test_parse_proper(self):
        parsed = parse_en_pl(html["proper"])
        cached = load_json("proper")
        assert parsed == cached

    def test_parse_sprain(self):
        parsed = parse_en_pl(html["sprain"])
        cached = load_json("sprain")
        assert parsed == cached

    def test_parse_presuppose(self):
        parsed = parse_en_pl(html["presuppose"])
        cached = load_json("presuppose")
        assert parsed == cached

    def test_parse_hanker(self):
        parsed = parse_en_pl(html["hanker"])
        cached = load_json("hanker")
        assert parsed == cached

    def test_parse_holler(self):
        parsed = parse_en_pl(html["holler"])
        cached = load_json("holler")
        assert parsed == cached

    def test_parse_prevarication(self):
        parsed = parse_en_pl(html["prevarication"])
        cached = load_json("prevarication")
        assert parsed == cached

    def test_parse_penitent(self):
        parsed = parse_en_pl(html["penitent"])
        cached = load_json("penitent")
        assert parsed == cached

    def test_parse_garum(self):
        parsed = parse_en_pl(html["garum"])
        cached = load_json("garum")
        assert parsed == cached

    def test_parse_ilk(self):
        parsed = parse_en_pl(html["ilk"])
        cached = load_json("ilk")
        assert parsed == cached

    def test_parse_pudgy(self):
        parsed = parse_en_pl(html["pudgy"])
        cached = load_json("pudgy")
        assert parsed == cached

    def test_parse_dismember(self):
        parsed = parse_en_pl(html["dismember"])
        cached = load_json("dismember")
        assert parsed == cached

    def test_parse_quit(self):
        parsed = parse_en_pl(html["quit"])
        cached = load_json("quit")
        assert parsed == cached

    def test_parse_miser(self):
        parsed = parse_en_pl(html["miser"])
        cached = load_json("miser")
        assert parsed == cached

    def test_parse_blight(self):
        parsed = parse_en_pl(html["blight"])
        cached = load_json("blight")
        assert parsed == cached

    def test_parse_phthalates(self):
        parsed = parse_en_pl(html["phthalates"])
        cached = load_json("phthalates")
        assert parsed == cached

    def test_parse_affidavit(self):
        parsed = parse_en_pl(html["affidavit"])
        cached = load_json("affidavit")
        assert parsed == cached

    def test_parse_relapse(self):
        parsed = parse_en_pl(html["relapse"])
        cached = load_json("relapse")
        assert parsed == cached

    def test_parse_character(self):
        parsed = parse_en_pl(html["character"])
        cached = load_json("character")
        assert parsed == cached

    def test_parse_slump(self):
        parsed = parse_en_pl(html["slump"])
        cached = load_json("slump")
        assert parsed == cached

    def test_parse_garner(self):
        parsed = parse_en_pl(html["garner"])
        cached = load_json("garner")
        assert parsed == cached

    def test_parse_hum(self):
        parsed = parse_en_pl(html["hum"])
        cached = load_json("hum")
        assert parsed == cached

    def test_parse_unsound(self):
        parsed = parse_en_pl(html["unsound"])
        cached = load_json("unsound")
        assert parsed == cached

    def test_parse_condescending(self):
        parsed = parse_en_pl(html["condescending"])
        cached = load_json("condescending")
        assert parsed == cached

    def test_parse_ken(self):
        parsed = parse_en_pl(html["ken"])
        cached = load_json("ken")
        assert parsed == cached

    def test_parse_bewilder(self):
        parsed = parse_en_pl(html["bewilder"])
        cached = load_json("bewilder")
        assert parsed == cached

    def test_parse_crust(self):
        parsed = parse_en_pl(html["crust"])
        cached = load_json("crust")
        assert parsed == cached

    def test_parse_compassionate(self):
        parsed = parse_en_pl(html["compassionate"])
        cached = load_json("compassionate")
        assert parsed == cached

    def test_parse_squid(self):
        parsed = parse_en_pl(html["squid"])
        cached = load_json("squid")
        assert parsed == cached

    def test_parse_reclusive(self):
        parsed = parse_en_pl(html["reclusive"])
        cached = load_json("reclusive")
        assert parsed == cached

    def test_parse_are(self):
        parsed = parse_en_pl(html["are"])
        cached = load_json("are")
        assert parsed == cached

    def test_parse_gouge(self):
        parsed = parse_en_pl(html["gouge"])
        cached = load_json("gouge")
        assert parsed == cached

    def test_parse_satiate(self):
        parsed = parse_en_pl(html["satiate"])
        cached = load_json("satiate")
        assert parsed == cached

    def test_parse_ravage(self):
        parsed = parse_en_pl(html["ravage"])
        cached = load_json("ravage")
        assert parsed == cached

    def test_parse_ecstatic(self):
        parsed = parse_en_pl(html["ecstatic"])
        cached = load_json("ecstatic")
        assert parsed == cached

    def test_parse_mull(self):
        parsed = parse_en_pl(html["mull"])
        cached = load_json("mull")
        assert parsed == cached

    def test_parse_avowedly(self):
        parsed = parse_en_pl(html["avowedly"])
        cached = load_json("avowedly")
        assert parsed == cached

    def test_parse_lock(self):
        parsed = parse_en_pl(html["lock"])
        cached = load_json("lock")
        assert parsed == cached

    def test_parse_fettle(self):
        parsed = parse_en_pl(html["fettle"])
        cached = load_json("fettle")
        assert parsed == cached

    def test_parse_urchin(self):
        parsed = parse_en_pl(html["urchin"])
        cached = load_json("urchin")
        assert parsed == cached

    def test_parse_ferocious(self):
        parsed = parse_en_pl(html["ferocious"])
        cached = load_json("ferocious")
        assert parsed == cached

    def test_parse_scrawl(self):
        parsed = parse_en_pl(html["scrawl"])
        cached = load_json("scrawl")
        assert parsed == cached

    def test_parse_looey(self):
        parsed = parse_en_pl(html["looey"])
        cached = load_json("looey")
        assert parsed == cached

    def test_parse_snitch(self):
        parsed = parse_en_pl(html["snitch"])
        cached = load_json("snitch")
        assert parsed == cached

    def test_parse_squeamish(self):
        parsed = parse_en_pl(html["squeamish"])
        cached = load_json("squeamish")
        assert parsed == cached

    def test_parse_murmurs(self):
        parsed = parse_en_pl(html["murmurs"])
        cached = load_json("murmurs")
        assert parsed == cached

    def test_parse_harness(self):
        parsed = parse_en_pl(html["harness"])
        cached = load_json("harness")
        assert parsed == cached

    def test_parse_rapture(self):
        parsed = parse_en_pl(html["rapture"])
        cached = load_json("rapture")
        assert parsed == cached

    def test_parse_debauchery(self):
        parsed = parse_en_pl(html["debauchery"])
        cached = load_json("debauchery")
        assert parsed == cached

    def test_parse_amelioration(self):
        parsed = parse_en_pl(html["amelioration"])
        cached = load_json("amelioration")
        assert parsed == cached

    def test_parse_incapacity(self):
        parsed = parse_en_pl(html["incapacity"])
        cached = load_json("incapacity")
        assert parsed == cached

    def test_parse_scallion(self):
        parsed = parse_en_pl(html["scallion"])
        cached = load_json("scallion")
        assert parsed == cached

    def test_parse_prism(self):
        parsed = parse_en_pl(html["prism"])
        cached = load_json("prism")
        assert parsed == cached

    def test_parse_desolate(self):
        parsed = parse_en_pl(html["desolate"])
        cached = load_json("desolate")
        assert parsed == cached

    def test_parse_niggle(self):
        parsed = parse_en_pl(html["niggle"])
        cached = load_json("niggle")
        assert parsed == cached

    def test_parse_snap(self):
        parsed = parse_en_pl(html["snap"])
        cached = load_json("snap")
        assert parsed == cached

    def test_parse_lucent(self):
        parsed = parse_en_pl(html["lucent"])
        cached = load_json("lucent")
        assert parsed == cached

    def test_parse_spurious(self):
        parsed = parse_en_pl(html["spurious"])
        cached = load_json("spurious")
        assert parsed == cached

    def test_parse_pertain(self):
        parsed = parse_en_pl(html["pertain"])
        cached = load_json("pertain")
        assert parsed == cached

    def test_parse_allegiance(self):
        parsed = parse_en_pl(html["allegiance"])
        cached = load_json("allegiance")
        assert parsed == cached

    def test_parse_eminent(self):
        parsed = parse_en_pl(html["eminent"])
        cached = load_json("eminent")
        assert parsed == cached

    def test_parse_yore(self):
        parsed = parse_en_pl(html["yore"])
        cached = load_json("yore")
        assert parsed == cached

    def test_parse_dusk(self):
        parsed = parse_en_pl(html["dusk"])
        cached = load_json("dusk")
        assert parsed == cached

    def test_parse_bondage(self):
        parsed = parse_en_pl(html["bondage"])
        cached = load_json("bondage")
        assert parsed == cached

    def test_parse_starch(self):
        parsed = parse_en_pl(html["starch"])
        cached = load_json("starch")
        assert parsed == cached

    def test_parse_fertile(self):
        parsed = parse_en_pl(html["fertile"])
        cached = load_json("fertile")
        assert parsed == cached

    def test_parse_trump(self):
        parsed = parse_en_pl(html["trump"])
        cached = load_json("trump")
        assert parsed == cached

    def test_parse_aggrieve(self):
        parsed = parse_en_pl(html["aggrieve"])
        cached = load_json("aggrieve")
        assert parsed == cached

    def test_parse_cogitate(self):
        parsed = parse_en_pl(html["cogitate"])
        cached = load_json("cogitate")
        assert parsed == cached

    def test_parse_retrograde(self):
        parsed = parse_en_pl(html["retrograde"])
        cached = load_json("retrograde")
        assert parsed == cached

    def test_parse_inchoate(self):
        parsed = parse_en_pl(html["inchoate"])
        cached = load_json("inchoate")
        assert parsed == cached

    def test_parse_quandary(self):
        parsed = parse_en_pl(html["quandary"])
        cached = load_json("quandary")
        assert parsed == cached

    def test_parse_defenestration(self):
        parsed = parse_en_pl(html["defenestration"])
        cached = load_json("defenestration")
        assert parsed == cached

    def test_parse_vinegar(self):
        parsed = parse_en_pl(html["vinegar"])
        cached = load_json("vinegar")
        assert parsed == cached

    def test_parse_greyhound(self):
        parsed = parse_en_pl(html["greyhound"])
        cached = load_json("greyhound")
        assert parsed == cached

    def test_parse_hem(self):
        parsed = parse_en_pl(html["hem"])
        cached = load_json("hem")
        assert parsed == cached

    def test_parse_piety(self):
        parsed = parse_en_pl(html["piety"])
        cached = load_json("piety")
        assert parsed == cached

    def test_parse_poof(self):
        parsed = parse_en_pl(html["poof"])
        cached = load_json("poof")
        assert parsed == cached

    def test_parse_rue(self):
        parsed = parse_en_pl(html["rue"])
        cached = load_json("rue")
        assert parsed == cached

    def test_parse_brawl(self):
        parsed = parse_en_pl(html["brawl"])
        cached = load_json("brawl")
        assert parsed == cached

    def test_parse_divest(self):
        parsed = parse_en_pl(html["divest"])
        cached = load_json("divest")
        assert parsed == cached

    def test_parse_hustings(self):
        parsed = parse_en_pl(html["hustings"])
        cached = load_json("hustings")
        assert parsed == cached

    def test_parse_lone(self):
        parsed = parse_en_pl(html["lone"])
        cached = load_json("lone")
        assert parsed == cached

    def test_parse_countersink(self):
        parsed = parse_en_pl(html["countersink"])
        cached = load_json("countersink")
        assert parsed == cached

    def test_parse_apposition(self):
        parsed = parse_en_pl(html["apposition"])
        cached = load_json("apposition")
        assert parsed == cached

    def test_parse_weep(self):
        parsed = parse_en_pl(html["weep"])
        cached = load_json("weep")
        assert parsed == cached

    def test_parse_parallelogram(self):
        parsed = parse_en_pl(html["parallelogram"])
        cached = load_json("parallelogram")
        assert parsed == cached

    def test_parse_detain(self):
        parsed = parse_en_pl(html["detain"])
        cached = load_json("detain")
        assert parsed == cached

    def test_parse_extraneous(self):
        parsed = parse_en_pl(html["extraneous"])
        cached = load_json("extraneous")
        assert parsed == cached

    def test_parse_overwrought(self):
        parsed = parse_en_pl(html["overwrought"])
        cached = load_json("overwrought")
        assert parsed == cached

    def test_parse_gape(self):
        parsed = parse_en_pl(html["gape"])
        cached = load_json("gape")
        assert parsed == cached

    def test_parse_insidious(self):
        parsed = parse_en_pl(html["insidious"])
        cached = load_json("insidious")
        assert parsed == cached

    def test_parse_cobblestone(self):
        parsed = parse_en_pl(html["cobblestone"])
        cached = load_json("cobblestone")
        assert parsed == cached

    def test_parse_puff(self):
        parsed = parse_en_pl(html["puff"])
        cached = load_json("puff")
        assert parsed == cached

    def test_parse_pestilence(self):
        parsed = parse_en_pl(html["pestilence"])
        cached = load_json("pestilence")
        assert parsed == cached

    def test_parse_crotchety(self):
        parsed = parse_en_pl(html["crotchety"])
        cached = load_json("crotchety")
        assert parsed == cached

    def test_parse_verdant(self):
        parsed = parse_en_pl(html["verdant"])
        cached = load_json("verdant")
        assert parsed == cached

    def test_parse_tart(self):
        parsed = parse_en_pl(html["tart"])
        cached = load_json("tart")
        assert parsed == cached

    def test_parse_infallibility(self):
        parsed = parse_en_pl(html["infallibility"])
        cached = load_json("infallibility")
        assert parsed == cached

    def test_parse_fierce(self):
        parsed = parse_en_pl(html["fierce"])
        cached = load_json("fierce")
        assert parsed == cached

    def test_parse_curate(self):
        parsed = parse_en_pl(html["curate"])
        cached = load_json("curate")
        assert parsed == cached

    def test_parse_glimpse(self):
        parsed = parse_en_pl(html["glimpse"])
        cached = load_json("glimpse")
        assert parsed == cached

    def test_parse_simular(self):
        parsed = parse_en_pl(html["simular"])
        cached = load_json("simular")
        assert parsed == cached

    def test_parse_extoll(self):
        parsed = parse_en_pl(html["extoll"])
        cached = load_json("extoll")
        assert parsed == cached

    def test_parse_grit(self):
        parsed = parse_en_pl(html["grit"])
        cached = load_json("grit")
        assert parsed == cached

    def test_parse_knead(self):
        parsed = parse_en_pl(html["knead"])
        cached = load_json("knead")
        assert parsed == cached

    def test_parse_meting(self):
        parsed = parse_en_pl(html["meting"])
        cached = load_json("meting")
        assert parsed == cached

    def test_parse_ballot(self):
        parsed = parse_en_pl(html["ballot"])
        cached = load_json("ballot")
        assert parsed == cached

    def test_parse_conjugate(self):
        parsed = parse_en_pl(html["conjugate"])
        cached = load_json("conjugate")
        assert parsed == cached

    def test_parse_frolic(self):
        parsed = parse_en_pl(html["frolic"])
        cached = load_json("frolic")
        assert parsed == cached

    def test_parse_junction(self):
        parsed = parse_en_pl(html["junction"])
        cached = load_json("junction")
        assert parsed == cached

    def test_parse_hewing(self):
        parsed = parse_en_pl(html["hewing"])
        cached = load_json("hewing")
        assert parsed == cached

    def test_parse_abscess(self):
        parsed = parse_en_pl(html["abscess"])
        cached = load_json("abscess")
        assert parsed == cached

    def test_parse_pinnace(self):
        parsed = parse_en_pl(html["pinnace"])
        cached = load_json("pinnace")
        assert parsed == cached

    def test_parse_recess(self):
        parsed = parse_en_pl(html["recess"])
        cached = load_json("recess")
        assert parsed == cached

    def test_parse_recuperate(self):
        parsed = parse_en_pl(html["recuperate"])
        cached = load_json("recuperate")
        assert parsed == cached

    def test_parse_progeny(self):
        parsed = parse_en_pl(html["progeny"])
        cached = load_json("progeny")
        assert parsed == cached

    def test_parse_dissemination(self):
        parsed = parse_en_pl(html["dissemination"])
        cached = load_json("dissemination")
        assert parsed == cached

    def test_parse_specious(self):
        parsed = parse_en_pl(html["specious"])
        cached = load_json("specious")
        assert parsed == cached

    def test_parse_heath(self):
        parsed = parse_en_pl(html["heath"])
        cached = load_json("heath")
        assert parsed == cached

    def test_parse_foreshadow(self):
        parsed = parse_en_pl(html["foreshadow"])
        cached = load_json("foreshadow")
        assert parsed == cached

    def test_parse_conflate(self):
        parsed = parse_en_pl(html["conflate"])
        cached = load_json("conflate")
        assert parsed == cached

    def test_parse_sumac(self):
        parsed = parse_en_pl(html["sumac"])
        cached = load_json("sumac")
        assert parsed == cached

    def test_parse_dairy(self):
        parsed = parse_en_pl(html["dairy"])
        cached = load_json("dairy")
        assert parsed == cached

    def test_parse_flagellating(self):
        parsed = parse_en_pl(html["flagellating"])
        cached = load_json("flagellating")
        assert parsed == cached

    def test_parse_precocious(self):
        parsed = parse_en_pl(html["precocious"])
        cached = load_json("precocious")
        assert parsed == cached

    def test_parse_address(self):
        parsed = parse_en_pl(html["address"])
        cached = load_json("address")
        assert parsed == cached

    def test_parse_languish(self):
        parsed = parse_en_pl(html["languish"])
        cached = load_json("languish")
        assert parsed == cached

    def test_parse_amuse(self):
        parsed = parse_en_pl(html["amuse"])
        cached = load_json("amuse")
        assert parsed == cached

    def test_parse_uncanny(self):
        parsed = parse_en_pl(html["uncanny"])
        cached = load_json("uncanny")
        assert parsed == cached

    def test_parse_perpetuate(self):
        parsed = parse_en_pl(html["perpetuate"])
        cached = load_json("perpetuate")
        assert parsed == cached

    def test_parse_heathen(self):
        parsed = parse_en_pl(html["heathen"])
        cached = load_json("heathen")
        assert parsed == cached

    def test_parse_discernment(self):
        parsed = parse_en_pl(html["discernment"])
        cached = load_json("discernment")
        assert parsed == cached

    def test_parse_abort(self):
        parsed = parse_en_pl(html["abort"])
        cached = load_json("abort")
        assert parsed == cached

    def test_parse_iniquity(self):
        parsed = parse_en_pl(html["iniquity"])
        cached = load_json("iniquity")
        assert parsed == cached

    def test_parse_vary(self):
        parsed = parse_en_pl(html["vary"])
        cached = load_json("vary")
        assert parsed == cached

    def test_parse_featureless(self):
        parsed = parse_en_pl(html["featureless"])
        cached = load_json("featureless")
        assert parsed == cached

    def test_parse_crave(self):
        parsed = parse_en_pl(html["crave"])
        cached = load_json("crave")
        assert parsed == cached

    def test_parse_glaze(self):
        parsed = parse_en_pl(html["glaze"])
        cached = load_json("glaze")
        assert parsed == cached

    def test_parse_cricket(self):
        parsed = parse_en_pl(html["cricket"])
        cached = load_json("cricket")
        assert parsed == cached

    def test_parse_reify(self):
        parsed = parse_en_pl(html["reify"])
        cached = load_json("reify")
        assert parsed == cached

    def test_parse_amorphous(self):
        parsed = parse_en_pl(html["amorphous"])
        cached = load_json("amorphous")
        assert parsed == cached

    def test_parse_intangible(self):
        parsed = parse_en_pl(html["intangible"])
        cached = load_json("intangible")
        assert parsed == cached

    def test_parse_daft(self):
        parsed = parse_en_pl(html["daft"])
        cached = load_json("daft")
        assert parsed == cached

    def test_parse_colander(self):
        parsed = parse_en_pl(html["colander"])
        cached = load_json("colander")
        assert parsed == cached

    def test_parse_lesion(self):
        parsed = parse_en_pl(html["lesion"])
        cached = load_json("lesion")
        assert parsed == cached

    def test_parse_rein(self):
        parsed = parse_en_pl(html["rein"])
        cached = load_json("rein")
        assert parsed == cached

    def test_parse_teat(self):
        parsed = parse_en_pl(html["teat"])
        cached = load_json("teat")
        assert parsed == cached

    def test_parse_entice(self):
        parsed = parse_en_pl(html["entice"])
        cached = load_json("entice")
        assert parsed == cached

    def test_parse_expound(self):
        parsed = parse_en_pl(html["expound"])
        cached = load_json("expound")
        assert parsed == cached

    def test_parse_resent(self):
        parsed = parse_en_pl(html["resent"])
        cached = load_json("resent")
        assert parsed == cached

    def test_parse_fling(self):
        parsed = parse_en_pl(html["fling"])
        cached = load_json("fling")
        assert parsed == cached

    def test_parse_matricide(self):
        parsed = parse_en_pl(html["matricide"])
        cached = load_json("matricide")
        assert parsed == cached

    def test_parse_buggery(self):
        parsed = parse_en_pl(html["buggery"])
        cached = load_json("buggery")
        assert parsed == cached

    def test_parse_aegis(self):
        parsed = parse_en_pl(html["aegis"])
        cached = load_json("aegis")
        assert parsed == cached

    def test_parse_egregious(self):
        parsed = parse_en_pl(html["egregious"])
        cached = load_json("egregious")
        assert parsed == cached

    def test_parse_scourge(self):
        parsed = parse_en_pl(html["scourge"])
        cached = load_json("scourge")
        assert parsed == cached

    def test_parse_mould(self):
        parsed = parse_en_pl(html["mould"])
        cached = load_json("mould")
        assert parsed == cached

    def test_parse_rad(self):
        parsed = parse_en_pl(html["rad"])
        cached = load_json("rad")
        assert parsed == cached

    def test_parse_extruding(self):
        parsed = parse_en_pl(html["extruding"])
        cached = load_json("extruding")
        assert parsed == cached

    def test_parse_drama(self):
        parsed = parse_en_pl(html["drama"])
        cached = load_json("drama")
        assert parsed == cached

    def test_parse_murmur(self):
        parsed = parse_en_pl(html["murmur"])
        cached = load_json("murmur")
        assert parsed == cached

    def test_parse_smug(self):
        parsed = parse_en_pl(html["smug"])
        cached = load_json("smug")
        assert parsed == cached

    def test_parse_toil(self):
        parsed = parse_en_pl(html["toil"])
        cached = load_json("toil")
        assert parsed == cached

    def test_parse_fungible(self):
        parsed = parse_en_pl(html["fungible"])
        cached = load_json("fungible")
        assert parsed == cached

    def test_parse_plodding(self):
        parsed = parse_en_pl(html["plodding"])
        cached = load_json("plodding")
        assert parsed == cached

    def test_parse_bustle(self):
        parsed = parse_en_pl(html["bustle"])
        cached = load_json("bustle")
        assert parsed == cached

    def test_parse_acute(self):
        parsed = parse_en_pl(html["acute"])
        cached = load_json("acute")
        assert parsed == cached

    def test_parse_pouty(self):
        parsed = parse_en_pl(html["pouty"])
        cached = load_json("pouty")
        assert parsed == cached

    def test_parse_harass(self):
        parsed = parse_en_pl(html["harass"])
        cached = load_json("harass")
        assert parsed == cached

    def test_parse_pram(self):
        parsed = parse_en_pl(html["pram"])
        cached = load_json("pram")
        assert parsed == cached

    def test_parse_dilate(self):
        parsed = parse_en_pl(html["dilate"])
        cached = load_json("dilate")
        assert parsed == cached

    def test_parse_sow(self):
        parsed = parse_en_pl(html["sow"])
        cached = load_json("sow")
        assert parsed == cached

    def test_parse_requisite(self):
        parsed = parse_en_pl(html["requisite"])
        cached = load_json("requisite")
        assert parsed == cached

    def test_parse_wedge(self):
        parsed = parse_en_pl(html["wedge"])
        cached = load_json("wedge")
        assert parsed == cached

    def test_parse_disjunction(self):
        parsed = parse_en_pl(html["disjunction"])
        cached = load_json("disjunction")
        assert parsed == cached

    def test_parse_swell(self):
        parsed = parse_en_pl(html["swell"])
        cached = load_json("swell")
        assert parsed == cached

    def test_parse_contempt(self):
        parsed = parse_en_pl(html["contempt"])
        cached = load_json("contempt")
        assert parsed == cached

    def test_parse_birch(self):
        parsed = parse_en_pl(html["birch"])
        cached = load_json("birch")
        assert parsed == cached

    def test_parse_stakeout(self):
        parsed = parse_en_pl(html["stakeout"])
        cached = load_json("stakeout")
        assert parsed == cached

    def test_parse_ibex(self):
        parsed = parse_en_pl(html["ibex"])
        cached = load_json("ibex")
        assert parsed == cached

    def test_parse_submit(self):
        parsed = parse_en_pl(html["submit"])
        cached = load_json("submit")
        assert parsed == cached

    def test_parse_fowl(self):
        parsed = parse_en_pl(html["fowl"])
        cached = load_json("fowl")
        assert parsed == cached

    def test_parse_ostensibly(self):
        parsed = parse_en_pl(html["ostensibly"])
        cached = load_json("ostensibly")
        assert parsed == cached

    def test_parse_indignant(self):
        parsed = parse_en_pl(html["indignant"])
        cached = load_json("indignant")
        assert parsed == cached

    def test_parse_unbecoming(self):
        parsed = parse_en_pl(html["unbecoming"])
        cached = load_json("unbecoming")
        assert parsed == cached

    def test_parse_insensate(self):
        parsed = parse_en_pl(html["insensate"])
        cached = load_json("insensate")
        assert parsed == cached

    def test_parse_influence(self):
        parsed = parse_en_pl(html["influence"])
        cached = load_json("influence")
        assert parsed == cached

    def test_parse_noncommissioned(self):
        parsed = parse_en_pl(html["noncommissioned"])
        cached = load_json("noncommissioned")
        assert parsed == cached

    def test_parse_matronly(self):
        parsed = parse_en_pl(html["matronly"])
        cached = load_json("matronly")
        assert parsed == cached

    def test_parse_effeminate(self):
        parsed = parse_en_pl(html["effeminate"])
        cached = load_json("effeminate")
        assert parsed == cached

    def test_parse_nominal(self):
        parsed = parse_en_pl(html["nominal"])
        cached = load_json("nominal")
        assert parsed == cached

    def test_parse_rife(self):
        parsed = parse_en_pl(html["rife"])
        cached = load_json("rife")
        assert parsed == cached

    def test_parse_scuffed(self):
        parsed = parse_en_pl(html["scuffed"])
        cached = load_json("scuffed")
        assert parsed == cached

    def test_parse_unscathed(self):
        parsed = parse_en_pl(html["unscathed"])
        cached = load_json("unscathed")
        assert parsed == cached

    def test_parse_roil(self):
        parsed = parse_en_pl(html["roil"])
        cached = load_json("roil")
        assert parsed == cached

    def test_parse_nadir(self):
        parsed = parse_en_pl(html["nadir"])
        cached = load_json("nadir")
        assert parsed == cached

    def test_parse_coffer(self):
        parsed = parse_en_pl(html["coffer"])
        cached = load_json("coffer")
        assert parsed == cached

    def test_parse_gout(self):
        parsed = parse_en_pl(html["gout"])
        cached = load_json("gout")
        assert parsed == cached

    def test_parse_leap(self):
        parsed = parse_en_pl(html["leap"])
        cached = load_json("leap")
        assert parsed == cached

    def test_parse_indirection(self):
        parsed = parse_en_pl(html["indirection"])
        cached = load_json("indirection")
        assert parsed == cached

    def test_parse_ambler(self):
        parsed = parse_en_pl(html["ambler"])
        cached = load_json("ambler")
        assert parsed == cached

    def test_parse_supress(self):
        parsed = parse_en_pl(html["supress"])
        cached = load_json("supress")
        assert parsed == cached

    def test_parse_helot(self):
        parsed = parse_en_pl(html["helot"])
        cached = load_json("helot")
        assert parsed == cached

    def test_parse_dapper(self):
        parsed = parse_en_pl(html["dapper"])
        cached = load_json("dapper")
        assert parsed == cached

    def test_parse_erstwhile(self):
        parsed = parse_en_pl(html["erstwhile"])
        cached = load_json("erstwhile")
        assert parsed == cached

    def test_parse_geezer(self):
        parsed = parse_en_pl(html["geezer"])
        cached = load_json("geezer")
        assert parsed == cached

    def test_parse_audacity(self):
        parsed = parse_en_pl(html["audacity"])
        cached = load_json("audacity")
        assert parsed == cached

    def test_parse_trombone(self):
        parsed = parse_en_pl(html["trombone"])
        cached = load_json("trombone")
        assert parsed == cached

    def test_parse_ascend(self):
        parsed = parse_en_pl(html["ascend"])
        cached = load_json("ascend")
        assert parsed == cached

    def test_parse_voluptuous(self):
        parsed = parse_en_pl(html["voluptuous"])
        cached = load_json("voluptuous")
        assert parsed == cached

    def test_parse_denigration(self):
        parsed = parse_en_pl(html["denigration"])
        cached = load_json("denigration")
        assert parsed == cached

    def test_parse_transcendent(self):
        parsed = parse_en_pl(html["transcendent"])
        cached = load_json("transcendent")
        assert parsed == cached

    def test_parse_corpulent(self):
        parsed = parse_en_pl(html["corpulent"])
        cached = load_json("corpulent")
        assert parsed == cached

    def test_parse_haphazard(self):
        parsed = parse_en_pl(html["haphazard"])
        cached = load_json("haphazard")
        assert parsed == cached

    def test_parse_bowels(self):
        parsed = parse_en_pl(html["bowels"])
        cached = load_json("bowels")
        assert parsed == cached

    def test_parse_stem(self):
        parsed = parse_en_pl(html["stem"])
        cached = load_json("stem")
        assert parsed == cached

    def test_parse_flaunt(self):
        parsed = parse_en_pl(html["flaunt"])
        cached = load_json("flaunt")
        assert parsed == cached

    def test_parse_readily(self):
        parsed = parse_en_pl(html["readily"])
        cached = load_json("readily")
        assert parsed == cached

    def test_parse_peer(self):
        parsed = parse_en_pl(html["peer"])
        cached = load_json("peer")
        assert parsed == cached

    def test_parse_despoil(self):
        parsed = parse_en_pl(html["despoil"])
        cached = load_json("despoil")
        assert parsed == cached

    def test_parse_vex(self):
        parsed = parse_en_pl(html["vex"])
        cached = load_json("vex")
        assert parsed == cached

    def test_parse_glibness(self):
        parsed = parse_en_pl(html["glibness"])
        cached = load_json("glibness")
        assert parsed == cached

    def test_parse_artifact(self):
        parsed = parse_en_pl(html["artifact"])
        cached = load_json("artifact")
        assert parsed == cached

    def test_parse_ord(self):
        parsed = parse_en_pl(html["ord"])
        cached = load_json("ord")
        assert parsed == cached

    def test_parse_utilitarian(self):
        parsed = parse_en_pl(html["utilitarian"])
        cached = load_json("utilitarian")
        assert parsed == cached

    def test_parse_dolt(self):
        parsed = parse_en_pl(html["dolt"])
        cached = load_json("dolt")
        assert parsed == cached

    def test_parse_stint(self):
        parsed = parse_en_pl(html["stint"])
        cached = load_json("stint")
        assert parsed == cached

    def test_parse_estranged(self):
        parsed = parse_en_pl(html["estranged"])
        cached = load_json("estranged")
        assert parsed == cached

    def test_parse_succint(self):
        parsed = parse_en_pl(html["succint"])
        cached = load_json("succint")
        assert parsed == cached

    def test_parse_hassle(self):
        parsed = parse_en_pl(html["hassle"])
        cached = load_json("hassle")
        assert parsed == cached

    def test_parse_rivet(self):
        parsed = parse_en_pl(html["rivet"])
        cached = load_json("rivet")
        assert parsed == cached

    def test_parse_undertones(self):
        parsed = parse_en_pl(html["undertones"])
        cached = load_json("undertones")
        assert parsed == cached

    def test_parse_whiff(self):
        parsed = parse_en_pl(html["whiff"])
        cached = load_json("whiff")
        assert parsed == cached

    def test_parse_unraveling(self):
        parsed = parse_en_pl(html["unraveling"])
        cached = load_json("unraveling")
        assert parsed == cached

    def test_parse_gruff(self):
        parsed = parse_en_pl(html["gruff"])
        cached = load_json("gruff")
        assert parsed == cached

    def test_parse_vocation(self):
        parsed = parse_en_pl(html["vocation"])
        cached = load_json("vocation")
        assert parsed == cached

    def test_parse_committ(self):
        parsed = parse_en_pl(html["committ"])
        cached = load_json("committ")
        assert parsed == cached

    def test_parse_mince(self):
        parsed = parse_en_pl(html["mince"])
        cached = load_json("mince")
        assert parsed == cached

    def test_parse_flimsy(self):
        parsed = parse_en_pl(html["flimsy"])
        cached = load_json("flimsy")
        assert parsed == cached

    def test_parse_bumble(self):
        parsed = parse_en_pl(html["bumble"])
        cached = load_json("bumble")
        assert parsed == cached

    def test_parse_whirling(self):
        parsed = parse_en_pl(html["whirling"])
        cached = load_json("whirling")
        assert parsed == cached

    def test_parse_unbridle(self):
        parsed = parse_en_pl(html["unbridle"])
        cached = load_json("unbridle")
        assert parsed == cached

    def test_parse_gingerly(self):
        parsed = parse_en_pl(html["gingerly"])
        cached = load_json("gingerly")
        assert parsed == cached

    def test_parse_twang(self):
        parsed = parse_en_pl(html["twang"])
        cached = load_json("twang")
        assert parsed == cached

    def test_parse_teeter(self):
        parsed = parse_en_pl(html["teeter"])
        cached = load_json("teeter")
        assert parsed == cached

    def test_parse_manatee(self):
        parsed = parse_en_pl(html["manatee"])
        cached = load_json("manatee")
        assert parsed == cached

    def test_parse_succulent(self):
        parsed = parse_en_pl(html["succulent"])
        cached = load_json("succulent")
        assert parsed == cached

    def test_parse_centrifugal(self):
        parsed = parse_en_pl(html["centrifugal"])
        cached = load_json("centrifugal")
        assert parsed == cached

    def test_parse_edifice(self):
        parsed = parse_en_pl(html["edifice"])
        cached = load_json("edifice")
        assert parsed == cached

    def test_parse_tungsten(self):
        parsed = parse_en_pl(html["tungsten"])
        cached = load_json("tungsten")
        assert parsed == cached

    def test_parse_asphyxia(self):
        parsed = parse_en_pl(html["asphyxia"])
        cached = load_json("asphyxia")
        assert parsed == cached

    def test_parse_obscurity(self):
        parsed = parse_en_pl(html["obscurity"])
        cached = load_json("obscurity")
        assert parsed == cached

    def test_parse_unscrupulous(self):
        parsed = parse_en_pl(html["unscrupulous"])
        cached = load_json("unscrupulous")
        assert parsed == cached

    def test_parse_intercession(self):
        parsed = parse_en_pl(html["intercession"])
        cached = load_json("intercession")
        assert parsed == cached

    def test_parse_inexorable(self):
        parsed = parse_en_pl(html["inexorable"])
        cached = load_json("inexorable")
        assert parsed == cached

    def test_parse_fleeting(self):
        parsed = parse_en_pl(html["fleeting"])
        cached = load_json("fleeting")
        assert parsed == cached

    def test_parse_sounder(self):
        parsed = parse_en_pl(html["sounder"])
        cached = load_json("sounder")
        assert parsed == cached

    def test_parse_disgruntled(self):
        parsed = parse_en_pl(html["disgruntled"])
        cached = load_json("disgruntled")
        assert parsed == cached

    def test_parse_inducement(self):
        parsed = parse_en_pl(html["inducement"])
        cached = load_json("inducement")
        assert parsed == cached

    def test_parse_travois(self):
        parsed = parse_en_pl(html["travois"])
        cached = load_json("travois")
        assert parsed == cached

    def test_parse_crankshaft(self):
        parsed = parse_en_pl(html["crankshaft"])
        cached = load_json("crankshaft")
        assert parsed == cached

    def test_parse_caraway(self):
        parsed = parse_en_pl(html["caraway"])
        cached = load_json("caraway")
        assert parsed == cached

    def test_parse_awry(self):
        parsed = parse_en_pl(html["awry"])
        cached = load_json("awry")
        assert parsed == cached

    def test_parse_sleuth(self):
        parsed = parse_en_pl(html["sleuth"])
        cached = load_json("sleuth")
        assert parsed == cached

    def test_parse_pellet(self):
        parsed = parse_en_pl(html["pellet"])
        cached = load_json("pellet")
        assert parsed == cached

    def test_parse_phlebotomy(self):
        parsed = parse_en_pl(html["phlebotomy"])
        cached = load_json("phlebotomy")
        assert parsed == cached

    def test_parse_crackle(self):
        parsed = parse_en_pl(html["crackle"])
        cached = load_json("crackle")
        assert parsed == cached

    def test_parse_incursion(self):
        parsed = parse_en_pl(html["incursion"])
        cached = load_json("incursion")
        assert parsed == cached

    def test_parse_leeway(self):
        parsed = parse_en_pl(html["leeway"])
        cached = load_json("leeway")
        assert parsed == cached

    def test_parse_accessible(self):
        parsed = parse_en_pl(html["accessible"])
        cached = load_json("accessible")
        assert parsed == cached

    def test_parse_contract(self):
        parsed = parse_en_pl(html["contract"])
        cached = load_json("contract")
        assert parsed == cached

    def test_parse_simplistic(self):
        parsed = parse_en_pl(html["simplistic"])
        cached = load_json("simplistic")
        assert parsed == cached

    def test_parse_almanac(self):
        parsed = parse_en_pl(html["almanac"])
        cached = load_json("almanac")
        assert parsed == cached

    def test_parse_desultory(self):
        parsed = parse_en_pl(html["desultory"])
        cached = load_json("desultory")
        assert parsed == cached

    def test_parse_outpatient(self):
        parsed = parse_en_pl(html["outpatient"])
        cached = load_json("outpatient")
        assert parsed == cached

    def test_parse_array(self):
        parsed = parse_en_pl(html["array"])
        cached = load_json("array")
        assert parsed == cached

    def test_parse_neuroticism(self):
        parsed = parse_en_pl(html["neuroticism"])
        cached = load_json("neuroticism")
        assert parsed == cached

    def test_parse_augur(self):
        parsed = parse_en_pl(html["augur"])
        cached = load_json("augur")
        assert parsed == cached

    def test_parse_dyke(self):
        parsed = parse_en_pl(html["dyke"])
        cached = load_json("dyke")
        assert parsed == cached

    def test_parse_antsy(self):
        parsed = parse_en_pl(html["antsy"])
        cached = load_json("antsy")
        assert parsed == cached

    def test_parse_admission(self):
        parsed = parse_en_pl(html["admission"])
        cached = load_json("admission")
        assert parsed == cached

    def test_parse_sleazy(self):
        parsed = parse_en_pl(html["sleazy"])
        cached = load_json("sleazy")
        assert parsed == cached

    def test_parse_writ(self):
        parsed = parse_en_pl(html["writ"])
        cached = load_json("writ")
        assert parsed == cached

    def test_parse_cauldron(self):
        parsed = parse_en_pl(html["cauldron"])
        cached = load_json("cauldron")
        assert parsed == cached

    def test_parse_withering(self):
        parsed = parse_en_pl(html["withering"])
        cached = load_json("withering")
        assert parsed == cached

    def test_parse_cadence(self):
        parsed = parse_en_pl(html["cadence"])
        cached = load_json("cadence")
        assert parsed == cached

    def test_parse_cavity(self):
        parsed = parse_en_pl(html["cavity"])
        cached = load_json("cavity")
        assert parsed == cached

    def test_parse_collateral(self):
        parsed = parse_en_pl(html["collateral"])
        cached = load_json("collateral")
        assert parsed == cached

    def test_parse_feature(self):
        parsed = parse_en_pl(html["feature"])
        cached = load_json("feature")
        assert parsed == cached

    def test_parse_acorn(self):
        parsed = parse_en_pl(html["acorn"])
        cached = load_json("acorn")
        assert parsed == cached

    def test_parse_murky(self):
        parsed = parse_en_pl(html["murky"])
        cached = load_json("murky")
        assert parsed == cached

    def test_parse_jovial(self):
        parsed = parse_en_pl(html["jovial"])
        cached = load_json("jovial")
        assert parsed == cached

    def test_parse_tangent(self):
        parsed = parse_en_pl(html["tangent"])
        cached = load_json("tangent")
        assert parsed == cached

    def test_parse_enormity(self):
        parsed = parse_en_pl(html["enormity"])
        cached = load_json("enormity")
        assert parsed == cached

    def test_parse_prostrate(self):
        parsed = parse_en_pl(html["prostrate"])
        cached = load_json("prostrate")
        assert parsed == cached

    def test_parse_sever(self):
        parsed = parse_en_pl(html["sever"])
        cached = load_json("sever")
        assert parsed == cached

    def test_parse_venereal(self):
        parsed = parse_en_pl(html["venereal"])
        cached = load_json("venereal")
        assert parsed == cached

    def test_parse_loiter(self):
        parsed = parse_en_pl(html["loiter"])
        cached = load_json("loiter")
        assert parsed == cached

    def test_parse_accosted(self):
        parsed = parse_en_pl(html["accosted"])
        cached = load_json("accosted")
        assert parsed == cached

    def test_parse_adore(self):
        parsed = parse_en_pl(html["adore"])
        cached = load_json("adore")
        assert parsed == cached

    def test_parse_flexibility(self):
        parsed = parse_en_pl(html["flexibility"])
        cached = load_json("flexibility")
        assert parsed == cached

    def test_parse_embroidery(self):
        parsed = parse_en_pl(html["embroidery"])
        cached = load_json("embroidery")
        assert parsed == cached

    def test_parse_juncture(self):
        parsed = parse_en_pl(html["juncture"])
        cached = load_json("juncture")
        assert parsed == cached

    def test_parse_boast(self):
        parsed = parse_en_pl(html["boast"])
        cached = load_json("boast")
        assert parsed == cached

    def test_parse_longitude(self):
        parsed = parse_en_pl(html["longitude"])
        cached = load_json("longitude")
        assert parsed == cached

    def test_parse_ingot(self):
        parsed = parse_en_pl(html["ingot"])
        cached = load_json("ingot")
        assert parsed == cached

    def test_parse_katydid(self):
        parsed = parse_en_pl(html["katydid"])
        cached = load_json("katydid")
        assert parsed == cached

    def test_parse_Shia(self):
        parsed = parse_en_pl(html["Shia"])
        cached = load_json("Shia")
        assert parsed == cached

    def test_parse_actuary(self):
        parsed = parse_en_pl(html["actuary"])
        cached = load_json("actuary")
        assert parsed == cached

    def test_parse_throe(self):
        parsed = parse_en_pl(html["throe"])
        cached = load_json("throe")
        assert parsed == cached

    def test_parse_bifurcate(self):
        parsed = parse_en_pl(html["bifurcate"])
        cached = load_json("bifurcate")
        assert parsed == cached

    def test_parse_placate(self):
        parsed = parse_en_pl(html["placate"])
        cached = load_json("placate")
        assert parsed == cached

    def test_parse_leek(self):
        parsed = parse_en_pl(html["leek"])
        cached = load_json("leek")
        assert parsed == cached

    def test_parse_scurry(self):
        parsed = parse_en_pl(html["scurry"])
        cached = load_json("scurry")
        assert parsed == cached

    def test_parse_excoriation(self):
        parsed = parse_en_pl(html["excoriation"])
        cached = load_json("excoriation")
        assert parsed == cached

    def test_parse_primordial(self):
        parsed = parse_en_pl(html["primordial"])
        cached = load_json("primordial")
        assert parsed == cached

    def test_parse_potty(self):
        parsed = parse_en_pl(html["potty"])
        cached = load_json("potty")
        assert parsed == cached

    def test_parse_accentuate(self):
        parsed = parse_en_pl(html["accentuate"])
        cached = load_json("accentuate")
        assert parsed == cached

    def test_parse_wholly(self):
        parsed = parse_en_pl(html["wholly"])
        cached = load_json("wholly")
        assert parsed == cached

    def test_parse_tantalizing(self):
        parsed = parse_en_pl(html["tantalizing"])
        cached = load_json("tantalizing")
        assert parsed == cached

    def test_parse_fossick(self):
        parsed = parse_en_pl(html["fossick"])
        cached = load_json("fossick")
        assert parsed == cached

    def test_parse_gale(self):
        parsed = parse_en_pl(html["gale"])
        cached = load_json("gale")
        assert parsed == cached

    def test_parse_interlocutor(self):
        parsed = parse_en_pl(html["interlocutor"])
        cached = load_json("interlocutor")
        assert parsed == cached

    def test_parse_disparagement(self):
        parsed = parse_en_pl(html["disparagement"])
        cached = load_json("disparagement")
        assert parsed == cached

    def test_parse_quaver(self):
        parsed = parse_en_pl(html["quaver"])
        cached = load_json("quaver")
        assert parsed == cached

    def test_parse_amiable(self):
        parsed = parse_en_pl(html["amiable"])
        cached = load_json("amiable")
        assert parsed == cached

    def test_parse_harrowing(self):
        parsed = parse_en_pl(html["harrowing"])
        cached = load_json("harrowing")
        assert parsed == cached

    def test_parse_subsist(self):
        parsed = parse_en_pl(html["subsist"])
        cached = load_json("subsist")
        assert parsed == cached

    def test_parse_concede(self):
        parsed = parse_en_pl(html["concede"])
        cached = load_json("concede")
        assert parsed == cached

    def test_parse_scanty(self):
        parsed = parse_en_pl(html["scanty"])
        cached = load_json("scanty")
        assert parsed == cached

    def test_parse_harbour(self):
        parsed = parse_en_pl(html["harbour"])
        cached = load_json("harbour")
        assert parsed == cached

    def test_parse_hideously(self):
        parsed = parse_en_pl(html["hideously"])
        cached = load_json("hideously")
        assert parsed == cached

    def test_parse_canuck(self):
        parsed = parse_en_pl(html["canuck"])
        cached = load_json("canuck")
        assert parsed == cached

    def test_parse_lorry(self):
        parsed = parse_en_pl(html["lorry"])
        cached = load_json("lorry")
        assert parsed == cached

    def test_parse_fallout(self):
        parsed = parse_en_pl(html["fallout"])
        cached = load_json("fallout")
        assert parsed == cached

    def test_parse_pineal(self):
        parsed = parse_en_pl(html["pineal"])
        cached = load_json("pineal")
        assert parsed == cached

    def test_parse_indigence(self):
        parsed = parse_en_pl(html["indigence"])
        cached = load_json("indigence")
        assert parsed == cached

    def test_parse_ponder(self):
        parsed = parse_en_pl(html["ponder"])
        cached = load_json("ponder")
        assert parsed == cached

    def test_parse_doe(self):
        parsed = parse_en_pl(html["doe"])
        cached = load_json("doe")
        assert parsed == cached

    def test_parse_deviant(self):
        parsed = parse_en_pl(html["deviant"])
        cached = load_json("deviant")
        assert parsed == cached

    def test_parse_excerpt(self):
        parsed = parse_en_pl(html["excerpt"])
        cached = load_json("excerpt")
        assert parsed == cached

    def test_parse_contractions(self):
        parsed = parse_en_pl(html["contractions"])
        cached = load_json("contractions")
        assert parsed == cached

    def test_parse_beignet(self):
        parsed = parse_en_pl(html["beignet"])
        cached = load_json("beignet")
        assert parsed == cached

    def test_parse_caregivers(self):
        parsed = parse_en_pl(html["caregivers"])
        cached = load_json("caregivers")
        assert parsed == cached

    def test_parse_cellar(self):
        parsed = parse_en_pl(html["cellar"])
        cached = load_json("cellar")
        assert parsed == cached

    def test_parse_pejorative(self):
        parsed = parse_en_pl(html["pejorative"])
        cached = load_json("pejorative")
        assert parsed == cached

    def test_parse_soar(self):
        parsed = parse_en_pl(html["soar"])
        cached = load_json("soar")
        assert parsed == cached

    def test_parse_Formica(self):
        parsed = parse_en_pl(html["Formica"])
        cached = load_json("Formica")
        assert parsed == cached

    def test_parse_prescriptive(self):
        parsed = parse_en_pl(html["prescriptive"])
        cached = load_json("prescriptive")
        assert parsed == cached

    def test_parse_switch(self):
        parsed = parse_en_pl(html["switch"])
        cached = load_json("switch")
        assert parsed == cached

    def test_parse_miasma(self):
        parsed = parse_en_pl(html["miasma"])
        cached = load_json("miasma")
        assert parsed == cached

    def test_parse_mite(self):
        parsed = parse_en_pl(html["mite"])
        cached = load_json("mite")
        assert parsed == cached

    def test_parse_ravenous(self):
        parsed = parse_en_pl(html["ravenous"])
        cached = load_json("ravenous")
        assert parsed == cached

    def test_parse_frame(self):
        parsed = parse_en_pl(html["frame"])
        cached = load_json("frame")
        assert parsed == cached

    def test_parse_caustic(self):
        parsed = parse_en_pl(html["caustic"])
        cached = load_json("caustic")
        assert parsed == cached

    def test_parse_largesse(self):
        parsed = parse_en_pl(html["largesse"])
        cached = load_json("largesse")
        assert parsed == cached

    def test_parse_trifle(self):
        parsed = parse_en_pl(html["trifle"])
        cached = load_json("trifle")
        assert parsed == cached

    def test_parse_resort(self):
        parsed = parse_en_pl(html["resort"])
        cached = load_json("resort")
        assert parsed == cached

    def test_parse_augment(self):
        parsed = parse_en_pl(html["augment"])
        cached = load_json("augment")
        assert parsed == cached

    def test_parse_startling(self):
        parsed = parse_en_pl(html["startling"])
        cached = load_json("startling")
        assert parsed == cached

    def test_parse_frugality(self):
        parsed = parse_en_pl(html["frugality"])
        cached = load_json("frugality")
        assert parsed == cached

    def test_parse_introspective(self):
        parsed = parse_en_pl(html["introspective"])
        cached = load_json("introspective")
        assert parsed == cached

    def test_parse_catalyze(self):
        parsed = parse_en_pl(html["catalyze"])
        cached = load_json("catalyze")
        assert parsed == cached

    def test_parse_benighted(self):
        parsed = parse_en_pl(html["benighted"])
        cached = load_json("benighted")
        assert parsed == cached

    def test_parse_sway(self):
        parsed = parse_en_pl(html["sway"])
        cached = load_json("sway")
        assert parsed == cached

    def test_parse_agency(self):
        parsed = parse_en_pl(html["agency"])
        cached = load_json("agency")
        assert parsed == cached

    def test_parse_caption(self):
        parsed = parse_en_pl(html["caption"])
        cached = load_json("caption")
        assert parsed == cached

    def test_parse_horcrux(self):
        parsed = parse_en_pl(html["horcrux"])
        cached = load_json("horcrux")
        assert parsed == cached

    def test_parse_aloof(self):
        parsed = parse_en_pl(html["aloof"])
        cached = load_json("aloof")
        assert parsed == cached

    def test_parse_anguish(self):
        parsed = parse_en_pl(html["anguish"])
        cached = load_json("anguish")
        assert parsed == cached

    def test_parse_menace(self):
        parsed = parse_en_pl(html["menace"])
        cached = load_json("menace")
        assert parsed == cached

    def test_parse_maudlin(self):
        parsed = parse_en_pl(html["maudlin"])
        cached = load_json("maudlin")
        assert parsed == cached

    def test_parse_predator(self):
        parsed = parse_en_pl(html["predator"])
        cached = load_json("predator")
        assert parsed == cached

    def test_parse_sown(self):
        parsed = parse_en_pl(html["sown"])
        cached = load_json("sown")
        assert parsed == cached

    def test_parse_den(self):
        parsed = parse_en_pl(html["den"])
        cached = load_json("den")
        assert parsed == cached

    def test_parse_severance(self):
        parsed = parse_en_pl(html["severance"])
        cached = load_json("severance")
        assert parsed == cached

    def test_parse_recrudescence(self):
        parsed = parse_en_pl(html["recrudescence"])
        cached = load_json("recrudescence")
        assert parsed == cached

    def test_parse_impeccable(self):
        parsed = parse_en_pl(html["impeccable"])
        cached = load_json("impeccable")
        assert parsed == cached

    def test_parse_barrage(self):
        parsed = parse_en_pl(html["barrage"])
        cached = load_json("barrage")
        assert parsed == cached

    def test_parse_urge(self):
        parsed = parse_en_pl(html["urge"])
        cached = load_json("urge")
        assert parsed == cached

    def test_parse_mild(self):
        parsed = parse_en_pl(html["mild"])
        cached = load_json("mild")
        assert parsed == cached

    def test_parse_rectitude(self):
        parsed = parse_en_pl(html["rectitude"])
        cached = load_json("rectitude")
        assert parsed == cached

    def test_parse_conceited(self):
        parsed = parse_en_pl(html["conceited"])
        cached = load_json("conceited")
        assert parsed == cached

    def test_parse_pledge(self):
        parsed = parse_en_pl(html["pledge"])
        cached = load_json("pledge")
        assert parsed == cached

    def test_parse_tangential(self):
        parsed = parse_en_pl(html["tangential"])
        cached = load_json("tangential")
        assert parsed == cached

    def test_parse_tailgate(self):
        parsed = parse_en_pl(html["tailgate"])
        cached = load_json("tailgate")
        assert parsed == cached

    def test_parse_concierge(self):
        parsed = parse_en_pl(html["concierge"])
        cached = load_json("concierge")
        assert parsed == cached

    def test_parse_didn_t(self):
        parsed = parse_en_pl(html["didn't"])
        cached = load_json("didn't")
        assert parsed == cached

    def test_parse_moat(self):
        parsed = parse_en_pl(html["moat"])
        cached = load_json("moat")
        assert parsed == cached

    def test_parse_calamities(self):
        parsed = parse_en_pl(html["calamities"])
        cached = load_json("calamities")
        assert parsed == cached

    def test_parse_scag(self):
        parsed = parse_en_pl(html["scag"])
        cached = load_json("scag")
        assert parsed == cached

    def test_parse_commendable(self):
        parsed = parse_en_pl(html["commendable"])
        cached = load_json("commendable")
        assert parsed == cached

    def test_parse_defiant(self):
        parsed = parse_en_pl(html["defiant"])
        cached = load_json("defiant")
        assert parsed == cached

    def test_parse_hawk(self):
        parsed = parse_en_pl(html["hawk"])
        cached = load_json("hawk")
        assert parsed == cached

    def test_parse_orthogonal(self):
        parsed = parse_en_pl(html["orthogonal"])
        cached = load_json("orthogonal")
        assert parsed == cached

    def test_parse_nitwit(self):
        parsed = parse_en_pl(html["nitwit"])
        cached = load_json("nitwit")
        assert parsed == cached

    def test_parse_stain(self):
        parsed = parse_en_pl(html["stain"])
        cached = load_json("stain")
        assert parsed == cached

    def test_parse_treacherous(self):
        parsed = parse_en_pl(html["treacherous"])
        cached = load_json("treacherous")
        assert parsed == cached

    def test_parse_lynchpin(self):
        parsed = parse_en_pl(html["lynchpin"])
        cached = load_json("lynchpin")
        assert parsed == cached

    def test_parse_mainland(self):
        parsed = parse_en_pl(html["mainland"])
        cached = load_json("mainland")
        assert parsed == cached

    def test_parse_grope(self):
        parsed = parse_en_pl(html["grope"])
        cached = load_json("grope")
        assert parsed == cached

    def test_parse_bloke(self):
        parsed = parse_en_pl(html["bloke"])
        cached = load_json("bloke")
        assert parsed == cached

    def test_parse_hemorrhage(self):
        parsed = parse_en_pl(html["hemorrhage"])
        cached = load_json("hemorrhage")
        assert parsed == cached

    def test_parse_palpable(self):
        parsed = parse_en_pl(html["palpable"])
        cached = load_json("palpable")
        assert parsed == cached

    def test_parse_echelon(self):
        parsed = parse_en_pl(html["echelon"])
        cached = load_json("echelon")
        assert parsed == cached

    def test_parse_hewer(self):
        parsed = parse_en_pl(html["hewer"])
        cached = load_json("hewer")
        assert parsed == cached

    def test_parse_affliction(self):
        parsed = parse_en_pl(html["affliction"])
        cached = load_json("affliction")
        assert parsed == cached

    def test_parse_glisten(self):
        parsed = parse_en_pl(html["glisten"])
        cached = load_json("glisten")
        assert parsed == cached

    def test_parse_obviate(self):
        parsed = parse_en_pl(html["obviate"])
        cached = load_json("obviate")
        assert parsed == cached

    def test_parse_playdate(self):
        parsed = parse_en_pl(html["playdate"])
        cached = load_json("playdate")
        assert parsed == cached

    def test_parse_elide(self):
        parsed = parse_en_pl(html["elide"])
        cached = load_json("elide")
        assert parsed == cached

    def test_parse_planter(self):
        parsed = parse_en_pl(html["planter"])
        cached = load_json("planter")
        assert parsed == cached

    def test_parse_sabbatical(self):
        parsed = parse_en_pl(html["sabbatical"])
        cached = load_json("sabbatical")
        assert parsed == cached

    def test_parse_incongruous(self):
        parsed = parse_en_pl(html["incongruous"])
        cached = load_json("incongruous")
        assert parsed == cached

    def test_parse_burl(self):
        parsed = parse_en_pl(html["burl"])
        cached = load_json("burl")
        assert parsed == cached

    def test_parse_vitriolic(self):
        parsed = parse_en_pl(html["vitriolic"])
        cached = load_json("vitriolic")
        assert parsed == cached

    def test_parse_ulterior(self):
        parsed = parse_en_pl(html["ulterior"])
        cached = load_json("ulterior")
        assert parsed == cached

    def test_parse_abjure(self):
        parsed = parse_en_pl(html["abjure"])
        cached = load_json("abjure")
        assert parsed == cached

    def test_parse_taxis(self):
        parsed = parse_en_pl(html["taxis"])
        cached = load_json("taxis")
        assert parsed == cached

    def test_parse_indigo(self):
        parsed = parse_en_pl(html["indigo"])
        cached = load_json("indigo")
        assert parsed == cached

    def test_parse_shone(self):
        parsed = parse_en_pl(html["shone"])
        cached = load_json("shone")
        assert parsed == cached

    def test_parse_Lapp(self):
        parsed = parse_en_pl(html["Lapp"])
        cached = load_json("Lapp")
        assert parsed == cached

    def test_parse_deride(self):
        parsed = parse_en_pl(html["deride"])
        cached = load_json("deride")
        assert parsed == cached

    def test_parse_eulogise(self):
        parsed = parse_en_pl(html["eulogise"])
        cached = load_json("eulogise")
        assert parsed == cached

    def test_parse_hectic(self):
        parsed = parse_en_pl(html["hectic"])
        cached = load_json("hectic")
        assert parsed == cached

    def test_parse_stave(self):
        parsed = parse_en_pl(html["stave"])
        cached = load_json("stave")
        assert parsed == cached

    def test_parse_uncouth(self):
        parsed = parse_en_pl(html["uncouth"])
        cached = load_json("uncouth")
        assert parsed == cached

    def test_parse_ordain(self):
        parsed = parse_en_pl(html["ordain"])
        cached = load_json("ordain")
        assert parsed == cached

    def test_parse_lynx(self):
        parsed = parse_en_pl(html["lynx"])
        cached = load_json("lynx")
        assert parsed == cached

    def test_parse_genuflection(self):
        parsed = parse_en_pl(html["genuflection"])
        cached = load_json("genuflection")
        assert parsed == cached

    def test_parse_liver(self):
        parsed = parse_en_pl(html["liver"])
        cached = load_json("liver")
        assert parsed == cached

    def test_parse_modest(self):
        parsed = parse_en_pl(html["modest"])
        cached = load_json("modest")
        assert parsed == cached

    def test_parse_mooring(self):
        parsed = parse_en_pl(html["mooring"])
        cached = load_json("mooring")
        assert parsed == cached

    def test_parse_cobbler(self):
        parsed = parse_en_pl(html["cobbler"])
        cached = load_json("cobbler")
        assert parsed == cached

    def test_parse_savor(self):
        parsed = parse_en_pl(html["savor"])
        cached = load_json("savor")
        assert parsed == cached

    def test_parse_impunity(self):
        parsed = parse_en_pl(html["impunity"])
        cached = load_json("impunity")
        assert parsed == cached

    def test_parse_entrust(self):
        parsed = parse_en_pl(html["entrust"])
        cached = load_json("entrust")
        assert parsed == cached

    def test_parse_judder(self):
        parsed = parse_en_pl(html["judder"])
        cached = load_json("judder")
        assert parsed == cached

    def test_parse_clout(self):
        parsed = parse_en_pl(html["clout"])
        cached = load_json("clout")
        assert parsed == cached

    def test_parse_cogent(self):
        parsed = parse_en_pl(html["cogent"])
        cached = load_json("cogent")
        assert parsed == cached

    def test_parse_derangement(self):
        parsed = parse_en_pl(html["derangement"])
        cached = load_json("derangement")
        assert parsed == cached

    def test_parse_smiting(self):
        parsed = parse_en_pl(html["smiting"])
        cached = load_json("smiting")
        assert parsed == cached

    def test_parse_rummage(self):
        parsed = parse_en_pl(html["rummage"])
        cached = load_json("rummage")
        assert parsed == cached

    def test_parse_noose(self):
        parsed = parse_en_pl(html["noose"])
        cached = load_json("noose")
        assert parsed == cached

    def test_parse_amalgam(self):
        parsed = parse_en_pl(html["amalgam"])
        cached = load_json("amalgam")
        assert parsed == cached

    def test_parse_petit(self):
        parsed = parse_en_pl(html["petit"])
        cached = load_json("petit")
        assert parsed == cached

    def test_parse_boilerplate(self):
        parsed = parse_en_pl(html["boilerplate"])
        cached = load_json("boilerplate")
        assert parsed == cached

    def test_parse_front(self):
        parsed = parse_en_pl(html["front"])
        cached = load_json("front")
        assert parsed == cached

    def test_parse_tremble(self):
        parsed = parse_en_pl(html["tremble"])
        cached = load_json("tremble")
        assert parsed == cached

    def test_parse_volition(self):
        parsed = parse_en_pl(html["volition"])
        cached = load_json("volition")
        assert parsed == cached

    def test_parse_proclivity(self):
        parsed = parse_en_pl(html["proclivity"])
        cached = load_json("proclivity")
        assert parsed == cached

    def test_parse_waning(self):
        parsed = parse_en_pl(html["waning"])
        cached = load_json("waning")
        assert parsed == cached

    def test_parse_jovially(self):
        parsed = parse_en_pl(html["jovially"])
        cached = load_json("jovially")
        assert parsed == cached

    def test_parse_hoary(self):
        parsed = parse_en_pl(html["hoary"])
        cached = load_json("hoary")
        assert parsed == cached

    def test_parse_precipitate(self):
        parsed = parse_en_pl(html["precipitate"])
        cached = load_json("precipitate")
        assert parsed == cached

    def test_parse_eschew(self):
        parsed = parse_en_pl(html["eschew"])
        cached = load_json("eschew")
        assert parsed == cached

    def test_parse_superstition(self):
        parsed = parse_en_pl(html["superstition"])
        cached = load_json("superstition")
        assert parsed == cached

    def test_parse_bold(self):
        parsed = parse_en_pl(html["bold"])
        cached = load_json("bold")
        assert parsed == cached

    def test_parse_cobble(self):
        parsed = parse_en_pl(html["cobble"])
        cached = load_json("cobble")
        assert parsed == cached

    def test_parse_sedation(self):
        parsed = parse_en_pl(html["sedation"])
        cached = load_json("sedation")
        assert parsed == cached

    def test_parse_belcher(self):
        parsed = parse_en_pl(html["belcher"])
        cached = load_json("belcher")
        assert parsed == cached

    def test_parse_cramp(self):
        parsed = parse_en_pl(html["cramp"])
        cached = load_json("cramp")
        assert parsed == cached

    def test_parse_excessive(self):
        parsed = parse_en_pl(html["excessive"])
        cached = load_json("excessive")
        assert parsed == cached

    def test_parse_plainly(self):
        parsed = parse_en_pl(html["plainly"])
        cached = load_json("plainly")
        assert parsed == cached

    def test_parse_clandestine(self):
        parsed = parse_en_pl(html["clandestine"])
        cached = load_json("clandestine")
        assert parsed == cached

    def test_parse_bollard(self):
        parsed = parse_en_pl(html["bollard"])
        cached = load_json("bollard")
        assert parsed == cached

    def test_parse_credulous(self):
        parsed = parse_en_pl(html["credulous"])
        cached = load_json("credulous")
        assert parsed == cached

    def test_parse_ante(self):
        parsed = parse_en_pl(html["ante"])
        cached = load_json("ante")
        assert parsed == cached

    def test_parse_futon(self):
        parsed = parse_en_pl(html["futon"])
        cached = load_json("futon")
        assert parsed == cached

    def test_parse_synesthesia(self):
        parsed = parse_en_pl(html["synesthesia"])
        cached = load_json("synesthesia")
        assert parsed == cached

    def test_parse_single_out(self):
        parsed = parse_en_pl(html["single out"])
        cached = load_json("single out")
        assert parsed == cached

    def test_parse_mystical(self):
        parsed = parse_en_pl(html["mystical"])
        cached = load_json("mystical")
        assert parsed == cached

    def test_parse_grouch(self):
        parsed = parse_en_pl(html["grouch"])
        cached = load_json("grouch")
        assert parsed == cached

    def test_parse_uncanniness(self):
        parsed = parse_en_pl(html["uncanniness"])
        cached = load_json("uncanniness")
        assert parsed == cached

    def test_parse_epiphany(self):
        parsed = parse_en_pl(html["epiphany"])
        cached = load_json("epiphany")
        assert parsed == cached

    def test_parse_cowed(self):
        parsed = parse_en_pl(html["cowed"])
        cached = load_json("cowed")
        assert parsed == cached

    def test_parse_exonerate(self):
        parsed = parse_en_pl(html["exonerate"])
        cached = load_json("exonerate")
        assert parsed == cached

    def test_parse_during(self):
        parsed = parse_en_pl(html["during"])
        cached = load_json("during")
        assert parsed == cached

    def test_parse_affluence(self):
        parsed = parse_en_pl(html["affluence"])
        cached = load_json("affluence")
        assert parsed == cached

    def test_parse_bucolic(self):
        parsed = parse_en_pl(html["bucolic"])
        cached = load_json("bucolic")
        assert parsed == cached

    def test_parse_feasible(self):
        parsed = parse_en_pl(html["feasible"])
        cached = load_json("feasible")
        assert parsed == cached

    def test_parse_comestible(self):
        parsed = parse_en_pl(html["comestible"])
        cached = load_json("comestible")
        assert parsed == cached

    def test_parse_compulsion(self):
        parsed = parse_en_pl(html["compulsion"])
        cached = load_json("compulsion")
        assert parsed == cached

    def test_parse_bromide(self):
        parsed = parse_en_pl(html["bromide"])
        cached = load_json("bromide")
        assert parsed == cached

    def test_parse_vestibule(self):
        parsed = parse_en_pl(html["vestibule"])
        cached = load_json("vestibule")
        assert parsed == cached

    def test_parse_relief(self):
        parsed = parse_en_pl(html["relief"])
        cached = load_json("relief")
        assert parsed == cached

    def test_parse_abrupt(self):
        parsed = parse_en_pl(html["abrupt"])
        cached = load_json("abrupt")
        assert parsed == cached

    def test_parse_dapple(self):
        parsed = parse_en_pl(html["dapple"])
        cached = load_json("dapple")
        assert parsed == cached

    def test_parse_stye(self):
        parsed = parse_en_pl(html["stye"])
        cached = load_json("stye")
        assert parsed == cached

    def test_parse_angsty(self):
        parsed = parse_en_pl(html["angsty"])
        cached = load_json("angsty")
        assert parsed == cached

    def test_parse_larks(self):
        parsed = parse_en_pl(html["larks"])
        cached = load_json("larks")
        assert parsed == cached

    def test_parse_exacerbation(self):
        parsed = parse_en_pl(html["exacerbation"])
        cached = load_json("exacerbation")
        assert parsed == cached

    def test_parse_turgid(self):
        parsed = parse_en_pl(html["turgid"])
        cached = load_json("turgid")
        assert parsed == cached

    def test_parse_elk(self):
        parsed = parse_en_pl(html["elk"])
        cached = load_json("elk")
        assert parsed == cached

    def test_parse_paunch(self):
        parsed = parse_en_pl(html["paunch"])
        cached = load_json("paunch")
        assert parsed == cached

    def test_parse_hornbeam(self):
        parsed = parse_en_pl(html["hornbeam"])
        cached = load_json("hornbeam")
        assert parsed == cached

    def test_parse_scaffolding(self):
        parsed = parse_en_pl(html["scaffolding"])
        cached = load_json("scaffolding")
        assert parsed == cached

    def test_parse_obstruct(self):
        parsed = parse_en_pl(html["obstruct"])
        cached = load_json("obstruct")
        assert parsed == cached

    def test_parse_kestrel(self):
        parsed = parse_en_pl(html["kestrel"])
        cached = load_json("kestrel")
        assert parsed == cached

    def test_parse_impertinent(self):
        parsed = parse_en_pl(html["impertinent"])
        cached = load_json("impertinent")
        assert parsed == cached

    def test_parse_concision(self):
        parsed = parse_en_pl(html["concision"])
        cached = load_json("concision")
        assert parsed == cached

    def test_parse_myelin(self):
        parsed = parse_en_pl(html["myelin"])
        cached = load_json("myelin")
        assert parsed == cached

    def test_parse_possibility(self):
        parsed = parse_en_pl(html["possibility"])
        cached = load_json("possibility")
        assert parsed == cached

    def test_parse_revel(self):
        parsed = parse_en_pl(html["revel"])
        cached = load_json("revel")
        assert parsed == cached

    def test_parse_supplicant(self):
        parsed = parse_en_pl(html["supplicant"])
        cached = load_json("supplicant")
        assert parsed == cached

    def test_parse_caldron(self):
        parsed = parse_en_pl(html["caldron"])
        cached = load_json("caldron")
        assert parsed == cached

    def test_parse_amenity(self):
        parsed = parse_en_pl(html["amenity"])
        cached = load_json("amenity")
        assert parsed == cached

    def test_parse_supersede(self):
        parsed = parse_en_pl(html["supersede"])
        cached = load_json("supersede")
        assert parsed == cached

    def test_parse_fracture(self):
        parsed = parse_en_pl(html["fracture"])
        cached = load_json("fracture")
        assert parsed == cached

    def test_parse_nettle(self):
        parsed = parse_en_pl(html["nettle"])
        cached = load_json("nettle")
        assert parsed == cached

    def test_parse_heed(self):
        parsed = parse_en_pl(html["heed"])
        cached = load_json("heed")
        assert parsed == cached

    def test_parse_aproximate(self):
        parsed = parse_en_pl(html["aproximate"])
        cached = load_json("aproximate")
        assert parsed == cached

    def test_parse_regicide(self):
        parsed = parse_en_pl(html["regicide"])
        cached = load_json("regicide")
        assert parsed == cached

    def test_parse_cursory(self):
        parsed = parse_en_pl(html["cursory"])
        cached = load_json("cursory")
        assert parsed == cached

    def test_parse_pamphlet(self):
        parsed = parse_en_pl(html["pamphlet"])
        cached = load_json("pamphlet")
        assert parsed == cached

    def test_parse_uppercut(self):
        parsed = parse_en_pl(html["uppercut"])
        cached = load_json("uppercut")
        assert parsed == cached

    def test_parse_duffer(self):
        parsed = parse_en_pl(html["duffer"])
        cached = load_json("duffer")
        assert parsed == cached

    def test_parse_thence(self):
        parsed = parse_en_pl(html["thence"])
        cached = load_json("thence")
        assert parsed == cached

    def test_parse_humdrum(self):
        parsed = parse_en_pl(html["humdrum"])
        cached = load_json("humdrum")
        assert parsed == cached

    def test_parse_sanguine(self):
        parsed = parse_en_pl(html["sanguine"])
        cached = load_json("sanguine")
        assert parsed == cached

    def test_parse_shrivel(self):
        parsed = parse_en_pl(html["shrivel"])
        cached = load_json("shrivel")
        assert parsed == cached

    def test_parse_ermine(self):
        parsed = parse_en_pl(html["ermine"])
        cached = load_json("ermine")
        assert parsed == cached

    def test_parse_repress(self):
        parsed = parse_en_pl(html["repress"])
        cached = load_json("repress")
        assert parsed == cached

    def test_parse_bruiser(self):
        parsed = parse_en_pl(html["bruiser"])
        cached = load_json("bruiser")
        assert parsed == cached

    def test_parse_acclaim(self):
        parsed = parse_en_pl(html["acclaim"])
        cached = load_json("acclaim")
        assert parsed == cached

    def test_parse_poltergeist(self):
        parsed = parse_en_pl(html["poltergeist"])
        cached = load_json("poltergeist")
        assert parsed == cached

    def test_parse_summit(self):
        parsed = parse_en_pl(html["summit"])
        cached = load_json("summit")
        assert parsed == cached

    def test_parse_quack(self):
        parsed = parse_en_pl(html["quack"])
        cached = load_json("quack")
        assert parsed == cached

    def test_parse_spiffy(self):
        parsed = parse_en_pl(html["spiffy"])
        cached = load_json("spiffy")
        assert parsed == cached

    def test_parse_dew(self):
        parsed = parse_en_pl(html["dew"])
        cached = load_json("dew")
        assert parsed == cached

    def test_parse_aliment(self):
        parsed = parse_en_pl(html["aliment"])
        cached = load_json("aliment")
        assert parsed == cached

    def test_parse_concussion(self):
        parsed = parse_en_pl(html["concussion"])
        cached = load_json("concussion")
        assert parsed == cached

    def test_parse_septuagenarian(self):
        parsed = parse_en_pl(html["septuagenarian"])
        cached = load_json("septuagenarian")
        assert parsed == cached

    def test_parse_strew(self):
        parsed = parse_en_pl(html["strew"])
        cached = load_json("strew")
        assert parsed == cached

    def test_parse_slobber(self):
        parsed = parse_en_pl(html["slobber"])
        cached = load_json("slobber")
        assert parsed == cached

    def test_parse_solvent(self):
        parsed = parse_en_pl(html["solvent"])
        cached = load_json("solvent")
        assert parsed == cached

    def test_parse_frank(self):
        parsed = parse_en_pl(html["frank"])
        cached = load_json("frank")
        assert parsed == cached

    def test_parse_royal(self):
        parsed = parse_en_pl(html["royal"])
        cached = load_json("royal")
        assert parsed == cached

    def test_parse_barley(self):
        parsed = parse_en_pl(html["barley"])
        cached = load_json("barley")
        assert parsed == cached

    def test_parse_clench(self):
        parsed = parse_en_pl(html["clench"])
        cached = load_json("clench")
        assert parsed == cached

    def test_parse_imperturbable(self):
        parsed = parse_en_pl(html["imperturbable"])
        cached = load_json("imperturbable")
        assert parsed == cached

    def test_parse_tranquilize(self):
        parsed = parse_en_pl(html["tranquilize"])
        cached = load_json("tranquilize")
        assert parsed == cached

    def test_parse_virgil(self):
        parsed = parse_en_pl(html["virgil"])
        cached = load_json("virgil")
        assert parsed == cached

    def test_parse_lentils(self):
        parsed = parse_en_pl(html["lentils"])
        cached = load_json("lentils")
        assert parsed == cached

    def test_parse_incongruity(self):
        parsed = parse_en_pl(html["incongruity"])
        cached = load_json("incongruity")
        assert parsed == cached

    def test_parse_proclaim(self):
        parsed = parse_en_pl(html["proclaim"])
        cached = load_json("proclaim")
        assert parsed == cached

    def test_parse_appreciate(self):
        parsed = parse_en_pl(html["appreciate"])
        cached = load_json("appreciate")
        assert parsed == cached

    def test_parse_broth(self):
        parsed = parse_en_pl(html["broth"])
        cached = load_json("broth")
        assert parsed == cached

    def test_parse_humble(self):
        parsed = parse_en_pl(html["humble"])
        cached = load_json("humble")
        assert parsed == cached

    def test_parse_vitriol(self):
        parsed = parse_en_pl(html["vitriol"])
        cached = load_json("vitriol")
        assert parsed == cached

    def test_parse_afflict(self):
        parsed = parse_en_pl(html["afflict"])
        cached = load_json("afflict")
        assert parsed == cached

    def test_parse_subdue(self):
        parsed = parse_en_pl(html["subdue"])
        cached = load_json("subdue")
        assert parsed == cached

    def test_parse_laceration(self):
        parsed = parse_en_pl(html["laceration"])
        cached = load_json("laceration")
        assert parsed == cached

    def test_parse_arthritis(self):
        parsed = parse_en_pl(html["arthritis"])
        cached = load_json("arthritis")
        assert parsed == cached

    def test_parse_liason(self):
        parsed = parse_en_pl(html["liason"])
        cached = load_json("liason")
        assert parsed == cached

    def test_parse_vaporware(self):
        parsed = parse_en_pl(html["vaporware"])
        cached = load_json("vaporware")
        assert parsed == cached

    def test_parse_oust(self):
        parsed = parse_en_pl(html["oust"])
        cached = load_json("oust")
        assert parsed == cached

    def test_parse_jaunty(self):
        parsed = parse_en_pl(html["jaunty"])
        cached = load_json("jaunty")
        assert parsed == cached

    def test_parse_haunting(self):
        parsed = parse_en_pl(html["haunting"])
        cached = load_json("haunting")
        assert parsed == cached

    def test_parse_misnomer(self):
        parsed = parse_en_pl(html["misnomer"])
        cached = load_json("misnomer")
        assert parsed == cached

    def test_parse_layman(self):
        parsed = parse_en_pl(html["layman"])
        cached = load_json("layman")
        assert parsed == cached

    def test_parse_elusive(self):
        parsed = parse_en_pl(html["elusive"])
        cached = load_json("elusive")
        assert parsed == cached

    def test_parse_sedated(self):
        parsed = parse_en_pl(html["sedated"])
        cached = load_json("sedated")
        assert parsed == cached

    def test_parse_hovel(self):
        parsed = parse_en_pl(html["hovel"])
        cached = load_json("hovel")
        assert parsed == cached

