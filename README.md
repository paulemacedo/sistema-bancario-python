# Desafio: Sistema Bancário em Python
### Introdução
Este documento fornece uma visão geral do código desenvolvido para o desafio do bootcamp [Python AI Backend Developer](https://www.dio.me/bootcamp/coding-future-vivo-python-ai-backend-developer), que simula um sistema bancário básico chamado "Paule's Bank". O código permite a criação de usuários, criação de contas vinculadas a esses usuários, depósitos, saques, extratos e listagem de usuários e contas.

### Funcionalidades
1. Criação de Usuário
A função criar_usuario(Usuarios) permite a criação de um novo usuário. O usuário deve fornecer seu CPF (Cadastro de Pessoa Física) e outras informações pessoais, como nome completo, endereço e data de nascimento. O CPF é validado quanto à sua formatação e deve ter 11 dígitos.

2. Criação de Conta
A função criar_conta(conta, Usuarios) permite a criação de uma conta vinculada a um usuário existente. Para criar uma conta, é necessário fornecer o CPF do usuário ao qual a conta será vinculada. A agência é definida como "0001" e o número da conta é atribuído automaticamente.

3. Listar Usuários e Contas
As funções listar(Usuarios) e listar(conta) permitem listar todos os usuários e contas registrados no sistema, respectivamente.

4. Depósito
A função depositar(saldo, valor, extrato) permite aos usuários fazer depósitos em suas contas. O valor do depósito é adicionado ao saldo da conta e registrado no extrato.

5. Saque
A função sacar() permite aos usuários realizar saques de suas contas. Antes de efetuar o saque, são realizadas verificações para garantir que o saldo da conta não seja excedido, que o valor do saque não exceda o limite definido e que o número máximo de saques não tenha sido atingido.

6. Extrato
A função realizar_extrato(saldo, extrato) permite que os usuários visualizem o extrato de sua conta, incluindo todas as transações realizadas e o saldo atual.

7. Menu Principal
A função menu() exibe o menu principal do sistema, onde os usuários podem escolher entre as várias opções disponíveis.

8. Main
A função main() é responsável por coordenar a interação do usuário com o sistema bancário. Ela exibe o menu principal e chama as funções correspondentes de acordo com a escolha do usuário.

### Considerações Finais
O sistema "Paule's Bank" oferece uma funcionalidade básica de banco, permitindo aos usuários realizar operações bancárias simples, como criar uma conta, depositar dinheiro, sacar dinheiro, visualizar extratos e listar usuários e contas. No entanto, para um ambiente de produção, seria necessário adicionar mais funcionalidades, como transferências entre contas, autenticação de usuários e medidas de segurança adicionais.

