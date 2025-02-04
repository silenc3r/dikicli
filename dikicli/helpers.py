import json
from dikicli.parsers import Entity, PartOfSpeech, Meaning, Sentence


def flatten(translations):
    result = []
    if not translations:
        return result
    for t in translations:
        for w in t.word:
            result.append(Entity(w))
        for pos in t.parts_of_speech:
            if pos.part:
                result.append(PartOfSpeech(pos.part.replace("\xa0", " ")))
            for m in pos.meanings:
                result.append(Meaning(", ".join(m.meaning)))
                for e in m.examples:
                    result.append(Sentence(e))
    return result


def flatten_compat(trans_dict):
    """
    Convert translation dict format to flat array.
    """
    result = []
    if not trans_dict:
        return result
    for t in trans_dict:
        for w in t["Entry"]:
            result.append(Entity(w))
        for pos in t["PartsOfSpeech"]:
            if pos["Part"]:
                result.append(PartOfSpeech(pos["Part"]))
            for m in pos["Meanings"]:
                result.append(Meaning(", ".join(m["Meaning"])))
                for e in m["ExampleSentences"]:
                    result.append(Sentence([e["Sentence"], e["Translation"]]))
    return result


def to_dict(translations):
    result = []
    if not translations:
        return result

    for t in translations:
        entry = {}
        entry["Entry"] = list(t.word)
        entry["PartsOfSpeech"] = []
        for pos in t.parts_of_speech:
            meanings = []
            for m in pos.meanings:
                sentences = []
                for ex in m.examples:
                    ss = {"Sentence": ex[0], "Translation": ex[1]}
                    sentences.append(ss)
                meanings.append({"Meaning": m.meaning, "ExampleSentences": sentences})

            p = pos.part or ""
            p = p.replace("\xa0", " ")

            entry["PartsOfSpeech"].append({"Part": p, "Meanings": meanings})
        result.append(entry)

    return result


def to_json(dict_entry):
    """Convert dictionary entry to JSON."""
    return json.dumps(dict_entry, ensure_ascii=False)
