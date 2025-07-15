# operações bancárias: sacar, depositar, visualizar extrato

def menu():
    menu = f"""
========== Menu Bancário ==========
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
===================================

"""
    
    return input(menu)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0.00:
        print("Valor inválido para saque!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        if numero_saques >= limite_saques:
            print("Limite de saques diários atingido!")
        elif valor > limite:
            print(f"Valor máximo para saque é R${limite:.2f}!")
        else:
            numero_saques += 1
            saldo -= valor
            extrato.append(f"Saque:\t\tR${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor <= 0.00:
        print("Valor inválido para depósito!")
    else:
        saldo += valor
        extrato.append(f"Depósito:\tR${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato

def extrato_conta(saldo,/,*,extrato):
    if not extrato:
        print("Nenhuma movimentação registrada!")
    else:
        for operacao in extrato:
            print(f"{operacao}")
        print()
        print(f"Saldo atual:\tR${saldo:.2f}")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço completo (logradouro - número - bairro - cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):

    usuario_filtrado = [usuario for usuario in usuarios if cpf in usuario["cpf"]]
    return usuario_filtrado[0] if usuario_filtrado else None
    
def criar_conta(agencia, numero_conta, usuarios):
    # conta inicia em 1
    # agencia fixa: 0001
    # o usuario pode ter mais de uma conta, mas somente a ela
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado na base de dados!")

def listar_contas(contas):
    if not contas:
        print("Ainda não há contas cadastradas!")
    else:
        for conta in contas:
            linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 70)
            print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []
    extrato = []
    saldo = 0.00
    limite = 500.00
    numero_saques = 0

    while True:
        opcao = menu()
        opcao = opcao.lower().strip()
        print()
        if opcao == "s":
            print(f"Limite de saques diários: {3-numero_saques}/{LIMITE_SAQUES}")
            valor = float(input("Informe o valor para saque: R$"))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "d":
            valor = float(input("Informe o valor para depósito: R$"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "e": 
            extrato_conta(saldo,extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema!")
            break

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

main()