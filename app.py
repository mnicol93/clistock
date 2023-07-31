import curses
import argparse
from PyInquirer import prompt, print_json

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
def select_option():
    return 0
def menu():
    option = -1
    print_menu()
    while(option == -1):
        curses.noecho()
        option = screen.getch()-48
        if option == 0:
            screen.addstr(6,2,"")
            screen.refresh()
            return None

    curses.curs_set(1)
    screen.addstr(option+1,3,"")
    screen.refresh()

    curses.napms(1000)
    

menu()
screen.refresh()
curses.endwin()