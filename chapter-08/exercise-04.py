# Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
# Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
# linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
# Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
# adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
# palavras em ordem alfabética.**

file = open('romeo.txt')
unique_words = []
for line in file:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)
