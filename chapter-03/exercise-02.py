# Exercício 2: Reescreva seu programa de pagamento utilizando try e
# except, de forma que o programa consiga lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A
# seguir é mostrado duas execuções do programa

try:
    hours = float(input("Horas trabalhadas: "))
    rate = float(input("Valor hora: "))
    if hours > 40:
        income = 40 * rate + (hours - 40) * rate * 1.5
    else:
        income = hours * rate
    print(income)

except:
    print("Por favor entre com um número.")