import pytest
from python_exercises import count

def test_count_zeros():
    assert count.count([0,0,0],0) == 3

def test_count_random_number():
    assert count.count([4,4,4,4,4,4,4,4,4,4],4) == 10

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3
