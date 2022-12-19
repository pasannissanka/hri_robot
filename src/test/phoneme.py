from phonemizer import phonemize
from phonemizer.separator import Separator

text = "It is eleven thirty nine"

phn = phonemize(
    text,
    language='en-us',
    backend='espeak',
    separator=Separator(phone=None, word=' ', syllable='|'),
    strip=True,
    preserve_punctuation=True,
    njobs=4)

print(phn)
print(list(phn))


a = ["i", "ɪ", "e", "ɛ", "æ", "ʌ", "ə", "ɚ", "u", "ʊ", "o", "ɔ", "ɑ", "ɑɪ", "ɑʊ", "ɔɪ", "p", "b", "d", "t",
     "k", "g", "f", "v", "ɵ", "ð", "s", "z", "ʃ", "ʒ", "h", "ʧ", "ʤ", "m", "n", "ŋ", "l", "r", "w", "j", ]
