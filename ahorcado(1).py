import random


print("hola vamos a jugar al ahorcado")
x=input("di start para empezar")
if x=="start":

    IMAGES = ['''
    
    
        +---+
        |   |
            |
            |
            |
            |
            ========''', '''
    
    
        +---+
        |   |
        O   |
            |
            |
            |
            ========''', '''
    
        +---+
        |   |
        O   |
        |   |
            |
            |
            ========''', '''
    
        +---+
        |   |
        O   |
       /|   |
            |
            |
            ========''', '''
    
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            ========''', '''
    
    
        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            ========''', '''
    
        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
    
            ========''', '''
    
        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            ========''', '''
    
        ''']

    palabras = ["casa","perro","gato","ventana","ventana","ordenador","raton","atomo","molecula","wifi","teclado","pantalla","cable","phyton","volante","mando","moneda","aplicacion","taza","llave"]



    def respuesta():
        idx = random.randint(0, len(palabras) - 1)
        return palabras[idx]


    def mesa(hidden_word, tries):
        print(IMAGES[tries])
        print('')
        print(hidden_word)


    def run():
        word = respuesta()
        hidden_word = ['_'] * len(word)
        tries = 0

        while True:
            mesa(hidden_word, tries)
            current_letter = str(input('Escoge una letra: '))

            letter_indexes = []
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    letter_indexes.append(idx)

            if len(letter_indexes) == 0:
                tries += 1

                if tries == 7:
                    mesa(hidden_word, tries)
                    print('')
                    print('Perdiste! La palabra correcta era {}'.format(word))
                    break
            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter

                letter_indexes = []

            try:
                hidden_word.index('_')
            except ValueError:
                print('')
                print('Felicidades! ganaste. La palabra es: {}'.format(word))
                break


if __name__ == '__main__':

    print('B I E N V E N I D O S  AL  A H O R C A D O ')

    run()