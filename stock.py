class Stock:
    _symbol = ""
    _quantity = 0
    _price = 0.0

    def __init__(self, sym, qt, pr):
        self._symbol = sym
        self._quantity = qt
        self._price = pr
