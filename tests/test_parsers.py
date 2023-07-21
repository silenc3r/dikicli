import logging
import os
import tempfile
import shutil

import pytest

from dikicli.parsers import (
    _lookup_online,
    parse_en_pl,
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


@pytest.mark.vcr()
class TestEnPlParser:
    def test_parse_apple(self):
        html_dump = _lookup_online("apple")
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
        html_dump = _lookup_online("weight")
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
        html_dump = _lookup_online("abandon")
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
        html_dump = _lookup_online("switch")
        result = parse_en_pl(html_dump)
        result == [
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
        html_dump = _lookup_online("pet")
        result = parse_en_pl(html_dump)
        result == [
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
        html_dump = _lookup_online("snitch")
        result = parse_en_pl(html_dump)
        result == [
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
        html_dump = _lookup_online("guest")
        result = parse_en_pl(html_dump)
        result == [
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
        html_dump = _lookup_online("sad")
        result = parse_en_pl(html_dump)
        result == [
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
        html_dump = _lookup_online("vying")
        result = parse_en_pl(html_dump)
        result == [
            Entity(val="vying"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="współzawodniczenie"),
            Entity(val="vie"),
            Entity(val="vie for"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="współzawodniczyć, rywalizować"),
        ]

    def test_parse_hodgepodge(self):
        html_dump = _lookup_online("hodgepodge")
        result = parse_en_pl(html_dump)
        result == [
            Entity(val="hotch-potch"),
            Entity(val="hotchpotch"),
            Entity(val="hodge-podge"),
            Entity(val="hodgepodge"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="mieszanina, galimatias, miszmasz, groch z kapustą"),
        ]

    def test_parse_would(self):
        html_dump = _lookup_online("would")
        result = parse_en_pl(html_dump)
        result == [
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
            Meaning(val="(czasownik modalny używany do zapropowania komuśczegoś)"),
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
        html_dump = _lookup_online("tumult")
        result = parse_en_pl(html_dump)
        result == [
            Entity(val="tumult"),
            PartOfSpeech(val="rzeczownik"),
            Meaning(val="hałas, zgiełk, wrzawa"),
            PartOfSpeech(val="czasownik"),
            Meaning(val="niepokój, wzburzenie (wewnętrzne)"),
        ]

    def test_parse_subordinate(self):
        html_dump = _lookup_online("subordinate")
        result = parse_en_pl(html_dump)
        result == [
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

    def test_parse_non_existing_word(self):
        html_dump = _lookup_online("yyyy")
        result = parse_en_pl(html_dump)
        assert result == [
            Info(val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.")
        ]

    def test_parse_typo_eblem(self):
        html_dump = _lookup_online("eblem")
        result = parse_en_pl(html_dump)
        assert result == [
            Info(
                val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: emblem"
            )
        ]

    def test_parse_typo_wose(self):
        html_dump = _lookup_online("wose")
        result = parse_en_pl(html_dump)
        assert result == [
            Info(
                val="Nie znaleziono dokładnego tłumaczenia wpisanej frazy.\nCzy chodziło ci o: wise, whose, worse, dose, woke"
            )
        ]
