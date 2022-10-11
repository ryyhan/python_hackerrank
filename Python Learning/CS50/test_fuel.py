import pytest
from fuel import convert
from fuel import gauge


def test_convert1():
    assert convert("100/100") == 100

def test_convert2():
    assert convert("20/50") == 40

def test_convert3():
    with pytest.raises(ValueError):
        convert("100/50")

def test_convert4():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_gauge1():
    assert gauge(100) == "F"

def test_gauge2():
    assert gauge(40) == "40%"

def test_gauge3():
    assert gauge(99) == "F"

def test_gauge4():
    assert gauge(1) == "E"

