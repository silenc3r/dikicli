import requests
import sys
from pathlib import Path

from .core import URL, HEADERS
from .core import WordNotFound
from .core import parse, write_to_file, write_html_file, write_index_file


def create_file_prompt(filename):
    print(f"File doesn't exist: {filename}")
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
        print(f"New file crated: {filename}")


def print_result(result):
    # result is always a list
    # add line wrapping
    for t in result:
        print("[{}]".format(t['part']))
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
    with requests.get(URL.format(word=word), headers=HEADERS) as r:
        try:
            result = parse(r.content)
        except WordNotFound as e:
            print(str(e), file=sys.stderr)
            sys.exit(2)

    wfile = Path('/tmp/phony.txt')
    prefix = '-'

    print_result(result)

    if not wfile.is_file():
        create_file_prompt(wfile)
    write_to_file(wfile, word, prefix)

    write_html_file(word, result)
    write_index_file(wfile, prefix)
