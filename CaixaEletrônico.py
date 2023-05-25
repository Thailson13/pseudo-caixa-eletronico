import time


class Cliente:
    def __init__(self, nome, cartao, senha, saldo):
        self.nome = nome
        self.cartao = cartao
        self.senha = senha
        self.saldo = saldo


clientes = [
    Cliente("Thailson", "2501", "1820", 1000.0),
    Cliente("Matheus", "0507", "3340", 22000.0),
    Cliente("Lyranjor", "1309", "3510", 2500.0),
    Cliente("Valmir", "2409", "9999", 10000.0),
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
                print(cliente.nome + ",", "escolha uma opção:")
                print("1 - Saldo")
                print("2 - Saque")
                print("3 - Extrato")
                print("4 - Empréstimo")
                print("5 - Sair")
                opcao = input("Opção escolhida: ")
                if opcao == "1":
                    saldo(cliente)
                elif opcao == "2":
                    saque(cliente)
                elif opcao == "3":
                    extrato(cliente)
                elif opcao == "4":
                    emprestimo(cliente)
                elif opcao == "5":
                    print(
                        "Obrigado",
                        cliente.nome + ",",
                        "por utilizar nosso caixa eletrônico!",
                    )
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


def saldo(cliente):
    print(f"seu saldo é: R${cliente.saldo:.2f}")


def saque(cliente):
    valor = input("Digite o valor do saque: ")
    if is_numero(valor) and float(valor) <= cliente.saldo:
        cliente.saldo -= float(valor)
        print("Saque realizado com sucesso")
        print(f"Novo saldo: R${cliente.saldo:.2f}")
    else:
        print("Valor inválido ou saldo insuficiente")


def extrato(cliente):
    print("Extrato bancário:")
    print(f"Nome: {cliente.nome}")
    print(f"Número do cartão: {cliente.cartao}")
    print(f"Saldo atual: R${cliente.saldo:.2f}")
    print(f"Data: {time.strftime('%d/%m/%Y')}")


def emprestimo(cliente):
    valor = input("Digite o valor do empréstimo: ")
    if is_numero(valor) and float(valor) > 0:
        print("Empréstimo realizado com sucesso")
        newSaldo = cliente.saldo
        newSaldo = float(newSaldo) + float(valor)
        cliente.saldo = float(newSaldo)
        print(f"Novo saldo: R${newSaldo:.2f}")
        juros = 0.05
        juros = float(valor) * float(juros)
        print(f"Juros de 5% aplicado, valor do juros: R${juros:.2f}")

    else:
        print("Valor inválido")


menu()
