#language: pt

Funcionalidade: sacar

  Cenário: cliente saca se tiver saldo
   Quando cliente está autenticado
     E possui dinheiro disponível
   Entao valor é debitado em conta

  Cenário: cliente não saca se o saldo for insuficiente
   Quando cliente está autenticado
     E não possui dinheiro disponível
   Entao valor não é debitado em conta

  Cenário: cliente não saca se não estiver autenticado
   Quando cliente não está autenticado
   Entao valor não é debitado em conta