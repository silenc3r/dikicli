import requests
import sys
import textwrap
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


def pretty_print(translations, linewrap=0):

    def print_wrapped(text, width=linewrap, findent=0, sindent=0, bold=False):
        # don't use bold when stdout is pipe or redirect
        if bold and sys.stdout.isatty():
            text = "\033[0;1m" + text + "\033[0m"
        if width == 0:
            print(' '*findent, text)
        else:
            print(textwrap.fill(text, width=width,
                                initial_indent=' '*findent,
                                subsequent_indent=' '*sindent))
    indent = 5
    for i1, words in enumerate(translations):
        if i1 > 0:
            print("\n")
        for w in words:
            print_wrapped(w, bold=True)
        for i2, t in enumerate(translations[words]):
            if i2 > 0:
                print()
            part = t['part']
            if part:
                print("[{part}]".format(part=part))
            for i3, m in enumerate(t['meanings_list'], 1):
                if i3 > 1:
                    print()
                meaning = "{index:>3}. {meanings}".format(
                    index=i3, meanings=', '.join(m['meaning']))
                print_wrapped(meaning, sindent=indent, bold=True)
                for e in m['examples']:
                    print()
                    print_wrapped(e[0], findent=indent+2, sindent=indent+2)
                    print_wrapped(e[1], findent=indent+2, sindent=indent+3)


def main():
    import sys

    if len(sys.argv) != 2:
        return "Wrong arguments"
    word = sys.argv[1]

    cache_dir = Path('/tmp/')
    hist_file = Path('/tmp/phony.txt')
    prefix = '-'

    if word == '--display-index':
        import webbrowser
        webbrowser.open(cache_dir.joinpath('index.html').as_uri())
        sys.exit(0)

    if not hist_file.is_file():
        create_file_prompt(hist_file)

    cached = cache_lookup(word, cache_dir)
    if cached:
        pretty_print(cached, 78)
        sys.exit(0)

    with requests.get(URL.format(word=word), headers=HEADERS) as r:
        try:
            translation = parse(r.content)
        except WordNotFound as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)

    pretty_print(translation, 78)

    write_to_file(hist_file, word, prefix)

    write_html_file(word, translation, cache_dir)
    write_index_file(hist_file, prefix, cache_dir)
