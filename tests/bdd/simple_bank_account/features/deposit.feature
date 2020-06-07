#language: pt

Funcionalidade: depositar dinheiro em conta

    """
      Como cliente, eu quero que seja possível depositar dinheiro em minha própria conta
    """

  Cenário: cliente deposita dinheiro se estiver autenticado
    Dado que o cliente já tenha uma conta
    Quando o cliente estiver autenticado
      E informar o valor a ser depositado
    Então o valor é adicionado em sua conta

  Cenário: cliente não deposita dinheiro em conta se não estiver autenticado
    Dado que o cliente já tenha uma conta
    Quando o cliente não estiver autenticado
    Então operação de depósito não é realizada



