# Exercício 3: Escreva um programa que solicite ao usuário as horas e o
# valor da taxa por horas para calcular o valor a ser pago por horas de
# serviço.
# Digite as horas: 35
# Digite a taxa: 2.75
# Valor a ser pago: 96.25


worked_hours = eval(input("Horas trabalhadas: "))
rate_hour = eval(input("Pagamento por hora: "))

income = worked_hours * rate_hour

print("O salário é: ", income)