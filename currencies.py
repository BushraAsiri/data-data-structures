"""Currency converter utilities."""
RATES = {
    "USDEUR":0.85,
    "GBPEUR":1.13,
    "CHFEUR":0.86,
    "EURGBP":0.885
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    value, from_currency = amount

    direct = from_currency + currency
    if direct in RATES:
        return round(value * RATES[direct])

    reverse = currency + from_currency
    if reverse in RATES:
        return round(value / RATES[reverse])

    return None
