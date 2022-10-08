from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate(r"25.2.87.4")==True
    assert validate(r"255.2.9.45")==True
    assert validate(r"255.255.255.5086")==False
    assert validate(r"255.255.463.255")==False
    assert validate(r"255.8394.255.255")==False
    assert validate(r"48975.255.255.255")==False
    assert validate(r"1.2.09.09.98")==False
    assert validate(r"98.8")==False
    assert validate(r"255.255.255.255")==True
    assert validate(r"98999.8")==False
    assert validate(r"98999.8.093485.8943573487")==False



if __name__ == "__main__":
    main()
