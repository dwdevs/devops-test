import random
import threading

class InsufficientAmount(Exception):
    pass

class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        self.lock = threading.Lock()

    def spend_cash(self, amount):
        with self.lock:
            if self.balance < amount:
                raise InsufficientAmount('Not enough available to spend {}'.format(amount))
            self.balance -= amount

    def add_cash(self, amount):
        with self.lock:
            self.balance += amount
    
    def get_balance(self):
        with self.lock:
            return self.balance

wallet = Wallet(0)