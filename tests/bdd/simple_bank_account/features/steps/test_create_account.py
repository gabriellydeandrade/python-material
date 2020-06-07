from behave import *
from simple_bank_account import SimpleBankAccount


@when("a conta do cliente for criada")
def test_create_account(context):
    account = SimpleBankAccount(number=1, password=123456)
    context.result = account.balance


@then("o saldo de sua conta deve estar zerado")
def test_create_account(context):
    assert context.result == 0


