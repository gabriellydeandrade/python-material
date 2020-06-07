class SimpleBankAccount:
    def __init__(self, number: int, password: int):
        self.number = number
        self.password = password
        self.balance = 0
        self.is_authenticated = False

    def authenticate(self, number: int, password: int):
        if number == self.number and password == self.password:
            self.is_authenticated = True

    def deposit(self, quantity: float):
        self.balance += quantity


