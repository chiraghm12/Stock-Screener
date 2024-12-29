"""
Two Candle Stick Pattern Script for Stock Screener
"""

import utils

# get the symbols of Nifty500
SYMBOLS = utils.get_symbols()


def initialize_files():
    """
    Method for Initialize the new file:
    """
    # initialize the bullish engulfing pattern file
    utils.write_to_csv_file(file_name="Bullish_Engulfing", mode="w", data="NAME")

    # initialize the bearish engulfing pattern file
    utils.write_to_csv_file(file_name="Bearish_Engulfing", mode="w", data="NAME")

    # initialize the bullish kicker pattern file
    utils.write_to_csv_file(file_name="Bullish_Kicker", mode="w", data="NAME")

    # initialize the bearish kicker pattern file
    utils.write_to_csv_file(file_name="Bearish_Kicker", mode="w", data="NAME")

    # initialize the pro gap positive pattern file
    utils.write_to_csv_file(file_name="Pro_Gap_Positive", mode="w", data="NAME")


def filter_two_candle_pattern():
    """
    Method for filter the data for two candle stick pattern
    """
    # get the date for data fetch
    from_date, to_date = utils.get_date_for_two_candle()

    for symbol in SYMBOLS:
        print(symbol)

        # "https://www.nseindia.com/api/historical/securityArchives?from=24-12-2024&to=25-12-2024&symbol=KFINTECH&dataType=priceVolumeDeliverable&series=EQ"
        url = f"https://www.nseindia.com/api/historical/securityArchives?from={from_date}&to={to_date}&symbol={utils.symbol_purify(symbol)}&dataType=priceVolumeDeliverable&series=ALL"

        feed = utils.fetch_data_from_nse(url)

        # get the data of two days
        first_candle_data = feed.get("data")[0]
        second_candle_data = feed.get("data")[1]

        # get the name of symbol
        name = first_candle_data.get("CH_SYMBOL")

        # check for bullish engulfing
        if utils.is_bullish_engulfing(
            first_candle=first_candle_data, second_candle=second_candle_data
        ):
            utils.write_to_csv_file(file_name="Bullish_Engulfing", mode="a", data=name)

        # check for bearish engulfing
        if utils.is_bearish_engulfing(
            first_candle=first_candle_data, second_candle=second_candle_data
        ):
            utils.write_to_csv_file(file_name="Bearish_Engulfing", mode="a", data=name)

        # check for bullish kicker
        if utils.is_bullish_kicker(
            first_candle=first_candle_data, second_candle=second_candle_data
        ):
            utils.write_to_csv_file(file_name="Bullish_Kicker", mode="a", data=name)

        # check for bearish kicker
        if utils.is_bearish_kicker(
            first_candle=first_candle_data, second_candle=second_candle_data
        ):
            utils.write_to_csv_file(file_name="Bearish_Kicker", mode="a", data=name)

        # check for pro gap positive
        if utils.is_pro_gap_positive(
            first_candle=first_candle_data, second_candle=second_candle_data
        ):
            utils.write_to_csv_file(file_name="Pro_Gap_Positive", mode="a", data=name)


if __name__ == "__main__":
    # main method
    initialize_files()
    print("Filtering...")
    filter_two_candle_pattern()
    print("Finished..!!")
