from behave import *
from test.bdd.simple_bank_account.code.simple_bank_account import SimpleBankAccount


@when("a conta do cliente for criada")
def create_account(context):
    account = SimpleBankAccount(number=1, password=123456)
    context.result = account.balance


@then("o saldo de sua conta deverá ser nulo")
def create_account(context):
    assert context.result == 0


