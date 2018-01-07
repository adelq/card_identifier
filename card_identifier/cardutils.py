def format_card(card_num):
    """
    Formats card numbers to remove any spaces, unnecessary characters, etc

    Input: Card number, integer or string
    Output: Correctly formatted card number, string
    """
    import re
    card_num = str(card_num)
    # Regex to remove any nondigit characters
    return re.sub(r"\D", "", card_num)


def validate_card(card_num):
    """
    Check if credit card is valid using the Luhn algorithm

    Input: Card number, integer or string
    Output: Valid?, boolean
    """
    double = 0
    total = 0

    digits = str(card_num)

    for i in range(len(digits) - 1, -1, -1):
        for c in str((double + 1) * int(digits[i])):
            total += int(c)
        double = (double + 1) % 2

    return (total % 10) == 0
