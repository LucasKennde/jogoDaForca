import random

lista = ['Cavalo', 'Paralelepipedo', 'Casa']

palavra = random.choice(lista)
letra_usu = []
chances = 5
ganhou = False

while True:
  
    for letra in palavra:
        if letra.lower() in letra_usu:
            print(letra, end=" ")
        else:
            print(" _ ", end=(" "))
    
    print(f" - Você tem {chances} chances")
    tentativa = input("\n Escolha uma letra para adivinhar: ")
    letra_usu.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances-=1
    ganhou = True
    for letra in palavra:
        if letra.lower not in letra_usu:
            ganhou = False
    if chances == 0 or ganhou:
        break
if chances==0:
        print(f"\nVocê errou Brow. A palavra era {palavra}")
else:
        print(f"\nParabéns, você ganhou. a palavra era: {palavra}")
        
        
        
    
   