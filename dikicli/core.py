import re
from bs4 import BeautifulSoup
from pathlib import Path

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


class WordNotFound(Exception):
    pass


def parse(html_dump):
    soup = BeautifulSoup(html_dump, 'html.parser')
    for r in soup.find_all('div', class_='diki-results-left-column'):
        meanings_div = r.find_all('ol', class_='foreignToNativeMeanings')
        if meanings_div:
            parts = [p.get_text().strip()
                     for p in r.select('div.partOfSpeechSectionHeader')]
            assert len(parts) == len(meanings_div)
            break
    else:
        # if translation wasn't found check if there are any suggestions
        suggestions = soup.find('div', class_='dictionarySuggestions')
        if suggestions:
            raise WordNotFound(suggestions.get_text().strip())
        raise WordNotFound("Nie znaleziono tłumaczenia wpisanej frazy")

    translations = []
    for p, m in zip(parts, meanings_div):
        t = dict()
        t['part'] = p
        t['meanings_list'] = []
        for variant in m.find_all('li'):
            v = dict()
            v['meaning'] = [m.get_text() for m in variant.select('span.hw')]
            v['examples'] = []
            for e in variant.find_all('div', class_='exampleSentence'):
                pattern = re.compile('\s{3,}')
                example = pattern.sub(' ', e.get_text().strip())
                v['examples'].append(example)
            t['meanings_list'].append(v)
        translations.append(t)

    return translations


def parse_cached(filename):
    pass


def cache_lookup(word, cache_dir):
    # FIXME: location from config
    filename = Path(cache_dir + '{}.html'.format(word))
    if filename.is_file():
        return parse_cached(filename)


def get_words(words_file, prefix):
    with open(words_file, mode='rt') as f:
        return [l.rstrip()[len(prefix):] for l in f]


def write_to_file(words_file, word, prefix='-'):
    if word not in get_words(words_file, prefix):
        with open(words_file, mode='at') as f:
            f.write(prefix + word + '\n')


def write_html_file(word, translations):
    content = []
    for t in translations:
        content.append("<br>")
        content.append("<p>[{part}]</p>".format(part=t['part']))
        for i, m in enumerate(t['meanings_list'], 1):
            content.append("<p><strong>{i}. {meaning}</p></strong>".format(
                i=i, meaning=', '.join(m['meaning'])
            ))
            for e in m['examples']:
                content.append("<p>{example}</p>".format(example=e))
    content_str = '\n'.join(content)
    # FIXME: should get location from config
    with open('/tmp/template.html', mode='rt') as f:
        result = f.read()
        result = result.replace('{% word %}', word)
        result = result.replace('{% content %}', content_str)
    # FIXME: should get location from config
    fname = Path('/tmp/translations/{}.html'.format(word))
    with open(fname, mode='wt') as f:
        f.write(result)


def write_index_file(words_file, prefix):
    content = ['<br>', '<ul>']
    for word in get_words(words_file, prefix):
        # FIXME: should get location from config
        if Path('/tmp/translations/{word}.html'.format(word=word)).is_file():
            content.append(('<li><a href="translations/{word}.html">'
                            '{word}</a></li>').format(word=word))
    content.append('</ul>')
    content_str = '\n'.join(content)
    # FIXME: should get location from config
    with open('/tmp/template.html', mode='rt') as f:
        result = f.read()
        result = result.replace('{% word %}', "Index")
        result = result.replace('{% content %}', content_str)
    # FIXME: should get location from config
    with open('/tmp/index.html', mode='wt') as f:
        f.write(result)
