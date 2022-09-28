from working import convert
import pytest

def main():
    test_convert()

def test_convert():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")

    with pytest.raises(ValueError):
        convert("dsjhsdfhu")

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


if __name__ == "__main__":
    main()

