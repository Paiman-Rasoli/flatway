from flatway.flatten import flatten, flattenDict
from .fixtures import (mock_list_with_deep_one, mock_list_with_deep_five,
                       mock_tuple_with_deep_one, mock_tuple_with_deep_five,
                       mock_dictionary_deep_one, mock_dictionary_deep_three)


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


def test_flatten_of_dict_depth_one(mock_dictionary_deep_one):
    result = flattenDict(mock_dictionary_deep_one)
    expect = {"name": "Jhon", "en": True, "per": False, "age": 20}
    assert result == expect
    assert isinstance(result, dict)


def test_flatten_of_dict_depth_three(mock_dictionary_deep_three):
    result = flattenDict(mock_dictionary_deep_three, 3)
    expect = {
        "name": "Jhon",
        "en": True,
        "per": False,
        "newChild": True,
        "height": 100,
        "ids": [1, 2, 3, 4, 5],
        "age": 20
    }
    assert result == expect
    assert isinstance(result, dict)
