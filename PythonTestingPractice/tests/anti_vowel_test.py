import pytest
from python_exercises import anti_vowel


def test_vowel_string():
    assert anti_vowel.anti_vowel("Samson") == "Smsn"

