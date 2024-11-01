conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}

def currency_converter(amount, from_currency, to_currency):
    """
    Converts a given amount from one currency to another based on provided conversion rates.

    Parameters:
        -amount (float or int): The monetary value to be converted. Must be non-negative.
        -from_currency (str): The currency code of the original currency ('GBP', 'CNY', 'PHP', 'INR').
        -to_currency (str): The currency code to convert to ('GBP', 'CNY', 'PHP', 'INR').

    Returns:
        -float: The converted amount, rounded to two decimal places. Returns 0.0 if amount is negative.
    """
    # Handle negative amounts
    if amount < 0: 
        return 0.0
    
    # Get conversion rate and calculate the converted amount
    rate = conversion_rate.get(from_currency, {}).get(to_currency, None)
    if rate is None:
        return 0.0  # Return 0.0  if no valid conversion rate is found
    
    converted_amount = round(amount * rate, 2)
    return converted_amount
