from account import Account


class MyAccount(Account):
    def panic(self):
        self.withdraw(self.balance)


a = MyAccount('ryan', 10000000000000)
print(a.balance)
a.panic()
print(a.balance)
