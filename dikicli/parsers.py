from collections import namedtuple
from html.parser import HTMLParser


Entity = namedtuple("Entity", "val")
PartOfSpeech = namedtuple("PartOfSpeech", "val")
Meaning = namedtuple("Meaning", "val")
Variation = namedtuple("Variation", "val")
Sentence = namedtuple("Sentence", "val")
Info = namedtuple("Info", "val")


def join_with_space(str_list):
    # str_list cannot be empty
    s = iter(str_list)
    result = next(s)
    for elem in s:
        # don't add space before these chars
        if elem not in ",)":
            result += " "
        result += elem

    return result


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


class PlEnParser(HTMLParser):
    def set_all_false(self):
        self.pl_en_section = False
        self.left_column = False
        self.read_header = False
        self.read_part_of_speech = False
        self.read_meaning = False
        self.read_sentence = False
        self.read_sentence_translation = False
        self.in_ul = False

    def reset(self):
        super().reset()
        self.set_all_false()
        self.result = []
        self.sentences = []
        self.meanings = []
        self.variations = []
        self.header = []

    def parse(self, content):
        """Parse html string and return parsed output as list of items.

        content: html string
        returns: list of translation items
        """
        self.reset()
        self.feed(content)
        return self.result

    def handle_starttag(self, tag, attrs):
        if self.entering_pl_en(tag, attrs):
            self.pl_en_section = True
            return
        if self.entering_left_column(tag, attrs):
            self.left_column = True
            return

        if self.leaving_left_column(tag, attrs):
            self.set_all_false()
            return

        if not (self.left_column and self.pl_en_section):
            return

        if self.is_end_of_meaning(tag, attrs):
            self.read_meaning = False
        elif self.is_expecting_header(tag, attrs):
            self.read_header = True
        elif self.is_expecting_part_of_speech(tag, attrs):
            self.read_part_of_speech = True
        elif self.is_expecting_sentence_translation(tag, attrs):
            self.read_sentence_translation = True
        elif self.is_expecting_example_sentence(tag, attrs):
            # creating Meaning
            self.compile_meanings()
            self.read_meaning = False
            # creating Variation
            self.compile_variations()
            self.read_sentence = True
        elif self.entering_ul(tag, attrs):
            self.in_ul = True
        elif self.is_expecting_meaning(tag, attrs):
            self.read_meaning = True

    def handle_endtag(self, tag):
        if not (self.pl_en_section and self.left_column):
            return

        if tag == "h1":
            # creating Entity
            self.compile_entity()
            self.read_header = False
            self.read_meaning = False
        elif tag == "ul":
            self.in_ul = False
        elif tag == "li":
            # creating Meaning
            self.compile_meanings()
            self.read_meaning = False
            # creating Variation
            self.compile_variations()

    def handle_data(self, data):
        if not (self.pl_en_section and self.left_column):
            return

        data = data.strip()
        if data == "":
            return

        data = data.replace("\xa0", " ")

        if self.read_sentence_translation:
            self.sentences.append(data)
            # creating Sentence
            self.result.append(Sentence(self.sentences))
            self.sentences = []
            self.read_sentence_translation = False
        elif self.read_sentence:
            self.sentences.append(data)
            self.read_sentence = False
        elif self.read_part_of_speech:
            # creating PartOfSpeech
            self.result.append(PartOfSpeech(data))
            self.read_part_of_speech = False
        elif self.read_header:
            self.header.append(data)
        elif self.read_meaning:
            if self.in_ul:
                self.variations.append(data)
            else:
                self.meanings.append(data)

    def compile_entity(self):
        if len(self.header) != 0:
            header = join_with_space(self.header)
            self.result.append(Entity(header))
            self.header = []

    def compile_meanings(self):
        if len(self.meanings) != 0:
            m = join_with_space(self.meanings)
            self.result.append(Meaning(m))
            self.meanings = []

    def compile_variations(self):
        if len(self.variations) != 0:
            vs = join_with_space(self.variations)
            self.result.append(Variation(vs))
            self.variations = []

    def entering_pl_en(self, tag, attrs):
        return tag == "div" and attrs == [("id", "pl-en")]

    def leaving_left_column(self, tag, attrs):
        return (
            self.left_column
            and tag == "div"
            and (
                attrs == [("class", "diki-results-right-column")]
                or attrs == [("id", "pl-en")]
            )
        )

    def entering_ul(self, tag, attrs):
        return tag == "ul" and attrs == [("class", "nativeToForeignMeanings")]

    def entering_left_column(self, tag, attrs):
        return tag == "div" and attrs == [("class", "diki-results-left-column")]

    def is_expecting_header(self, tag, attrs):
        return tag == "h1"

    def is_expecting_part_of_speech(self, tag, attrs):
        return tag == "span" and attrs == [("class", "partOfSpeech")]

    def is_expecting_meaning(self, tag, attrs):
        return (
            (tag == "span" and attrs == [("class", "hw")])
            or (tag == "span" and attrs == [("class", "hwcomma")])
            or (tag == "span" and attrs == [("class", "hw hwLessPopularAlternative")])
        )

    def is_end_of_meaning(self, tag, attrs):
        return (
            (tag == "span" and attrs == [("class", "recordingsAndTranscriptions")])
            or (
                tag == "span"
                and attrs == [("class", "dictionaryEntryHeaderAdditionalInformation")]
            )
            or (tag == "span" and attrs == [("class", "meaningAdditionalInformation")])
        )

    def is_expecting_example_sentence(self, tag, attrs):
        return tag == "div" and attrs == [("class", "exampleSentence")]

    def is_expecting_sentence_translation(self, tag, attrs):
        return tag == "span" and attrs == [("class", "exampleSentenceTranslation")]


