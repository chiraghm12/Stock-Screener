"""
Script for Stock Screener
"""

import csv
import os
from datetime import datetime

import requests

import utils

TODAY_DATE = datetime.now().strftime("%d-%m-%Y")
SYMBOLS = []
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,en-IN;q=0.8,en-GB;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
}


def fetch_data_from_nse(link):
    """
    Method for fetch the data from nse.
    """
    try:
        output = requests.get(link, headers=HEADERS, timeout=300).json()
        # print(output)
    except ValueError:
        s = requests.Session()
        output = s.get("http://nseindia.com", headers=HEADERS)
        output = s.get(link, headers=HEADERS).json()
    return output


def fetch_instrument_keys_from_csv():
    """
    Method for get the instruments key of Nifty500 Stocks.
    """
    csv_file_path = "Nifty500.csv"
    column_name = "Symbol"
    global SYMBOLS  # pylint:disable=W0602

    # Open and read the CSV file
    with open(csv_file_path, mode="r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)  # Use DictReader to access columns by name
        for row in reader:
            # Extract only the desired columns
            SYMBOLS.append(row[column_name])

    # print("Column values:", len(SYMBOLS))
    # print(SYMBOLS)


def filter_data():
    """
    Method for filter the data
    """
    for symbol in SYMBOLS:
        print(symbol)
        # "https://www.nseindia.com/api/historical/securityArchives?from=24-12-2024&to=25-12-2024&symbol=KFINTECH&dataType=priceVolumeDeliverable&series=EQ"
        url = f"https://www.nseindia.com/api/historical/securityArchives?from={TODAY_DATE}&to={TODAY_DATE}&symbol={utils.symbol_purify(symbol)}&dataType=priceVolumeDeliverable&series=ALL"

        feed = fetch_data_from_nse(url)

        data = feed.get("data")[0]
        high_price = data.get("CH_TRADE_HIGH_PRICE")
        low_price = data.get("CH_TRADE_LOW_PRICE")
        open_price = data.get("CH_OPENING_PRICE")
        close_price = data.get("CH_CLOSING_PRICE")
        name = data.get("CH_SYMBOL")

        if utils.is_hammer(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            file_path = os.path.join("CandleStick", "Hammer.csv")
            with open(file_path, mode="a", newline="", encoding="UTF-8") as hammer_file:
                writer = csv.writer(hammer_file)
                writer.writerow([name])

        if utils.is_inverted_hammer(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            file_path = os.path.join("CandleStick", "Inverted_Hammer.csv")
            with open(
                file_path, mode="a", newline="", encoding="UTF-8"
            ) as inverted_hammer_file:
                writer = csv.writer(inverted_hammer_file)
                writer.writerow([name])

        if utils.is_doji(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            file_path = os.path.join("CandleStick", "Doji.csv")
            with open(file_path, mode="a", newline="", encoding="UTF-8") as doji_file:
                writer = csv.writer(doji_file)
                writer.writerow([name])

        if utils.is_spinning_top_bottom(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            file_path = os.path.join("CandleStick", "Spinning_Top_Bottom.csv")
            with open(
                file_path, mode="a", newline="", encoding="UTF-8"
            ) as spinning_top_bottom_file:
                writer = csv.writer(spinning_top_bottom_file)
                writer.writerow([name])


if __name__ == "__main__":
    utils.initialize_files()
    fetch_instrument_keys_from_csv()
    print("Filtering...")
    filter_data()
    print("Finished..!!")
