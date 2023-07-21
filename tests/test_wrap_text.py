import os
import shutil
import tempfile
import pytest

from dikicli.core import lookup_online
from dikicli.core import wrap_text
from dikicli.parsers import (
    parse_en_pl,
    parse_not_found,
    Entity,
    Meaning,
    PartOfSpeech,
    Sentence,
    Info,
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


@pytest.fixture
def conf_dict(env):
    config = {
        "data dir": os.environ["DIKI_DATA_DIR"],
        "linewrap": "78",
        "colors": "yes",
        "web browser": "default",
    }
    return config


def translate(word):
    html_dump = lookup_online(word).html
    result = parse_en_pl(html_dump)
    return result


@pytest.mark.vcr()
class TestWrapText:
    def test_wrap_invalid_word(self):
        html_dump = lookup_online("yyyy").html
        translation = parse_not_found(html_dump)
        result = wrap_text(translation)
        assert result == ["Nie znaleziono dokładnego tłumaczenia wpisanej frazy."]

    def test_wrap_typo_eblem(self):
        html_dump = lookup_online("eblem").html
        translation = parse_not_found(html_dump)
        result = wrap_text(translation)
        assert result == [
            "Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: emblem"
        ]

    def test_wrap_typo_wose(self):
        html_dump = lookup_online("wose").html
        translation = parse_not_found(html_dump)
        result = wrap_text(translation)
        assert result == [
            "Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: wise, whose, worse, dose, woke"
        ]

    def test_wrap_abate(self):
        translation = translate("abate")
        result = wrap_text(translation)
        assert result == [
            "abate",
            "[czasownik]",
            "  1. obniżać się, zmniejszać się",
            "  2. słabnąć, ustępować",
            "  3. cichnąć, wygasać",
            "  4. unieważniać",
        ]

    def test_wrap_abet(self):
        translation = translate("abet")
        result = wrap_text(translation)
        assert result == [
            "abet",
            "[czasownik]",
            "  1. podżegać (do czegoś)",
            "  2. pomagać (w zrobieniu czegoś nielegalnego)",
            "",
            "[rzeczownik]",
            "  1. przestępstwo",
        ]

    def test_wrap_weight(self):
        translation = translate("weight")
        result = wrap_text(translation)
        assert result == [
            "weight",
            "Wt",
            "wt.",
            "wt",
            "[rzeczownik]",
            "  1. waga, ciężar (miara tego, ile coś waży)",
            "",
            "      These sweets are sold by weight.",
            "      (Te cukierki są sprzedawane na wagę.)",
            "",
            "      What is the weight of this cheese? I want only 40 grams.",
            "      (Jaka jest waga tego sera? Chcę tylko 40 gram.)",
            "",
            "  2. waga (człowieka)",
            "",
            "      What is your height and weight?",
            "      (Jaki jest twój wzrost i waga?)",
            "",
            "      Her weight was dangerously low.",
            "      (Jej waga była niebezpiecznie niska.)",
            "",
            "  3. ciężar (bycie ciężkim)",
            "",
            "      My knees buckled under the weight.",
            "      (Kolana ugięły mi się pod wpływem ciężaru.)",
            "",
            "  4. ciężar (coś ciężkiego)",
            "",
            "      She won't be able to lift these weights herself.",
            "      (Ona nie będzie w stanie unieść sama tych ciężarów.)",
            "",
            "      These bags are such a weight, let me help you.",
            "      (Te torby to taki ciężar, pozwól, że ci pomogę.)",
            "",
            "  5. obciążenie, zmartwienie, ciężar",
            "",
            "      Raising a child is a huge weight for inexperienced people.",
            "      (Wychowywanie dziecka jest dużym obciążeniem dla niedoświadczonych osób.)",
            "",
            "      Her son causes her a lot of weight.",
            "      (Jej syn przysparza jej wiele zmartwień.)",
            "",
            "  6. waga, znaczenie, ranga",
            "",
            "      I didn't realise weight of the meeting.",
            "      (Nie zdawałem sobie sprawy z wagi tego spotkania.)",
            "",
            "      She attaches too much weight to petty problems.",
            "      (Ona przywiązuje zbyt dużo wagi do błahych problemów.)",
            "",
            "  7. duża ilość (czegoś)",
            "",
            "      I have a weight of apples in my garden.",
            "      (Mam dużą ilość jabłek w moim ogrodzie.)",
            "",
            "      My mother bought a weight of food because the shops are closed tomorrow.",
            "      (Moja mama kupiła dużą ilość jedzenia, bo jutro sklepy są zamknięte.)",
            "",
            "  8. odważnik, ciężarek",
            "",
            "      This weight is too heavy for me, I can't lift it.",
            "      (Ten odważnik jest dla mnie za ciężki, nie mogę go unieść.)",
            "",
            "      I do all exercises with weights - it helps me shape my body.",
            "      (Robię wszystkie ćwiczenia z ciężarkami - to pomaga mi wymodelować ciało.)",
            "",
            "  9. ciężar, ciężarek, obciążnik (używany do ćwiczeń)",
            "",
            "      Lifting weights can be a good exercise for building muscles.",
            "      (Podnoszenie ciężarów może być dobrym ćwiczeniem na budowę mięśni.)",
            "",
            "      A weight fell on my foot.",
            "      (Ciężarek spadł mi na nogę.)",
            "",
            "[czasownik]",
            "  1. przemawiać, przeważać",
            "",
            "[przymiotnik]",
            "  1. wagowy",
            "",
            "weight",
            "weight down",
            "[czasownik]",
            "  1. obciążać (np. sieć rybacką, łódź)",
            "",
            "      We can't take this box, it will weight our boat too much.",
            "      (Nie możemy zabrać tego pudła, za bardzo obciąży naszą łódź.)",
            "",
            "      Too many passengers may weight the ship too much.",
            "      (Zbyt wielu pasażerów może za bardzo obciążyć statek.)",
        ]

    def test_wrap_apple(self):
        translation = translate("apple")
        result = wrap_text(translation)
        assert result == [
            "apple",
            "[rzeczownik]",
            "  1. jabłko",
            "",
            "      I'll just have an apple.",
            "      (Po prostu zjem jabłko.)",
            "",
            "      Eating an apple every day will help keep you healthy.",
            "      (Jedzenie jednego jabłka dziennie pomoże ci pozostać zdrowym.)",
            "",
            "      I like green apples the most.",
            "      (Najbardziej lubię zielone jabłka.)",
            "",
            "[przymiotnik]",
            "  1. jabłkowy",
            "",
            "      Mary likes apple juice.",
            "      (Mary lubi sok jabłkowy.)",
            "",
            "      He ate the whole jar of apple mousse.",
            "      (On zjadł cały słoik musu jabłkowego.)",
            "",
            "      She drinks apple juice in the morning.",
            "      (Ona pije sok jabłkowy rano.)",
            "",
            "Apple",
            "[rzeczownik]",
            "  1. Apple (firma komputerowa)",
            "",
            "      Steve Jobs was one of the co-founders of Apple.",
            "      (Steve Jobs był jednym ze współzałożycieli Apple'a.)",
            "",
            "      I bought an Apple computer.",
            "      (Kupiłem komputer firmy Apple.)",
        ]

    def test_wrap_switch(self):
        translation = translate("switch")
        result = wrap_text(translation)
        assert result == [
            "switch",
            "[rzeczownik]",
            "  1. łącznik (napięcia), wyłącznik (sieciowy), kontakt (elektryczny)",
            "",
            "      We could use some light. Flip the switch on.",
            "      (Przydałoby nam się trochę światła. Naciśnij przełącznik.)",
            "",
            "      It's so dark that I can't even see the switch.",
            "      (Jest tak ciemno, że nawet nie widzę kontaktu.)",
            "",
            "      Don't touch the switch with wet hands.",
            "      (Nie dotykaj kontaktu mokrymi rękami.)",
            "",
            "  2. zmiana (z czegoś na coś), przejście (np. z komunizmu na kapitalizm)",
            "",
            "      For those looking to make the switch, some research is in order.",
            "      (Wszyscy, którzy chcą dokonać zmiany, powinni najpierw przeprowadzić badania.)",
            "",
            "      That switch will be good for our country.",
            "      (Ta zmiana będzie dobra dla naszego kraju.)",
            "",
            "  3. zwrotnica (kolejowa)",
            "",
            "      Somebody has to pull the switch or we won't make it.",
            "      (Ktoś musi pociągnąć za zwrotnicę albo nie damy rady.)",
            "",
            "      The two trains crashed into each other at the switch.",
            "      (Dwa pociągi zderzyły się ze sobą na zwrotnicy.)",
            "",
            "  4. rózga, witka",
            "",
            "      My grandfather hit me with the switch because I was naughty.",
            "      (Mój dziadek uderzył mnie rózgą, bo byłem niegrzeczny.)",
            "",
            "      His parents used to hit him with a switch as a punishment.",
            "      (Jego rodzice bili go rózgą w ramach kary.)",
            "",
            "[czasownik]",
            "  1. przełączać (programy, stacje radiowe)",
            "",
            "      He switched channels, hoping to find something more interesting.",
            "      (Przełączył kanał, próbując znaleźć coś bardziej interesującego.)",
            "",
            "      Stop switching radio stations, it's annoying!",
            "      (Przestań przełączać stacje radiowe, to denerwujące!)",
            "",
            "  2. zmieniać (np. taktykę), przechodzić (z jednej strony na drugą), przerzucać (się na coś)",
            "",
            "      He had to switch sides, as the building he looked for was on the other side of the street.",
            "      (On musiał zmienić stronę, ponieważ budynek, którego szukał był po drugiej stronie ulicy.)",
            "",
            "      He switched to veganism when he started dating this girl.",
            "      (Przerzucił się na weganizm, kiedy zaczął spotykać się z tą dziewczyną.)",
            "",
            "  3. zastępować (coś czymś), wymieniać (coś na coś), zmieniać (rzecz na inną)",
            "",
            "      He switched his BMW for a Jeep.",
            "      (On zamienił swoje BMW na Jeepa.)",
            "",
            "      You should switch your old phone for a new one.",
            "      (Powinieneś wymienić swój stary telefon na jakiś nowy.)",
            "",
            "  4. przepinać",
            "",
            "swap",
            "switch",
            "[czasownik]",
            "  1. zamieniać (się), wymieniać (się)",
            "",
            "      I want to switch places with you.",
            "      (Chcę się z tobą zamienić miejscami.)",
            "",
            "turnout",
            "switch",
            "set of points",
            "[rzeczownik]",
            "  1. rozjazd kolejowy",
            "",
            "      The train stopped at a switch.",
            "      (Pociąg zatrzymał się na rozjeździe kolejowym.)",
            "",
            "      The train turned right at the turnout.",
            "      (Pociąg skręcił w prawo na rozjeździe.)",
        ]
