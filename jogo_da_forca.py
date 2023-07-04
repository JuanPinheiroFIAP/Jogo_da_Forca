import random # Importanto a biblioteca random 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

letras_certas = [] # Lista onde está sendo guardada a palavra secreta dividida por letras
enforcou = False # Condição que será usada para parar o loop
acertou = False # Condição que será usada para parar o loop
tentativas = 0 # Condição que será usada para determinar o número de tentativas que o usuário terá para acertar a palavra 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

with open("palavras.txt", "r") as arquivo: # Abre um arquivo txt e com o "r" le cada linha de uma vez 
    palavras = [linha.strip() for linha in arquivo] # Adiciona na lista "palavras" cada conteudo que tem no arquivo
    numero_palavras = random.randrange(0, len(palavras)) # Escolhendo um numero aleatorio de acorco com o tamanho da lista que tenho(Começo de 0 para dar o numero certo de itens)
    palavra_secreta = palavras[numero_palavras].upper() # Pegando esse numero aleatorio gerado e escolhendo o item que corresponde a ele na lista 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

for numero in range(len(palavra_secreta)): # Cria a lista com o número exato de letras que tem na palavra escolhida 
    letras_certas.append("_")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

print("+" + "-"*30 + "+")
print("|" + " "*30 + "|")
print("|" + "Bem vindo ao meu jogo da forca".center(30) + "|")
print("|" + " "*30 + "|")
print("+" + "-"*30 + "+")
print(letras_certas)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

while not enforcou and not acertou:# Enquanto não se enforcou e não acertou
    print()
    chute = input("|"+"  Digite uma letra: ").strip().upper() # Pede para o usuário digitar uma letra \\ strip remove caracteres especiais 
    print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    index = 0 
    if chute in palavra_secreta:
        for letra in palavra_secreta:  # Cria um loop que percorre cada letra da palavra
            if chute == letra:
                letra = letra.lower()  
                letras_certas[index] = letra  # Na lista, coloca o [index = posição da letra caso tenha] a letra 
            index += 1  # Contador para que o programa avance para a próxima letra

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

        if "".join(letras_certas).upper() == palavra_secreta: # .join() - Junta todos os valores de uma lista, ou seja, ele está juntando os elementos da lista letras_certas e formando uma palavra
            
            print("*-------------------------------------------*")
            print(f"Parabéns, você acertou!\nA palavra era {palavra_secreta.capitalize()}!") # .capitalize - Deixa a primeira letra maiúscula e as demais minúsculas
            print("*-------------------------------------------*")
            acertou = True
            break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
            
    elif chute not in palavra_secreta: # Criando uma condição para quando o usuário errar a letra 

        print("*-------------------------------------------*")
        print("Essa letra não está na palavra!\nTente novamente!")
        print("*-------------------------------------------*")

        tentativas += 1 # Iniciando a contagem de tentativas
        numero_tentativas_restantes = len(palavra_secreta) - tentativas

        print("*-------------------------------------------*")
        print(f"Você tem {numero_tentativas_restantes} tentativas restantes")
        print("*-------------------------------------------*")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

        if tentativas >= len(palavra_secreta):

            print("*-------------------------------------------*")
            print("Você está sem tentativas!")
            print(f"A palavra era {palavra_secreta.capitalize()}!")
            print("*-------------------------------------------*")
            enforcou = True
            break
    print(letras_certas) # Mostra a lista como ela está no momento

#-----------------------------------------------------------------------------------------------------------------------------------------------------------