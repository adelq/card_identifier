# Card name constants
AMEX = 'AMEX'
DISCOVER = 'Discover'
MASTERCARD = 'MasterCard'
VISA = 'Visa'
UNKNOWN = 'Unknown'

# Card number constants
AMEX_2 = ('34', '37')
MASTERCARD_2 = ('51', '52', '53', '54', '55')
DISCOVER_2 = '65',
DISCOVER_4 = '6011',
VISA_1 = '4',


def identify_credit_card_type(card_num):
    """
    Identifies the card type based on the card number.
    This information is provided through the first 6 digits of the card number.

    Input: Card number, int or string
    Output: Card type, string

    >>> identify_credit_card_type('370000000000002')
    'AMEX'

    >>> identify_credit_card_type('6011000000000012')
    'Discover'

    >>> identify_credit_card_type('5424000000000015')
    'MasterCard'

    >>> identify_credit_card_type('4007000000027')
    'Visa'

    >>> identify_credit_card_type('400700000002')
    'Unknown'
    """

    card_type = UNKNOWN
    card_num = str(card_num)

    # AMEX
    if len(card_num) == 15 and card_num[:2] in AMEX_2:
        card_type = AMEX

    # MasterCard, Visa, and Discover
    elif len(card_num) == 16:
        # MasterCard
        if card_num[:2] in MASTERCARD_2:
            card_type = MASTERCARD

        # Discover
        elif (card_num[:2] in DISCOVER_2) or (card_num[:4] in DISCOVER_4):
            card_type = DISCOVER

        # Visa
        elif card_num[:1] in VISA_1:
            card_type = VISA

    # VISA
    elif (len(card_num) == 13) and (card_num[:1] in VISA_1):
        card_type = VISA

    return card_type
