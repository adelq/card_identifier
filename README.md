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
* Identify card issuer using binlist.net API

Card Identifier supports Python 2.7 and 3.4–3.6.

## Installation

To install Card Identifier, use pip:

    $ pip install card_identifier
