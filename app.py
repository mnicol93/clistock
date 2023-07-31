import curses
import argparse
from PyInquirer import prompt, print_json
#Handle screen content
screen = curses.initscr()

def print_menu():
    curses.curs_set(0)
    screen.addstr(0,2,"Welcome to CLIStock! What would you like to do? Please, introduce a number\n")
    screen.addstr(1,2,"==========================================================================\n")
    
    screen.addstr(2,3, "1. Check portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(3,3, "2. Check individual stock price")
    screen.refresh()
    curses.napms(200)
    screen.addstr(4,3, "3. Add stock to portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(5,3, "4. Sell stock from portfolio")
    screen.refresh()
    curses.napms(200)
    screen.addstr(6,3, "0. Exit")
def select_option(option):
    curses.noecho()
    while(option == -1):
        option = screen.getch()-48
    return option
    
def menu():
    option = -1
    print_menu()
    option = select_option(option)
    curses.curs_set(1)
    if option == 0:
        screen.addstr(6,3,"")
        screen.refresh()
    else:
        screen.addstr(option+1,3,"")
        #Call function selected by user
        options[option]()
    screen.refresh()

    curses.napms(1000)
    
def buy_stock():
    return 0
def sell_stock():
    return 0
def check_stock():
    return 0
def show_portfolio():
    return 0

#List storing menu functions to call dynamically
options = [None, show_portfolio, check_stock, buy_stock, sell_stock]

menu()
screen.refresh()
curses.endwin()