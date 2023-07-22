file_name = input('Digite o nome do arquivo: ')

try:
    file = open(file_name)
except:
    if file_name == 'na na boo boo':
        print(f'{file_name.upper()} PRA VOCÊ TAMBÉM!!!!')

    else:
        print(f'O arquivo {file_name} não foi encontrado!')
    exit()

line_quantity = 0
for line in file:
    line_quantity += 1

print(f'O arquivo {file_name} contém {line_quantity} linhas.')
