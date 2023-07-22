# Exercício 5: Escreva um programa que solicite ao usuário uma temperatura Celsius, 
# converta para Fahrenheit, e mostre a temperatura
# convertida.


celsius = float(input("Entre com os graus em celsius: \n"))

fahrenheit = celsius * 1.8 + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit}")
