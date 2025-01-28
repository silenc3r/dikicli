import logging
import os
import tempfile
import shutil

import pytest

from dikicli.core import lookup_online
from dikicli.core import ContentNotFound
from dikicli.parsers import (
    parse_en_pl,
    parse_pl_en,
    parse_cached,
    parse_not_found,
    generate_word_page,
    Entity,
    Meaning,
    Variation,
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


@pytest.mark.vcr()
class TestEnPlParser:
    def test_parse_apple(self):
        html_dump = lookup_online("apple").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="apple"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="jabłko"),
            Sentence(val=["I'll just have an apple.", "(Po prostu zjem jabłko.)"]),
            Sentence(
                val=[
                    "Eating an apple every day will help keep you healthy.",
                    "(Jedzenie jednego jabłka dziennie pomoże ci pozostać zdrowym.)",
                ]
            ),
            Sentence(
                val=[
                    "I like green apples the most.",
                    "(Najbardziej lubię zielone jabłka.)",
                ]
            ),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="jabłkowy"),
            Sentence(val=["Mary likes apple juice.", "(Mary lubi sok jabłkowy.)"]),
            Sentence(
                val=[
                    "He ate the whole jar of apple mousse.",
                    "(On zjadł cały słoik musu jabłkowego.)",
                ]
            ),
            Sentence(
                val=[
                    "She drinks apple juice in the morning.",
                    "(Ona pije sok jabłkowy rano.)",
                ]
            ),
            Entity(val="Apple"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="Apple (firma komputerowa)"),
            Sentence(
                val=[
                    "Steve Jobs was one of the co-founders of Apple.",
                    "(Steve Jobs był jednym ze współzałożycieli Apple'a.)",
                ]
            ),
            Sentence(
                val=["I bought an Apple computer.", "(Kupiłem komputer firmy Apple.)"]
            ),
        ]

    def test_parse_weight(self):
        html_dump = lookup_online("weight").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="weight"),
            Entity(val="Wt"),
            Entity(val="wt."),
            Entity(val="wt"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="waga, ciężar (miara tego, ile coś waży)"),
            Sentence(
                val=[
                    "These sweets are sold by weight.",
                    "(Te cukierki są sprzedawane na wagę.)",
                ]
            ),
            Sentence(
                val=[
                    "What is the weight of this cheese? I want only 40 grams.",
                    "(Jaka jest waga tego sera? Chcę tylko 40 gram.)",
                ]
            ),
            Meaning(val="waga (człowieka)"),
            Sentence(
                val=[
                    "What is your height and weight?",
                    "(Jaki jest twój wzrost i waga?)",
                ]
            ),
            Sentence(
                val=[
                    "Her weight was dangerously low.",
                    "(Jej waga była niebezpiecznie niska.)",
                ]
            ),
            Meaning(val="ciężar (bycie ciężkim)"),
            Sentence(
                val=[
                    "My knees buckled under the weight.",
                    "(Kolana ugięły mi się pod wpływem ciężaru.)",
                ]
            ),
            Meaning(val="ciężar (coś ciężkiego)"),
            Sentence(
                val=[
                    "She won't be able to lift these weights herself.",
                    "(Ona nie będzie w stanie unieść sama tych ciężarów.)",
                ]
            ),
            Sentence(
                val=[
                    "These bags are such a weight, let me help you.",
                    "(Te torby to taki ciężar, pozwól, że ci pomogę.)",
                ]
            ),
            Meaning(val="obciążenie, zmartwienie, ciężar"),
            Sentence(
                val=[
                    "Raising a child is a huge weight for inexperienced people.",
                    "(Wychowywanie dziecka jest dużym obciążeniem dla niedoświadczonych osób.)",
                ]
            ),
            Sentence(
                val=[
                    "Her son causes her a lot of weight.",
                    "(Jej syn przysparza jej wiele zmartwień.)",
                ]
            ),
            Meaning(val="waga, znaczenie, ranga"),
            Sentence(
                val=[
                    "I didn't realise weight of the meeting.",
                    "(Nie zdawałem sobie sprawy z wagi tego spotkania.)",
                ]
            ),
            Sentence(
                val=[
                    "She attaches too much weight to petty problems.",
                    "(Ona przywiązuje zbyt dużo wagi do błahych problemów.)",
                ]
            ),
            Meaning(val="duża ilość (czegoś)"),
            Sentence(
                val=[
                    "I have a weight of apples in my garden.",
                    "(Mam dużą ilość jabłek w moim ogrodzie.)",
                ]
            ),
            Sentence(
                val=[
                    "My mother bought a weight of food because the shops are closed tomorrow.",
                    "(Moja mama kupiła dużą ilość jedzenia, bo jutro sklepy są zamknięte.)",
                ]
            ),
            Meaning(val="odważnik, ciężarek"),
            Sentence(
                val=[
                    "This weight is too heavy for me, I can't lift it.",
                    "(Ten odważnik jest dla mnie za ciężki, nie mogę go unieść.)",
                ]
            ),
            Sentence(
                val=[
                    "I do all exercises with weights - it helps me shape my body.",
                    "(Robię wszystkie ćwiczenia z ciężarkami - to pomaga mi wymodelować ciało.)",
                ]
            ),
            Meaning(val="ciężar, ciężarek, obciążnik (używany do ćwiczeń)"),
            Sentence(
                val=[
                    "Lifting weights can be a good exercise for building muscles.",
                    "(Podnoszenie ciężarów może być dobrym ćwiczeniem na budowę mięśni.)",
                ]
            ),
            Sentence(val=["A weight fell on my foot.", "(Ciężarek spadł mi na nogę.)"]),
            PartOfSpeech(val="czasownik"),
            Meaning(val="przemawiać, przeważać"),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="wagowy"),
            Entity(val="weight"),
            Entity(val="weight down"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="obciążać (np. sieć rybacką, łódź)"),
            Sentence(
                val=[
                    "We can't take this box, it will weight our boat too much.",
                    "(Nie możemy zabrać tego pudła, za bardzo obciąży naszą łódź.)",
                ]
            ),
            Sentence(
                val=[
                    "Too many passengers may weight the ship too much.",
                    "(Zbyt wielu pasażerów może za bardzo obciążyć statek.)",
                ]
            ),
        ]

    def test_parse_abandon(self):
        html_dump = lookup_online("abandon").html
        result1 = parse_en_pl(html_dump)
        assert result1 == [
            Entity(val="abandon"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="porzucać, opuszczać"),
            Sentence(
                val=[
                    "When Jack abandoned his family, the police went looking for him.",
                    "(Kiedy Jack porzucił swoją rodzinę, policja zaczęła go szukać.)",
                ]
            ),
            Sentence(
                val=[
                    "She had to abandon her idea of going to college because she was too poor.",
                    "(Ona musiała porzucić swój pomysł pójścia do szkoły wyższej, bo była zbyt biedna.)",
                ]
            ),
            Sentence(
                val=[
                    "Her grandparents abandoned Poland in the 1950s.",
                    "(Jej dziadkowie opuścili Polskę w latach 50.)",
                ]
            ),
            Sentence(
                val=[
                    "All young people abandoned this city.",
                    "(Wszyscy młodzi ludzie opuścili to miasto.)",
                ]
            ),
            Meaning(val="porzucać (kogoś lub coś)"),
            Sentence(
                val=[
                    "He abandoned his wife and children.",
                    "(On porzucił swoją żonę i dzieci.)",
                ]
            ),
            Sentence(
                val=[
                    "She abandoned the bad habit of smoking.",
                    "(Ona porzuciła zły nawyk palenia papierosów.)",
                ]
            ),
            Sentence(
                val=[
                    "A doe abandoned her babies to save her own life.",
                    "(Łania porzuciła swoje młode, aby ratować swoje własne życie.)",
                ]
            ),
            Meaning(
                val="rezygnować, zaniechać (przestać coś robić z powodu problemów)"
            ),
            Sentence(
                val=[
                    "I abandoned swimming after the accident.",
                    "(Po wypadku zrezygnowałem z pływania.)",
                ]
            ),
            Sentence(
                val=[
                    "My brother abandoned his studies after he failed an exam.",
                    "(Mój brat zrezygnował ze studiów po tym, jak nie zdał egzaminu.)",
                ]
            ),
            Sentence(
                val=[
                    "He abandoned his job after two weeks.",
                    "(On zrezygnował z pracy po dwóch tygodniach.)",
                ]
            ),
            Sentence(
                val=[
                    "She abandoned dancing when she became a mother.",
                    "(Ona porzuciła taniec, kiedy została matką.)",
                ]
            ),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="pasja, zapamiętanie"),
            Sentence(val=["He beat her in abandon.", "(On bił ją w zapamiętaniu.)"]),
            Sentence(
                val=[
                    "She slapped her daughter with abandon.",
                    "(Ona spoliczkowała swoją córkę w pasji.)",
                ]
            ),
            Meaning(val="żywiołowość, zapał, brak powściągliwości"),
            Entity(val="abandon something to somebody"),
            PartOfSpeech(val="phrasal verb"),
            Meaning(val="zrzec się czegoś na rzecz kogoś, rzucić coś na pastwę kogoś"),
            Entity(val="abandon oneself to something"),
            PartOfSpeech(val="phrasal verb"),
            Meaning(val="oddawać się czemuś"),
        ]

    def test_parse_switch(self):
        html_dump = lookup_online("switch").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="switch"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(
                val="łącznik (napięcia), wyłącznik (sieciowy), kontakt (elektryczny)"
            ),
            Sentence(
                val=[
                    "We could use some light. Flip the switch on.",
                    "(Przydałoby nam się trochę światła. Naciśnij przełącznik.)",
                ]
            ),
            Sentence(
                val=[
                    "It's so dark that I can't even see the switch.",
                    "(Jest tak ciemno, że nawet nie widzę kontaktu.)",
                ]
            ),
            Sentence(
                val=[
                    "Don't touch the switch with wet hands.",
                    "(Nie dotykaj kontaktu mokrymi rękami.)",
                ]
            ),
            Meaning(
                val="zmiana (z czegoś na coś), przejście (np. z komunizmu na kapitalizm)"
            ),
            Sentence(
                val=[
                    "For those looking to make the switch, some research is in order.",
                    "(Wszyscy, którzy chcą dokonać zmiany, powinni najpierw przeprowadzić badania.)",
                ]
            ),
            Sentence(
                val=[
                    "That switch will be good for our country.",
                    "(Ta zmiana będzie dobra dla naszego kraju.)",
                ]
            ),
            Meaning(val="zwrotnica (kolejowa)"),
            Sentence(
                val=[
                    "Somebody has to pull the switch or we won't make it.",
                    "(Ktoś musi pociągnąć za zwrotnicę albo nie damy rady.)",
                ]
            ),
            Sentence(
                val=[
                    "The two trains crashed into each other at the switch.",
                    "(Dwa pociągi zderzyły się ze sobą na zwrotnicy.)",
                ]
            ),
            Meaning(val="rózga, witka"),
            Sentence(
                val=[
                    "My grandfather hit me with the switch because I was naughty.",
                    "(Mój dziadek uderzył mnie rózgą, bo byłem niegrzeczny.)",
                ]
            ),
            Sentence(
                val=[
                    "His parents used to hit him with a switch as a punishment.",
                    "(Jego rodzice bili go rózgą w ramach kary.)",
                ]
            ),
            PartOfSpeech(val="czasownik"),
            Meaning(val="przełączać (programy, stacje radiowe)"),
            Sentence(
                val=[
                    "He switched channels, hoping to find something more interesting.",
                    "(Przełączył kanał, próbując znaleźć coś bardziej interesującego.)",
                ]
            ),
            Sentence(
                val=[
                    "Stop switching radio stations, it's annoying!",
                    "(Przestań przełączać stacje radiowe, to denerwujące!)",
                ]
            ),
            Meaning(
                val="zmieniać (np. taktykę), przechodzić (z jednej strony na drugą), przerzucać (się na coś)"
            ),
            Sentence(
                val=[
                    "He had to switch sides, as the building he looked for was on the other side of the street.",
                    "(On musiał zmienić stronę, ponieważ budynek, którego szukał był po drugiej stronie ulicy.)",
                ]
            ),
            Sentence(
                val=[
                    "He switched to veganism when he started dating this girl.",
                    "(Przerzucił się na weganizm, kiedy zaczął spotykać się z tą dziewczyną.)",
                ]
            ),
            Meaning(
                val="zastępować (coś czymś), wymieniać (coś na coś), zmieniać (rzecz na inną)"
            ),
            Sentence(
                val=[
                    "He switched his BMW for a Jeep.",
                    "(On zamienił swoje BMW na Jeepa.)",
                ]
            ),
            Sentence(
                val=[
                    "You should switch your old phone for a new one.",
                    "(Powinieneś wymienić swój stary telefon na jakiś nowy.)",
                ]
            ),
            Meaning(val="przepinać"),
            Entity(val="swap"),
            Entity(val="switch"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="zamieniać (się), wymieniać (się)"),
            Sentence(
                val=[
                    "I want to switch places with you.",
                    "(Chcę się z tobą zamienić miejscami.)",
                ]
            ),
            Entity(val="turnout"),
            Entity(val="switch"),
            Entity(val="set of points"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="rozjazd kolejowy"),
            Sentence(
                val=[
                    "The train stopped at a switch.",
                    "(Pociąg zatrzymał się na rozjeździe kolejowym.)",
                ]
            ),
            Sentence(
                val=[
                    "The train turned right at the turnout.",
                    "(Pociąg skręcił w prawo na rozjeździe.)",
                ]
            ),
        ]

    def test_parse_pet(self):
        html_dump = lookup_online("pet").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="pet"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="zwierzątko domowe, zwierzę domowe"),
            Sentence(
                val=["Do you have any pets?", "(Czy masz jakieś zwierzęta domowe?)"]
            ),
            Sentence(
                val=[
                    "I feed my pet once a day.",
                    "(Karmię moje zwierzątko domowe raz dziennie.)",
                ]
            ),
            PartOfSpeech(val="wykrzyknik"),
            Meaning(
                val="kochanie, skarbie (sposób zwracania się do bliskiej osoby, zwłaszcza kobiety lub dziecka)"
            ),
            Sentence(
                val=["Would you pass the salt, pet?", "(Podasz mi sól, kochanie?)"]
            ),
            Sentence(
                val=["Good day to you, pet.", "(Życzę ci dobrego dnia, skarbie.)"]
            ),
            PartOfSpeech(val="czasownik"),
            Meaning(val="pieścić, głaskać (np. kota)"),
            Sentence(val=["I petted my cat.", "(Głaskałem mojego kota.)"]),
            Sentence(
                val=[
                    "How often do you pet your dog?",
                    "(Jak często głaskasz swojego psa?)",
                ]
            ),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="ulubiony, ukochany"),
            Sentence(
                val=[
                    "Matthew is my pet student.",
                    "(Matthew jest moim ulubionym uczniem.)",
                ]
            ),
            Sentence(
                val=[
                    "Animals is his pet subject.",
                    "(Zwierzęta to jego ulubiony temat.)",
                ]
            ),
            Entity(val="positron emission tomography"),
            Entity(val="PET"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="pozytonowa tomografia emisyjna, PET"),
            Entity(val="polyethylene terephthalate"),
            Entity(val="PET"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(
                val="politereftalan etylenowy (polimer używany przy produkcji butelek PET)"
            ),
            Entity(val="pentaerythritol tetranitrate"),
            Entity(val="PET"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(
                val="tetraazotan pentaerytrytolu, pentryt (organiczny związek chemiczny)"
            ),
        ]

    def test_parse_snitch(self):
        html_dump = lookup_online("snitch").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="snitch"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="donosiciel, kapuś, kabel"),
            Meaning(val="drobna kradzież"),
            Meaning(val="nochal, kinol, kichawa"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="donosić, kablować (na kogoś)"),
            Meaning(val="zwędzić (coś), buchnąć (coś)"),
        ]

    def test_parse_guest(self):
        html_dump = lookup_online("guest").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="guest"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="gość (np. w domu, w hotelu)"),
            Sentence(
                val=[
                    "I have guests coming over tonight.",
                    "(Dzisiaj wieczorem przychodzą do mnie goście.)",
                ]
            ),
            Sentence(
                val=["How many guests have you invited?", "(Ilu zaprosiłeś gości?)"]
            ),
            Sentence(
                val=[
                    "Guests are asked to leave their rooms by 11am.",
                    "(Goście proszeni są o opuszczenie pokoi przed 11 rano.)",
                ]
            ),
            Sentence(
                val=[
                    "How many guests do you want to invite to your party?",
                    "(Ilu gości chcesz zaprosić na swoje przyjęcie?)",
                ]
            ),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="gościnny (dla użytku gości)"),
            Sentence(
                val=[
                    "We have a guest house where you can sleep.",
                    "(Mamy domek gościnny, w którym możecie spać.)",
                ]
            ),
            Sentence(
                val=[
                    "You can sleep in the guest room.",
                    "(Możesz spać w pokoju gościnnym.)",
                ]
            ),
            Meaning(val="gościnny (goszczący gdzieś na chwilę, np. występ)"),
            Sentence(
                val=[
                    "This group is on guest performance.",
                    "(Ta grupa jest na występach gościnnych.)",
                ]
            ),
            Sentence(
                val=[
                    "He has a guest concert in Warsaw.",
                    "(On ma gościnny koncert w Warszawie.)",
                ]
            ),
            PartOfSpeech(val="czasownik"),
            Meaning(val="wystąpić gościnnie"),
            Sentence(
                val=[
                    "He guests on a TV program.",
                    "(On występuje gościnnie w programie telewizyjnym.)",
                ]
            ),
            Sentence(
                val=[
                    "Would you like to guest on our radio program?",
                    "(Chciałbyś wystąpić gościnnie w naszym programie radiowym?)",
                ]
            ),
            Entity(val="as somebody's guest"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="jako czyjś gość"),
            Entity(val="Be my guest."),
            Meaning(val="Czuj się jak u siebie w domu."),
            Meaning(
                val='Proszę bardzo., Nie krępuj się. (dosł. "Bądź moim gościem." - używane jako pozwolenie)'
            ),
        ]

    def test_parse_sad(self):
        html_dump = lookup_online("sad").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="sad"),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="smutny"),
            Sentence(
                val=[
                    "She's sad because she lost her favourite doll.",
                    "(Ona jest smutna, bo zgubiła swoją ulubioną lalkę.)",
                ]
            ),
            Sentence(
                val=[
                    "Don't be so sad, everything will be OK.",
                    "(Nie bądź taki smutny, wszystko będzie dobrze.)",
                ]
            ),
            Meaning(val="przykry, żałosny"),
            Sentence(val=["It was a sad accident.", "(To był przykry wypadek.)"]),
            Sentence(val=["It was a sad sight.", "(To był żałosny widok.)"]),
            Meaning(val="żałosny, godny pożałowania (np. pomysł)"),
            Sentence(
                val=[
                    "She came up with a sad idea.",
                    "(Ona wpadła na godny pożałowania pomysł.)",
                ]
            ),
            Entity(val="Software Architecture Document"),
            Entity(val="SAD"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="Dokument Architektury Oprogramowania (w informatyce)"),
            Entity(val="single administrative document"),
            Entity(val="SAD"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="jednolity dokument administracyjny"),
            Entity(val="single administration document"),
            Entity(val="SAD"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="ujednolicony dokument administracyjny"),
            Entity(val="seasonal affective disorder"),
            Entity(val="SAD"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="sezonowe zaburzenie afektywne"),
        ]

    def test_parse_vying(self):
        html_dump = lookup_online("vying").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="vying"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="współzawodniczenie"),
            Entity(val="vie"),
            Entity(val="vie for"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="współzawodniczyć, rywalizować"),
        ]

    def test_parse_hodgepodge(self):
        html_dump = lookup_online("hodgepodge").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="hotch-potch"),
            Entity(val="hotchpotch"),
            Entity(val="hodge-podge"),
            Entity(val="hodgepodge"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="mieszanina, galimatias, miszmasz, groch z kapustą"),
        ]

    def test_parse_would(self):
        html_dump = lookup_online("would").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="would"),
            PartOfSpeech(val="czasownik"),
            Meaning(
                val="(czasownik modalny używany do opisywania czyichś zamiarów w przeszłości)"
            ),
            Sentence(val=["He said he would come.", "(On powiedział, że przyjdzie.)"]),
            Sentence(
                val=[
                    "Mary told me she would help me.",
                    "(Mary mi powiedziała, że mi pomoże.)",
                ]
            ),
            Meaning(
                val="(czasownik modalny używany do mówienia o hipotetycznych sytuacjach w przyszłości)"
            ),
            Sentence(
                val=[
                    "I would be happy if she agreed to go out with me.",
                    "(Byłbym szczęśliwy, gdyby zgodziła się ze mną umówić.)",
                ]
            ),
            Sentence(
                val=[
                    "I would visit you if I had more free time.",
                    "(Odwiedziłbym cię, gdybym miał więcej wolnego czasu.)",
                ]
            ),
            Meaning(
                val="(czasownik modalny używany do mówienia o hipotetycznych sytuacjach z przeszłości)"
            ),
            Sentence(
                val=[
                    "I would have gone there, but I was too scared.",
                    "(Poszedłbym tam, ale byłem zbyt przerażony.)",
                ]
            ),
            Sentence(
                val=[
                    "I would have bought that flat if I had more money.",
                    "(Kupiłbym tamto mieszkanie, gdybym miał więcej pieniędzy.)",
                ]
            ),
            Meaning(
                val="(czasownik modalny używany do mówienia o czymś, co działo się często w przeszłości)"
            ),
            Sentence(
                val=[
                    "At the weekends they would meet up secretly.",
                    "(W czasie weekendów oni zwykli spotykać się potajemnie.)",
                ]
            ),
            Sentence(
                val=[
                    "He would play computer games every day when he was a child.",
                    "(On grał (zwykł grać) w gry komputerowe codziennie, kiedy był dzieckiem.)",
                ]
            ),
            Meaning(val="(czasownik modalny używany w grzecznych prośbach)"),
            Sentence(val=["Would you help me?", "(Pomógłbyś mi?)"]),
            Sentence(
                val=[
                    "Would you close the window? It is chilly in here.",
                    "(Czy zamknąłbyś okno? Chłodno tutaj.)",
                ]
            ),
            Meaning(val="(czasownik modalny używany do zapropowania komuś czegoś)"),
            Sentence(val=["Would you like a tea?", "(Masz ochotę na herbatę?)"]),
            Sentence(
                val=[
                    "Would you like to go to the cinema tomorrow?",
                    "(Chciałbyś pójść jutro do kina?)",
                ]
            ),
            Meaning(val="(czasownik modalny używany do wyrażenia chęci na coś)"),
            Sentence(
                val=["I would like to meet you.", "(Chciałbym się z tobą spotkać.)"]
            ),
            Sentence(
                val=[
                    "She would like to watch a film.",
                    "(Ona chciałaby obejrzeć film.)",
                ]
            ),
            Meaning(val="(czasownik modalny używany do wyrażania lub pytania o radę)"),
            Sentence(
                val=[
                    "What would you do, if you were me?",
                    "(Co byś zrobił na moim miejscu?)",
                ]
            ),
            Sentence(val=["Which shirt would you buy?", "(Którą koszulę byś kupił?)"]),
            Meaning(
                val="(czasownik modalny używany do mówienia o typowym dla kogoś zachowaniu)"
            ),
            Sentence(
                val=[
                    "He would go and spoil the party!",
                    "(On by tylko poszedł i zepsuł imprezę!)",
                ]
            ),
            Sentence(
                val=[
                    "I hate going out with her, she would always talk about herself.",
                    "(Nie cierpię z nią wychodzić, ona by tylko gadała o sobie.)",
                ]
            ),
            Entity(val="will"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="będzie (używane do tworzenia form czasu przyszłego)"),
            Sentence(
                val=[
                    "I hope it will not rain tomorrow!",
                    "(Mam nadzieję, że jutro nie będzie padać!)",
                ]
            ),
            Sentence(
                val=["Our party will be great!", "(Nasza impreza będzie świetna!)"]
            ),
            Sentence(val=["It will be sunny tomorrow.", "(Jutro będzie słonecznie.)"]),
            Sentence(val=["Who will be at the party?", "(Kto będzie na przyjęciu?)"]),
            Sentence(
                val=[
                    "We will visit our friends next week.",
                    "(Odwiedzimy naszych przyjaciół w przyszłym tygodniu.)",
                ]
            ),
            Meaning(
                val="może (używane do powiedzenia, że ktoś jest gotowy, aby coś zrobić)"
            ),
            Sentence(
                val=["He will meet you now.", "(On może się teraz z tobą spotkać.)"]
            ),
            Sentence(
                val=[
                    "Mr Smith will see you now.",
                    "(Pan Smith może się teraz z tobą zobaczyć.)",
                ]
            ),
            Sentence(val=["Tom will go there with you.", "(Tom z tobą tam pójdzie.)"]),
            Sentence(
                val=["I'll come here in a few minutes.", "(Przyjdę tu za kilka minut.)"]
            ),
            Meaning(val="czy (ktoś coś zrobi, używane do tworzenia próśb)"),
            Sentence(val=["Will you help me?", "(Czy mi pomożesz?)"]),
            Sentence(
                val=[
                    "Will you buy me this doll, mommy?",
                    "(Mamusiu, kupisz mi tę lalkę?)",
                ]
            ),
            Sentence(val=["Who will go there with me?", "(Kto tam ze mną pójdzie?)"]),
            Sentence(
                val=[
                    "Will you go with me to the party this Saturday?",
                    "(Czy pójdziesz ze mną na imprezę w tę sobotę?)",
                ]
            ),
            Meaning(
                val="będzie (do wyrażania tego, co jest zawsze prawdziwe w danej sytuacji)"
            ),
            Sentence(
                val=[
                    "If you don't eat now, you will be hungry.",
                    "(Jeżeli teraz nie zjesz, będziesz głodny.)",
                ]
            ),
            Sentence(
                val=[
                    "If you study, you will get good grades.",
                    "(Jeżeli będziesz się uczyć, dostaniesz dobre oceny.)",
                ]
            ),
            Meaning(val="może, będzie (do wyrażenia jakiejś możliwości)"),
            Sentence(val=["I think it will rain.", "(Myślę, że będzie padać.)"]),
            Sentence(
                val=["He will come here tomorrow.", "(On może tu jutro przyjdzie.)"]
            ),
            Meaning(val="używane, by wyrazić przekonanie, że coś jest prawdziwe"),
            Sentence(
                val=[
                    "That will be my son coming home now.",
                    "(To mój syn właśnie przyszedł do domu.)",
                ]
            ),
            Sentence(
                val=[
                    "That will be the branch tapping the window.",
                    "(To gałąź stukająca w okno.)",
                ]
            ),
            Meaning(val="bądź, bądźcie (używane w dawaniu rozkazów)"),
            Sentence(
                val=["You will be silent and polite.", "(Bądźcie cicho i grzeczni.)"]
            ),
            Meaning(
                val="ciągle robić (używane do określenia czyichś denerwujących nawyków)"
            ),
            Sentence(
                val=[
                    "Jenny will keep knocking on the table.",
                    "(Jenny ciągle uderza palcami o stół.)",
                ]
            ),
            Meaning(val="pragnąć, zmuszać"),
            Sentence(
                val=["I'm willing him to visit us.", "(Pragnę, by on nas odwiedził.)"]
            ),
            Sentence(
                val=["He willed us to do it.", "(On zmusił nas do zrobienia tego.)"]
            ),
            Meaning(val="zapisywać w testamencie"),
            Sentence(
                val=[
                    "He promised to will me his car.",
                    "(On obiecał zapisać mi w testamencie swój samochód.)",
                ]
            ),
            Sentence(
                val=[
                    "My grandpa willed all his money to me.",
                    "(Mój dziadek zapisał mi w testamencie wszystkie swoje pieniądze.)",
                ]
            ),
            Meaning(val="chcieć"),
            Sentence(
                val=[
                    "I will help you because I love you.",
                    "(Chcę ci pomóc, ponieważ cię kocham.)",
                ]
            ),
            Sentence(val=["He won't see me.", "(On nie chce mnie widzieć.)"]),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="wola, determinacja"),
            Sentence(
                val=[
                    "All you need to succeed is good will.",
                    "(Wszystko czego potrzebujesz, by odnieść sukces to dobra wola.)",
                ]
            ),
            Sentence(
                val=[
                    "I will do nothing against my parents will.",
                    "(Nie zrobię nic wbrew woli rodziców.)",
                ]
            ),
            Sentence(
                val=[
                    "My strong will led me to this success.",
                    "(Moja silna wola doprowadziła mnie do tego sukcesu.)",
                ]
            ),
            Entity(val="have to"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="musieć"),
            Sentence(val=["I have to study.", "(Muszę się uczyć.)"]),
            Sentence(
                val=[
                    "My mother told me that I have to do the dishes.",
                    "(Moja mama powiedziała mi, że muszę umyć naczynia.)",
                ]
            ),
            Sentence(
                val=[
                    "He doesn't have to go to the dentist.",
                    "(On nie musi iść do dentysty.)",
                ]
            ),
            Sentence(val=["We don't have to fight.", "(Nie musimy walczyć.)"]),
            Entity(val="would you"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="czy mógłbyś (w grzecznych prośbach i propozycjach)"),
            Sentence(
                val=[
                    "Would you mind opening the window for me, please?",
                    "(Czy mógłbyś otworzyć dla mnie okno?)",
                ]
            ),
            Entity(val="have"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="mieć, posiadać"),
            Sentence(
                val=[
                    "I have two brothers and a sister.",
                    "(Mam dwóch braci i siostrę.)",
                ]
            ),
            Sentence(
                val=["Have you got a camera?", "(Czy masz aparat fotograficzny?)"]
            ),
            Sentence(
                val=[
                    "That's all I've got to say.",
                    "(To wszystko, co mam do powiedzenia.)",
                ]
            ),
            Sentence(val=["Do you have any money?", "(Czy masz jakieś pieniądze?)"]),
            Sentence(val=["I have two boats.", "(Posiadam dwie łodzie.)"]),
            Sentence(
                val=["My parents have a big house.", "(Moi rodzice mają duży dom.)"]
            ),
            Sentence(val=["Do you have money?", "(Masz przy sobie pieniądze?)"]),
            Sentence(
                val=[
                    "I don't have any money.",
                    "(Nie mam przy sobie żadnych pieniędzy.)",
                ]
            ),
            Meaning(val="mieć (np. jakąś cechę, właściwość)"),
            Sentence(
                val=["She has long, dark hair.", "(Ona ma długie, ciemne włosy.)"]
            ),
            Sentence(
                val=[
                    "My wife doesn't have patience.",
                    "(Moja żona nie ma cierpliwości.)",
                ]
            ),
            Sentence(
                val=["Do you have something to say?", "(Masz coś do powiedzenia?)"]
            ),
            Sentence(
                val=[
                    "I just wanted you to have something to remember us by.",
                    "(Chciałem, byś miała coś, co będzie ci o nas przypominać.)",
                ]
            ),
            Meaning(val="robić coś"),
            Meaning(val="jeść, pić"),
            Sentence(val=["Let's have dinner.", "(Zjedzmy obiad.)"]),
            Sentence(
                val=[
                    '"Why are you so weak?" "I didn\'t have breakfast."',
                    '("Czemu jesteś taki słaby?" "Nie jadłem śniadania.")',
                ]
            ),
            Meaning(val="doświadczać"),
            Sentence(
                val=[
                    "I had too many bad things in my life.",
                    "(Doświadczyłem zbyt wielu złych rzeczy w moim życiu.)",
                ]
            ),
            Meaning(val="czuć, odczuwać (np. różne uczucia)"),
            Meaning(val="cierpieć (np. na choroby)"),
            Sentence(val=["He has Lyme disease.", "(On cierpi na boreliozę.)"]),
            Sentence(val=["Jane has cancer.", "(Jane cierpi na raka.)"]),
            Meaning(val="otrzymywać, mieć"),
            Meaning(val="mieć (czas)"),
            Sentence(val=["Keep talking, I have time.", "(Mów dalej, mam czas.)"]),
            Sentence(
                val=[
                    "I don't have time for your jokes.",
                    "(Nie mam czasu na twoje żarty.)",
                ]
            ),
            Meaning(val="mieć (coś w określonej pozycji, w określonym stanie)"),
            Meaning(val="mieć (pracę, obowiązki)"),
            Sentence(
                val=["I have too many responsibilities.", "(Mam za dużo obowiązków.)"]
            ),
            Meaning(val="mieć dostępne (np. pokoje w hotelu)"),
            Sentence(
                val=["We have two rooms available.", "(Mamy dostępne dwa pokoje.)"]
            ),
            Meaning(val="trzymać (np. kogoś za ramię)"),
            Sentence(
                val=[
                    "He had my hand this whole time.",
                    "(On trzymał mnie za rękę cały ten czas.)",
                ]
            ),
            Meaning(val="mieć (gości)"),
            Sentence(
                val=[
                    "I can't go out tonight, I have guests.",
                    "(Nie mogę dziś wyjść, mam gości.)",
                ]
            ),
            Meaning(val="organizować (np. imprezę)"),
            Sentence(
                val=[
                    "I'm having a party this Saturday.",
                    "(Organizuję imprezę w tą sobotę.)",
                ]
            ),
            Meaning(val="skutkować, odnosić skutek"),
            Meaning(val="mieć (szansę, okazję)"),
            Sentence(
                val=[
                    "Do you think I have a chance with her?",
                    "(Czy myślisz, że mam u niej szansę?)",
                ]
            ),
            Meaning(val="rodzić (dziecko)"),
            Sentence(
                val=[
                    "The thought of having a baby was scary, but a little exciting too.",
                    "(Myśl o urodzeniu dziecka była straszna, ale też nieco ekscytująca.)",
                ]
            ),
            Meaning(val="sprawiać (żeby ktoś coś zrobił)"),
            Sentence(
                val=[
                    "I had him clean his room.",
                    "(Sprawiłem, by on posprzątał swój pokój.)",
                ]
            ),
            Meaning(val="przekonywać (kogoś)"),
            Meaning(val="mieć kogoś (gdy mamy na myśli, że ktoś uprawiał z kimś seks)"),
            Sentence(
                val=[
                    "I think she's had a lot of men.",
                    "(Myślę że ona miała wielu mężczyzn.)",
                ]
            ),
            Meaning(val="mieć, miewać (np. ból głowy)"),
            Sentence(val=["I have a headache.", "(Mam ból głowy.)"]),
            Sentence(val=["I have stomachaches.", "(Miewam bóle brzucha.)"]),
            Meaning(val="palić, zapalić (papierosa)"),
            Sentence(val=["I'm going to have a smoke.", "(Idę zapalić.)"]),
            Meaning(val="głosić, nieść (np. plotka)"),
            Entity(val="have something"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="częstować się czymś"),
            Sentence(
                val=[
                    "Have a sandwich, I made them for everyone.",
                    "(Poczęstuj się kanapką, zrobiłem je dla wszystkich.)",
                ]
            ),
            Sentence(
                val=[
                    "Have some of the pie, it is delicious.",
                    "(Poczęstuj się kawałkiem placka, jest przepyszny.)",
                ]
            ),
            Entity(val="I'd"),
            PartOfSpeech(val="czasownik"),
            Meaning(val='skrócona forma "I had"'),
            Meaning(val='skrócona forma "I would"'),
            Entity(val="they'd"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val='skrócona forma "they had"'),
            Sentence(
                val=[
                    "They'd known each other only during their two high school years.",
                    "(Oni znali się tylko przez dwa lata w liceum.)",
                ]
            ),
            Sentence(
                val=[
                    "At first they'd wanted just a place in the country.",
                    "(Na początku oni chceli tylko miejsca na wsi.)",
                ]
            ),
            Sentence(
                val=[
                    "They'd been looking for a way to move out of the city.",
                    "(Oni szukali sposobu, żeby wyprowadzić się z miasta.)",
                ]
            ),
            Meaning(val='skrócona forma "they would"'),
            Sentence(
                val=[
                    "They would be able to run again for the same office in 2005.",
                    "(Oni będą mogli ubiegać się o ten sam urząd w 2005 roku.)",
                ]
            ),
            Sentence(
                val=[
                    "They would be on their feet again in a day or so.",
                    "(Oni będą na nogach za około dzień.)",
                ]
            ),
            Sentence(
                val=[
                    "They would remember him for a long time to come.",
                    "(One zapamiętają go potem na długo.)",
                ]
            ),
            Entity(val="she'd"),
            Meaning(val='skrócona forma "she had"'),
            Sentence(
                val=[
                    "She didn't tell me where she'd been or with who.",
                    "(Ona nie powiedziała mi, gdzie była albo z kim.)",
                ]
            ),
            Sentence(
                val=[
                    "If she wanted to choose me, she'd have done it a long time ago.",
                    "(Jeśli ona chciałaby wybrać mnie, zrobiłaby to dawno temu.)",
                ]
            ),
            Meaning(val='skrócona forma "she would"'),
            Sentence(
                val=[
                    "She'd want to hear the news from you.",
                    "(Ona chciałaby usłyszeć wieści od ciebie.)",
                ]
            ),
            Sentence(
                val=[
                    "She'd be happy for you.",
                    "(Ona cieszyłaby się twoim szczęściem.)",
                ]
            ),
            Entity(val="he'd"),
            PartOfSpeech(val="czasownik"),
            Meaning(val='skrócona forma "he had"'),
            Meaning(val='skrócona forma "he would"'),
            Entity(val="we'd"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(
                val='skrócona forma "we had" (tylko, gdy "had" jest czasownikiem modalnym)'
            ),
            Sentence(
                val=[
                    "We'd better told him what happened.",
                    "(Lepiej żebyśmy mu powiedzieli, co się stało.)",
                ]
            ),
            Sentence(
                val=[
                    "We'd been thinking about this proposal and this is our opinion.",
                    "(Myśleliśmy o tej propozycji i to jest nasza opinia.)",
                ]
            ),
            Meaning(val='skrócona forma "we would"'),
            Sentence(
                val=[
                    "We'd like to see him do a better job.",
                    "(Chcielibyśmy, żeby on lepiej wykonywał swoją robotę.)",
                ]
            ),
            Sentence(
                val=[
                    "We'd like some starters and broth.",
                    "(Poprosimy jakieś przystawki i rosół.)",
                ]
            ),
            Entity(val="you'd"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val='skrócona forma "you had"'),
            Sentence(
                val=[
                    "You'd better not take his words seriously.",
                    "(Lepiej nie bierz jego słów na poważnie.)",
                ]
            ),
            Meaning(val='skrócona forma "you would"'),
            Sentence(
                val=[
                    "You'd have to get up very early in the morning.",
                    "(Musiałbyś wstać bardzo wcześnie rano.)",
                ]
            ),
            Entity(val="it'd"),
            Meaning(val='skrócona forma "it had"'),
            Meaning(val='skrócona forma "it would"'),
            Entity(val="-'d"),
            PartOfSpeech(val="suffiks"),
            Meaning(val="skrót od 'would'"),
            Sentence(
                val=["She'd be a good teacher.", "(Ona byłaby dobrą nauczycielką.)"]
            ),
            Meaning(val="skrót od 'had' (tylko gdy jest czasownikiem modalnym)"),
            Sentence(
                val=["I'd finished before you came.", "(Skończyłem zanim przyszłaś.)"]
            ),
            Sentence(
                val=[
                    "I had a lot of work last week.",
                    "(W ostatnim tygodniu miałem dużo pracy.)",
                ]
            ),
            Meaning(val="skrót od 'did'"),
            Entity(val="have had it"),
            PartOfSpeech(val="idiom"),
            Meaning(val="mieć czegoś po dziurki w nosie, mieć czegoś dosyć"),
            Sentence(val=["I've had it with these people.", "(Mam dosyć tych ludzi.)"]),
            Sentence(
                val=["That's it, I've had it with you!", "(Wystarczy, mam cię dosyć!)"]
            ),
            Meaning(val="być w złym stanie, nie działać dobrze"),
            Meaning(val="być wykończonym"),
            Meaning(val="być straconym (na przegranej pozycji)"),
            Entity(val="be had"),
            Meaning(val="zostać oszukanym, zostać wykiwanym"),
        ]

    def test_parse_tumult(self):
        html_dump = lookup_online("tumult").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="tumult"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="hałas, zgiełk, wrzawa"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="niepokój, wzburzenie (wewnętrzne)"),
        ]

    def test_parse_subordinate(self):
        html_dump = lookup_online("subordinate").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="subordinate"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="podporządkowywać, podporządkować (coś czemuś)"),
            Meaning(val="uzależniać (coś od czegoś)"),
            Entity(val="subordinate"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="podwładny (w organizacji)"),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="niższy rangą, niższy stopniem (np. w wojsku)"),
            Meaning(val="podporządkowany (komuś), zależny (od kogoś)"),
            Entity(val="be subordinate to somebody"),
            Meaning(val="podlegać komuś"),
        ]

    def test_parse_remarkable(self):
        html_dump = lookup_online("remarkable").html
        result = parse_en_pl(html_dump)
        assert result == [
            Entity(val="remarkable"),
            PartOfSpeech(val="przymiotnik"),
            Meaning(
                val="niezwykły, warty odnotowania, godny uwagi, wybitny, niesamowity, zdumiewający, wyjątkowy"
            ),
            Sentence(
                val=[
                    "A computer is a remarkable feat of technology.",
                    "(Komputer jest wartym odnotowania osiągnięciem technologii.)",
                ]
            ),
            Sentence(
                val=[
                    "Could you recommend a remarkable book?",
                    "(Czy mógłbyś polecić książkę godną uwagi?)",
                ]
            ),
            Sentence(
                val=["It's a remarkable monument!", "(To jest niezwykły pomnik!)"]
            ),
            Sentence(
                val=[
                    "He was a remarkable man who stood for peace in the world.",
                    "(On był niezwykłym człowiekiem, który opowiadał się za pokojem na świecie.)",
                ]
            ),
        ]


