import pytest


@pytest.fixture
def mock_list_with_deep_one():
    return [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12]


@pytest.fixture
def mock_tuple_with_deep_one():
    return (1, 2, 3, 4, 5, 6, 7, 8,
            (9, 10, 11),
            12)


@pytest.fixture
def mock_list_with_deep_five():
    return [1, 2, 3, 4, 5, 6, 7, 8, [
        9,
        10,
        11,
        [
            12, 13,
            [
                14, 15,
                [16, 17, [
                    18,
                    19,
                    20
                ]]
            ]
        ]
    ]]


@pytest.fixture
def mock_tuple_with_deep_five():
    return (1, 2, 3, 4, 5, 6, 7, 8, (
        9,
        10,
        (
            11, 12,
            (
                13, 14,
                (15, 16, (
                    17,
                    18,
                    19,
                    20
                ))
            )
        )
    ))
