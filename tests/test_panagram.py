import pytest
from solved.panagram import panagram


def test_panagram():
    result = panagram("the quick brown fox jumps over the lazy dog")
    assert result is True
    sentence = "qwertyuiopasdfghjklzxcvbnm"
    assert panagram(sentence) is True
    assert panagram("abc") is False
