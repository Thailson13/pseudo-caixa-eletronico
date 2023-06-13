import time

class Cliente:
    def __init__(self, nome, cartao, senha, saldo):
        self.nome = nome
        self.cartao = cartao
        self.senha = senha
        self.saldo = saldo
        self.extrato = []

clientes = [
    Cliente("Thailson Júlio", "5233 6145 0898 0931", "2501", 1000.0),
    # número do cartão é fictisio - Gerado no https://www.4devs.com.br/gerador_de_numero_cartao_credito
]

def menu():
    print("Bem-vindo ao Caixa Eletrônico")
    cartao = input("Digite o número do seu cartão: ")
    cliente = identificar_cliente(cartao)
    if cliente:
        senha = input("Digite sua senha: ")
        if senha == cliente.senha:
            print("Login realizado com sucesso")
            while True:
                print(f"{cliente.nome}, escolha uma opção:")
                print("1 - Saldo")
                print("2 - Saque")
                print("3 - Extrato")
                print("4 - Empréstimo")
                print("5 - Sair")
                opcao = input("Opção escolhida: ")
                if opcao == "1":
                    exibir_saldo(cliente)
                elif opcao == "2":
                    realizar_saque(cliente)
                elif opcao == "3":
                    exibir_extrato(cliente)
                elif opcao == "4":
                    realizar_emprestimo(cliente)
                elif opcao == "5":
                    print(f"Obrigado, {cliente.nome}, por utilizar nosso caixa eletrônico!")
                    break
                else:
                    print("Opção inválida")
        else:
            print("Senha incorreta")
    else:
        print("Cartão não identificado")

def identificar_cliente(cartao):
    for cliente in clientes:
        if cliente.cartao == cartao:
            return cliente
    return None

def is_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def exibir_saldo(cliente):
    print(f"Seu saldo é: R${cliente.saldo:.2f}")

def realizar_saque(cliente):
    valor = input("Digite o valor do saque: ")
    if is_numero(valor):
        valor = float(valor)
        if valor <= cliente.saldo:
            cliente.saldo -= valor
            cliente.extrato.append(f"Saque: -R${valor:.2f}")
            print("Saque realizado com sucesso")
            print(f"Novo saldo: R${cliente.saldo:.2f}")
        else:
            print("Saldo insuficiente")
    else:
        print("Valor inválido")

def exibir_extrato(cliente):
    print("Extrato bancário:")
    print(f"Nome: {cliente.nome}")
    print(f"Número do cartão: {cliente.cartao}")
    print(f"Saldo atual: R${cliente.saldo:.2f}")
    print(f"Data: {time.strftime('%d/%m/%Y')}")
    print("Transações:")
    for transacao in cliente.extrato:
        print(transacao)
    print()

def realizar_emprestimo(cliente):
    valor = input("Digite o valor do empréstimo: ")
    if is_numero(valor):
        valor = float(valor)
        if valor > 0:
            juros = valor * 0.05
            novo_saldo = cliente.saldo + valor
            cliente.saldo = novo_saldo
            cliente.extrato.append(f"Empréstimo: +R${valor:.2f}")
            cliente.extrato.append(f"Juros: +R${juros:.2f}")
            print("Empréstimo realizado com sucesso")
            print(f"Novo saldo: R${novo_saldo:.2f}")
            print(f"Valor do juros: R${juros:.2f}")
        else:
            print("Valor inválido")
    else:
        print("Valor inválido")

menu()
