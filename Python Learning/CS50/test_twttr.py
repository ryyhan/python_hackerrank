import pytest
from twttr import shorten

def test_shorten():
    assert shorten("twitter")=="twttr"

def test_caps():
    assert shorten("TWITTER")=="TWTTR"

def test_num():
    assert shorten("twitter32")=="twttr32"

def test_spaces():
    assert shorten("twitt, er")=="twtt, r"


