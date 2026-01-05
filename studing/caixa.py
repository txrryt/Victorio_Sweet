import funcao

#sistema de caixa
# usuario, nome , saldo inicial 1.000
#criar um menu para realizar operações
# saque = retirar, depositar = adicionar saldo , verificar saldo 
#fazer contas para transferir saldo entre elas

conta1 = ("Terry")
conta2 = ("Carlos")
conta3 = ("Thiago")


Saldo_conta1= 100
Saldo_conta2 = 100
Saldo_conta3 = 100





#Saldo = 1000
Limite =-200

while True:
  print ("=== Bem vindo ao Banco ===")
  askconta = input("por favor me informe sua conta: ")

  if askconta == "conta1":
   print ("Bem vindo Terry!")
   print (f"Saldo em conta {Saldo_conta1}")

  elif askconta == "conta2":
    print ("Bem vindo Carlos!") 
    print (f"Saldo em conta {Saldo_conta2}")

  elif askconta == "conta3":
    print ("Bem Vindo Thiago!") 
    print (f"Saldo em conta {Saldo_conta3}")


  else:
    break 

  while True:
 
  
 
   funcao.menu()
   escolha = int (input ("digite a opção que deseja: "))

   if escolha == 1:
    Saque = float (input ("digite o valor que deseja sacar em sua conta: "))
    if Saque>Saldo_conta1:
     print (f"Você não tem saldo suficiente para esse saque, pois seu saldo atual é de {Saldo_conta1}")
     print (" ")
     if Saque>Saldo_conta2:
        print (f"Você não tem saldo suficiente para esse saque, pois seu saldo atual é de {Saldo_conta1}")
        print (" ")
        if Saque>Saldo_conta3:
           print (f"Você não tem saldo suficiente para esse saque, pois seu saldo atual é de {Saldo_conta1}")
           print (" ")
       
    else:
       print(funcao.subtração(Saldo_conta1,Saque))
       print(funcao.subtração(Saldo_conta2,Saque))
       print(funcao.subtração(Saldo_conta3,Saque))
       
       Saldo_conta1-=Saque
       Saldo_conta2-=Saque
       Saldo_conta3-=Saque
       print (" ")
       print (" ")

   elif escolha == 2:
    depósito = float (input ("digite o valor que deseja depositar em sua conta: "))
    resultado_dep1 = (Saldo_conta1 + depósito)
    resultado_dep2 = (Saldo_conta2 + depósito)
    print (funcao.soma(Saldo_conta1,depósito))
    print (funcao.soma(Saldo_conta2,depósito))
    print (funcao.soma(Saldo_conta3,depósito))
    Saldo_conta1+=depósito
    Saldo_conta2+=depósito
    Saldo_conta3+=depósito
 # print (f"Feito! vocẽ depositou {depósito} e ficou com {resultado_dep} em sua conta!")
    print (" ")
    print (" ")

   elif escolha == 3:
     print (" === Saldos ===")
     print (f"O saldo da conta de Terry é de {Saldo_conta1}") 
     print (f"O saldo da conta de Carlos {Saldo_conta2}") 
     print (f"O saldo da conta de Thiago {Saldo_conta3}") 
     print (" ")
     print (" ")


   elif escolha ==4:
     transferir = float (input("digite o valor que deseja transferir: "))
     whichconta = input ("digite qual conta deseja transferir: ")
     if whichconta == "conta1":
       Saldo_conta2-transferir
       
      
       

       #print (" ")
       #print (" ")