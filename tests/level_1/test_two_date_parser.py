from datetime import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from__tomorrow():
    assert compose_datetime_from('tomorrow', '10:00') == datetime(2023, 9, 12, 10, 0)


def test_compose_datetime_from__not_tomorrow():
    assert compose_datetime_from('any_random_string', '10:00') == datetime(2023, 9, 11, 10, 0)


def test_compose_datetime_from__wrong_time_format():
    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '10 00')


def test_compose_datetime_from__wrong_time_value():
    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '-1:00')
