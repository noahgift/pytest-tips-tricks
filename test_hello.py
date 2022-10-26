""" this is the module docstring so the linter will not complain"""
from hello import more_hello, more_goodbye


def test_more_hello():
    """test more hello"""
    assert more_hello() == "hi"


def test_more_goodbye():
    """test more goodbye"""
    assert more_goodbye() == "bye"
