# Learning Objective:
# This tutorial will teach you how to develop a simple command-line tool in Python
# to track a mock stock portfolio. You will learn to:
# 1. Use an external library (`yfinance`) to fetch real-time financial data.
# 2. Understand basic API interaction (abstracted by the library).
# 3. Process and display structured data (like stock prices and company names).
# 4. Build a basic command-line interface (CLI) to accept stock symbols.
# 5. Implement fundamental error handling for robust applications.

# --- Step 1: Import necessary libraries ---

# The 'yfinance' library (often aliased as 'yf') is an open-source tool
# that allows Python users to download historical market data and real-time quotes
# from Yahoo Finance. It simplifies the process of interacting with financial data APIs.
# You might need to install it first: pip install yfinance
import yfinance as yf

# The 'sys' module provides access to system-specific parameters and functions.
# We'll use 'sys.argv' to read command-line arguments provided by the user.
import sys

# --- Step 2: Define your mock portfolio and configuration ---

# This list holds the stock ticker symbols for our default mock portfolio.
# These are widely recognized companies, making it easy to test.
DEFAULT_PORTFOLIO_TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# --- Step 3: Function to fetch real-time stock data ---

# This function takes a single ticker symbol as input and attempts to
# retrieve its current market data using 'yfinance'.
def fetch_stock_data(ticker_symbol):
    """
    Fetches real-time stock data for a given ticker symbol.

    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., "AAPL").

    Returns:
        dict: A dictionary containing relevant stock information (name, price)
              or None if data cannot be fetched.
    """
    # Create a Ticker object for the given symbol.
    # This object acts as an interface to Yahoo Finance data for that specific stock.
    ticker = yf.Ticker(ticker_symbol)

    try:
        # The '.info' attribute of the Ticker object contains a dictionary
        # with a wide range of financial information for the stock.
        # We're specifically interested in the 'shortName' (company name)
        # and 'regularMarketPrice' (current price).
        stock_info = ticker.info

        # Check if we successfully retrieved necessary data.
        # Sometimes, for invalid tickers or network issues, these keys might be missing.
        if 'shortName' in stock_info and 'regularMarketPrice' in stock_info:
            return {
                "symbol": ticker_symbol.upper(), # Ensure symbol is uppercase for consistency
                "name": stock_info['shortName'],
                "price": stock_info['regularMarketPrice']
            }
        else:
            # If essential keys are missing, it means we couldn't get full data.
            print(f"Warning: Could not get full data for {ticker_symbol.upper()}. Missing info.")
            return None
    except Exception as e:
        # This 'try-except' block is crucial for error handling.
        # If the ticker symbol is invalid, or there's a network issue,
        # 'yfinance' might raise an exception. We catch it here to prevent
        # the program from crashing and provide a user-friendly message.
        print(f"Error fetching data for {ticker_symbol.upper()}: {e}")
        return None

# --- Step 4: Function to display stock information ---

# This function takes the processed stock data (from fetch_stock_data)
# and prints it in a nicely formatted way to the console.
def display_stock_info(stock_data):
    """
    Displays the fetched stock information in a user-friendly format.

    Args:
        stock_data (dict): A dictionary containing 'symbol', 'name', and 'price'.
    """
    # F-strings (formatted string literals) are a modern Python feature
    # that make string formatting very easy and readable.
    # Here, we're displaying the symbol, company name, and price,
    # formatted to two decimal places for currency.
    print(f"[{stock_data['symbol']}] {stock_data['name']}: ${stock_data['price']:.2f}")

# --- Step 5: Main function to run the command-line tool ---

# The 'main' function orchestrates the entire process.
# It determines which tickers to track based on user input (command-line arguments)
# and then fetches and displays data for them.
def main():
    """
    Main function to parse command-line arguments and track stock portfolio.
    """
    # 'sys.argv' is a list in Python that contains the command-line arguments
    # passed to the script. The first element (sys.argv[0]) is always the
    # name of the script itself.
    # So, if len(sys.argv) > 1, it means the user provided additional arguments.
    if len(sys.argv) > 1:
        # If arguments are provided, these are treated as the ticker symbols
        # the user wants to look up. We slice 'sys.argv' from the second element onwards.
        tickers_to_track = [arg.upper() for arg in sys.argv[1:]]
        print(f"\n--- Tracking specified tickers: {', '.join(tickers_to_track)} ---")
    else:
        # If no arguments are provided, we default to tracking our predefined portfolio.
        tickers_to_track = DEFAULT_PORTFOLIO_TICKERS
        print("\n--- Tracking default portfolio ---")

    # Iterate through each ticker symbol in our chosen list.
    for ticker_symbol in tickers_to_track:
        # Call our function to get the data for the current ticker.
        data = fetch_stock_data(ticker_symbol)
        if data:
            # If data was successfully fetched (not None), display it.
            display_stock_info(data)
        else:
            # If data was not fetched (e.g., due to an error), inform the user.
            print(f"Could not retrieve data for {ticker_symbol.upper()}.")

    print("\n--- Update Complete ---")

# --- Step 6: Entry point for the script ---

# This conditional block ensures that the 'main()' function is called
# only when the script is executed directly (not when it's imported as a module).
# This is a common and important Python idiom for structuring scripts.
if __name__ == "__main__":
    main()

# --- Example Usage (How to run this script from your terminal) ---

# 1. Save this code as a Python file, for example, 'stock_tracker.py'.

# 2. Make sure you have the 'yfinance' library installed:
#    pip install yfinance

# 3. Open your terminal or command prompt.

# 4. To track the default portfolio (AAPL, GOOGL, MSFT, AMZN, TSLA):
#    python stock_tracker.py

# 5. To track specific tickers (e.g., NVIDIA and Netflix):
#    python stock_tracker.py NVDA NFLX

# 6. To track a single ticker (e.g., Intel):
#    python stock_tracker.py INTC

# 7. To see an error example (for an invalid ticker):
#    python stock_tracker.py NOTASTOCK