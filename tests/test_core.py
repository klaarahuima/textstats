import pytest

from textstats import char_frequencies


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Aa", {"a": 2}),
        ("A B", {"a": 1, "b": 1}),
        ("Hello!", {"h": 1, "e": 1, "l": 2, "o": 1, "!": 1}),
    ],
)
def test_char_frequencies(text, expected):
    assert char_frequencies(text) == expected

def test_char_frequencies_digits():
    assert char_frequencies("a11b2") == {
        "a": 1,
        "1": 2,
        "b": 1,
        "2": 1,
    }
    
def test_char_frequencies_whitespace():
    assert char_frequencies("A a\nB\tb") == {
        "a": 2,
        "b": 2,
    }
