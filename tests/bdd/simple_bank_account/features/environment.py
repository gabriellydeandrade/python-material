from simple_bank_account import SimpleBankAccount

# São hooks que podem ser executados antes ou depois dos testes. É um comparativo com a fixture do unittest
# ref doc.: https://behave.readthedocs.io/en/latest/context_attributes.html?highlight=before_all()#context-attributes


def before_tag(context, tag):
    if tag == "cliente_tem_conta":
        account = SimpleBankAccount(client_name="Seiji Amasawa", number=2, password=654321)
        context.account = account

    if tag == "cliente_autenticado":
        context.account.authenticate(number=2, password=654321)


