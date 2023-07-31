import curses
import argparse
from stockfetch import StockDataFetcher
from buycommand import BuyStockCommand
from sellcommand import SellStockCommand
from commandinvoker import CommandInvoker
from utils import press_enter

# Handle screen content
screen = curses.initscr()
# Handles all operations with DB and API
sdata = StockDataFetcher()


def print_menu():
    curses.curs_set(0)
    screen.addstr(
        0, 2, "Welcome to CLIStock! What would you like to do? Please, introduce a number\n")
    screen.addstr(
        1, 2, "==========================================================================\n")

    screen.addstr(2, 3, "1. Check portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(3, 3, "2. Check individual stock price")
    screen.refresh()
    curses.napms(200)
    screen.addstr(4, 3, "3. Add stock to portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(5, 3, "4. Sell stock from portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(6, 3, "0. Exit")


def select_option(option):
    curses.noecho()
    while (option < 0 or option > 4):
        option = screen.getch()-48
    return option


def menu():
    option = -1
    print_menu()
    option = select_option(option)
    curses.curs_set(1)
    if option == 0:
        screen.addstr(6, 3, "")
        screen.refresh()
        curses.endwin()
        return 0
    else:
        screen.addstr(option+1, 3, "")

    screen.refresh()

    curses.napms(500)
    screen.clear()
    screen.refresh()
    # Call function selected by user
    options[option]()
    return option


def buy_stock():
    quantity = 5
    symbol = "msft"

    invoker = CommandInvoker()
    buy = BuyStockCommand(symbol, quantity, sdata)

    screen.clear()
    screen.refresh()

    screen.addstr(3, 5, "Buying " + str(quantity) +
                  " shares of " + symbol + ". Please wait...")
    screen.refresh()

    invoker.set_command(buy)
    result = invoker.execute_command()
    screen.addstr(6, 5, "Success! New amount owned of " +
                  result['symbol'] + " is " + str(result['quantity']) + " with an average price of " + str(result['avg_price']) + "$.")
    press_enter(screen, 8, 5)
    screen.refresh()
    curses.napms(1000)
    screen.clear()
    screen.refresh()
    return 0


def sell_stock():
    return 0


def check_stock():
    screen.addstr(0, 0, "Checking stock price, please wait")
    screen.refresh()
    curses.napms(300)
    price = sdata.get_price_str("msft", "&summary=true")

    screen.addstr(2, 0, price)
    screen.refresh()

    press_enter(screen, 3, 0)

    return 0


def show_portfolio():

    return 0


# List storing menu functions to call dynamically
options = [None, show_portfolio, check_stock, buy_stock, sell_stock]


def main():
    option = 1
    while (option > 0):
        option = menu()
        screen.refresh()
    curses.endwin()


if __name__ == "__main__":
    main()
