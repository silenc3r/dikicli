import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = 'https://www.diki.pl/%s'
HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko'}
WORDS_FILE = '/tmp/list.txt'


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


def get_words(words_file):
    with open(words_file, mode='rt') as f:
        return set(l.rstrip()[1:] for l in f)


def write_to_file(words_file, word, prefix='-'):
    if word not in get_words(words_file):
        with open(words_file, mode='at') as f:
            f.write(prefix + word + '\n')


def check_file_exists(filename):
    filepath = Path(filename)
    return filepath.is_file()


def create_file_prompt(filename):
    print(f"File doesn't exist: {filename}")
    input("Do you want to create it? (Y/n)")
    # FIXME
    # TODO: need sys.exit(1) somewhere


def print_result(result):
    # add line wrapping
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


def main():
    import sys

    if len(sys.argv) != 2:
        return "Wrong arguments"
    word = sys.argv[1]
    with requests.get(URL % word, headers=HEADERS) as r:
        result = parse(r.content)

    print_result(result)

    if isinstance(result, list):
        if check_file_exists(WORDS_FILE):
            write_to_file(WORDS_FILE, word, '-')
        else:
            create_file_prompt(WORDS_FILE)
            write_to_file(WORDS_FILE, word, '-')
