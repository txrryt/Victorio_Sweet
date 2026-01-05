import getpass #só para deixar invísivel a palavra no input
while True: #loop para rodar o jogo
    palavra = getpass.getpass ("digite uma palavra: ") #deixa a palavra inserida invisível 
    letra_acertadas = [] #lista vazia para ficar salvo a palavra e tentativas
    acertos = len(palavra)
    for i in range(len(palavra)): #for para ler a quantidade de letras da lista (palavra)
        letra_acertadas.append ("_")  #para adicionar em todas as letras da palavra o "_"      
    print (letra_acertadas) #para printar todas as letras da palavra só que em "_", como adicionamos antes
    for i in range (6): #for para que o jogo te de 6 vidas (6 loops)
        chute = input ("digite uma letra: ") #chute ou palpite da letra em que o jogador deseja tentar advinhar
        indice = 0 #indice para contar onde a palavra chutada encontrará
        for letra in palavra: # loop
          
           if chute == letra:
               letra_acertadas.pop(indice)
               
               letra_acertadas.insert(indice,chute) 
               for p in letra_acertadas:
                  if p != "_":
                     print("você acertou")
                     acertos -=1
                    # break
                  elif acertos == palavra:
                     print ("você acertou a palavra! Parabéns")
                     break
                

           else:
         
             print ("não tem essa letra na palavra")
           indice +=1
        print (letra_acertadas)