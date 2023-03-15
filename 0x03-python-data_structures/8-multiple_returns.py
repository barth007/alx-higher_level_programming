#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
        return sentence
    else:
        length = len(sentence)
        return length, sentence[0]
