import random

def fatorial (n):
 
 if n == 0 or n == 1:
    return 1
 else:
   return  n*fatorial(n-1)
 





#Fator = int (input ("digite um número: "))
#print (função.fatorial(Fator))

import random

def fatorial (n):
 
 if n == 0 or n == 1:
    return 1
 else:
   return  n*fatorial(n-1)
 


#print (fatorial(5))



#lista = [ 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17, 18, 19 ,20]
def gerar_lista ():
 lista_peso = []
 for i in range(20): 
   i = random.randint (1,101)
   lista_peso.append (i)
  

 return lista_peso


def ordenador (listinha):
  lista_ordenada=[] #lista vazia
  for menor_numero in lista_ordenada: #loop na lista
   for x in lista_ordenada: #segundo loop na lista
    listagrande = []
    if menor_numero<=x:#condição do número ser menor e o outro apresentado no segundo loop
   

     menor_numero == x # se for igual o número ele vai virar o mesmo
     lista_ordenada.append(menor_numero) # e será adicionado na lista
     listinha.append ()
    # listagrande.append (x)


   
   #menor_numero >=x
   #menor_numero.remove(lista_ordenada)
    # menor_numero>x
     #listinha.remove(x)
     
    # lista_ordenada.append (lista_ordenada)
    #else:
      #menor_numero == x
      #menor_numero.append (lista_ordenada)
 # return (listinha)

def menu ():
   #Usuário = ("Terry")
   print ("=== Bem vindo a sua conta! ===")
   print ("Digite 1 para realizar um saque")
   print ("Digite 2 para realizar um depósito")
   print ("Digite 3 para verificar o saldo em sua conta")
   print ("Digite 4 para transferir o seu saldo")
   print ("Digite 5 para sair")

def subtração(a,b):
  return a - b

def soma (a,b):
   return a + b

def quadrado (a): #lado ao quadrado
    quadros = a*a
    return (quadros)


def retangulo (a, b): # base x altura
    retangul = b*a
    return (retangul)

def triangulo (a,b): # base x altura / 2
    triang = b*a/2
    return (triang)

def circulo (b): # PI (3,14) x raio ao quadrado
    circle = 3.14*b*b
    return circle

def volume (a):
    v = a*a*a
    return (v)

def trapezio (B,b,a):
    trape = ((B+b)*a/2)
    return (trape)

def menuquadros ():
    print ("Digite 1 para calcular o quadrado")
    print ("Digite 2 para calcular o retangulo")
    print ("Digite 3 para calcular o triangulo")
    print ("Digite 4 para calcular o circulo")
    print ("Digite 5 para calcular o volume")
    print ("Digite 6 para calcular o trapezio")
    print ("                                                                                       ")


def raios_c (raio):
    lista_valors = []  
    for i in raio:
        raio = circulo(i)
        lista_valors.append (raio)
    return (lista_valors)



#funcoes do banco

def sacar(saldo, valor, limite=-200):
    """Realiza um saque, permitindo uso do cheque especial, sem usar abs()."""

    if valor <= 0:
        print("Valor inválido. O saque deve ser maior que zero.")
        return saldo

    # logica de matematica - com - é +, então coloca - pra o limite não sair errado
    limite_positivo = -limite 
    saldo_disponivel = saldo + limite_positivo

    if valor > saldo_disponivel:
        print(f"Operação negada! Seu limite de cheque especial é R$ {limite_positivo:.2f}.")
        print(f"Você pode sacar até R$ {saldo_disponivel:.2f}.")
        return saldo

    saldo -= valor
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    if saldo < 0:
        print(f"Atenção! Você está usando R$ {-saldo:.2f} do seu cheque especial.")  # -saldo torna o valor positivo

    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo


# Função depositos

def depositar(saldo, valor):
    """Realiza um depósito"""
    if valor <= 0:
        print("Valor inválido. O depósito deve ser maior que zero.")
        return saldo

    saldo += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo


      #Função transferencia   
def transferir(saldo_origem, saldo_destino, valor, limite=-200):
    """Transfere saldo entre duas contas, permitindo uso do cheque especial"""
    if valor <= 0:
        print("Valor inválido. A transferência deve ser maior que zero.")
        return saldo_origem, saldo_destino

     #Saldo disponivel calculado
    saldo_disponivel = saldo_origem - limite  # exemplo 100 - (-200) = 300

    if valor > saldo_disponivel:
        print(f"Saldo insuficiente! Seu limite de cheque especial é R$ {-limite:.2f}.")
        print(f"Você pode transferir até R$ {saldo_disponivel:.2f}.")
        return saldo_origem, saldo_destino

    # Faz a transferência
    saldo_origem -= valor
    saldo_destino += valor
    print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")

    # Se entrou no limite
    if saldo_origem < 0:
        print(f"Você está usando R$ {-saldo_origem:.2f} do seu cheque especial.")
    return saldo_origem, saldo_destino