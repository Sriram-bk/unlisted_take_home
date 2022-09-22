import re
from nltk import download, tokenize


def match_parens(sentence: str):
    open_parens = re.findall(r"\(", sentence)
    close_parens = re.findall(r"\)", sentence)

    diff = len(open_parens) - len(close_parens)

    if diff > 0:
        return sentence[:-1] + diff * ")" + sentence[-1]

    return sentence


def match_parens_per_sentence(s: str):
    sentences = tokenize.sent_tokenize(s)

    return " ".join(list(map(lambda sentence: match_parens(sentence), sentences)))


if __name__ == "__main__":
    inp = "(I prefer (20 degrees and above)! I (like the (beach and the sun. "

    print(match_parens_per_sentence(inp))
