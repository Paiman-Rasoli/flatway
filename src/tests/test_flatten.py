from flatway.flatten import flatten
from .fixtures import (mock_list_with_deep_one, mock_list_with_deep_five,
                       mock_tuple_with_deep_one, mock_tuple_with_deep_five)


def test_flatten_of_list_with_deep_one(mock_list_with_deep_one):
    result = flatten(mock_list_with_deep_one)
    expect = [x for x in range(1, 13)]
    assert result == expect
    assert isinstance(result, list)


def test_flatten_of_list_with_deep_five(mock_list_with_deep_five):
    result = flatten(mock_list_with_deep_five, 5)
    expect = [x for x in range(1, 21)]
    assert result == expect
    assert isinstance(result, list)


def test_of_tuple_with_depth_one(mock_tuple_with_deep_one):
    result = flatten(mock_tuple_with_deep_one)
    expect = tuple([x for x in range(1, 13)])
    assert result == expect
    assert isinstance(result, tuple)


def test_of_tuple_with_depth_five(mock_tuple_with_deep_five):
    result = flatten(mock_tuple_with_deep_five, 5)
    expect = tuple([x for x in range(1, 21)])
    assert result == expect
    assert isinstance(result, tuple)
