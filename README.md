Card Identifier
===============

[![Build Status](https://travis-ci.org/adelq/card_identifier.svg?branch=master)](https://travis-ci.org/adelq/card_identifier)

Python library for credit/debit card identification and utilities


## Quickstart

```python
>>> card = "5401683100112371"
>>> validate_card(card)
True
>>> format_card("5401 6831 0011 2371")
"5401683100112371"
>>> identify_card_type(card)
"MasterCard"
>>> identify_card_issuer(card)["scheme"]
"MASTERCARD"
>>> identify_card_issuer(card)["bank"]["name"]
"CHASE"
>>> identify_card_issuer(card)["type"]
"CREDIT"
```

Card Identifier takes out the busy work from simple card operations. This
includes validation, formatting, and identification.

## Features

* Card number validation
* Card number reformatting
* Identify card type (VISA, MasterCard, etc)
* Identify card issuer using the binlist.net API

Card Identifier supports Python 2.7 and 3.4–3.6.

## Installation

To install Card Identifier, use pip:

    $ pip install card_identifier

## API Documentation

### `cardutils`

#### `cardutils.format_card`

Formats card numbers to remove any spaces, unnecessary characters, etc.

**Input:** Card number, integer or string

**Output:** Correctly formatted card number, string

**Usage**

```python
>>> from card_identifier.cardutils import format_card
>>> format_card("5401 6831 0011 2371woops")
"5401683100112371"
```

#### `cardutils.validate_card`

Check if card is valid using the Luhn algorithm.

**Input**: Card number, integer or string

**Output**: Valid?, boolean

**Usage**

```python
>>> from card_identifier.cardutils import validate_card
>>> validate_card("5401683100112371")
True
>>> validate_card("1234567890123456")
False
```

### `card_type`

#### `card_type.identify_card_type`

Identifies the card type based on the card number.
This information is provided through the first 6 digits of the card number.

**Input**: Card number, int or string

**Output**: Card type, string

**Usage**

```python
>>> from card_identifier.card_type import identify_card_type
>>> identify_card_type('370000000000002')
'AMEX'

>>> identify_card_type('6011000000000012')
'Discover'

>>> identify_card_type('5424000000000015')
'MasterCard'

>>> identify_card_type('4007000000027')
'Visa'

>>> identify_card_type('400700000002')
'Unknown'
```

### `card_issuer`

#### `card_issuer.identify_card_issuer`

Determines the card issuer using an IIN database (https://binlist.net)

**Input**: Card number, int or string

**Output**: Card issuer information, dictionary (spec by binlist.net)

**Usage**

```python
>>> from card_identifier.card_issuer import identify_card_issuer
>>> identify_card_issuer("5401683100112371")
{
  "bank": {
    "city": "",
    "logo": "",
    "name": "CHASE",
    "phone": "8005243880",
    "url": ""
  },
  "brand": "",
  "country": {
    "alpha2": "US",
    "latitude": 38,
    "longitude": -97,
    "name": "United States",
    "numeric": "840"
  },
  "number": {"length": None, "prefix": "540168"},
  "prepaid": False,
  "scheme": "MASTERCARD",
  "type": "CREDIT"
}
```
