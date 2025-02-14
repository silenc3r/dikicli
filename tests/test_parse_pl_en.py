import json
import pathlib

from dikicli.core import parse_pl_en

test_dir = pathlib.Path(__file__).resolve().parent
html_dir = test_dir / "htmldump_pl"
json_dir = test_dir / "json_pl"

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
    def test_parse_zabytkowy(self):
        parsed = parse_pl_en(html["zabytkowy"])
        cached = load_json("zabytkowy")
        assert parsed == cached

    def test_parse_szerszeń(self):
        parsed = parse_pl_en(html["szerszeń"])
        cached = load_json("szerszeń")
        assert parsed == cached

    def test_parse_utrzymać(self):
        parsed = parse_pl_en(html["utrzymać"])
        cached = load_json("utrzymać")
        assert parsed == cached

    def test_parse_paskudny(self):
        parsed = parse_pl_en(html["paskudny"])
        cached = load_json("paskudny")
        assert parsed == cached

    def test_parse_jawor(self):
        parsed = parse_pl_en(html["jawor"])
        cached = load_json("jawor")
        assert parsed == cached

    def test_parse_pośredni(self):
        parsed = parse_pl_en(html["pośredni"])
        cached = load_json("pośredni")
        assert parsed == cached

    def test_parse_nadawca(self):
        parsed = parse_pl_en(html["nadawca"])
        cached = load_json("nadawca")
        assert parsed == cached

    def test_parse_trzoda(self):
        parsed = parse_pl_en(html["trzoda"])
        cached = load_json("trzoda")
        assert parsed == cached

    def test_parse_stonowany(self):
        parsed = parse_pl_en(html["stonowany"])
        cached = load_json("stonowany")
        assert parsed == cached

    def test_parse_okropny(self):
        parsed = parse_pl_en(html["okropny"])
        cached = load_json("okropny")
        assert parsed == cached

    def test_parse_zgryz(self):
        parsed = parse_pl_en(html["zgryz"])
        cached = load_json("zgryz")
        assert parsed == cached

    def test_parse_świecki(self):
        parsed = parse_pl_en(html["świecki"])
        cached = load_json("świecki")
        assert parsed == cached

    def test_parse_kauczuk(self):
        parsed = parse_pl_en(html["kauczuk"])
        cached = load_json("kauczuk")
        assert parsed == cached

    def test_parse_obły(self):
        parsed = parse_pl_en(html["obły"])
        cached = load_json("obły")
        assert parsed == cached

    def test_parse_spójny(self):
        parsed = parse_pl_en(html["spójny"])
        cached = load_json("spójny")
        assert parsed == cached

    def test_parse_przekątna(self):
        parsed = parse_pl_en(html["przekątna"])
        cached = load_json("przekątna")
        assert parsed == cached

    def test_parse_wrotki(self):
        parsed = parse_pl_en(html["wrotki"])
        cached = load_json("wrotki")
        assert parsed == cached

    def test_parse_oszukać(self):
        parsed = parse_pl_en(html["oszukać"])
        cached = load_json("oszukać")
        assert parsed == cached

    def test_parse_wartki(self):
        parsed = parse_pl_en(html["wartki"])
        cached = load_json("wartki")
        assert parsed == cached

    def test_parse_wyblakły(self):
        parsed = parse_pl_en(html["wyblakły"])
        cached = load_json("wyblakły")
        assert parsed == cached

    def test_parse_uciecha(self):
        parsed = parse_pl_en(html["uciecha"])
        cached = load_json("uciecha")
        assert parsed == cached

    def test_parse_ukrywać(self):
        parsed = parse_pl_en(html["ukrywać"])
        cached = load_json("ukrywać")
        assert parsed == cached

    def test_parse_kundel(self):
        parsed = parse_pl_en(html["kundel"])
        cached = load_json("kundel")
        assert parsed == cached

    def test_parse_jesion(self):
        parsed = parse_pl_en(html["jesion"])
        cached = load_json("jesion")
        assert parsed == cached

    def test_parse_bukmacher(self):
        parsed = parse_pl_en(html["bukmacher"])
        cached = load_json("bukmacher")
        assert parsed == cached

    def test_parse_umożliwiać(self):
        parsed = parse_pl_en(html["umożliwiać"])
        cached = load_json("umożliwiać")
        assert parsed == cached

    def test_parse_raczkować(self):
        parsed = parse_pl_en(html["raczkować"])
        cached = load_json("raczkować")
        assert parsed == cached

    def test_parse_wartka(self):
        parsed = parse_pl_en(html["wartka"])
        cached = load_json("wartka")
        assert parsed == cached

    def test_parse_posiadłość(self):
        parsed = parse_pl_en(html["posiadłość"])
        cached = load_json("posiadłość")
        assert parsed == cached

    def test_parse_funkcjonariusz(self):
        parsed = parse_pl_en(html["funkcjonariusz"])
        cached = load_json("funkcjonariusz")
        assert parsed == cached

    def test_parse_powiązany(self):
        parsed = parse_pl_en(html["powiązany"])
        cached = load_json("powiązany")
        assert parsed == cached

    def test_parse_kunszt(self):
        parsed = parse_pl_en(html["kunszt"])
        cached = load_json("kunszt")
        assert parsed == cached

    def test_parse_lipa(self):
        parsed = parse_pl_en(html["lipa"])
        cached = load_json("lipa")
        assert parsed == cached

    def test_parse_cyrograf(self):
        parsed = parse_pl_en(html["cyrograf"])
        cached = load_json("cyrograf")
        assert parsed == cached

    def test_parse_całkowicie(self):
        parsed = parse_pl_en(html["całkowicie"])
        cached = load_json("całkowicie")
        assert parsed == cached

    def test_parse_wpis(self):
        parsed = parse_pl_en(html["wpis"])
        cached = load_json("wpis")
        assert parsed == cached

    def test_parse_kolacja(self):
        parsed = parse_pl_en(html["kolacja"])
        cached = load_json("kolacja")
        assert parsed == cached

    def test_parse_narzeczona(self):
        parsed = parse_pl_en(html["narzeczona"])
        cached = load_json("narzeczona")
        assert parsed == cached

    def test_parse_brzoza(self):
        parsed = parse_pl_en(html["brzoza"])
        cached = load_json("brzoza")
        assert parsed == cached

    def test_parse_nieład(self):
        parsed = parse_pl_en(html["nieład"])
        cached = load_json("nieład")
        assert parsed == cached

    def test_parse_mianownik(self):
        parsed = parse_pl_en(html["mianownik"])
        cached = load_json("mianownik")
        assert parsed == cached

    def test_parse_rajfur(self):
        parsed = parse_pl_en(html["rajfur"])
        cached = load_json("rajfur")
        assert parsed == cached

    def test_parse_kawka(self):
        parsed = parse_pl_en(html["kawka"])
        cached = load_json("kawka")
        assert parsed == cached

    def test_parse_czerstwy(self):
        parsed = parse_pl_en(html["czerstwy"])
        cached = load_json("czerstwy")
        assert parsed == cached

    def test_parse_odwlekać(self):
        parsed = parse_pl_en(html["odwlekać"])
        cached = load_json("odwlekać")
        assert parsed == cached

    def test_parse_skubać(self):
        parsed = parse_pl_en(html["skubać"])
        cached = load_json("skubać")
        assert parsed == cached

    def test_parse_bluza(self):
        parsed = parse_pl_en(html["bluza"])
        cached = load_json("bluza")
        assert parsed == cached

    def test_parse_bejca(self):
        parsed = parse_pl_en(html["bejca"])
        cached = load_json("bejca")
        assert parsed == cached

    def test_parse_złośliwy(self):
        parsed = parse_pl_en(html["złośliwy"])
        cached = load_json("złośliwy")
        assert parsed == cached

    def test_parse_opiekować(self):
        parsed = parse_pl_en(html["opiekować"])
        cached = load_json("opiekować")
        assert parsed == cached

    def test_parse_potwarz(self):
        parsed = parse_pl_en(html["potwarz"])
        cached = load_json("potwarz")
        assert parsed == cached

    def test_parse_doceniać(self):
        parsed = parse_pl_en(html["doceniać"])
        cached = load_json("doceniać")
        assert parsed == cached

    def test_parse_wirówka(self):
        parsed = parse_pl_en(html["wirówka"])
        cached = load_json("wirówka")
        assert parsed == cached

    def test_parse_drzwi(self):
        parsed = parse_pl_en(html["drzwi"])
        cached = load_json("drzwi")
        assert parsed == cached

    def test_parse_opis(self):
        parsed = parse_pl_en(html["opis"])
        cached = load_json("opis")
        assert parsed == cached

    def test_parse_opaska(self):
        parsed = parse_pl_en(html["opaska"])
        cached = load_json("opaska")
        assert parsed == cached

    def test_parse_przystępny(self):
        parsed = parse_pl_en(html["przystępny"])
        cached = load_json("przystępny")
        assert parsed == cached

    def test_parse_ponury(self):
        parsed = parse_pl_en(html["ponury"])
        cached = load_json("ponury")
        assert parsed == cached

    def test_parse_przejściówka(self):
        parsed = parse_pl_en(html["przejściówka"])
        cached = load_json("przejściówka")
        assert parsed == cached

    def test_parse_statyw(self):
        parsed = parse_pl_en(html["statyw"])
        cached = load_json("statyw")
        assert parsed == cached

    def test_parse_czołgać(self):
        parsed = parse_pl_en(html["czołgać"])
        cached = load_json("czołgać")
        assert parsed == cached

    def test_parse_farsa(self):
        parsed = parse_pl_en(html["farsa"])
        cached = load_json("farsa")
        assert parsed == cached

    def test_parse_niedosyt(self):
        parsed = parse_pl_en(html["niedosyt"])
        cached = load_json("niedosyt")
        assert parsed == cached

    def test_parse_buk(self):
        parsed = parse_pl_en(html["buk"])
        cached = load_json("buk")
        assert parsed == cached

    def test_parse_mord(self):
        parsed = parse_pl_en(html["mord"])
        cached = load_json("mord")
        assert parsed == cached

    def test_parse_przelecieć(self):
        parsed = parse_pl_en(html["przelecieć"])
        cached = load_json("przelecieć")
        assert parsed == cached

    def test_parse_uczciwy(self):
        parsed = parse_pl_en(html["uczciwy"])
        cached = load_json("uczciwy")
        assert parsed == cached

    def test_parse_powielać(self):
        parsed = parse_pl_en(html["powielać"])
        cached = load_json("powielać")
        assert parsed == cached

    def test_parse_metoda(self):
        parsed = parse_pl_en(html["metoda"])
        cached = load_json("metoda")
        assert parsed == cached

    def test_parse_pielęgnować(self):
        parsed = parse_pl_en(html["pielęgnować"])
        cached = load_json("pielęgnować")
        assert parsed == cached

    def test_parse_pachołek(self):
        parsed = parse_pl_en(html["pachołek"])
        cached = load_json("pachołek")
        assert parsed == cached

    def test_parse_bezpodstawnie(self):
        parsed = parse_pl_en(html["bezpodstawnie"])
        cached = load_json("bezpodstawnie")
        assert parsed == cached

    def test_parse_szczątkowy(self):
        parsed = parse_pl_en(html["szczątkowy"])
        cached = load_json("szczątkowy")
        assert parsed == cached

    def test_parse_obowiązkowy(self):
        parsed = parse_pl_en(html["obowiązkowy"])
        cached = load_json("obowiązkowy")
        assert parsed == cached

    def test_parse_kichać(self):
        parsed = parse_pl_en(html["kichać"])
        cached = load_json("kichać")
        assert parsed == cached

    def test_parse_tapicerka(self):
        parsed = parse_pl_en(html["tapicerka"])
        cached = load_json("tapicerka")
        assert parsed == cached

    def test_parse_bezczelny(self):
        parsed = parse_pl_en(html["bezczelny"])
        cached = load_json("bezczelny")
        assert parsed == cached

    def test_parse_otulić(self):
        parsed = parse_pl_en(html["otulić"])
        cached = load_json("otulić")
        assert parsed == cached

    def test_parse_nadmiarowy(self):
        parsed = parse_pl_en(html["nadmiarowy"])
        cached = load_json("nadmiarowy")
        assert parsed == cached

    def test_parse_gramatura(self):
        parsed = parse_pl_en(html["gramatura"])
        cached = load_json("gramatura")
        assert parsed == cached

    def test_parse_dopełniacz(self):
        parsed = parse_pl_en(html["dopełniacz"])
        cached = load_json("dopełniacz")
        assert parsed == cached

    def test_parse_dbać(self):
        parsed = parse_pl_en(html["dbać"])
        cached = load_json("dbać")
        assert parsed == cached

    def test_parse_kornik(self):
        parsed = parse_pl_en(html["kornik"])
        cached = load_json("kornik")
        assert parsed == cached

    def test_parse_igrzyska(self):
        parsed = parse_pl_en(html["igrzyska"])
        cached = load_json("igrzyska")
        assert parsed == cached

    def test_parse_zagadnienie(self):
        parsed = parse_pl_en(html["zagadnienie"])
        cached = load_json("zagadnienie")
        assert parsed == cached

    def test_parse_ilość(self):
        parsed = parse_pl_en(html["ilość"])
        cached = load_json("ilość")
        assert parsed == cached

    def test_parse_awanturniczy(self):
        parsed = parse_pl_en(html["awanturniczy"])
        cached = load_json("awanturniczy")
        assert parsed == cached

    def test_parse_umiarkowany(self):
        parsed = parse_pl_en(html["umiarkowany"])
        cached = load_json("umiarkowany")
        assert parsed == cached

    def test_parse_jodła(self):
        parsed = parse_pl_en(html["jodła"])
        cached = load_json("jodła")
        assert parsed == cached

    def test_parse_kręty(self):
        parsed = parse_pl_en(html["kręty"])
        cached = load_json("kręty")
        assert parsed == cached

    def test_parse_przekraczać(self):
        parsed = parse_pl_en(html["przekraczać"])
        cached = load_json("przekraczać")
        assert parsed == cached

    def test_parse_świerk(self):
        parsed = parse_pl_en(html["świerk"])
        cached = load_json("świerk")
        assert parsed == cached

    def test_parse_odźwierny(self):
        parsed = parse_pl_en(html["odźwierny"])
        cached = load_json("odźwierny")
        assert parsed == cached

    def test_parse_deklinacja(self):
        parsed = parse_pl_en(html["deklinacja"])
        cached = load_json("deklinacja")
        assert parsed == cached

    def test_parse_potęga(self):
        parsed = parse_pl_en(html["potęga"])
        cached = load_json("potęga")
        assert parsed == cached

    def test_parse_świadomość(self):
        parsed = parse_pl_en(html["świadomość"])
        cached = load_json("świadomość")
        assert parsed == cached

    def test_parse_harmonijny(self):
        parsed = parse_pl_en(html["harmonijny"])
        cached = load_json("harmonijny")
        assert parsed == cached

    def test_parse_maskować(self):
        parsed = parse_pl_en(html["maskować"])
        cached = load_json("maskować")
        assert parsed == cached

    def test_parse_zuchwały(self):
        parsed = parse_pl_en(html["zuchwały"])
        cached = load_json("zuchwały")
        assert parsed == cached

    def test_parse_urzędnik(self):
        parsed = parse_pl_en(html["urzędnik"])
        cached = load_json("urzędnik")
        assert parsed == cached

    def test_parse_adresat(self):
        parsed = parse_pl_en(html["adresat"])
        cached = load_json("adresat")
        assert parsed == cached

    def test_parse_skrzypek(self):
        parsed = parse_pl_en(html["skrzypek"])
        cached = load_json("skrzypek")
        assert parsed == cached

    def test_parse_smuga(self):
        parsed = parse_pl_en(html["smuga"])
        cached = load_json("smuga")
        assert parsed == cached

    def test_parse_globus(self):
        parsed = parse_pl_en(html["globus"])
        cached = load_json("globus")
        assert parsed == cached

    def test_parse_postarzeć(self):
        parsed = parse_pl_en(html["postarzeć"])
        cached = load_json("postarzeć")
        assert parsed == cached

    def test_parse_trup(self):
        parsed = parse_pl_en(html["trup"])
        cached = load_json("trup")
        assert parsed == cached

    def test_parse_kasztanowy(self):
        parsed = parse_pl_en(html["kasztanowy"])
        cached = load_json("kasztanowy")
        assert parsed == cached

    def test_parse_zdanie(self):
        parsed = parse_pl_en(html["zdanie"])
        cached = load_json("zdanie")
        assert parsed == cached

    def test_parse_starzeć(self):
        parsed = parse_pl_en(html["starzeć"])
        cached = load_json("starzeć")
        assert parsed == cached

    def test_parse_nijaki(self):
        parsed = parse_pl_en(html["nijaki"])
        cached = load_json("nijaki")
        assert parsed == cached

    def test_parse_niepotrzebnie(self):
        parsed = parse_pl_en(html["niepotrzebnie"])
        cached = load_json("niepotrzebnie")
        assert parsed == cached

    def test_parse_kora(self):
        parsed = parse_pl_en(html["kora"])
        cached = load_json("kora")
        assert parsed == cached

    def test_parse_kajdanki(self):
        parsed = parse_pl_en(html["kajdanki"])
        cached = load_json("kajdanki")
        assert parsed == cached

    def test_parse_przedostatni(self):
        parsed = parse_pl_en(html["przedostatni"])
        cached = load_json("przedostatni")
        assert parsed == cached

    def test_parse_chłosta(self):
        parsed = parse_pl_en(html["chłosta"])
        cached = load_json("chłosta")
        assert parsed == cached

    def test_parse_miniony(self):
        parsed = parse_pl_en(html["miniony"])
        cached = load_json("miniony")
        assert parsed == cached

    def test_parse_kamerton(self):
        parsed = parse_pl_en(html["kamerton"])
        cached = load_json("kamerton")
        assert parsed == cached

    def test_parse_przepastny(self):
        parsed = parse_pl_en(html["przepastny"])
        cached = load_json("przepastny")
        assert parsed == cached

    def test_parse_dorożka(self):
        parsed = parse_pl_en(html["dorożka"])
        cached = load_json("dorożka")
        assert parsed == cached

    def test_parse_służb(self):
        parsed = parse_pl_en(html["służb"])
        cached = load_json("służb")
        assert parsed == cached

    def test_parse_powieka(self):
        parsed = parse_pl_en(html["powieka"])
        cached = load_json("powieka")
        assert parsed == cached

    def test_parse_pupa(self):
        parsed = parse_pl_en(html["pupa"])
        cached = load_json("pupa")
        assert parsed == cached

    def test_parse_celownik(self):
        parsed = parse_pl_en(html["celownik"])
        cached = load_json("celownik")
        assert parsed == cached

    def test_parse_konstrukcja(self):
        parsed = parse_pl_en(html["konstrukcja"])
        cached = load_json("konstrukcja")
        assert parsed == cached

    def test_parse_zaślepka(self):
        parsed = parse_pl_en(html["zaślepka"])
        cached = load_json("zaślepka")
        assert parsed == cached

    def test_parse_przedział(self):
        parsed = parse_pl_en(html["przedział"])
        cached = load_json("przedział")
        assert parsed == cached

    def test_parse_obrzydliwy(self):
        parsed = parse_pl_en(html["obrzydliwy"])
        cached = load_json("obrzydliwy")
        assert parsed == cached

    def test_parse_łagodny(self):
        parsed = parse_pl_en(html["łagodny"])
        cached = load_json("łagodny")
        assert parsed == cached

    def test_parse_bolączka(self):
        parsed = parse_pl_en(html["bolączka"])
        cached = load_json("bolączka")
        assert parsed == cached

    def test_parse_wywrotka(self):
        parsed = parse_pl_en(html["wywrotka"])
        cached = load_json("wywrotka")
        assert parsed == cached

    def test_parse_bezpodstawny(self):
        parsed = parse_pl_en(html["bezpodstawny"])
        cached = load_json("bezpodstawny")
        assert parsed == cached

    def test_parse_oślizgły(self):
        parsed = parse_pl_en(html["oślizgły"])
        cached = load_json("oślizgły")
        assert parsed == cached

    def test_parse_patroszyć(self):
        parsed = parse_pl_en(html["patroszyć"])
        cached = load_json("patroszyć")
        assert parsed == cached

    def test_parse_powstać(self):
        parsed = parse_pl_en(html["powstać"])
        cached = load_json("powstać")
        assert parsed == cached

    def test_parse_trąbka(self):
        parsed = parse_pl_en(html["trąbka"])
        cached = load_json("trąbka")
        assert parsed == cached

    def test_parse_frajer(self):
        parsed = parse_pl_en(html["frajer"])
        cached = load_json("frajer")
        assert parsed == cached

    def test_parse_krowa(self):
        parsed = parse_pl_en(html["krowa"])
        cached = load_json("krowa")
        assert parsed == cached

    def test_parse_koc(self):
        parsed = parse_pl_en(html["koc"])
        cached = load_json("koc")
        assert parsed == cached

    def test_parse_topola(self):
        parsed = parse_pl_en(html["topola"])
        cached = load_json("topola")
        assert parsed == cached

    def test_parse_kocyk(self):
        parsed = parse_pl_en(html["kocyk"])
        cached = load_json("kocyk")
        assert parsed == cached

    def test_parse_czereśnia(self):
        parsed = parse_pl_en(html["czereśnia"])
        cached = load_json("czereśnia")
        assert parsed == cached

    def test_parse_bubel(self):
        parsed = parse_pl_en(html["bubel"])
        cached = load_json("bubel")
        assert parsed == cached

    def test_parse_biernik(self):
        parsed = parse_pl_en(html["biernik"])
        cached = load_json("biernik")
        assert parsed == cached

    def test_parse_poważny(self):
        parsed = parse_pl_en(html["poważny"])
        cached = load_json("poważny")
        assert parsed == cached

    def test_parse_bug(self):
        parsed = parse_pl_en(html["bug"])
        cached = load_json("bug")
        assert parsed == cached

    def test_parse_ułożony(self):
        parsed = parse_pl_en(html["ułożony"])
        cached = load_json("ułożony")
        assert parsed == cached

    def test_parse_odpowiadający(self):
        parsed = parse_pl_en(html["odpowiadający"])
        cached = load_json("odpowiadający")
        assert parsed == cached

    def test_parse_cło(self):
        parsed = parse_pl_en(html["cło"])
        cached = load_json("cło")
        assert parsed == cached

    def test_parse_narzeczeni(self):
        parsed = parse_pl_en(html["narzeczeni"])
        cached = load_json("narzeczeni")
        assert parsed == cached

    def test_parse_odpychający(self):
        parsed = parse_pl_en(html["odpychający"])
        cached = load_json("odpychający")
        assert parsed == cached

    def test_parse_front(self):
        parsed = parse_pl_en(html["front"])
        cached = load_json("front")
        assert parsed == cached

    def test_parse_swobodny(self):
        parsed = parse_pl_en(html["swobodny"])
        cached = load_json("swobodny")
        assert parsed == cached

    def test_parse_szklarnia(self):
        parsed = parse_pl_en(html["szklarnia"])
        cached = load_json("szklarnia")
        assert parsed == cached

    def test_parse_wałek(self):
        parsed = parse_pl_en(html["wałek"])
        cached = load_json("wałek")
        assert parsed == cached

    def test_parse_nachalny(self):
        parsed = parse_pl_en(html["nachalny"])
        cached = load_json("nachalny")
        assert parsed == cached

    def test_parse_bordo(self):
        parsed = parse_pl_en(html["bordo"])
        cached = load_json("bordo")
        assert parsed == cached

    def test_parse_ognisko(self):
        parsed = parse_pl_en(html["ognisko"])
        cached = load_json("ognisko")
        assert parsed == cached
