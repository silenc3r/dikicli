import pytest

from dikicli.helpers import flatten
import dikicli.core
from dikicli.core import lookup_online
from dikicli.parsers import generate_word_page
from dikicli.parsers import (
    parse_en_pl,
    parse_cached,
    Entity,
    Meaning,
    PartOfSpeech,
    Sentence,
    Info,
)


def translate(word):
    html_dump = lookup_online(word).html
    result = parse_en_pl(html_dump)
    return result


def translate_old(word):
    html_dump = lookup_online(word).html
    result = dikicli.core._parse_html(html_dump)
    return result


@pytest.mark.vcr
class TestGenerateCacheAndBack:
    def test_compare_weight_parsing(self):
        word = "weight"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_switch_parsing(self):
        word = "switch"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_pet_parsing(self):
        word = "pet"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_snitch_parsing(self):
        word = "snitch"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_guest_parsing(self):
        word = "guest"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_sad_parsing(self):
        word = "sad"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_vying_parsing(self):
        word = "vying"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_hodgepodge_parsing(self):
        word = "hodgepodge"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_would_parsing(self):
        word = "would"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_tumult_parsing(self):
        word = "tumult"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_subordinate_parsing(self):
        word = "subordinate"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations

    def test_compare_apple_parsing(self):
        word = "apple"
        translations = translate(word)
        html_cached = generate_word_page(translations)
        back_translations = parse_cached(html_cached)
        assert translations == back_translations
