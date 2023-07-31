class Stock:
    _symbol = ""
    _quantity = 0
    _price = 0.0
    _name = ""

    def __init__(self, sym, qt, pr, name):
        self._symbol = sym
        self._quantity = qt
        self._price = pr
        self._name = name
