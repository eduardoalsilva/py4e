# Exercício 7: Reescreva o programa de notas do capítulo anterior 
# usando a função computarNotas que recebe a pontuação como parâmetro e
# retorna a nota como uma string.
# Pontuação Nota
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


def computarNotas(points):
    if 0.9 <= points <= 1.0:
        nota = 'A'
    elif 0.8 <= points < 0.9:
        nota = 'B'
    elif 0.7 <= points < 0.8:
        nota = 'C'
    elif 0.6 <= points < 0.7:
        nota = 'D'
    elif points < 0.6:
        nota = 'F'
    else:
        nota = 'Por favor entre com um número de 0.0 a 1.0'

    return nota

try:
    studentPoints = float(input("Por favor entre com uma nota de 0.0 a 1.0: \n"))
    print(computarNotas(studentPoints))

except:
    print("Por favor entre com um valor numérico.")