import curses
import argparse
from stockfetch import StockDataFetcher
from buycommand import BuyStockCommand
from sellcommand import SellStockCommand
from portfolio import ShowPortfolio
from stock import Stock
from stockobserver import StockObserverConcrete
from commandinvoker import CommandInvoker
from utils import press_enter, get_input, print_menu, select_option

# Handle screen content
screen = curses.initscr()
# Handles all operations with DB and API
sdata = StockDataFetcher()
total_investment = 0


def menu(observer):
    option = -1
    print_menu(screen, curses)
    option = select_option(option, screen, curses)
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
    # Buy Stock
    if option == 1:
        show_portfolio(observer)
    elif option == 3:
        buy_stock(buying=True)
    # Sell Stock
    elif option == 4:
        buy_stock(buying=False)
    else:
        options[option]()
    return option


def buy_stock(buying):
    quantity = -1
    symbol = get_input(screen, curses, "Introduce Stock Symbol: ",
                       "Enter to confirm, backspace to delete")
    while quantity < 1:
        screen.clear()
        screen.refresh()
        quantity = int(get_input(screen, curses, "Introduce Amount of Shares: ",
                                 "Enter to confirm, backspace to delete, Number bigger than 0"))
    text = ""

    invoker = CommandInvoker()
    if buying:
        buy = BuyStockCommand(symbol, quantity, sdata)
        invoker.set_command(buy)
        text = "Buying"
    else:
        sell = SellStockCommand(symbol, quantity, sdata)
        invoker.set_command(sell)
        text = "Selling"

    screen.clear()
    screen.refresh()

    screen.addstr(3, 5, text + " " + str(quantity) +
                  " shares of " + symbol + ". Please wait...")
    screen.refresh()

    result = invoker.execute_command()
    if result == None:
        screen.addstr(6, 5, "You don't own any shares of " + symbol)
        screen.refresh()
        press_enter(screen, 8, 5)
    else:
        screen.addstr(6, 5, "Success! New amount owned of " +
                      result['symbol'] + " is " + str(round(result['quantity'])) + " with an average price of " + str(result['avg_price']) + "$.")
        press_enter(screen, 8, 5)

    screen.clear()
    screen.refresh()

    return 0


def check_stock():
    stock = get_input(screen, curses, "Introduce Stock Symbol: ",
                      "Enter to confirm, backspace to delete")
    price = sdata.get_price(str(stock), "&summary=true")

    screen.addstr(3, 0, price)
    screen.refresh()

    press_enter(screen, 5, 0)

    return 0


def show_portfolio(observer):
    index = 2

    invoker = CommandInvoker()
    portfolio = ShowPortfolio(sdata)

    invoker.set_command(portfolio)
    screen.addstr(
        0, 0, "Symbol--|Name-----------------------------------|Qty--|Price---|Open--|Avg------|P/L------|Benefit------|")
    screen.addstr(
        1, 0, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    result = invoker.execute_command()

    for res in result:
        price = sdata.get_stock_data(res['symbol'], "&summary=true")
        stock = Stock(res['symbol'], res['quantity'],
                      price['Summary']['Price'], res['name'], price['Summary']['PreviousClose'])
        # TESTING:

        # if stock._symbol == 'msft':
        #     stock._price += 40.0

        # Detect whether stock had a variation in price of <> 1% to notify later
        if stock.update():
            observer.attach_observer(stock)
        else:
            observer.detach_observer(stock)
        # Calculations
        avg_price_round = "%0.2f" % res['avg_price']
        benefit = ((res['quantity'] * stock._price) -
                   (res['quantity'] * res['avg_price']))
        pl = "%0.2f" % (
            (benefit/(res['quantity'] * res['avg_price'])) * 100)
        benefit = "%0.2f" % benefit
        # Printing table
        screen.addstr(index, 0, res['symbol'])
        screen.addstr(index, 8, '|' + res['name'])
        screen.addstr(index, 48, '|' + str(res['quantity']))
        screen.addstr(index, 54, '|' + str(stock._price))
        screen.addstr(index, 63, '|' + str(stock._open_price))
        screen.addstr(index, 70, '|' + str(avg_price_round))
        screen.addstr(index, 80, '|' + str(pl) + '%')
        screen.addstr(index, 90, '|' + str(benefit))
        screen.addstr(index, 104, '|')
        screen.addstr(
            index+1, 0, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        index += 2

    press_enter(screen, index + 2, 0)
    index = 0
    # Observer notifies to print the subjects that changed, returns index to print 'Continue'
    index = observer.notify_observer(index, curses, screen)

    press_enter(screen, index + 1, 0)

    return 0


# List storing menu functions to call dynamically
options = [None, show_portfolio, check_stock,
           buy_stock, buy_stock]


def main():
    observer = StockObserverConcrete()
    option = 1
    while (option > 0):
        option = menu(observer)
        screen.refresh()
    curses.endwin()


if __name__ == "__main__":
    main()
