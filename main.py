from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C


def tokenize(text: str):
    return [
        (m.surface(), m.dictionary_form(), m.normalized_form(), m.reading_form(), m.part_of_speech())
        for m in tokenizer_obj.tokenize(text, mode)
    ]

from pprint import pprint

h = tokenize("座りながら手を上げている。");pprint(h)
h = tokenize("座っている。");pprint(h)
