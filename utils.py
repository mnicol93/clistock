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
