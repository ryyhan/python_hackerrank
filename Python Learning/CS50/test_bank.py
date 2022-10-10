import pytest
from bank import value

def test_value1():
    assert value("Hola") == 20

def test_value2():
    assert value("Hello") == 0

def test_value3():
    assert value("sup") == 100

def test_value4():
    assert value("supPP") == 100

