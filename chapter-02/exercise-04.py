# Exercício 4: Suponha que executamos as seguintes declaração por
# atribuição:
# Largura = 17
# Altura = 12.0
# Para cada uma das expressões a seguir, escreva o valor da expressão e o tipo (do
# valor da expressão).
# 1. Largura//2
# 2. Largura/2.0
# 3. Altura/3
# 4. 1 + 2 * 5


weight = eval(input("Digite a largura: "))
height = eval(input("Digite a altura: "))

print(f"1. A divisão inteira da largura por 2 é: {weight//2}")
print(f"2. A divisão flutuante da largura por 2 é: {weight/2.0}")
print(f"3. A divisão da altura por 3 é: {height/3}")
print("1 + 2 * 5 = ", 1 + 2 * 5)