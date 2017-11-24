import re
from bs4 import BeautifulSoup
from pathlib import Path

URL = 'https://www.diki.pl/%s'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


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
            return suggestions.get_text().strip()
        return "Nie znaleziono tłumaczenia wpisanej frazy"

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


def get_words(words_file, prefix):
    with open(words_file, mode='rt') as f:
        return set(l.rstrip()[len(prefix):] for l in f)


def write_to_file(words_file, word, prefix='-'):
    if word not in get_words(words_file, prefix):
        with open(words_file, mode='at') as f:
            f.write(prefix + word + '\n')


def check_file_exists(filename):
    filepath = Path(filename)
    return filepath.is_file()
