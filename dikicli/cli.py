import requests
import sys
from pathlib import Path

from .core import URL, HEADERS
from .core import WordNotFound
from .core import parse, write_to_file, write_html_file, write_index_file
from .core import cache_lookup


def create_file_prompt(filename):
    print("File doesn't exist: {}".format(filename))
    answer = input("Do you want to create it? (y/N) ").lower()
    if answer not in ['y', 'yes']:
        print("aborting...", file=sys.stderr)
        sys.exit(1)
    else:
        parent = filename.parent
        if not parent.exists():
            answer = input("Parent directory doesn't exist, "
                           "do you want to create it? (y/N) ").lower()
            if answer in ['y', 'yes']:
                parent.mkdir(parents=True)
            else:
                print("aborting...", file=sys.stderr)
                sys.exit(1)
        filename.touch()
        print("New file crated: {}".format(filename))


def print_translation(result, linewrap=None):
    # add line wrapping
    for keys, value in result.items():
        for k in keys:
            print(k)
        for t in value:
            part = t['part']
            if part is not None:
                print("[{}]".format(part))
            for m in t['meanings_list']:
                print("# ", end='')
                print(', '.join(m['meaning']))
                for e in m['examples']:
                    print(e)
            print()


def main():
    import sys

    if len(sys.argv) != 2:
        return "Wrong arguments"
    word = sys.argv[1]

    cache_dir = Path('/tmp/')
    hist_file = Path('/tmp/phony.txt')
    prefix = '-'

    cached = cache_lookup(word, cache_dir)
    if cached:
        print_translation(cached)
        sys.exit(0)

    with requests.get(URL.format(word=word), headers=HEADERS) as r:
        try:
            translation = parse(r.content)
        except WordNotFound as e:
            print(str(e), file=sys.stderr)
            sys.exit(2)

    print_translation(translation)

    if not hist_file.is_file():
        create_file_prompt(hist_file)
    write_to_file(hist_file, word, prefix)

    write_html_file(word, translation, cache_dir)
    write_index_file(hist_file, prefix, cache_dir)
