# Exercício 6: Reescreva seu programa de cálculo de pagamento com um
# 1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
# calculoPagamento que aceita dois parâmetros(horas e TaxaHora).

def calculate_income(hours, rate):
    if hours > 40:
        income = 40 * rate + (hours - 40) * rate * 1.5
    else:
        income = hours * rate

    return income

try:
    worked_hours = float(input("Horas trabalhadas: \n"))
    hour_rate = float(input("Valor hora: \n"))
    print(calculate_income(worked_hours, hour_rate))

except:
    print("Por favor entre com um valor numérico.")