def translate_pl_en(word):
    html_dump = lookup_online(word).html
    result = parse_pl_en(html_dump)
    return result


@pytest.mark.vcr()
class TestPlEnParser:
    def test_pl_apple(self):
        result = translate_pl_en("apple")
        assert result == [
            Entity(val="Apple"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="Apple"),
            Variation(val="Apple (firma komputerowa)"),
            Sentence(
                val=[
                    "Steve Jobs was one of the co-founders of Apple.",
                    "(Steve Jobs był jednym ze współzałożycieli Apple'a.)",
                ]
            ),
            Sentence(
                val=["I bought an Apple computer.", "(Kupiłem komputer firmy Apple.)"]
            ),
        ]

    def test_pl_krowa(self):
        result = translate_pl_en("krowa")
        assert result == [
            Entity(val="krowa"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="cow"),
            Variation(val="krowa"),
            Sentence(val=["Cows give milk.", "(Krowy dają mleko.)"]),
            Sentence(val=["The field was full of cows.", "(Pole było pełne krów.)"]),
            Variation(val="krowa, stara krowa, babsko"),
            Sentence(
                val=[
                    "What is this cow doing in my house?",
                    "(Co to babsko robi w moim domu?)",
                ]
            ),
            Sentence(
                val=[
                    "Don't listen to this old cow, she's telling fairy tales.",
                    "(Nie słuchaj tej starej krowy, ona opowiada bajki.)",
                ]
            ),
            Sentence(
                val=[
                    "My new teacher is a cow, I don't like her.",
                    "(Moja nowa nauczycielka to stara krowa, nie lubię jej.)",
                ]
            ),
            Meaning(val="moo cow, moo-cow"),
            Variation(val="krowa (używane przez dzieci)"),
            Meaning(val="hawkie"),
            Meaning(val="milk kye"),
        ]

    def test_pl_wypić(self):
        result = translate_pl_en("wypić")
        assert result == [
            Entity(val="wypić"),
            PartOfSpeech(val="idiom"),
            Meaning(val="down something"),
            Variation(val="wyżłopać, wypić"),
            Sentence(
                val=["He downed the beer and belched.", "(On wyżłopał piwo i beknął.)"]
            ),
            Sentence(
                val=[
                    "After the race, she downed a whole bottle of water.",
                    "(Po wyścigu ona wypiła całą butelkę wody.)",
                ]
            ),
            PartOfSpeech(val="czasownik"),
            Meaning(val="neck"),
            Variation(val="wypić, obalić, golnąć, zrobić butelkę"),
            Sentence(
                val=[
                    "She necked a mug of beer in 15 seconds.",
                    "(Ona obaliła kufel piwa w 15 sekund.)",
                ]
            ),
            Sentence(
                val=[
                    "I can neck this glass of vodka.",
                    "(Mogę wypić ten kieliszek wódki.)",
                ]
            ),
            Meaning(val="partake, partake of something"),
            Variation(val="zjeść (porcję czegoś), wypić"),
            Sentence(
                val=[
                    "Would you like to partake of a glass of water?",
                    "(Masz ochotę wypić szklankę wody?)",
                ]
            ),
            Entity(val="wypić coś"),
            PartOfSpeech(val="phrasal verb"),
            Meaning(val="knock something back"),
            Variation(val="wypić coś, wychylić coś"),
            Entity(val="pić"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="drink"),
            Sentence(val=["What would you like to drink?", "(Co chciałbyś do picia?)"]),
            Sentence(
                val=["She drank a glass of water.", "(Ona wypiła szklankę wody.)"]
            ),
            Sentence(
                val=[
                    "Can I have something to drink?",
                    "(Czy mogę prosić coś do picia?)",
                ]
            ),
            Meaning(val="have"),
            Variation(val="jeść, pić"),
            Sentence(val=["Let's have dinner.", "(Zjedzmy obiad.)"]),
            Sentence(
                val=[
                    '"Why are you so weak?" "I didn\'t have breakfast."',
                    '("Czemu jesteś taki słaby?" "Nie jadłem śniadania.")',
                ]
            ),
            Entity(val="wypijać"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="consume"),
            Variation(val="zjadać, wypijać, spożywać, konsumować (np. jedzenie)"),
            Sentence(
                val=[
                    "You can't consume alcohol in public places.",
                    "(Nie możesz spożywać alkoholu w miejscach publicznych.)",
                ]
            ),
            Sentence(
                val=[
                    "I consume 2000 calories a day.",
                    "(Spożywam 2000 kalorii dziennie.)",
                ]
            ),
            Entity(val="wypicie"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="downing"),
            Variation(val="wyżłopanie, wypicie"),
            Meaning(val="partaking"),
            Variation(val="zjedzenie (porcji czegoś), wypicie"),
        ]

    def test_pl_kilogram(self):
        result = translate_pl_en("kilogram")
        assert result == [
            Entity(val="kilogram"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="kilogram, kilo, kilogramme, kg"),
            Sentence(
                val=["It weighs about 10 kilograms.", "(To waży około 10 kilogramów.)"]
            ),
        ]

    def test_pl_oszust(self):
        result = translate_pl_en("oszust")
        assert result == [
            Entity(val="oszust"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="fraud"),
            Variation(val="oszust, naciągacz"),
            Sentence(
                val=[
                    "You're not a lawyer, you're a fraud.",
                    "(Nie jesteś prawnikiem, jesteś oszustem.)",
                ]
            ),
            Sentence(
                val=[
                    "I invested in your business and you took my money. You're a fraud.",
                    "(Zainwestowałem w twój biznes, a ty wziąłeś moje pieniądze. Jesteś oszustem.)",
                ]
            ),
            Meaning(val="crook"),
            Sentence(
                val=[
                    "Most of these politicians are just a bunch of crooks.",
                    "(Większość z tych polityków to tylko banda oszustów.)",
                ]
            ),
            Sentence(
                val=[
                    "I was deceived by some crook who told me it was gold.",
                    "(Zostałem nabrany przez jakiegoś oszusta, który powiedział mi, że to było złoto.)",
                ]
            ),
            Meaning(val="cheat"),
            Variation(val="oszust, krętacz, szuler (np. w kartach)"),
            Sentence(
                val=[
                    "Jordan Belfort is a well-known American cheat.",
                    "(Jordan Belfort to dobrze znany amerykański krętacz.)",
                ]
            ),
            Sentence(
                val=[
                    "I don't want to play with him, he's a cheat.",
                    "(Nie chcę z nim grać, to oszust.)",
                ]
            ),
            Meaning(val="cheater"),
            Variation(val="oszust"),
            Sentence(val=["Her husband is a cheater.", "(Jej mąż jest oszustem.)"]),
            Sentence(
                val=[
                    "She called me a liar and a cheater.",
                    "(Ona nazwała mnie kłamcą i oszustem.)",
                ]
            ),
            Meaning(val="trickster, tricker"),
            Variation(val="oszust, naciągacz"),
            Meaning(val="fake"),
            Variation(val="fałszerz, oszust"),
            Sentence(
                val=[
                    "This man is a fake. Don't trust him.",
                    "(Ten facet jest oszustem. Nie ufaj mu.)",
                ]
            ),
            Sentence(
                val=[
                    "A fake is somebody who would use you to his own advantage.",
                    "(Oszustem jest ktoś, kto wykorzystałby cię na swoją własną korzyść.)",
                ]
            ),
            Meaning(val="fiddler"),
            Variation(val="kanciarz, oszust"),
            Meaning(
                val="con artist, con man, conman, rip-off artist, con merchant, scam artist"
            ),
            Variation(val="kanciarz, oszust"),
            Sentence(
                val=[
                    "This con artist has deceived a lot of people.",
                    "(Ten kanciarz oszukał wielu ludzi.)",
                ]
            ),
            Meaning(val="impostor, imposter"),
            Variation(val="impostor, oszust (podający się za kogoś innego), szalbierz"),
            Meaning(val="slicker"),
            Meaning(val="Hollywood"),
            Variation(val="kłamca, oszust"),
            Sentence(
                val=[
                    "Don't believe this Hollywood, he wants to steal from you!",
                    "(Nie wierz temu oszustowi, on chce cię okraść!)",
                ]
            ),
            Sentence(
                val=[
                    "My brother is such a Hollywood - don't believe a word he says.",
                    "(Mój brat jest takim kłamcą - nie wierz w żadne jego słowo.)",
                ]
            ),
            Meaning(val="crowder"),
            Meaning(val="swindler"),
            Variation(val="oszust, szachraj, kanciarz, szacher macher"),
            Meaning(val="fabricator"),
            Variation(val="fałszerz, oszust, łgarz"),
            Meaning(val="adventurer"),
            Variation(val="awanturnik, aferzysta, oszust"),
            Meaning(val="humbug"),
            Variation(val="oszust, szachraj"),
            Meaning(val="player"),
            Variation(val="manipulant, oszust, krętacz"),
            Sentence(
                val=[
                    "I wouldn't trust this player if I were you.",
                    "(Nie ufałbym temu krętaczowi na twoim miejscu.)",
                ]
            ),
            Sentence(
                val=[
                    "Don't believe him, he's a player - he must be cheating.",
                    "(Nie wierz mu, to manipulant - na pewno oszukuje.)",
                ]
            ),
            Sentence(
                val=[
                    "I know that he's a player but I'm watching his every move - he won't lie to me.",
                    "(Wiem, że to oszust, ale obserwuję każdy jego ruch - nie okłamie mnie.)",
                ]
            ),
            Meaning(val="phoney, phony"),
            Variation(val="pozer, oszust"),
            Meaning(val="racketeer"),
            Variation(val="gangster, szantażysta, oszust, grandziarz"),
            Meaning(val="deceiver"),
            Variation(val="oszust, kłamca, fałszywiec"),
            Meaning(val="faker"),
            Variation(val="oszust, fałszerz"),
            Meaning(val="victimiser, victimizer"),
            Variation(val="oszust, naciągacz"),
            Meaning(val="ringer"),
            Variation(
                val="oszust, profesjonalista udający amatora w grze (np. w bilard)"
            ),
            Meaning(val="imp"),
            Meaning(val="wyle"),
            Variation(val="oszust, kłamca, fałszywiec"),
            Meaning(val="fraudster"),
            Meaning(val="sharper"),
            Variation(val="oszust (karciany), szuler"),
            Meaning(val="scammer, scamster"),
            Variation(val="oszust, naciągacz, kanciarz"),
            Meaning(val="diddler"),
            Variation(val="oszust, krętacz, szuler"),
            Meaning(val="chouser"),
            Meaning(val="cozener"),
            Meaning(val="fleecer"),
            Variation(val="oszust, szachraj, kanciarz"),
            Meaning(val="flimflammer"),
            Variation(val="oszust, szachraj, kanciarz"),
            Meaning(val="gabber"),
            Variation(val="oszust, kłamca"),
            Meaning(val="hoodwinker"),
            Meaning(val="confidence trickster"),
            Variation(val="oszust, naciągacz"),
            Meaning(val="defrauder"),
            Variation(val="defraudant, oszust"),
            Meaning(val="snake oil salesman"),
            Variation(
                val='osoba świadomie sprzedająca podróbki lub fałszywy towar (np. "cudowne" leki), oszust'
            ),
            Meaning(val="chouse, chowse"),
            Meaning(val="chicaner"),
            Meaning(val="baffler"),
            Meaning(val="bunco artist"),
            Meaning(val="sandbagger"),
            Variation(val="oszust, krętacz"),
            Meaning(val="confidence man"),
            Meaning(val="double-crosser"),
            Meaning(val="bilker"),
            Variation(val="oszust, naciągacz"),
            Meaning(val="off artist"),
            Variation(val="oszust, naciągacz, kanciarz"),
            Meaning(val="chiseller, chiseler"),
            Variation(val="oszust, kanciarz"),
            Meaning(val="welsher, welcher"),
            Variation(val="oszust (uciekający z pieniędzmi)"),
            Meaning(val="four flusher"),
            Variation(val="oszust, krętacz"),
            Meaning(val="bunco thief"),
            Meaning(val="gypster"),
            Variation(val="kanciarz, oszust"),
            Meaning(val="mountebank"),
            Variation(val="szarlatan, oszust, hochsztapler"),
            Meaning(val="cogger"),
            Variation(val="oszust (np. w grze w kości)"),
            Meaning(val="falser"),
            Variation(val="oszust, kłamca, fałszywiec"),
            Meaning(val="faitour"),
            Variation(val="impostor, oszust (podający się za kogoś innego), szalbierz"),
            Meaning(val="chiseller"),
            Variation(val="oszust, kanciarz"),
            Meaning(val="burn artist"),
            Variation(val="oszust, kanciarz, naciągacz"),
            Meaning(val="magsman"),
            Variation(val="oszust, naciągacz"),
            Meaning(val="pseudo"),
            Variation(val="fałszywiec, oszust, udawacz"),
        ]

    def test_pl_auto(self):
        result = translate_pl_en("auto")
        assert result == [
            Entity(val="samochód osobowy, auto osobowe"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="car, auto, automobile"),
            Sentence(
                val=[
                    "He got struck by a car and is in hospital now.",
                    "(On został potrącony przez samochód i jest teraz w szpitalu.)",
                ]
            ),
            Sentence(
                val=[
                    "I think we should buy a second car.",
                    "(Myślę, że powinniśmy kupić drugi samochód.)",
                ]
            ),
            Sentence(
                val=[
                    "I wanted to buy this car but it was too expensive.",
                    "(Chciałem kupić ten samochód, ale był za drogi.)",
                ]
            ),
            Sentence(
                val=[
                    "I bought myself a brand new automobile.",
                    "(Kupiłem sobie zupełnie nowy samochód.)",
                ]
            ),
        ]

    def test_pl_droga(self):
        result = translate_pl_en("droga")
        assert result == [
            Entity(val="droga"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="road"),
            Variation(val="droga"),
            Sentence(val=["Which road do we take?", "(Którą drogą pojedziemy?)"]),
            Sentence(
                val=["He kept his eyes on the road.", "(On uważnie patrzył na drogę.)"]
            ),
            Sentence(
                val=[
                    "This road is in very bad condition.",
                    "(Ta droga jest w bardzo złym stanie.)",
                ]
            ),
            Variation(val="droga (przenośnie, np. droga do celu)"),
            Sentence(
                val=[
                    "The road to championship was a hard one.",
                    "(Droga do mistrzostwa była ciężka.)",
                ]
            ),
            Sentence(
                val=[
                    "My road to success wasn't easy but I did my best.",
                    "(Droga do sukcesu nie była łatwa, ale robiłem co mogłem.)",
                ]
            ),
            Meaning(val="path"),
            Variation(val="ścieżka (po której można gdzieś dotrzeć), droga"),
            Sentence(
                val=[
                    "They followed the path until they got to the river.",
                    "(Oni podążali wzdłuż ścieżki, aż dotarli do rzeki.)",
                ]
            ),
            Sentence(
                val=[
                    "He chose an interesting career path.",
                    "(On wybrał interesującą ścieżkę kariery.)",
                ]
            ),
            Sentence(
                val=["This is the path to victory!", "(To jest droga do zwycięstwa!)"]
            ),
            Meaning(val="way"),
            Variation(val="trasa, droga"),
            Sentence(
                val=[
                    "Could you tell me the way to the airport?",
                    "(Możesz mi wskazać drogę na lotnisko?)",
                ]
            ),
            Sentence(
                val=[
                    "They stopped for fuel on their way home.",
                    "(W drodze do domu zatrzymali się, żeby zatankować.)",
                ]
            ),
            Sentence(
                val=[
                    "The way to our new house was bumpy.",
                    "(Droga do naszego nowego domu była wyboista.)",
                ]
            ),
            Variation(val="droga, przejście (przestrzeń przed czymś)"),
            Sentence(val=["Get out of the way.", "(Zejdź z drogi.)"]),
            Sentence(
                val=[
                    "The way was too narrow to fit the piano.",
                    "(Przejście było zbyt wąskie, aby zmieścić pianino.)",
                ]
            ),
            Meaning(val="route"),
            Variation(val="trasa, droga"),
            Sentence(
                val=[
                    "Take Route 65 north and get off at exit 4A.",
                    "(Pojedź drogą numer 65 na północ i zjedź na wyjeździe numer 4A.)",
                ]
            ),
            Sentence(
                val=[
                    "As you travel, have her follow the route on the map.",
                    "(Jak będziecie jechać, niech ona śledzi trasę na mapie.)",
                ]
            ),
            Sentence(
                val=[
                    "What is the shortest route from here to the airport?",
                    "(Jaka jest najkrótsza droga stąd na lotnisko?)",
                ]
            ),
            Meaning(val="drive"),
            Variation(val="jazda, droga, podróż (samochodem)"),
            Sentence(
                val=["The drive home is easier.", "(Jazda do domu jest łatwiejsza.)"]
            ),
            Sentence(val=["This is a long drive.", "(To jest długa droga.)"]),
            Sentence(
                val=[
                    "We've got a long drive ahead of us.",
                    "(Mamy długą drogę przed sobą.)",
                ]
            ),
            Sentence(val=["It's a 90 mile drive.", "(To 90 mil drogi.)"]),
            Variation(val="droga (używane w nazwach dróg)"),
            Sentence(
                val=[
                    "Have your ever been to Rodeo Drive?",
                    "(Czy byłeś kiedyś na Rodeo Drive?)",
                ]
            ),
            Meaning(val="track"),
            Variation(val="ścieżka, droga"),
            Sentence(
                val=[
                    "Follow this track and you'll find the beach you're looking for.",
                    "(Podążaj tą drogą, a znajdziesz plażę, której szukasz.)",
                ]
            ),
            Sentence(
                val=[
                    "I saw a hare on a forest track.",
                    "(Zobaczyłem zająca na leśnej ścieżce.)",
                ]
            ),
            Variation(val="tor, droga (np. burzy, tajfunu)"),
            Sentence(
                val=[
                    "You can watch the track of the storm online.",
                    "(Możesz oglądać tor burzy w internecie.)",
                ]
            ),
            Sentence(
                val=[
                    "We have to analyze the track of the hurricane to be ready for it in the future.",
                    "(Musimy przeanalizować drogę huraganu, żeby w przyszłości być na niego gotowym.)",
                ]
            ),
            Meaning(val="channel"),
            Variation(val="kanał, droga (system, metoda uzyskiwania informacji, dóbr)"),
            Sentence(
                val=[
                    "There should be a direct channel of communication between the two offices.",
                    "(Pomiędzy tymi dwoma biurami powinien być bezpośredni kanał komunikacyjny.)",
                ]
            ),
            Sentence(
                val=[
                    "Please use the usual channel of contact.",
                    "(Proszę korzystać ze zwykłego kanału kontaktu.)",
                ]
            ),
            Variation(val="kanał, droga, sposób (np. wyrażania siebie)"),
            Sentence(
                val=[
                    "That was an unusual channel of expressing emotions.",
                    "(To był niezwykły sposób wyrażania emocji.)",
                ]
            ),
            Sentence(
                val=[
                    "He found a channel of expressing his inner feelings.",
                    "(On znalazł sposób na wyrażenie swoich wewnętrznych uczuć.)",
                ]
            ),
            Meaning(val="avenue"),
            Variation(val="droga (sposób osiągnięcia czegoś), możliwość"),
            Sentence(
                val=[
                    "This job was her avenue to success.",
                    "(Ta praca była dla niej drogą do sukcesu.)",
                ]
            ),
            Sentence(
                val=[
                    "My avenue of escape is through this door.",
                    "(Moja droga ucieczki wiedzie przez te drzwi.)",
                ]
            ),
            Meaning(val="pad"),
            Variation(val="droga, ścieżka"),
            Meaning(val="trackway"),
            Variation(val="ścieżka, droga"),
            Meaning(val="passway"),
            Meaning(val="marg"),
            Variation(val="ulica, droga (w adresach, zapożyczone z jęz. indyjskiego)"),
            Entity(val="drogi"),
            PartOfSpeech(val="przymiotnik"),
            Meaning(val="expensive"),
            Sentence(
                val=[
                    "This watch is too expensive for me.",
                    "(Ten zegarek jest dla mnie za drogi.)",
                ]
            ),
            Sentence(
                val=[
                    "She bought a very expensive dress.",
                    "(Ona kupiła bardzo drogą sukienkę.)",
                ]
            ),
            Sentence(
                val=[
                    "Living in the city is really expensive.",
                    "(Życie w mieście jest naprawdę drogie.)",
                ]
            ),
            Meaning(val="beloved"),
            Variation(val="ukochany, drogi"),
            Sentence(
                val=[
                    "My beloved wife died two years ago.",
                    "(Moja ukochana żona zmarła dwa lata temu.)",
                ]
            ),
            Sentence(
                val=[
                    "This beloved country is threatened.",
                    "(Ten ukochany kraj jest zagrożony.)",
                ]
            ),
            Sentence(
                val=[
                    "His beloved son studies at the university.",
                    "(Jego ukochany syn studiuje na uniwersytecie.)",
                ]
            ),
            Meaning(val="dear"),
            Variation(val="drogi, szanowny (używane w nagłówkach listów)"),
            Sentence(
                val=[
                    "Dear Sir or Madam, (at the beginning of a letter)",
                    "(Szanowni Państwo, (na początku listu))",
                ]
            ),
            Sentence(
                val=[
                    "Dear Kate, (at the beginning of a letter)",
                    "(Droga Kate, (na początku listu))",
                ]
            ),
            Variation(val="drogi (np. przyjaciel)"),
            Sentence(
                val=[
                    "My dear friend died last year.",
                    "(Mój drogi przyjaciel zmarł w zeszłym roku.)",
                ]
            ),
            Sentence(
                val=[
                    "His brother was very dear to him.",
                    "(Jego brat był mu bardzo drogi.)",
                ]
            ),
            Sentence(
                val=[
                    "It's good to be back in dear old Warsaw.",
                    "(Dobrze być z powrotem w kochanej starej Warszawie.)",
                ]
            ),
            Variation(val="drogi, kosztowny"),
            Sentence(
                val=[
                    "Cigarettes in the European Union are dearer than in the countries that are not the member states.",
                    "(Papierosy w Unii Europejskiej są droższe niż w krajach niebędących krajami członkowskimi.)",
                ]
            ),
            Sentence(
                val=[
                    "I thought he was a scrooge, but he bought the dearest TV.",
                    "(Myślałem, że on jest skąpy, ale kupił najdroższy telewizor.)",
                ]
            ),
            Meaning(val="lush"),
            Variation(val="drogi, luksusowy, bogaty"),
            Meaning(val="darling"),
            Variation(val="drogi, najukochańszy, najdroższy"),
            Sentence(
                val=[
                    "She's always been my darling sister.",
                    "(Ona zawsze była moją najukochańszą siostrą.)",
                ]
            ),
            Sentence(
                val=[
                    "My darling wife is an angel.",
                    "(Moja najukochańsza żona jest aniołem.)",
                ]
            ),
            Meaning(val="valued"),
            Variation(val="drogi, ceniony, cenny"),
            Meaning(val="pricey, pricy"),
            Variation(val="drogi, kosztowny"),
            Meaning(val="high-priced"),
            Meaning(val="high-cost"),
            Variation(val="drogi, kosztowny"),
            Meaning(val="cher"),
            Variation(
                val="drogi, ukochany, kochany (używane do mężczyzny lub chłopaka)"
            ),
            Meaning(val="spendy"),
            Variation(val="drogi, kosztowny"),
            Meaning(val="cost-prohibitive"),
            Variation(val="kosztowny, drogi"),
            Meaning(val="high-street"),
            Variation(val="elegancki, drogi, prestiżowy"),
            Meaning(val="expenseful"),
            Meaning(val="spenny"),
            Meaning(val="exy"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="roads"),
            Sentence(
                val=[
                    "The roads in Poland are in bad shape.",
                    "(Drogi w Polsce są w złym stanie.)",
                ]
            ),
            Sentence(
                val=[
                    "There are far too many accidents on European roads.",
                    "(Na europejskich drogach dochodzi do zbyt wielu wypadków.)",
                ]
            ),
            Meaning(val="tract"),
            Variation(val="przewód (pokarmowy), drogi (oddechowe), układ (rozrodczy)"),
            Sentence(
                val=[
                    "Nancy has a urinary tract infection.",
                    "(Nancy ma zakażenie dróg moczowych.)",
                ]
            ),
            Sentence(
                val=[
                    "Something seems to be stuck in the dog's food tract.",
                    "(Wygląda na to, że coś utknęło w przewodzie pokarmowym psa.)",
                ]
            ),
            Sentence(
                val=[
                    "We need to clear his air tract.",
                    "(Musimy udrożnić jego drogi oddechowe.)",
                ]
            ),
            Meaning(val="swankiness"),
            Variation(val="drogi, luksusowy, stylowy"),
            Meaning(val="trackside"),
            Variation(val="obszar wzdłuż ścieżki, drogi"),
            Variation(val="obszar wzdłuż toru, drogi"),
            Meaning(val="dautie, dawtie"),
            Variation(val="drogi, najukochańszy, najdroższy"),
            Entity(val="swoją drogą"),
            PartOfSpeech(val="przysłówek"),
            Meaning(val="by the way, BTW, bee-tee-dubs"),
            Variation(
                val="jakby co, swoją drogą, przy okazji, nawiasem mówiąc, à propos"
            ),
            Sentence(
                val=[
                    "By the way, what are you searching for?",
                    "(Swoją drogą, czego szukasz?)",
                ]
            ),
            Sentence(
                val=[
                    "How are you doing now, by the way?",
                    "(Jak sobie teraz radzisz, swoją drogą?)",
                ]
            ),
            Sentence(
                val=[
                    "By the way, I must buy some shoes.",
                    "(Swoją drogą, muszę kupić jakieś buty.)",
                ]
            ),
            Entity(val="mój drogi"),
            Meaning(val="my dear fellow"),
            Variation(val="mój drogi, mój przyjacielu"),
        ]


