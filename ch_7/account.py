class Account:
    """A bank account"""

    owner: str
    balance: float

    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Account({self.owner!r}, {self.balance!r})"

    def withdraw(self, amount:float):
        self.balance -= amount

    def deposit(self, amount:float):
        self.balance += amount

    def inquiry(self) -> float:
        return self.balance


# Calls Account.__init__(a, 'Wade', 1000.0)
a = Account('Wade', 1000.0)
a.deposit(200)

# get
print(a.owner)
print(a.balance)

# set
a.balance = 20.0
print(a.balance)

# delete
del a.balance
# this will cause an error because the attribute doesn't exist
# print(a.balance)


# the instance variables
print(vars(a))
print(type(a))
print(type(a).deposit)
print()




# Calls Account.__init__(a, 'Fay', 40000000.0)
b = Account('Fay', 40000000.0)
b.withdraw(500000)

print(b.owner)
print(b.balance)

# the instance variables
print(vars(b))
print(type(b))
print(type(b).deposit)

#setting new attributes
b.nickname = "FBI"
print(vars(b))

# get
print(getattr(b, 'owner'))
# set
setattr(b, 'balance', 5000000000000000)
print(b.balance)
# delete
# this will cause an error because the attribute doesn't exist
# delattr(b, 'balance')
# print(b.balance)

print(hasattr(b, 'balance'))

# bound method
w = b.withdraw
print(w)
w(100)
print(w)
