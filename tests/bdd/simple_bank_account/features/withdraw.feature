#language: pt

Funcionalidade: sacar
    """
      Como cliente, eu quero que seja possível sacar dinheiro da minha própria conta
    """

  @cliente_tem_conta # Isso é um hook do behave
  @cliente_autenticado
  Cenário: cliente saca se tiver saldo
   Quando o cliente tiver o saldo de "100" reais disponível na conta
   Então  "100" reais poderá ser debitado de sua conta

  @cliente_tem_conta
  @cliente_autenticado
  Cenário: cliente não saca se o saldo for insuficiente
   Quando o cliente tiver o saldo de "100" reais disponível na conta
   Então "101" reais não é debitado de sua conta

  @cliente_tem_conta
  Cenário: cliente não saca se não estiver autenticado
   Quando o cliente não estiver autenticado para sacar
   Então valor não é debitado em conta