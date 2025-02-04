from collections import namedtuple
from html.parser import HTMLParser


Entity = namedtuple("Entity", "val")
PartOfSpeech = namedtuple("PartOfSpeech", "val")
Meaning = namedtuple("Meaning", "val")
Variation = namedtuple("Variation", "val")
Sentence = namedtuple("Sentence", "val")
Info = namedtuple("Info", "val")


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

def parse_cached(html_dump):
    return CachedParser().parse(html_dump)