class NotFoundParser(HTMLParser):
    def reset(self):
        super().reset()
        self.info = []
        self.suggestions = []
        self.should_read = True
        self.in_p = False
        self.in_suggestions = False

    def parse(self, content):
        self.reset()
        self.feed(content)
        result = self.info
        if self.suggestions:
            result += "\n"
            result += "".join(self.suggestions)
        return [Info(result)]

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.in_p = True
        elif tag == "div" and attrs == [("class", "dictionarySuggestions")]:
            self.in_suggestions = True

    def handle_endtag(self, tag):
        if tag == "div":
            self.in_suggestions = False

    def handle_data(self, data):
        if self.in_p and self.should_read and data.strip() != "":
            self.info = data.strip()
            self.should_read = False
        elif self.in_suggestions and data.strip() != "":
            self.suggestions.append(data.lstrip())


def generate_html_lines(translations):
    """Create list of html strings that make up word page.
    translations: list of translation elements
    returns: list of html lines
    """
    content = []

    def peek(index, type_):
        if not index < len(translations):
            return False

        return isinstance(translations[index], type_)

    def append_indented(tag, indent):
        indent_str = " " * indent * 4
        content.append(indent_str + tag)

    def consume_entity(index, indent=0):
        elem = translations[index]
        if not isinstance(elem, Entity):
            raise ValueError("Expected `Entity`, got %s: %s" % (type(elem), elem))
        append_indented('<div class="word">', indent + 1)
        append_indented(f"<h2>{elem.val}</h2>", indent + 2)
        while peek(index + 1, Entity):
            index += 1
            elem = translations[index]
            append_indented(f"<h2>{elem.val}</h2>", indent + 2)
        append_indented("</div><!--close word-->", indent + 1)
        index = consume_pos(index + 1, indent + 1)
        append_indented("<br>", indent + 1)
        return index

    def consume_pos(index, indent):
        elem = translations[index]
        if isinstance(elem, PartOfSpeech):
            append_indented(f'<div class="part-of-speech">', indent)
            append_indented(f'<p class="part-name">[{elem.val}]</p>', indent + 1)
            append_indented("<ol>", indent + 1)
            index = consume_meaning(index + 1, indent + 2)
            append_indented("</ol>", indent + 1)
            append_indented("</div><!--close part-of-speech-->", indent)
            if peek(index, PartOfSpeech):
                append_indented("<br>", indent)
                index = consume_pos(index, indent)
            return index
        elif isinstance(elem, Meaning):
            append_indented("<ol>", indent)
            index = consume_meaning(index, indent + 1)
            append_indented("</ol>", indent)
            return index
        else:
            raise ValueError(
                "Expected `PartOfSpeech` or `Meaning`, got %s: %s" % (type(elem), elem)
            )

    def consume_meaning(index, indent):
        elem = translations[index]
        if not isinstance(elem, Meaning):
            raise ValueError("Expected `Meaning`, got %s: %s" % s(type(elem), elem))

        append_indented("<li>", indent)
        append_indented('<div class="meaning">', indent + 1)
        append_indented(f"<p><strong><span>{elem.val}</span></strong></p>", indent + 2)
        index = consume_variation(index + 1, indent + 2)
        append_indented("</div><!--close meaning-->", indent + 1)
        append_indented("</li>", indent)

        if peek(index, Meaning):
            index = consume_meaning(index, indent)

        return index

    def consume_variation(index, indent):
        if index >= len(translations):
            return index
        elem = translations[index]
        if isinstance(elem, Variation):
            # TODO
            pass
        elif isinstance(elem, Sentence):
            append_indented('<div class="examples">', indent)
            index = consume_sentence(index, indent + 1)
            append_indented("</div><!--close examples-->", indent)
            return index
        else:
            return index

    def consume_sentence(index, indent):
        if index >= len(translations):
            return index

        elem = translations[index]
        if isinstance(elem, Sentence):
            append_indented(
                f"<p><span>{elem.val[0]}</span><br><span>{elem.val[1]}</span></p>",
                indent,
            )
            index = consume_sentence(index + 1, indent)

        return index

    content.append('<div class="translation">')
    index = 0
    while index < len(translations):
        index = consume_entity(index)
    content.append("</div><!--close translation-->")
    return content


