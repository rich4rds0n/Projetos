import random
from palavras import palavras
from forca_visual import vidas_visual
import string

def get_palavra_valida(palavras):
    palavra = random.choice(palavras)

    while '-' in palavra or ' ' in palavra or 'Á' in palavra or 'É' in palavra or 'Í' in palavra or 'Ã' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = get_palavra_valida(palavras)
    palavra_letras = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()

    vidas = 8

    while len(palavra_letras) > 0 and vidas > 0:
        print('Você tem', vidas, 'vidas restantes e você já usou as letras:', ' '.join(letras_usadas))
        
        palavra_lista = [letter if letter in letras_usadas else '_' for letter in palavra]
        print(vidas_visual[vidas])
        print('Palavra atual:', ' '.join(palavra_lista))

        letra_usuario = input('Digite uma letra:').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in palavra_letras:
                palavra_letras.remove(letra_usuario)
                print('')

            else:
                vidas = vidas - 1
                print('A letra,', letra_usuario, 'não está na palavra.' )

        elif letra_usuario in letras_usadas:
            print('Letra já usada. Tente outra.')

        else:
            print('Caractere inválido. Tente novamente.')

    if vidas == 0:
        print(vidas_visual[vidas])
        print('Você perdeu. A palavra é:', palavra)
    else:
        print('Você adivinhoua palavra', palavra, '!!')


if __name__ == '__main__':
    forca()