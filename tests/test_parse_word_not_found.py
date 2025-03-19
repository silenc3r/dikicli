import pathlib
import pytest

from dikicli.core import parse_en_pl, WordNotFound

test_dir = pathlib.Path(__file__).resolve().parent
html_dir = test_dir / "htmldump_word_not_found"

html = {}
for filepath in html_dir.iterdir():
    word = filepath.stem
    with open(filepath) as f:
        html[word] = f.read()


class TestNotFound:
    def test_parse_cordland(self):
        with pytest.raises(WordNotFound) as exc_info:
            parse_en_pl(html["cornland"])
        assert (
            str(exc_info.value)
            == "Nie znaleziono dokładnego tłumaczenia wpisanej frazy."
        )

    def test_parse_greaves(self):
        with pytest.raises(WordNotFound) as exc_info:
            parse_en_pl(html["greaves"])
        assert (
            str(exc_info.value)
            == """\
Nie znaleziono dokładnego tłumaczenia wpisanej frazy.
Czy chodziło ci o: graves, Graves"""
        )
