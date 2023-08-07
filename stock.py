from stockobserver import Observer


class Stock(Observer):
    _symbol = ""
    _quantity = 0
    _open_price = 0.0
    _price = 0.0
    _variation = 0.0
    _name = ""

    def __init__(self, sym, qt, pr, name, op):
        self._symbol = sym
        self._quantity = qt
        self._open_price = op
        self._price = pr
        self._variation = abs(
            self._open_price - self._price) / self._price * 100
        self._name = name

    def update_variation(self):
        return (self._open_price - self._price) / self._price * 100

    def update(self):
        if self._open_price != self._price:
            change = self.update_variation()
            if change > 1.0 or change < -1.0:
                return True

    def print(self, idx, curses, screen):
        text = "The stock " + self._name + " had a change since opening of: "
        variation = self._variation
        # Initialize color pairs
        curses.start_color()
        if variation < 1:
            color = curses.COLOR_GREEN
        else:
            color = curses.COLOR_RED
        variation = "%0.3f" % variation + "%"
        # Color pair 1 (green on black)
        curses.init_pair(1, color, curses.COLOR_BLACK)

        # Print the text in default color (usually white on black)
        screen.addstr(idx, 0, text)

        # Print the 'variation' text in green
        screen.addstr(idx, len(text), str(variation), curses.color_pair(1))

        screen.refresh()