@pytest.mark.vcr
class TestNotFoundParser:
    def test_parse_non_existing_word(self):
        html_dump = lookup_online("yyyy")
        assert isinstance(html_dump, ContentNotFound)
        result = parse_not_found(html_dump.html)
        assert result == [
            Info(val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.")
        ]

    def test_parse_typo_eblem(self):
        html_dump = lookup_online("eblem")
        assert isinstance(html_dump, ContentNotFound)
        result = parse_not_found(html_dump.html)
        assert result == [
            Info(
                val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: emblem"
            )
        ]

    def test_parse_typo_wose(self):
        html_dump = lookup_online("wose")
        assert isinstance(html_dump, ContentNotFound)
        result = parse_not_found(html_dump.html)
        assert result == [
            Info(
                val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: wise, whose, worse, dose, woke"
            )
        ]


@pytest.mark.vcr
class TestCachedParser:
    def test_guest(self):
        html_dump = lookup_online("guest").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_switch(self):
        html_dump = lookup_online("switch").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_weight(self):
        html_dump = lookup_online("weight").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_would(self):
        html_dump = lookup_online("would").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_subordinate(self):
        html_dump = lookup_online("subordinate").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_apple(self):
        html_dump = lookup_online("apple").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_sad(self):
        html_dump = lookup_online("sad").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_pet(self):
        html_dump = lookup_online("pet").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_abandon(self):
        html_dump = lookup_online("abandon").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations

    def test_tumult(self):
        html_dump = lookup_online("tumult").html
        translations = parse_en_pl(html_dump)
        cached_html = generate_word_page(translations)
        cached_translations = parse_cached(cached_html)
        assert translations == cached_translations
