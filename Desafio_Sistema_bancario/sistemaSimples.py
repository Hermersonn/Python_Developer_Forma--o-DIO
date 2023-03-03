print("----- BEM VINDO AO BANCO LOPES -----")
opçao = '''
    
Digite a operaçao desejada.

1 - Deposito
2 - Saque
3 - Extrato 
4 - Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = int(input(opçao))
    
    if menu == 1:
        deposito = float(input("Digite o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: {deposito:.2f}"
            print(f"Deposito de: R${deposito} feito com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    if menu == 2:
        saque = float(input("Digite o valor do saque: "))
        if saque > 0:
            if saque > limite:
                print("Operação falhou! Valor do saque excede o limite.")
            elif saque > saldo:
                print(f"Operaçao falhou! Você não tem saldo suficiente.")
            elif numero_saques > LIMITE_SAQUES:
                print("Operaçao falhou! Número máximo de saques excedido.")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R${saque:.2f}"
                print(f"Saque de: R${saque} realizado com sucesso!")
        else:
            print("Valor invalido!")
    
    if menu == 3:
        print("========== EXTRATO ==========")
        print(f"Não foi realizado movimentação" if not extrato else extrato)
        print(f"\nsaldo R${saldo}")
    elif menu == 4:
        print("Obrigado por ultilizar nossos serviços !")
        break
    else:
        print("Opção invalida !")