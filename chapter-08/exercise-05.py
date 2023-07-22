# Exercício 5: Escreva um programa que leia uma caixa de email, e quando
# você encontrar uma linha que comece com “De”, você vai separar a linha
# em palavras usando a função split. Nós estamos interessados em quem
# envia a mensagem, que é a segunda palavra na linha que começa com
# From.

file = open('mbox-short.txt')
senders = 0
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    senders += 1
    print(words[1])

print(senders)
