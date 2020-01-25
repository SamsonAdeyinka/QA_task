import pytest
from application import factorial

def test_fact_number():
    assert factorial.fact(5)==120

def test_fact_one():
    assert factorial.fact(1)==1

def test_fact_zero():
    assert factorial.fact(0)==1
