import decimal
from datetime import datetime

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense

VALID_SMS_TEXT = '123.12 $, 9999999999993456 11.09.23 12:55 COFFE_SHOP authcode 1234'
VALID_SMS_WITH_INTEGER_AMOUNT_TEXT = '123 $, 9999999999993456 11.09.23 12:55 COFFE_SHOP authcode 1234'
INVALID_DATETIME_FORMAT_SMS_TEXT = '123.12 $, 9999999999993456 11.09.2023 12:55 COFFE_SHOP authcode 1234'

ADDITIONAL_INFO_BEFORE_AUTHCODE_SMS_TEXT = ('123.12 $, 9999999999993456 11.09.23 12:55 COFFE_SHOP SAINT P.'
                                            ' NEVSKY AVENUE authcode 1234')

ADDITIONAL_INFO_AFTER_AUTHCODE_SMS_TEXT = ('123.12 $, 9999999999993456 11.09.23 12:55 COFFE_SHOP '
                                           'authcode 1234 DO NOT SHARE YOU CODE!')
VALID_SMS = SmsMessage(VALID_SMS_TEXT, 'andrey', datetime(2023, 9, 11))
EMPTY_BANK_CARDS = []
ONE_VALID_BANK_CARDS = [BankCard('3456', 'user_1')]
EQUAL_LAST_DIGIT_BANK_CARDS = [BankCard('3456', 'user_1'), BankCard('3456', 'user_2')]
FEW_VALID_BANK_CARDS = [BankCard('1234', 'user_1'), BankCard('3456', 'user_2')]
NOT_FOUND_BANK_CARDS = [BankCard('1234', 'user_1')]


def test_parse_ineco_expense__valid_data_():
    expense = parse_ineco_expense(VALID_SMS, ONE_VALID_BANK_CARDS)
    amount = expense.amount
    card = expense.card
    spend_in = expense.spent_in
    spend_at = expense.spent_at
    assert amount == decimal.Decimal('123.12'), 'invalid amount!!!'
    assert card == BankCard('3456', 'user_1'), 'invalid card!!!'
    assert spend_at == datetime(2023, 9, 11, 12, 55)
    assert spend_in == 'COFFE_SHOP'


def test_parse_ineco_integer_amount():
    sms = SmsMessage(VALID_SMS_WITH_INTEGER_AMOUNT_TEXT, 'user_1', datetime.now())
    expense = parse_ineco_expense(sms, ONE_VALID_BANK_CARDS)
    assert expense.amount == decimal.Decimal('123.00')


def test_parse_ineco_expense__empty_bank_cards():
    with pytest.raises(IndexError):
        parse_ineco_expense(VALID_SMS, EMPTY_BANK_CARDS)


def test_parse_ineco_expense__valid_data_few_cards():
    expense = parse_ineco_expense(VALID_SMS, FEW_VALID_BANK_CARDS)
    assert expense.card == FEW_VALID_BANK_CARDS[1], 'invalid card!!!'


def test_parse_ineco_expense__valid_data_equal_last_digit_in_cards():
    expense = parse_ineco_expense(VALID_SMS, EQUAL_LAST_DIGIT_BANK_CARDS)
    assert expense.card == EQUAL_LAST_DIGIT_BANK_CARDS[0], 'invalid card!!!'


def test_parse_ineco_expense__card_not_found():
    with pytest.raises(IndexError):
        parse_ineco_expense(VALID_SMS, NOT_FOUND_BANK_CARDS)


def test_parse_ineco_expense__additional_info_before_authcode_in_sms_text():
    sms = SmsMessage(ADDITIONAL_INFO_BEFORE_AUTHCODE_SMS_TEXT, 'user_1', datetime.now())
    expense = parse_ineco_expense(sms, ONE_VALID_BANK_CARDS)
    amount = expense.amount
    card = expense.card
    spend_in = expense.spent_in
    spend_at = expense.spent_at
    assert amount == decimal.Decimal('123.12'), 'invalid amount!!!'
    assert card == BankCard('3456', 'user_1'), 'invalid card!!!'
    assert spend_at == datetime(2023, 9, 11, 12, 55)
    assert spend_in == 'COFFE_SHOP SAINT P. NEVSKY AVENUE'


def test_parse_ineco_expense__additional_info_after_authcode_in_sms_text():
    sms = SmsMessage(ADDITIONAL_INFO_AFTER_AUTHCODE_SMS_TEXT, 'user_1', datetime.now())
    expense = parse_ineco_expense(sms, ONE_VALID_BANK_CARDS)
    amount = expense.amount
    card = expense.card
    spend_in = expense.spent_in
    spend_at = expense.spent_at
    assert amount == decimal.Decimal('123.12'), 'invalid amount!!!'
    assert card == BankCard('3456', 'user_1'), 'invalid card!!!'
    assert spend_at == datetime(2023, 9, 11, 12, 55)
    assert spend_in == 'COFFE_SHOP'


def test_parse_ineco_expense__invalid_date_time_format_in_sms_text():
    sms = SmsMessage(INVALID_DATETIME_FORMAT_SMS_TEXT, 'user_1', datetime.now())
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, ONE_VALID_BANK_CARDS)
