#!/usr/bin/python3
from functools import total_ordering


def multiple_returns(sentence):
    total = len(sentence)
    char = sentence[0] if total > 0 else "None"
    new = total, char
    return new
