# operações bancárias: sacar, depositar, visualizar extrato

menu = f"""
========== Menu Bancário ==========
[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair
===================================

"""

saldo = 0.00
limite = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = 0

while True:
    opcao = input(menu)
    opcao = opcao.lower().strip()

    if opcao == "s":
        print(f"Limite de saques diários: {3-numero_saques}/{LIMITE_SAQUES}")
        valor = float(input("Informe o valor para saque: R$"))
        if valor <= 0.00:
            print("Valor inválido para saque!")
        elif valor > saldo:
            print("Saldo insuficiente!")
        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários atingido!")
            elif valor > limite:
                print(f"Valor máximo para saque é R${limite:.2f}!")
            else:
                saldo -= valor
                numero_saques += 1
                movimentacoes += 1
                extrato.append([movimentacoes, f"Saque: R${valor:.2f}"])
                print(f"Saque de R${valor:.2f} realizado com sucesso!")

    elif opcao == "d":
        valor = float(input("Informe o valor para depósito: R$"))
        if valor <= 0.00:
            print("Valor inválido para depósito!")
            continue
        movimentacoes += 1
        extrato.append([movimentacoes, f"Depósito: R${valor:.2f}"])
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        if not extrato:
            print("Nenhuma movimentação registrada!")
        else:
            for operacao in extrato:
                print(f"{operacao[0]}. {operacao[1]}")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")