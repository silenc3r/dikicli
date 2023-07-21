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
                result.append(PartOfSpeech(pos.part.replace(" ", " ")))
            for m in pos.meanings:
                result.append(Meaning(", ".join(m.meaning)))
                for e in m.examples:
                    result.append(Sentence(e))
    return result
