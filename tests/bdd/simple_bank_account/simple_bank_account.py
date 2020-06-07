class SimpleBankAccount:
    def __init__(self, name: str, number: int, password: int):
        self.client_name = name
        self.number = number
        self.password = password
        self.balance = 0
        self.is_authenticated = False

    def authenticate(self, number: int, password: int):
        if number == self.number and password == self.password:
            self.is_authenticated = True

    def deposit(self, quantity: float):
        if self.is_authenticated:
            self.balance += quantity


