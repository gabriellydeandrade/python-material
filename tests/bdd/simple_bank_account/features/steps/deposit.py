from behave import when, then


@when("o cliente informar o valor a ser depositado")
def deposit_value(context):
    context.account.deposit(quantity=100)
    context.result = context.account.balance


@then("o valor é adicionado em sua conta")
def validate_deposit_successful(context):
    assert context.result == 100


@when("o cliente não estiver autenticado para depositar")
def is_not_authenticated(context):
    context.value_before_deposit_operation = context.account.balance
    assert context.account.is_authenticated is False


@then("operação de depósito não é realizada")
def validate_deposit_is_not_successful(context):
    context.account.deposit(quantity=100)
    assert context.value_before_deposit_operation == context.account.balance


