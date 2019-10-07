
import pytest

from game_class import *

test = Game('test', '03545', '£20', 'DA157JQ')

def test_lat():
    assert Game.lat_find(test) == 51.42991

def test_long():
    assert Game.long_find(test) == 0.089816

def test_lat1():
    assert type(Game.lat_find(test)) == float

def test_long1():
    assert type(Game.long_find(test)) == float

def test_name():
    assert type(test.name) == str