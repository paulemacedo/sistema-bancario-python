from abc import ABC, abstractmethod
from datetime import datetime
import textwrap
import re

class conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._agencia = "0001"
        self._numero = numero
        self._saldo = 0
        self._historico = Historico()
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
   
        
    @classmethod
    def nova_conta(cls, cliente, numero ):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
        
        return True
    
class conta_Corrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        saldo_insuficiente = valor > self.saldo
        
        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        if excedeu_saques:
            print("Operação falhou! Número de saques excedido.")
        if saldo_insuficiente:
            print("Operação falhou! Saldo insuficiente.")
        else: 
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f''' 
            Agência: {self.agencia}
            Conta: {self.numero}
            Titular: {self.cliente.nome}
            '''
            
class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
        
    def add_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transaçao(self, conta, transacao):
        transacao.register(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class cliente_PF(cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Transacao(ABC):
    
    @property 
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def register(cls, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    
    def register(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.add_transacao(self)
        
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    
    def register(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.add_transacao(self)
        #FIXME: não permite cliente escolher a conta

def menu():
  menu = """
  ============ Paule's bank ===============
  [1] Criar Clientes
  [2] Criar Conta
  [3] Listar Contas
  [4] Depositar
  [5] Sacar
  [6] Extrato
  [0] Sair
  =========================================
  => """
  return input(menu)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    #FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def realizar_transacao(clientes, tipo_transacao):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Informe o valor da transação: "))
    transacao = tipo_transacao(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta")
        return
    
    cliente.realizar_transacao(conta, transacao)

def realizar_extrato(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta")
        return
    
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações"
    else: 
        for transacao in transacoes:
            extrato += f"\n {transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo:\n\t R$ {conta.saldo:.2f}")
    print("==========================================")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o CPF do cliente")
    cpf = extrair_numeros_cpf(cpf)
    
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = conta_Corrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n conta criada com sucesso")

def extrair_numeros_cpf(cpf):
    cpf_numerico = re.sub(r'\D', '', cpf)
    return cpf_numerico

def criar_cliente(clientes):
    cpf = input("Digite o CPF do cliente")
    cpf = extrair_numeros_cpf(cpf)
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("Cliente ja cadastrado")
        return
    elif  len(cpf) != 11  or not cpf.isdigit():
        print("CPF Invalido")
        return 
    
    nome = input("Digite o nome do cliente")
    data_de_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = ("Informe seu endereço (Rua, nº - bairro - cidade/Sigla do estado):  ")
    
    cliente = cliente_PF(nome=nome, data_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)
    
    print("\n cliente criado com sucesso")    
    
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print (textwrap.dedent(str(conta)))
        
def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        
        if opcao == "1":
            criar_cliente(clientes)
        
        elif opcao == "2":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "3":
            listar_contas(contas)
            
        elif opcao == "4":
            realizar_transacao(clientes, Deposito)
            
        elif opcao == "5":
            realizar_transacao(clientes, Saque)

        elif opcao == "6":
            realizar_extrato(clientes)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()