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
