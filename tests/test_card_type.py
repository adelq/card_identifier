from nose.tools import assert_equals
from card_identifier.card_type import identify_credit_card_type

# Test card numbers, more should be added.
amex_cards = [
    '370000000000002',
    '372322409401021',
    '372322409401005',
    '375987654321001'
]
discover_cards = [
    '6011000000000012',
    '6011985115969525'
]
mc_cards = [
    '5424000000000015',
    '5589871003986236',
    '5401683100112371'
]
visa_cards = [
    '4007000000027',
    '4012888888881881',
    '4266841343738991'
]
unknown_cards = [
    '400700000002',
    '6090883271926957',
    '6006496142903742460'
]


class TestIdentifyCreditCardType(object):
    def check_card(self, card, type):
        assert_equals(identify_credit_card_type(card), type)

    def test_amex(self):
        for amex_card in amex_cards:
            yield self.check_card, amex_card, "AMEX"

    def test_discover(self):
        for discover_card in discover_cards:
            yield self.check_card, discover_card, "Discover"

    def test_mc(self):
        for mc_card in mc_cards:
            yield self.check_card, mc_card, "MasterCard"

    def test_visa(self):
        for visa_card in visa_cards:
            yield self.check_card, visa_card, "Visa"

    def test_unknown(self):
        for unknown_card in unknown_cards:
            yield self.check_card, unknown_card, "Unknown"
