from nose.tools import assert_equals
from card_identifier.card_issuer import identify_card_issuer

# Test card numbers, more should be added.
amex_cards = [
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
    '4012888888881881',
    '4266841343738991'
]
maestro_cards = [
    '6010566891909991'
]

unknown_cards = [
    '6684424830380130',
]

# Map of issuer name to what all the cards match to
issuers = {
    "amex": "VISA",
    "discover": "DISCOVER",
    "mc": "MASTERCARD",
    "visa": "VISA",
    "maestro": "VISA",
    "unknown": "Not found"
}


class TestIdentifyCreditCardIssuer(object):
    def check_card(self, card_num, card_issuer):
        assert_equals(identify_card_issuer(card_num)["scheme"],
                      issuers[card_issuer])

    def test_amex(self):
        for amex_card in amex_cards:
            yield self.check_card, amex_card, "amex"

    def test_discover(self):
        for discover_card in discover_cards:
            yield self.check_card, discover_card, "discover"

    def test_mc(self):
        for mc_card in mc_cards:
            yield self.check_card, mc_card, "mc"

    def test_visa(self):
        for visa_card in visa_cards:
            yield self.check_card, visa_card, "visa"

    def test_maestro(self):
        for maestro_card in maestro_cards:
            yield self.check_card, maestro_card, "maestro"

    def test_unknown(self):
        for unknown_card in unknown_cards:
            yield self.check_card, unknown_card, "unknown"
