# Exercício 6: Reescreva o programa que solicita o usuário uma lista de
# números e prints e imprime em tela o maior número e o menor número
# quando o usuário digitar a palavra “feito”. Escreva um programa para
# armazenar as entradas do usuário em uma lista e use as funções max()
# e min() para computar o número máximo e o mínimo depois que o laço
# for completo

numbers = list(map(int, input('Enter a space-separeted numbers: \n').split()))

print('Maximum:', max(numbers), '\n' + 'Minimum:', min(numbers))