def generate_word_page(translations):
    html_lines = generate_html_lines(translations)
    return "\n".join(html_lines)


class CachedParser(HTMLParser):
    def reset(self):
        super().reset()
        self.result = []
        self.sentences = []
        self.meanings = []
        self.read_entity = False
        self.read_part_of_speech = False
        self.read_meaning = False
        self.read_examples = False

    def parse(self, content):
        self.reset()
        self.feed(content)
        return self.result

    def handle_starttag(self, tag, attrs):
        if tag == "div" and attrs == [("class", "word")]:
            self.read_entity = True
        elif tag == "div" and attrs == [("class", "part-of-speech")]:
            self.read_part_of_speech = True
        elif tag == "div" and attrs == [("class", "meaning")]:
            self.read_meaning = True
        elif tag == "div" and attrs == [("class", "examples")]:
            self.read_examples = True

    def handle_endtag(self, tag):
        if tag == "div":
            self.read_entity = False
            self.read_examples = False
        elif tag == "strong":
            self.result.append(Meaning("".join(self.meanings)))
            self.meanings = []
            self.read_meaning = False
        elif tag == "span" and len(self.sentences) == 2:
            self.result.append(Sentence(self.sentences))
            self.sentences = []

    def handle_data(self, data):
        if data.strip() == "":
            return
        if self.read_entity:
            self.result.append(Entity(data))
        elif self.read_part_of_speech:
            self.result.append(PartOfSpeech(data[1:-1]))
            self.read_part_of_speech = False
        elif self.read_meaning:
            self.meanings.append(data)
        elif self.read_examples:
            self.sentences.append(data)


def parse_en_pl(html_dump):
    return EnPlParser().parse(html_dump)


def parse_pl_en(html_dump):
    return PlEnParser().parse(html_dump)


def parse_cached(html_dump):
    return CachedParser().parse(html_dump)


def parse_not_found(html_dump):
    return NotFoundParser().parse(html_dump)
