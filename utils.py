def press_enter(screen, enterX, enterY):
    screen.addstr(enterX, enterY, "Press Enter to continue")
    enter = False
    while enter != True:
        enter = True if screen.getch() == ord('\n') else False
    screen.clear()
    screen.refresh()


def get_input(screen, curses, indications, instructions):
    curses.echo(1)
    screen.addstr(0, 0, indications)
    screen.addstr(1, 0, instructions)
    stock = screen.getstr(0, 32).decode('UTF-8')
    curses.noecho()

    return stock


def print_menu(screen, curses):
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


def select_option(option, screen, curses):
    curses.noecho()
    while (option < 0 or option > 4):
        option = screen.getch()-48
    return option
