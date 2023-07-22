file_name = input('Digite o nome do arquivo:\n')
try:
    file = open(file_name)
except:
    print(f'O arquivo {file_name} não foi encontrado!')
    exit()

for line in file:
    print(line.upper())
    
