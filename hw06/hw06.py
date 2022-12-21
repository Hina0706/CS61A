passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            next_value = Fib(1)
        else:
            next_value = Fib(self.previous + self.value)
        next_value.previous = self.value
        return next_value


    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price, stock = 0, save = 0):
        self.name = name
        self.price = price
        self.stock = stock
        self.save = save

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.save < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.save)
        elif self.save > self.price:
            change = self.save - self.price
            self.save = 0
            self.stock -= 1
            return 'Here is your {1} and ${0} change.'.format(change, self.name)
        elif self.save == self.price:
            self.save = 0
            self.stock -= 1
            return 'Here is your {0}.'.format(self.name)

    def deposit(self, dollar):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $15.'
        else:
            self.save += dollar
            return 'Current balance: ${0}'.format(self.save)

    def restock(self, number):
        self.stock += number
        return 'Current {1} stock: {0}'.format(self.stock, self.name)


