# A função contagem() conta quantas letras existem em uma palavra

def contagem(string, letra):
    i = 0
    for char in string:
        if char.lower() == letra.lower():
            i+=1
        else:
            continue
    return i

# Tanto a palavra quanto a letra são inseridas pelo usuário

st = input("Digite a palavra: ")
let = input("Digite a letra: ")

print("A palavra {} tem {} vezes a letra {}.".format(st, contagem(st, let), let))
