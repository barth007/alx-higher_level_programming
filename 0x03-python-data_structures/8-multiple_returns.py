#!/usr/bin/python3
def multiple_returns(sentence):
    if not isinstance(sentence, str):
        return (None, )
    elif not sentence:
        return sentence[0] = None
    else:
        length = len(sentence)
        return length, sentence[0]
