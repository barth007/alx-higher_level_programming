#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, )
    else:
        length = len(sentence)
        return length, sentence[0]
