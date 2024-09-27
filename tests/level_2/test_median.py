from functions.level_2.one_median import get_median_value


def test__get_median_value__empty_list_return_none():
    assert get_median_value(items=[]) is None


def test__get_median_value__one_element_in_list():
    assert 2 == get_median_value([2, ])


def test__get_median_value__odd_element_in_list():
    assert 3 == get_median_value([1, 2, 3, 4, 5])


def test__get_median_value__even_element_in_list():
    assert 1.5 == get_median_value([1, 2, ])
