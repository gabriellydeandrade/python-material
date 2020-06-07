# language: pt

Funcionalidade: criar conta

  """
    Como cliente, eu quero que seja possível criar uma nova conta no banco para possibilitar depositar e sacar dinheiro
  """

  Cenário: cliente solicita criação de conta
    Quando a conta do cliente for criada
    Entao o saldo de sua conta deve estar zerado
