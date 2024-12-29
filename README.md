# Stock-Screener
Stock Screener for NIFTY500 Stocks. Screener Filter the CandleStick Pattern occurs in Stocks.

Screener filter following CandleStick Patterns:
* **Hammer**
* **Inverted Hammer**
* **Doji**
* **Spinning Top / Bottom**
* **Engulfing (Bullish/Bearish)**
* **Kicker (Bullish/Bearish)**
* **Pro Gap Positive**

## Installation

#### Prerequisites
* Python 3.8 or Later

## Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2 Create Virtual Environment
    ```
    python -m venv venv
    ```

3. Activate the Virtual Environment:

    * On Windows:

        ```bash
        venv\Scripts\activate
        ```

    * On Mac or Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the file
    * For One Candle-Stick Pattern

        ```
        python -m one_candle_pattern.py
        ```
    * For Two Candle-Stick Pattern

        ```
        python -m two_candle_pattern.py
        ```

## Data and Reports

After Filtering the CandleStick, the application creates a individual CSV files for CandleStick Pattern in the separate folder named CandleStick in the system for particular Date folder.

Two Files:
 - A CSV file contains Stock names with Hammer
 - A CSV file contains stock names with Doji
 - A CSV file contains stock name with Inverted Hammer
 - A CSV file contains stock name with Spinning Top and Bottom
 - A CSV file contains stock name with Engulfing(Bullish/Bearish)
 - A CSV file contains stock name with Kicker(Bullish/Bearish)
 - A CSV file contains stock name with Pro Gap Positive

## Acknowledgements

We would like to thank the following resources and libraries that made this project possible:

* **Open Source Community**: For providing valuable resources, libraries, and tools that aid in the development of web applications.
* **NSE**: We would like to express our gratitude to the NSE for making stock market data accessible, which has helped in the development of this project.


## Disclaimer
The use of NSE data is intended for informational and educational purposes only. This project is neither affiliated with nor endorsed by the National Stock Exchange of India. We are not responsible for any inaccuracies or misuse of the data within this project.
