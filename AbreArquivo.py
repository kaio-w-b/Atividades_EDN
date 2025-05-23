with open('minhas_notas.txt', 'w') as arquivo:
    arquivo.write('Bom Dia!\n')
    arquivo.write('Boa Tarde!\n')
    arquivo.write('Boa Noite!\n')

with open('minhas_notas.txt', 'a') as arquivo:
    arquivo.write('Olá!\n')
    arquivo.write('Adeus!\n')

with open('minhas_notas.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
