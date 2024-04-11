import re
#Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.


def extrair_numeros_cpf(cpf):
    cpf_numerico = re.sub(r'\D', '', cpf)
    return cpf_numerico
  
def listar(Lista):
    for i in range(len(Lista)):
        print (Lista[i])
        
def filtrar_usuario(CPF, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf" == CPF]]
    return usuarios_filtrados[0] if usuarios_filtrados else None
  
def criar_usuario(Usuarios):
    CPF = input("Digite seu CPF (apenas numeros): ")
    CPF = extrair_numeros_cpf(CPF)
    Usuarios = filtrar_usuario(CPF, Usuarios)
    
    if Usuarios:
      return "Usuario  ja existe"
    elif  len(CPF) != 11  or not CPF.isdigit():
        return "CPF Invalido"
  
    Nome = input("Insira Seu Nome Completo: ")
    Endereco = ("Informe seu endereço (Rua, nº - bairro - cidade/Sigla do estado):  ")
    Data_de_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
          
    Usuarios.append({'Nome': Nome, 'CPF': CPF, 'Data_de_nascimento': Data_de_nascimento, 'Endereco': Endereco})
    
    print ("usuario criado")
        
def criar_conta(conta, Usuarios):
    agencia = "0001"
    numero_conta = len(conta) + 1  #não funcioonaria pra caso houvesse exclusão de contas
    cpf = input("Digite o CPF do usuario cadastrado")
    usuario = filtrar_usuario(cpf, Usuarios)
    
    if usuario:
        conta.append({'conta': numero_conta, 'agencia': agencia, 'usuario': cpf})
    else:
      return "Usuario inexistente"

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."

    elif excedeu_limite:
        return"Operação falhou! O valor do saque excede o limite."

    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
        return saldo,extrato
    else:
        return "Operação falhou! O valor informado é inválido."
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        return "Operação falhou! O valor informado é inválido."
    
def realizar_extrato(saldo, /, * , extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def main():  

  LIMITE_SAQUES = 3
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  conta = []
  
  menu = """
  ============ Paule's bank ===============
  [1] Criar Usuario
  [2] Criar Conta
  [3] Listar Usuarios
  [4] Listar Contas
  [5] Depositar
  [6] Sacar
  [7] Extrato
  [0] Sair
  =========================================
  => """

  while True:

      opcao = input(menu)
          
      if opcao == "1":
          criar_usuario(usuarios)
      
      elif opcao == "2":
          criar_conta(conta, usuarios)
                
      elif opcao == "3":
          listar(usuarios)
          
      elif opcao == "4":
          listar(conta)
      elif opcao == "5":
          valor = float(input("Informe o valor do depósito: "))
          depositar(saldo, valor, extrato)
          
      elif opcao == "6":
          valor = float(input("Informe o valor do saque: "))
          sacar(saldo=saldo,valor=valor ,extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

      elif opcao == "7":
          realizar_extrato(saldo, extrato=extrato)

      elif opcao == "0":
          break

      else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")
          
main()