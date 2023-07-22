l = []
read = True
while read:
    num = input('Digite um número ou \'Done\' para encerrar. \n')

    try:
        l.append(int(num))

    except:
        if num == 'Done':
            read = False
        else:
            print("Valor inválido!")
            continue

total = sum(l)
quantidade = len(l)
media = sum(l)/len(l)

print("Total: {}\nQuantidade: {}\nMédia: {}".format(total, quantidade, media))
