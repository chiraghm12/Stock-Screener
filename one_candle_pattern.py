"""
One Candle Stick Pattern Script for Stock Screener
"""

import utils

SYMBOLS = utils.get_symbols()


def initialize_files():
    """
    Method for initialize the csv files
    """
    # initialize the Hmamer pattern file
    utils.write_to_csv_file(file_name="Hammer", mode="w", data="NAME")

    # initialize the Inverted_Hammer pattern file
    utils.write_to_csv_file(file_name="Inverted_Hammer", mode="w", data="NAME")

    # initialize the Doji pattern file
    utils.write_to_csv_file(file_name="Doji", mode="w", data="NAME")

    # initialize the Spinning_Top_Bottom pattern file
    utils.write_to_csv_file(file_name="Spinning_Top_Bottom", mode="w", data="NAME")


def filter_data():
    """
    Method for filter the data for single candle stick pattern
    """
    date = utils.get_date_for_one_candle()

    for symbol in SYMBOLS:
        print(symbol)
        # "https://www.nseindia.com/api/historical/securityArchives?from=24-12-2024&to=25-12-2024&symbol=KFINTECH&dataType=priceVolumeDeliverable&series=EQ"
        url = f"https://www.nseindia.com/api/historical/securityArchives?from={date}&to={date}&symbol={utils.symbol_purify(symbol)}&dataType=priceVolumeDeliverable&series=ALL"

        feed = utils.fetch_data_from_nse(url)

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
            utils.write_to_csv_file(file_name="Hammer", mode="a", data=name)

        if utils.is_inverted_hammer(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            utils.write_to_csv_file(file_name="Inverted_Hammer", mode="a", data=name)

        if utils.is_doji(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            utils.write_to_csv_file(file_name="Doji", mode="a", data=name)

        if utils.is_spinning_top_bottom(
            high_price=high_price,
            close_price=close_price,
            open_price=open_price,
            low_price=low_price,
        ):
            # Append to CSV
            utils.write_to_csv_file(
                file_name="Spinning_Top_Bottom", mode="a", data=name
            )


if __name__ == "__main__":
    initialize_files()
    print("Filtering...")
    filter_data()
    print("Finished..!!")
