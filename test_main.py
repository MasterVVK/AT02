# test_main.py

import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4

def test_empty_string():
    assert count_vowels("") == 0

def test_numbers_and_special_chars():
    assert count_vowels("12345!@#$%") == 0

def test_vowels_with_spaces():
    assert count_vowels(" a e i o u ") == 5
    assert count_vowels(" A E I O U ") == 5
