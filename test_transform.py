import pytest
from transform import Dataitem
import pandas as pd


def test_input_format():
    dataitem = Dataitem('groups.csv', 'items.csv', 'output.json')
    dataitem.input()
    assert dataitem.input_1[-4:] == '.csv'

def test_read_1_format():
    dataitem = Dataitem('groups.csv', 'items.csv', 'output.json')
    assert isinstance(dataitem.read_1(), pd.DataFrame)

def test_read_2_format():
    dataitem = Dataitem('groups.csv', 'items.csv', 'output.json')
    assert isinstance(dataitem.read_2(), pd.DataFrame)

def test_transform():
    dataitem = Dataitem('groups.csv', 'items.csv', 'output.json')
    dataitem.transform()