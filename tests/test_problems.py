import pytest
from solved.problems import freq, palindrome, prime

def test_palindrome():
    assert palindrome("s") is True
    assert palindrome("malayalam") is True
    assert palindrome(12321) is True
    assert palindrome(1.1) is True
    assert palindrome(123) is False
    assert palindrome("sanju") is False


def test_freq():
    sentence = "sanju s kumar"
    test_freq = {"s": 2, "a": 2, "n": 1, "j": 1, "u": 2, "k": 1, "m": 1, "r": 1, " ": 2}
    assert freq(sentence) == test_freq

    sentence = "aldrin thomas"
    test_freq = {
        "a": 2,
        "l": 1,
        "d": 1,
        "r": 1,
        "i": 1,
        "n": 1,
        "t": 1,
        "h": 1,
        "o": 1,
        "m": 1,
        "s": 1,
        " ": 1,
    }

    assert freq(sentence) == test_freq
    assert freq("aaa") == {"a": 3}
    assert freq("aaa") != {"a": 1}
    assert freq("  ") == {" ": 2}


def test_prime():
    numbers = {
        -23: False,
        -1: False,
        0: False,
        1: False,
        2: True,
        3: True,
        4: False,
        5: True,
        6: False,
        104729: True,
    }
    for key, value in numbers.items():
        assert prime(key) == value
