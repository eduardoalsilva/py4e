# Exercício 2: Descubra qual linha do programa acima não está devidamente protegida. Veja se você pode construir um arquivo de texto que
# causa falha no programa e depois modifique o programa para que a
# linha seja propriamente protegida e por fim, teste o programa para ter
# certeza que ele manipula corretamente o novo arquivo de texto.

file = open('example.txt')
for line in file:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
