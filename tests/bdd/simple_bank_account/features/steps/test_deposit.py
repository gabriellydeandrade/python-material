from behave import *
from simple_bank_account import SimpleBankAccount


@given("que o cliente já tenha uma conta")
def user_account(context):
    account = SimpleBankAccount(name="Seiji Amasawa", number=2, password=654321)
    context.account = account


@when("o cliente estiver autenticado")
def is_authenticated(context):
    context.account.authenticate(number=2, password=654321)
    assert context.account.is_authenticated is True


@when("informar o valor a ser depositado")
def deposit_value(context):
    context.account.deposit(quantity=100)
    context.result = context.account.balance


@then("o valor é adicionado em sua conta")
def validate_deposit_successful(context):
    assert context.result == 100


@when("o cliente não estiver autenticado")
def is_not_authenticated(context):
    context.value_before_deposit_operation = context.account.balance
    assert context.account.is_authenticated is False


@then("operação de depósito não é realizada")
def validate_deposit_is_not_successful(context):
    context.account.deposit(quantity=100)
    assert context.value_before_deposit_operation == context.account.balance


