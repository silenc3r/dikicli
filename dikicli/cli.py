import requests
import sys
from pathlib import Path

from .core import URL, HEADERS
from .core import parse, write_to_file, check_file_exists


def create_file_prompt(filename):
    print(f"File doesn't exist: {filename}")
    answer = input("Do you want to create it? (y/N) ").lower()
    if answer not in ['y', 'yes']:
        print("aborting...")
        sys.exit(1)
    else:
        parent = filename.parent
        if not parent.exists():
            ap = input("Parent directory doesn't exist, "
                       "do you want to create it? (y/N) ").lower()
            if ap in ['y', 'yes']:
                parent.mkdir(parents=True)
            else:
                print("aborting...")
                sys.exit(1)
        filename.touch()
        print(f"New file crated: {filename}")


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

    wfile = Path('/tmp/phony.txt')
    prefix = '-'

    if isinstance(result, list):
        if not check_file_exists(wfile):
            create_file_prompt(wfile)
        write_to_file(wfile, word, prefix)
