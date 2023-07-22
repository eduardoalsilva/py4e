# Exercício 3: Escreva um programa que peça por uma pontuação entre
# 0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem
# de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota
# usando a seguinte tabela
# Pontuação Nota
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

try:
    points = float(input("Entre com uma pontuação entre 0.0 e 1.0: \n"))
    if 0.9 <= points <= 1.0:
        print("A")
    elif 0.8 <= points < 0.9:
        print("B")
    elif 0.7 <= points < 0.8:
        print("C")
    elif 0.6 <= points < 0.7:
        print("D")
    elif points < 0.6:
        print("F")
    else:
        print("Por favor entre com o valor de 0.0 a 1.0")
        

except:
    print("Por favor entre com um valor numérico.")