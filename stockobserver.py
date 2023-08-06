from __future__ import annotations
from abc import ABC, abstractmethod
from collections import defaultdict
from random import randrange
from typing import List


class StockObserver(ABC):

    @abstractmethod
    def attach_observer(self, observer):
        pass

    @abstractmethod
    def detach_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self, curses, screen):
        pass


class StockObserverConcrete(StockObserver):
    # Store all stocks
    _observers = []
    # Store stock-price dictionary
    _stock_list = defaultdict(dict)

    def attach_observer(self, observer):
        self._observers.append(observer)

    def detach_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self, index, curses, screen):
        screen.clear()
        screen.refresh()
        for observer in self._observers:
            index += 1
            observer.print(index, curses, screen)
        return index + 1


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def print(self, idx, curses, screen):
        pass
