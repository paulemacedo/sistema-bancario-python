menu = '''
##### paule's bank #####
[1] Extrato
[2] Saque
[3] Deposito
[0] Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
3

while True:
  op = input(menu)

  if op == "1":
    print("\n############ extrato ############")
    print("não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("#################################\n")


  elif op == "2":
    valor = float(input("Informe o valor do saque: "))
    if valor > 0 and valor < saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
      limite -= valor
      print("Saque realizado com sucesso")
      numero_saques += 1
      extrato += f"saque: R${valor:.2f}\n"
      
    elif valor > saldo:
      print("Você não posssui saldo para realizar esse saque")
      
    elif numero_saques >= LIMITE_SAQUES or valor > limite:
      print("Limite de saque atingido")

  elif op == "3":
    valor = float(input("Informe o valor do deposito: "))
    
    if valor > 0:
        saldo += valor
        print("deposito realizado com sucesso")
        extrato += f"deposito: R$ {valor:.2f}\n"
    else:
        print("operação falhou! o valor informado é invalido.")


  elif op == "0":
    break

  else:
    print(
        "operação invalida, por favor selecione novamente a operação desejada")
