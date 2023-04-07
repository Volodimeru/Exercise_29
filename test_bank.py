from bank import value

def test_value_0():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_value_20():
    assert value("HI") == 20
    assert value("hi") == 20

def test_value_100():
    assert value("What's up") == 100
    assert value("who are you?") == 100


