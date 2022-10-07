import pytest
from plates import is_valid

def main():
    test_MinMax()
    test_valid()
    test_valid2()
    test_valid3()
    test_valid4()

def test_valid():
    #assert is_valid("AA") == True
    #assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False


def test_valid2():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_valid3():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_valid4():
    assert is_valid("PI3.14") == False


def test_MinMax():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

if __name__=="__main__":
    main()