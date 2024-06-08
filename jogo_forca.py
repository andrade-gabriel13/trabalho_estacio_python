import random

# Passo 1: Escolher uma Palavra Aleatória
def escolher_palavra():
    palavras = [
        'desenvolvimento', 'tecnologia', 'logica', 'programacao', 
        'tendencias', 'algoritmo', 'software', 'hardware', 'inovacao', 
        'computacao'
    ]
    return random.choice(palavras)

# Passo 2: Criar a Função de Exibir a Forca
def exibir_forca(tentativas):
    estagios = [
        '''
           ------
           |    |
                |
                |
                |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
                |
        =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
                |
        =========
        '''
    ]
    print(estagios[tentativas])

# Passo 3: Iniciar o Jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_' for _ in palavra]
    tentativas = 0
    letras_tentadas = []
    
    print("Bem-vindo ao jogo da forca!")
    print("Digite 'sair' a qualquer momento para encerrar o jogo.")
    exibir_forca(tentativas)
    print("Palavra: " + ' '.join(palavra_oculta))
    
    # Passo 4: Loop Principal do Jogo
    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()
        
        if letra == 'sair':
            print("Jogo encerrado. A palavra era:", palavra)
            break
        
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Por favor, digite apenas uma letra.")
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print("Acertou!")
        else:
            tentativas += 1
            print("Errou!")
        
        exibir_forca(tentativas)
        print("Palavra: " + ' '.join(palavra_oculta))
        
        # Passo 5: Verificação de Vitória e Derrota
        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
        
        if tentativas == 6:
            print("Você perdeu! A palavra era:", palavra)
            break
    
    # Passo 6: Finalização do Jogo
    print("Obrigado por jogar!")

# Executar o jogo
jogar()
