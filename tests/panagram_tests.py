import pytest
from panagram.panagram import panagram


def test_panagram():
    sentence = "the quick brown fox jumps over the lazy dog"
    result = panagram(sentence)
    assert result is True
    sentence = "qwertyuiopasdfghjklzxcvbnm"
    assert panagram(sentence) is True
    sentence = "abc"
    assert panagram(sentence) is False
