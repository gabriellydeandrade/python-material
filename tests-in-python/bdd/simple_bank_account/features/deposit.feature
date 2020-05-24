#language: pt

Funcionalidade: depositar
  Cenario: cliente deposita dinheiro se estiver autenticado
    Quando o cliente estiver autenticado
      E informar o valor a ser depositado
    Entao o valor é adicionado em sua conta

  Cenario: cliente não deposita dinheiro se não estiver autenticado
    Quando o cliente não estiver autenticado
    Entao operação de depósito não é realizada



