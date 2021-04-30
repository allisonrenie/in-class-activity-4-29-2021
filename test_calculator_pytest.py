import calculator
import pytest

def test_add():
    assert calculator.add(3,4) == 7

def test_subtract():
    assert calculator.subtract(21,14) == 7

def test_multiply():
    assert calculator.multiply(7,3) == 21
    assert calculator.multiply(7,1) == 8

def test_divide():
    assert calculator.divide(21,3) == 7
