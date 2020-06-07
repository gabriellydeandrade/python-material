from behave import when, then
from random import randint


@when('o cliente tiver o saldo de "{valor:d}" reais disponível na conta')
def has_money_in_account(context, valor):
    context.account.balance = valor


@then('"{valor:d}" reais poderá ser debitado de sua conta')
def money_could_be_withdrawn(context, valor):
    context.value_before = context.account.balance
    context.account.withdraw(quantity=valor)

    context.value_after = context.account.balance

    assert context.value_after == context.value_before - valor, "{} != {}".format(context.value_after, context.value_before - valor)


@then('"{valor:d}" reais não é debitado de sua conta')
def money_could_not_be_withdrawn(context, valor):
    context.value_before = context.account.balance
    r = context.account.withdraw(quantity=valor)

    context.value_after = context.account.balance

    assert context.value_after == context.value_before, "{} != {}".format(context.value_after, context.value_before - valor)
    assert r == "Saldo não disponível", "{} != Saldo não disponível".format(r)


@when("o cliente não estiver autenticado para sacar")
def is_not_authenticated(context):
    context.value_before_withdraw_operation = context.account.balance
    assert context.account.is_authenticated is False


@then('valor não é debitado em conta')
def money_could_not_be_withdrawn_if_client_is_not_authenticated(context):
    context.value_before = context.account.balance
    r = context.account.withdraw(quantity=randint(10, 100))

    context.value_after = context.account.balance

    assert context.value_after == context.value_before, "{} != {}".format(context.value_after, context.value_before - valor)

