l = []
read = True

while True:
    num = input()

    try:
        l.append(int(num))
    except:
        if num == 'Done':
            break
        else:
            print("Valor inválido!")

soma = sum(l)
quantidade = len(l)
minimo = min(l)
maximo = max(l)

print("Soma: {}\nQuantidade: {}\nMínimo: {}\nMáximo: {}".format(soma, quantidade, minimo, maximo))
