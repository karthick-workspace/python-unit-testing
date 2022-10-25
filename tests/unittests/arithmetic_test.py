from src.unittests.arithmetic import *
import pytest


# pytest tests/unittests/arithmetic_test.py

def test_add():
    assert add(5, 5) == 10


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 10) == 100


def test_division():
    assert division(10, 5) == 2


@pytest.mark.skip(reason="this operation is not in scope")
def test_modulus():
    assert modulus(10,5) == 0


@pytest.mark.xfail(reason="Using TDD, train_model() is not implemented")
def test_exponentiation():
    ...

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert division(10, 0) == 2