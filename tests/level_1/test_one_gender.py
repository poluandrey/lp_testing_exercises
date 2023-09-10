from functions.level_1.one_gender import genderalize


def test_genderalize_gender_male():
    result = genderalize('table', 'moon', 'male')
    expected_result = 'table'
    assert result == expected_result


def test_genderalize_gender_not_male():
    result = genderalize('table', 'moon', 'female')
    expected_result = 'moon'
    assert result == expected_result


def test_genderalize_gender_none():
    result = genderalize('table', 'moon', gender=None)
    expected_result = 'moon'
    assert result == expected_result
