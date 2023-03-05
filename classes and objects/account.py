class Account:
    def __int__(self, id: int, name: str, balance: int):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount) -> str:
        self.balance += amount
        return f"{self.balance}"

    def debit(self, amount) -> str:
        if amount <= self.balance:
            self.balance - amount
            return f"{self.balance}"

        else:
            return f"Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {id} has {self.balance} balance"


