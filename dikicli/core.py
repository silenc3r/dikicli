import re
import requests
from bs4 import BeautifulSoup

URL = 'https://www.diki.pl/%s'


def parse(html_dump):
    soup = BeautifulSoup(html_dump, 'html.parser')
    results = soup.find('div', class_='diki-results-left-column')

    # if translation wasn't found check if there are any suggestions
    if not results:
        suggestions = soup.find('div', class_='dictionarySuggestions')
        if suggestions:
            return suggestions.get_text().strip()
        return "Nie znaleziono tłumaczenia wpisanej frazy"

    # parts of the speech are in separate divs from translations
    parts = [p.get_text().strip()
             for p in results.select('div.partOfSpeechSectionHeader')]

    meanings_div = results.find_all('ol', class_='foreignToNativeMeanings')
    assert len(parts) == len(meanings_div)

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


def main():
    import sys

    word = sys.argv[1]
    # check requests context manager
    with requests.get(URL % word) as r:
        result = parse(r.content)

    if isinstance(result, list):
        for t in result:
            print("[{}]".format(t['part']))
            for m in t['meanings_list']:
                print("# ", end='')
                print(', '.join(m['meaning']))
                for e in m['examples']:
                    print(e)
            print()
    else:
        print(result)