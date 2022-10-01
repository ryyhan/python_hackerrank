from seasons import validate
import pytest
def main():
    test_validate()

def test_validate():
    assert validate("2001-10-23")==("2001","10","23")
    assert validate('1998-7-3')==None
    assert validate("October 23, 2001")==None

if __name__=="__main__":
    main()