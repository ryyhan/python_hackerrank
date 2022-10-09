from jar import Jar
import pytest

def test_init():
    jar=Jar()
    assert jar.capacity==12
    jar1=Jar(6)
    assert jar1.capacity==6


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size==5


def test_withdraw():
    jar=Jar()
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size==3

    with pytest.raises(ValueError):
        jar.withdraw(10)

