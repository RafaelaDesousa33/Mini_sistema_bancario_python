"""
Mini sistema bancário
Funções: criar conta, depositar, sacar, transferir
Pode usar *args para depósitos múltiplos e **kwargs para detalhes da conta
"""
nomeInput = ""
cpfInput = ""
saldoInput = 0

      
def criarConta():
    global nomeInput 
    global cpfInput 
    global saldoInput 

    nomeInput = input("Digite o seu nome:")
    cpfInput = input("Digite seu cpf:")
    saldoInput = float(input("Digite seu saldo:"))

    print("Titular:" , nomeInput)
    print("Cpf:" , cpfInput)
    print(f"saldo: R${saldoInput}")

def depositar():
  global saldoInput
  valorDigitado = float(input("Digite o valor que deseja depositar:"))
  if valorDigitado != 0:
     saldoInput+=valorDigitado
  else:
     print("Valor invalido")

def sacar():
   global saldoInput
   valorDigitado = float(input("Digite o valor que deseja sacar:"))
   if valorDigitado <= saldoInput:
      saldoInput-=valorDigitado
   else:
      print("Valor invalido")

def mostrarSaldo():
    print(f"Saldo: R${saldoInput}")



while True:
    print("Escolha uma opção: criar conta | depositar | sacar | saldo | sair")
    escolha = input("Digite sua escolha: ").lower()

    if escolha == "criar conta":
        criarConta()
    elif escolha == "depositar":
        depositar()
    elif escolha == "sacar":
        sacar()
    elif escolha == "saldo":
        mostrarSaldo()
    elif escolha == "sair":
        print("Programa encerrado.")
        break



