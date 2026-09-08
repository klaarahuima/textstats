import pytest
from textstats import longest_word, word_count


@pytest.mark.parametrize("text,expected", [
    ("", 0), ("one", 1), ("the end.", 2), ("Don't stop: 2 of us are hungry.", 7), (" I like python-3", 3)
])

def test_word_count(text : str, expected: int):
    assert word_count(text) == expected

