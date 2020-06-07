from behave import *
from simple_bank_account import SimpleBankAccount


@when("o cliente estiver autenticado")
def is_authenticated(context):
    account = SimpleBankAccount(number=1, password=123456)
    account.authenticate(number=1, password=123456)
    context.account = account
    assert account.is_authenticated is True


@when("informar o valor a ser depositado")
def deposit_value(context):
    context.account.deposit(quantity=100)
    context.result = context.account.balance


@then("o valor é adicionado em sua conta")
def assert_deposit_successful(context):
    assert context.result == 100


@when("o cliente não estiver autenticado")
def is_not_authenticated(context):
    account = SimpleBankAccount(number=1, password=123456)
    context.value_before_deposit_operation = account.balance
    context.account = account
    assert account.is_authenticated is False


@then("operação de depósito não é realizada")
def assert_deposit_is_not_successful(context):
    assert context.value_before_deposit_operation == context.account.balance


