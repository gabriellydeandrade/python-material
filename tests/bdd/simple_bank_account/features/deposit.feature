#language: pt

Funcionalidade: depositar

    """
      Como cliente, eu quero que seja possível depositar dinheiro em minha própria conta
    """

  @cliente_tem_conta
  @cliente_autenticado
  Cenário: cliente deposita dinheiro se estiver autenticado
    Quando o cliente informar o valor a ser depositado
    Então o valor é adicionado em sua conta

  @cliente_tem_conta
  Cenário: cliente não deposita dinheiro em conta se não estiver autenticado
    Quando o cliente não estiver autenticado para depositar
    Então operação de depósito não é realizada



