from functions.level_1.five_title import change_copy_item


TITLE_LESS_THAN_ONE_HUNDRED = 'This is short title'
TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED = "This is a string with 93 charac" * 3
TITLE_WITH_ADDITIONAL_STR_MORE_THAN_ONE_HUNDRED = "This is a string with 93 charac" * 5
TITLE_WITHOUT_ELEMENT_IN_BRACKETS = 'Copy of title without elements in brackets'
TITLE_WITH_NOT_DIGIT_ELEMENT_IN_BRACKETS = 'Copy of title without elements in brackets (test)'
TITLE_WITH_EMPTY_IN_BRACKETS = 'Copy of title without elements in brackets ()'
TITLE_WITH_ONE_DIGIT_IN_BRACKETS = 'Copy of title without elements in brackets (1)'
TITLE_WITH_FEW_DIGIT_IN_BRACKETS = 'Copy of title without elements in brackets (12345)'
TITLE_WITH_FEW_DIGIT_WITH_DELIMITER_IN_BRACKETS = 'Copy of title without elements in brackets (12,345)'
TITLE_WITH_FEW_BRACKETS = 'Copy of title without elements in brackets (1) (2) (3)'


def test_change_copy_item__with_title_with_additional_str_len_equal_hundred():
    assert TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED == change_copy_item(TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED)


def test_change_copy_item__with_title_with_additional_str_len_equal_hundred_and_len_less_than_zero():
    assert TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED == change_copy_item(TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED, -1)


def test_change_copy_item__with_title_with_additional_str_len_equal_hundred_and_len_equal_zero():
    assert TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED == change_copy_item(TITLE_WITH_ADDITIONAL_STR_EQUAL_ONE_HUNDRED, 0)


def test_change_copy_item__with_title_with_additional_str_len_more_than_hundred():
    assert TITLE_WITH_ADDITIONAL_STR_MORE_THAN_ONE_HUNDRED == change_copy_item(TITLE_WITH_ADDITIONAL_STR_MORE_THAN_ONE_HUNDRED)


def test_change_copy_item__with_title_less_than_one_hundred_and_not_start_with_additional_str():
    expected_title = 'Copy of ' + TITLE_LESS_THAN_ONE_HUNDRED
    assert expected_title == change_copy_item(TITLE_LESS_THAN_ONE_HUNDRED)


def test_change_copy_item__title_without_element_in_brackets():
    expected_title = TITLE_WITHOUT_ELEMENT_IN_BRACKETS + ' (2)'
    assert expected_title == change_copy_item(TITLE_WITHOUT_ELEMENT_IN_BRACKETS)


def test_change_copy_item__title_with_not_digit_element_in_brackets():
    expected_title = TITLE_WITH_NOT_DIGIT_ELEMENT_IN_BRACKETS + ' (2)'
    assert expected_title == change_copy_item(TITLE_WITH_NOT_DIGIT_ELEMENT_IN_BRACKETS)


def test_change_copy_item__title_with_empty_in_brackets():
    expected_title = TITLE_WITH_EMPTY_IN_BRACKETS + ' (2)'
    assert expected_title == change_copy_item(TITLE_WITH_EMPTY_IN_BRACKETS)


def test_change_copy_item__title_with_one_digit_in_brackets():
    expected_title = 'Copy of title without elements in brackets (2)'
    assert expected_title == change_copy_item(TITLE_WITH_ONE_DIGIT_IN_BRACKETS)


def test_change_copy_item__title_with_few_digit_in_brackets():
    expected_title = 'Copy of title without elements in brackets (12346)'
    assert expected_title == change_copy_item(TITLE_WITH_FEW_DIGIT_IN_BRACKETS)


def test_change_copy_item__title_with_delimiter_between_digit_in_brackets():
    expected_title = 'Copy of title without elements in brackets (12,345) (2)'
    assert expected_title == change_copy_item(TITLE_WITH_FEW_DIGIT_WITH_DELIMITER_IN_BRACKETS)


def test_change_copy_item__title_with_few_digits():
    expected_title = 'Copy of title without elements in brackets (1) (2) (4)'
    assert expected_title == change_copy_item(TITLE_WITH_FEW_BRACKETS)
