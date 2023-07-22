# Exercício 1: Reescreva seu programa de pagamento, para pagar 
# ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
# trabalhado acima de 40 horas

hours = float(input("Quantidade de horas: \n"))
rate = float(input("Valor hora: \n"))
income = 0

if hours > 40:
    income = 40 * rate + (hours - 40) * rate * 1.5
else:
    income = hours * rate

print(f"O pagamento é: {income}")