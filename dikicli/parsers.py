from collections import namedtuple
from html.parser import HTMLParser
from urllib.request import Request
from urllib.request import urlopen

import os
import sys


def _lookup_online(word: str) -> str:
    URL = "https://www.diki.pl/" + word
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; "
            "Trident/7.0;  rv:11.0) like Gecko"
        )
    }

    request = Request(URL, headers=HEADERS)
    response = urlopen(request)
    content = response.read().decode("utf-8")
    return content


Entity = namedtuple("Entity", "val")
PartOfSpeech = namedtuple("PartOfSpeech", "val")
Meaning = namedtuple("Meaning", "val")
Sentence = namedtuple("Sentence", "val")


class EnPlParser(HTMLParser):
    def set_all_false(self):
        self._en_pl = False
        self._left_column = False
        self._read_header = False
        self._read_part_of_speech = False
        self._read_meaning = False
        self._read_sentence = False
        self._read_sentence_translation = False

    def reset(self):
        super().reset()
        self.set_all_false()
        self.result = []
        self.sentences = []
        self.meanings = []
        self.header = []

    def parse(self, content):
        "Entry point. The only function that should be called."
        self.reset()
        self.feed(content)
        return self.result

    def handle_starttag(self, tag, attrs):
        if self.is_en_pl(tag, attrs):
            self._en_pl = True
            return
        if self.is_left_column(tag, attrs):
            self._left_column = True
            return

        if self.leaving_left_column(tag, attrs):
            self.set_all_false()
            return

        if not (self._left_column and self._en_pl):
            return

        if self.is_end_of_header_line(tag, attrs):
            self._read_meaning = False
            if len(self.header) != 0:
                hline = "".join(self.header).strip().rstrip(",").strip()
                self.result.append(Entity(hline))
                self.header = []
        elif self.is_end_of_meaning(tag, attrs):
            self._read_meaning = False
            if len(self.meanings) != 0:
                m = "".join(self.meanings).rstrip()
                self.result.append(Meaning(m))
                self.meanings = []
        elif self.is_expecting_header(tag, attrs):
            self._read_header = True
        elif self.is_expecting_sentence_translation(tag, attrs):
            self._read_sentence_translation = True
        elif self.is_expecting_example_sentence(tag, attrs):
            self._read_sentence = True
        elif self.is_expecting_meaning(tag, attrs):
            self._read_meaning = True
        elif self.is_expecting_part_of_speech(tag, attrs):
            self._read_part_of_speech = True

    def handle_endtag(self, tag):
        if not (self._en_pl and self._left_column):
            return

        if tag == "div":
            if len(self.sentences) != 0:
                self.result.append(Sentence(self.sentences))
                self.sentences = []

        if tag == "h1":
            self._read_header = False
            # self._read_meaning = False  # probably not needed
            if len(self.header) != 0:
                raise Exception("Couldn't find an end of a header line", self.header)

    def handle_data(self, data):
        if not (self._en_pl and self._left_column):
            return

        data = data.replace("\xa0", " ")
        if self._read_sentence_translation:
            self.sentences.append(data.strip())
            self._read_sentence_translation = False
        elif self._read_sentence:
            if data.strip() == "":
                return
            self.sentences.append(data.strip())
            self._read_sentence = False
        elif self._read_meaning:
            if self._read_header:
                self.header.append(data)
            else:
                self.meanings.append(data)
        elif self._read_part_of_speech:
            self._read_part_of_speech = False
            self.result.append(PartOfSpeech(data))

    def is_en_pl(self, tag, attrs):
        return tag == "div" and attrs == [("id", "en-pl")]

    def leaving_left_column(self, tag, attrs):
        return (
            self._left_column
            and tag == "div"
            and (
                attrs == [("class", "diki-results-right-column")]
                or attrs == [("id", "pl-en")]
            )
        )

    def is_left_column(self, tag, attrs):
        return tag == "div" and attrs == [("class", "diki-results-left-column")]

    def is_expecting_header(self, tag, attrs):
        return tag == "h1"

    def is_end_of_header_line(self, tag, attrs):
        return (
            tag == "span"
            # and attrs == [("class", "recordingsAndTranscriptions")]
            and attrs == [("class", "dictionaryEntryHeaderAdditionalInformation")]
        )

    def is_expecting_part_of_speech(self, tag, attrs):
        return tag == "span" and attrs == [("class", "partOfSpeech")]

    def is_expecting_meaning(self, tag, attrs):
        return (tag == "span" and attrs == [("class", "hw")]) or (
            tag == "span" and attrs == [("class", "hw hwLessPopularAlternative")]
        )

    def is_end_of_meaning(self, tag, attrs):
        return (
            self._read_meaning
            and tag == "span"
            and attrs == [("class", "meaningAdditionalInformation")]
        )

    def is_expecting_example_sentence(self, tag, attrs):
        return tag == "div" and attrs == [("class", "exampleSentence")]

    def is_expecting_sentence_translation(self, tag, attrs):
        return tag == "span" and attrs == [("class", "exampleSentenceTranslation")]


def parse_en_pl(html_dump):
    return EnPlParser().parse(html_dump)


def wrap_text(translations, linewrap=0):
    """Pretty print translations.

    If lienwrap is set to 0 disable line wrapping.
    """

    def wrap(text, width=linewrap, findent=0, sindent=0, bold=False):
        if width == 0:
            text = " " * findent + text
        else:
            import textwrap
            text = textwrap.fill(
                text,
                width=width,
                initial_indent=" " * findent,
                subsequent_indent=" " * sindent,
            )
        # don't use bold when stdout is pipe or redirect
        if bold and sys.stdout.isatty():
            text = "\033[0;1m" + text + "\033[0m"
        return text

    result = []
    meaning_idx = 0
    for i, x in enumerate(translations):
        if isinstance(x, Entity):
            meaning_idx = 1
            if i > 0 and not isinstance(translations[i-1], Entity):
                result.append("")
            result.append(wrap(x.val, bold=True))
        elif isinstance(x, PartOfSpeech):
            if i > 0 and not isinstance(translations[i-1], Entity):
                result.append("")
            result.append(f"[{x.val}]")
        elif isinstance(x, Meaning):
            if i > 0 and isinstance(translations[i-1], Sentence):
                result.append("")
            result.append(wrap(f"{meaning_idx:>3}. {x.val}", sindent=5, bold=True))
            meaning_idx += 1
        elif isinstance(x, Sentence):
            result.append("")
            s1 = wrap(x.val[0], findent=6, sindent=6)
            s2 = wrap(x.val[1], findent=6, sindent=7)
            result.append(s1)
            result.append(s2)

    return "\n".join(result)
