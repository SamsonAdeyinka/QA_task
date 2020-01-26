import pytest
from python_exercises import multiply_list

def test_multiply():
    assert multiply_list.multiply_all([2,2,3]) == 12

def test_negative_multiply():
    assert multiply_list.multiply_all([-2,-2,-2]) == -8

def test_multiply_zero():
    assert multiply_list.multiply_all([0,0]) == 0

