#language: pt

Funcionalidade: sacar
  Cenario: cliente saca se tiver saldo
   Quando cliente está autenticado
     E possui dinheiro disponível
   Entao valor é debitado em conta

  Cenario: cliente não saca se o saldo for insuficiente
   Quando cliente está autenticado
     E não possui dinheiro disponível
   Entao valor não é debitado em conta

  Cenario: cliente não saca se não estiver autenticado
   Quando cliente não está autenticado
   Entao valor não é debitado em conta