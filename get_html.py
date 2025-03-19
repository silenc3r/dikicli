#!/usr/bin/env python3

import sys

from dikicli.core import lookup_online

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage:\n\t{sys.argv[0]} <word>")
        exit(2)

    word = sys.argv[1]
    html_dump = lookup_online(word)
    with open(f"{word}.html", "w") as f:
        f.write(html_dump)
