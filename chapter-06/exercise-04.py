# A função contagem() conta quantas letras existem em uma palavra

def contagem(palavra, letra):
    i = palavra.lower().count(letra.lower())
    return i


# Tanto a palavra quanto a letra são inseridas pelo usuário

string = input("Entre com a palavra: ")
char = input("Entre com a letra: ")
print('A letra {} aparecer {} vezes na palavra {}. '.format(char, contagem(string, char), string))
