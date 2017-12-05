import pytest
import urllib.parse
import urllib.request

from dikicli.core import WordNotFound
from dikicli.core import parse

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


def get_html(word):
    safe_url = URL.format(word=urllib.parse.quote(word))
    req = urllib.request.Request(safe_url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return response.read()


class TestParsing:
    def test_parse_simple(self):
        html_dump = get_html('juxtaposition')
        parsed = parse(html_dump, native_to_foreign=False)
        assert len(parsed) == 1
        key = list(parsed.keys())[0]
        assert isinstance(key, tuple)
        assert key[0] == 'juxtaposition'
        assert len(parsed[key]) == 1
        assert isinstance(parsed[key], list)
        parts = parsed[key][0]
        assert isinstance(parts, dict)
        assert 'part' in parts
        assert 'meanings_list' in parts
        assert isinstance(parts['part'], str)
        mlist = parts['meanings_list']
        assert isinstance(mlist, list)
        assert isinstance(mlist[0], dict)
        assert 'examples' in mlist[0]
        assert 'meaning' in mlist[0]
        assert isinstance(mlist[0]['examples'], list)
        assert len(mlist[0]['examples']) == 0
        assert isinstance(mlist[0]['meaning'], list)
        assert len(mlist[0]['meaning']) == 1
        assert mlist[0]['meaning'][0] == 'zestawienie'

    def test_parse_complex(self):
        words = ['guest', 'dog', 'work', 'moll', 'apple']
        for word in words:
            html_dump = get_html(word)
            parsed = parse(html_dump, native_to_foreign=False)
            assert len(parsed) > 0
            for key in parsed.keys():
                assert isinstance(key, tuple)
                assert isinstance(parsed[key], list)
                assert len(parsed[key]) > 0
                for part in parsed[key]:
                    assert isinstance(part, dict)
                    assert 'part' in part
                    assert 'meanings_list' in part
                    assert len(part['meanings_list']) > 0
                    for m in part['meanings_list']:
                        assert 'examples' in m
                        assert 'meaning' in m
                        assert len(m['meaning']) > 0
                        assert isinstance(m['meaning'], list)
                        assert isinstance(m['examples'], list)
                        for e in m['examples']:
                            assert isinstance(e, tuple)

    def test_parse_native(self):
        words = ['krowa', 'moll', 'wąwóz']
        for word in words:
            html_dump = get_html(word)
            parsed = parse(html_dump, native_to_foreign=True)
            assert len(parsed) > 0
            for key in parsed.keys():
                assert isinstance(key, tuple)
                assert isinstance(parsed[key], list)
                assert len(parsed[key]) > 0
                for part in parsed[key]:
                    assert isinstance(part, dict)
                    assert 'part' in part
                    assert 'meanings_list' in part
                    assert len(part['meanings_list']) > 0
                    for m in part['meanings_list']:
                        assert 'examples' in m
                        assert 'meaning' in m
                        assert len(m['meaning']) > 0
                        assert isinstance(m['meaning'], list)
                        assert isinstance(m['examples'], list)
                        for e in m['examples']:
                            assert isinstance(e, tuple)

    def test_parse_raises_not_found(self):
        html_dump = get_html('vvvvxxxx')
        with pytest.raises(WordNotFound) as e:
            parse(html_dump)
            assert str(e.value) == "Nie znaleziono tłumaczenia wpisanej frazy"

    def test_parse_raises_suggestions(self):
        html_dump = get_html('colag')
        with pytest.raises(WordNotFound) as e:
            parse(html_dump)
            assert 'Czy chodziło ci o:' in str(e.value)
