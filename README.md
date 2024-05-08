# Desafio: Sistema Bancário em Python
### Introdução
Este documento fornece uma visão geral do código desenvolvido para o desafio do bootcamp [Python AI Backend Developer](https://www.dio.me/bootcamp/coding-future-vivo-python-ai-backend-developer), O sistema simula funcionalidades básicas de um banco, como criação de usuários, criação de contas, depósitos, saques, extratos e listagem de usuários e contas.

### Funcionalidades
1. Criação de Usuário:
A função criar_cliente(clientes) permite a criação de um novo usuário.
O usuário deve fornecer seu CPF, nome completo, data de nascimento e endereço.
O CPF é validado quanto à sua formatação, exigindo 11 dígitos numéricos.
2. Criação de Conta:
A função criar_conta(numero_conta, clientes, contas) permite a criação de uma conta vinculada a um usuário existente.
O número da conta é atribuído automaticamente, e a agência é definida como "0001".
3. Listar Usuários e Contas:
As funções listar_contas(contas) e listar_clientes(clientes) permitem listar todos os usuários e contas registrados no sistema, respectivamente.
4. Depósito:
A função depositar(clientes) permite aos usuários fazer depósitos em suas contas.
O valor do depósito é adicionado ao saldo da conta e registrado no extrato.
5. Saque:
A função sacar(clientes) permite aos usuários realizar saques de suas contas.
São realizadas verificações para garantir que o saldo da conta não seja excedido, que o valor do saque não exceda o limite definido e que o número máximo de saques não tenha sido atingido.
6. Extrato:
A função realizar_extrato(clientes) permite que os usuários visualizem o extrato de sua conta, incluindo todas as transações realizadas e o saldo atual.
### Diagrama UML

![Trilha Python - desafio](https://github.com/paulemacedo/sistema-bancario-python/assets/59907505/a6c17a07-b24f-4c49-afba-cabbf35a66f3)

### Considerações Finais
O sistema "Paule's Bank" oferece uma funcionalidade básica de banco, permitindo aos usuários realizar operações bancárias simples. Para um ambiente de produção, seria necessário adicionar mais funcionalidades, como transferências entre contas, autenticação de usuários e medidas de segurança adicionais. O diagrama UML fornece uma visão geral da estrutura de classes do sistema.

