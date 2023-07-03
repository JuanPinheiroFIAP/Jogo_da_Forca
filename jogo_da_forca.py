palavra_secreta = "BANANA"
letras_certas = []  # Lista onde está sendo guardada a palavra secreta dividida por letras

for numero in range(len(palavra_secreta)): # Cria a lista com o número exato de letras que tem na palavra escolhida 
    letras_certas.append("_")
print(letras_certas)

enforcou = False # Condição que será usada para parar o loop
acertou = False # Condição que será usada para parar o loop
tentativas = 0 # Condição que será usada para determinar o número de tentativas que o usuário terá para acertar a palavra  

# Enquanto não se enforcou e não acertou
while not enforcou and not acertou:
    chute = input("Digite uma letra: ").strip().upper()  # Pede para o usuário digitar uma letra
   
    index = 0 
    if chute in palavra_secreta:
        for letra in palavra_secreta:  # Cria um loop que percorre cada letra da palavra
            if chute == letra:
                letra = letra.lower()  
                letras_certas[index] = letra  # Na lista, coloca o [index = posição da letra caso tenha] a letra 
            index += 1  # Contador para que o programa avance para a próxima letra

        if "".join(letras_certas).upper() == palavra_secreta: # .join() - Junta todos os valores de uma lista, ou seja, ele está juntando os elementos da lista letras_certas e formando uma palavra
            print(f"Parabéns, você acertou!\nA palavra era {palavra_secreta.capitalize()}!") # .capitalize - Deixa a primeira letra maiúscula e as demais minúsculas
            acertou = True
            break
            
    elif chute not in palavra_secreta: # Criando uma condição para quando o usuário errar a letra 
        print("Essa letra não está na palavra!\nTente novamente!")
        tentativas += 1 # Iniciando a contagem de tentativas
        numero_tentativas_restantes = len(palavra_secreta) - tentativas
        print(f"Você tem {numero_tentativas_restantes} tentativas restantes")

        if tentativas >= len(palavra_secreta):
            print("Você está sem tentativas!")
            print()
            enforcou = True
    
    print(letras_certas) # Mostra a lista como ela está no momento
