"""
Script has Utility Methods
"""

import csv
import os


def initialize_files():
    """
    Method for Initialize the csv files for store the Stocks name according to the pattern.
    """

    if not os.path.exists("CandleStick"):
        os.mkdir("CandleStick")

    # initialize file for Hammer
    file_path = os.path.join("CandleStick", "Hammer.csv")
    with open(file_path, mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name"])

    # initialize file for Doji
    file_path = os.path.join("CandleStick", "Doji.csv")
    with open(file_path, mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name"])

    # initialize file for Inverted Hammer
    file_path = os.path.join("CandleStick", "Inverted_Hammer.csv")
    with open(file_path, mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name"])

    # initialize file for Spinning Top-Bottom
    file_path = os.path.join("CandleStick", "Spinning_Top_Bottom.csv")
    with open(file_path, mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name"])


def is_inverted_hammer(open_price, high_price, low_price, close_price):
    """
    Method for check if candle is inverted hammer or not.

    Args:
        open_price (float): candle's open price
        high_price (float): candle's high price
        low_price (float): candle's low price
        close_price (float): candle's close price

    Returns:
        bool: True or False
    """
    if open_price == 0 and close_price == 0 and low_price == 0 and high_price == 0:
        return False

    if open_price == close_price == high_price == low_price:
        return False

    body = abs(close_price - open_price)  # Real body
    lower_shadow = 0
    upper_shadow = 0
    if close_price > open_price:
        upper_shadow = high_price - close_price
        lower_shadow = open_price - low_price
    else:
        upper_shadow = high_price - open_price
        lower_shadow = close_price - low_price

    if (upper_shadow >= (body * 2)) and (lower_shadow <= (body * 0.5)):
        return True
    return False


def is_hammer(open_price, high_price, low_price, close_price):
    """
    Method for check if candle is hammer or not.

    Args:
        open_price (float): candle's open price
        high_price (float): candle's high price
        low_price (float): candle's low price
        close_price (float): candle's close price

    Returns:
        bool: True or False
    """
    if open_price == 0 and close_price == 0 and low_price == 0 and high_price == 0:
        return False

    if open_price == close_price == high_price == low_price:
        return False

    body = abs(close_price - open_price)  # Real body
    lower_shadow = 0
    upper_shadow = 0
    if close_price > open_price:
        upper_shadow = high_price - close_price
        lower_shadow = open_price - low_price
    else:
        upper_shadow = high_price - open_price
        lower_shadow = close_price - low_price

    if (lower_shadow >= (body * 2)) and (upper_shadow <= (body * 0.5)):
        return True
    return False


def is_spinning_top_bottom(open_price, high_price, low_price, close_price):
    """
    Method for check if candle is spinning top-bottom or not.

    Args:
        open_price (float): candle's open price
        high_price (float): candle's high price
        low_price (float): candle's low price
        close_price (float): candle's close price

    Returns:
        bool: True or False
    """
    if open_price == 0 and close_price == 0 and low_price == 0 and high_price == 0:
        return False

    if open_price == close_price == high_price == low_price:
        return False

    body = abs(close_price - open_price)  # Real body
    lower_shadow = 0
    upper_shadow = 0

    if close_price > open_price:
        upper_shadow = high_price - close_price
        lower_shadow = open_price - low_price
    else:
        upper_shadow = high_price - open_price
        lower_shadow = close_price - low_price

    if (lower_shadow >= body * 1.5) and (upper_shadow >= body * 1.5):
        return True

    return False


def is_doji(open_price, high_price, low_price, close_price):
    """
    Method for check if candle is doji or not.

    Args:
        open_price (float): candle's open price
        high_price (float): candle's high price
        low_price (float): candle's low price
        close_price (float): candle's close price

    Returns:
        bool: True or False
    """
    if open_price == close_price == high_price == low_price:
        return False

    if open_price == close_price:
        return True

    return False


def symbol_purify(symbol):
    """
    Method for purify the symbol for use in query params
    """
    symbol = symbol.replace("&", "%26")  # URL Parse for Stocks Like M&M Finance
    return symbol
