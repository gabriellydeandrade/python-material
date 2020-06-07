class Client:
    def __init__(self, client_name: str):
        self.name = client_name
        self.is_authenticated = False


class SimpleBankAccount(Client):
    def __init__(self, client_name: str, number: int, password: int):
        super().__init__(client_name=client_name)
        self.number = number
        self.password = password
        self.balance = 0

    def authenticate(self, number: int, password: int):
        if number == self.number and password == self.password:
            self.is_authenticated = True

    def deposit(self, quantity: float):
        if self.is_authenticated:
            self.balance += quantity


