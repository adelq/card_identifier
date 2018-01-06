from nose.tools import assert_equals, assert_true
from card_identifier.cardutils import validate_card, format_card

# Test card numbers
valid_cards = [
    '370000000000002',
    '371449635398431',
    '372322409401021',
    '372322409401005',
    '378282246310005',
    '5610591081018250',
    '3530111333300000',
    '6011000000000012',
    '6011985115969525',
    '5424000000000015',
    '5401683100112371',
    '4007000000027',
    '4012888888881881',
    '4266841343738991',
    '6006496142903742460'
]


class TestCardValidity(object):
    def is_valid(self, card):
        assert_true(validate_card(card))

    def test_valid_cards(self):
        for valid_card in valid_cards:
            yield self.is_valid, valid_card


class TestCardFormatting(object):
    def test_space_removal(self):
        assert_equals(format_card("4266 8413 4373 8991"), "4266841343738991")

    def test_char_removal(self):
        assert_equals(format_card("426684woops1343738991"), "4266841343738991")
