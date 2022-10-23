import pytest

def inc(a,b):
    return  a/b


def test_answer():
    assert inc(10,2) == 5


test_answer()
