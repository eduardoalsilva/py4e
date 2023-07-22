file_name = input('Digite o nome do arquivo: ')
try:
    file = open(file_name)

except:
    print(f'O arquivo {file_name} não foi encontrado!')
    exit()

spams = []

for line in file:
    if line.startswith('X-DSPAM-Confidence'):
        spam_line = line.split(':')
        spams.append(float(spam_line[1]))

print(f'Média de confiança de spam é: {sum(spams)/len(spams)}')
