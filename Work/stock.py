# stock.py

from typedproperty import String, Integer, Float

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    __slots__ = ('_name','_shares','_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    '''
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected an float')
        self._price = value
    '''

    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price
    
    def sell(self, sells):
        '''
        Sell a number of shares and return the remaining number.
        '''
        self.shares -= sells