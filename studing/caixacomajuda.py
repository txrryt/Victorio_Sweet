import funcao

# contas 
conta1 = "Terry"
conta2 = "Carlos"
conta3 = "Thiago"

#saldos
saldo_conta1 = 100
saldo_conta2 = 100
saldo_conta3 = 100

#limites
limite = -200  # valor do cheque especial

#primeiro while pra perguntar a conta
while True:
    print("=== Bem-vindo ao Banco ===")
    askconta = input("Informe sua conta (conta1, conta2, conta3): ")

    if askconta == "conta1":
        nome = conta1   #colocando assim serve pra apelidar as contas, pra melhorar e simplificar pra mim
        saldo = saldo_conta1   # colocando sempre dentro do seu próprio if o saldo, separando e podendo usar melhor no cod
    elif askconta == "conta2":
        nome = conta2
        saldo = saldo_conta2
    elif askconta == "conta3":
        nome = conta3
        saldo = saldo_conta3
    else:                                   #lembrando sempre desse else que serve pra encerrar caso nao coloque algo válido
        print("Conta não encontrada. Encerrando...")
        break

    print(f"\nOlá, {nome}! Seu saldo atual é R$ {saldo:.2f}\n") #aqui ja usei 'nome', inves de 'conta1' pq de toda forma ele vai printar 'terry'

 #Outro while pra poder abrir o programa do banco, menu e operações
    while True:
        funcao.menu()  # chamando a função criada com as op
        try:  #try e except ( melhor forma pra nao ter que deixar tudo em string e caso alguem coloque palavras inves de número vai dar erro!)
            escolha = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        # aqui nosso primeiro if para o dono da conta sacar o saldo que tiver!
        if escolha == 1:
            valor = float(input("Digite o valor do saque: "))
            saldo = funcao.sacar(saldo, valor, limite) # chamando a função de saque e printando saldo, valor e limte após

        # DEPÓSITO
        elif escolha == 2:
            valor = float(input("Digite o valor do depósito: "))
            saldo = funcao.depositar(saldo, valor)

        # SALDO
        elif escolha == 3:
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
            if saldo < 0:
                print(f"⚠️ Você está usando R$ {abs(saldo):.2f} do cheque especial!")

        # TRANSFERÊNCIA
        elif escolha == 4:
            valor = float(input("Digite o valor que deseja transferir: "))
            destino = input("Para qual conta deseja transferir (conta1, conta2, conta3)? ")

            if destino == askconta:
                print("Você não pode transferir para sua própria conta.")
                continue

            if destino == "conta1":
                saldo, saldo_conta1 = funcao.transferir(saldo, saldo_conta1, valor, limite)
            elif destino == "conta2":
                saldo, saldo_conta2 = funcao.transferir(saldo, saldo_conta2, valor, limite)
            elif destino == "conta3":
                saldo, saldo_conta3 = funcao.transferir(saldo, saldo_conta3, valor, limite)
            else:
                print("Conta destino inválida.")

        #sair
        elif escolha == 5:
            print("Saindo da conta...\n")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Atualiza o saldo da conta logada
    if askconta == "conta1":
        saldo_conta1 = saldo
    elif askconta == "conta2":
        saldo_conta2 = saldo
    elif askconta == "conta3":
        saldo_conta3 = saldo