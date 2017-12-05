import logging
import pytest
import urllib.parse
import urllib.request

from pathlib import Path

from context import TEST_DIR

from dikicli.core import WordNotFound
from dikicli.core import get_config, get_words, parse, parse_cached
from dikicli.templates import CONFIG_TEMPLATE

logger = logging.getLogger(__name__)

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


def get_html(word):
    safe_url = URL.format(word=urllib.parse.quote(word))
    req = urllib.request.Request(safe_url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return response.read()


class ParserTester:
    def _test_translations_dict(self, html_dump, native=False, cached=False):
        if cached:
            parsed = parse_cached(html_dump)
        else:
            parsed = parse(html_dump, native)
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


class TestParsing(ParserTester):
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
            self._test_translations_dict(html_dump)

    def test_parse_native(self):
        words = ['krowa', 'moll', 'wąwóz']
        for word in words:
            html_dump = get_html(word)
            self._test_translations_dict(html_dump, native=True)

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


class TestParsingCached(ParserTester):
    cache_dir = Path(TEST_DIR).joinpath('html_cache')

    def test_parse_cached(self):
        for filename in self.cache_dir.iterdir():
            with open(filename, mode='r') as f:
                html_dump = f.read()
            self._test_translations_dict(html_dump, cached=True)


class TestGetWords:
    words = ['guest', '+dog', 'work', '-moll', '*apple', '-donkey',
             '-juxtaposition', 'grave', '*pen', '-glass']

    def test_get_words_no_prefix(self, tmpdir):
        prefix = ''
        f = tmpdir.mkdir('dikicli').join('words.txt')
        f.write('\n'.join(self.words))
        path = Path(f)
        any_prefix_words = ['guest', 'dog', 'work', 'moll', 'apple', 'donkey',
                            'juxtaposition', 'grave', 'pen', 'glass']
        assert get_words(path, prefix) == any_prefix_words

    def test_get_words_dash_prefix(self, tmpdir):
        prefix = '-'
        f = tmpdir.mkdir('dikicli').join('words.txt')
        f.write('\n'.join(self.words))
        path = Path(f)
        dash_prefix_words = ['moll', 'donkey', 'juxtaposition', 'glass']
        assert get_words(path, prefix) == dash_prefix_words


class TestConfig:
    t_data_dir = '/derp'
    t_prefix = '*'
    t_linewrap = 5
    t_colors = 'false'
    t_web_browser = 'weasel'

    def test_config_file_overwrites_defaults(self, tmpdir):
        f = tmpdir.mkdir('dikicli').join('config.conf')
        config_file = Path(f)
        f.write(CONFIG_TEMPLATE.format(
            data_dir=self.t_data_dir, prefix=self.t_prefix,
            linewrap=self.t_linewrap, colors=self.t_colors,
            browser=self.t_web_browser))
        config = get_config(config_file)
        assert config['dikicli'].get('data dir') == self.t_data_dir
        assert config['dikicli'].get('prefix') == self.t_prefix
        assert config['dikicli'].getint('linewrap') == self.t_linewrap
        assert config['dikicli'].get('colors') == self.t_colors
        assert config['dikicli'].get('web browser') == self.t_web_browser

    def test_config_file_invalid_prefix(self, tmpdir):
        f = tmpdir.mkdir('dikicli').join('config.conf')
        config_file = Path(f)
        self.t_prefix = '$'
        f.write(CONFIG_TEMPLATE.format(
            data_dir=self.t_data_dir, prefix=self.t_prefix,
            linewrap=self.t_linewrap, colors=self.t_colors,
            browser=self.t_web_browser))
        config = get_config(config_file)
        assert config['dikicli'].get('prefix') == '-'

    def test_config_file_invalid_linewrap(self, tmpdir):
        f = tmpdir.mkdir('dikicli').join('config.conf')
        config_file = Path(f)
        self.t_linewrap = -10
        f.write(CONFIG_TEMPLATE.format(
            data_dir=self.t_data_dir, prefix=self.t_prefix,
            linewrap=self.t_linewrap, colors=self.t_colors,
            browser=self.t_web_browser))
        config = get_config(config_file)
        assert config['dikicli'].getint('linewrap') == 78
        self.t_linewrap = 'seventy eight'
        f.write(CONFIG_TEMPLATE.format(
            data_dir=self.t_data_dir, prefix=self.t_prefix,
            linewrap=self.t_linewrap, colors=self.t_colors,
            browser=self.t_web_browser))
        config = get_config(config_file)
        assert config['dikicli'].getint('linewrap') == 78

    def test_config_file_invalid_colors(self, tmpdir):
        f = tmpdir.mkdir('dikicli').join('config.conf')
        config_file = Path(f)
        self.t_colors = 'maybe'
        f.write(CONFIG_TEMPLATE.format(
            data_dir=self.t_data_dir, prefix=self.t_prefix,
            linewrap=self.t_linewrap, colors=self.t_colors,
            browser=self.t_web_browser))
        config = get_config(config_file)
        assert config['dikicli'].get('colors') == 'yes'
