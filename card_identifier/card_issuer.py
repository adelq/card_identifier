binlist_url = "https://lookup.binlist.net/"
status_404 = {
    "brand": "Not found",
    "bank": "Not found",
    "card_type": "Not found",
    "card_category": "",
    "error": True,
    "scheme": "Not found"
}


def find_card(iin):
    """
    Takes in IIN/BIN number, and returns the issuer using the binlist.net API

    Input: IIN number, int or string
    Output: Dictionary containing credit card issuer information
    """
    import requests

    iin = str(iin)

    response = requests.get(binlist_url + iin)

    # Check for a 404 status code
    if response.status_code == 404:
        status_404['bin'] = iin
        return status_404

    return response.json()


def identify_card_issuer(card_num):
    """
    Determines the card issuer using an IIN database

    Input: Card number, int or string
    Output: Card issuer information, dictionary (spec by binlist.net)
    """
    card_num = str(card_num)

    # IIN on the credit card being searched
    card_iin = card_num[:6]

    return find_card(card_iin)
