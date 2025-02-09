import pathlib

DIR = pathlib.Path(__file__).resolve().parent


def get_words():
    for filepath in (DIR / "htmldump_en").iterdir():
        yield filepath.stem


def generate():
    with open(DIR / "test_parse_en_pl.py", mode="w") as f:
        f.write(
            """\
import json
import pathlib

from dikicli.core import parse_en_pl

test_dir = pathlib.Path(__file__).resolve().parent
html_dir = test_dir / "htmldump_en"
json_dir = test_dir / "json_en"

html = {}
for filepath in html_dir.iterdir():
    word = filepath.stem
    with open(filepath) as f:
        html[word] = f.read()


def load_json(word):
    with open(json_dir / f"{word}.json") as f:
        content = json.load(f)
    return content


"""
        )

        f.write("class TestAll:\n")

        for word in get_words():
            safe_word = word.replace("'", "_").replace("-", "_").replace(" ", "_")
            f.write(
                f"""\
    def test_parse_{safe_word}(self):
        parsed = parse_en_pl(html["{word}"])
        cached = load_json("{word}")
        assert parsed == cached

"""
            )


if __name__ == "__main__":
    generate()
