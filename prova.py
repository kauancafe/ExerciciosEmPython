
# Questão 1:

'''
Numero1 = int(input(''))
Numero2 = int(input(''))
Maior = 0
Menor = 1
Soma = 0
Mult = 1
if Numero1 >= Numero2:
    Maior = Numero1
    Menor = Numero2
else:
    Maior = Numero2
    Menor = Numero1
for i in range(Menor+1,Maior,1):
    if(i % 2 == 0):
        Soma += i
    else:
        Mult *= i
print(f'Multiplicação dos ímpares: {Mult}\nSoma dos pares: {Soma}')
'''

# Questão 2:

'''
não fiz :(
'''


# Questão 3:

"""
Valor = int(input())
if(Valor<0 or Valor>1000):
    print('Valor inválido, tente novamente.')
else:
    Cem = Valor // 100
    Resto_Cem = Valor % 100
    Cinq = Resto_Cem // 50
    Resto_Cinq = Resto_Cem % 50
    Vin = Resto_Cinq // 20
    Resto_Vin = Resto_Cinq % 20
    Dez = Resto_Vin // 10
    Resto_Dez = Resto_Vin % 10
    Cinco = Resto_Dez // 5
    Resto_Cinco = Resto_Dez % 5
    Dois = Resto_Cinco // 2
    Resto_Dois = Resto_Cinco % 2
    Um = Resto_Dois // 1
    Resto_um = Resto_Dois % 1
    print(f'''
{Cem} nota(s) de 100,00
{Cinq} nota(s) de 50,00
{Vin} nota(s) de 20,00
{Dez} nota(s) de 10,00
{Cinco} nota(s) de 5,00
{Dois} nota(s) de 2,00
{Um} nota(s) de 1,00
''')
"""

# Questão 4
'''
Lista = [[],[],[],[],[],[],[],[],[]]
#0-codigo /1-area / 2-valor / 3-aluguel / 4- status positivo / 5- status negativo /6-parada do codigo / 7- imoveis vagos / 8 - aluguel mensal
while len(Lista[6]) == 0:
    Codigo = int(input('Digite o codigo: '))
    if(Codigo == 0):
        Lista[6].append('1')
    else:
        Lista[0].append(Codigo)
        Area = float(input('Digite a área: '))
        Lista[1].append(Area)
        Valor = float(input('Digite o valor: '))
        Lista[2].append(Valor)
        Aluguel = float(input('Digite o aluguel: '))
        Lista[3].append(Aluguel)
        Status = str(input('Responda com "sim" ou "não".\nEstá alugado? ')).upper()
        if(Status == 'SIM'):
            Lista[4].append(Status)
            Lista[8].append(Aluguel)
        else:
            Lista[5].append(Status)
            Lista[7].append(Aluguel)

        print(f'\nCódigo: {Codigo}\nÁrea: {Area:.2f}m²\nValor: R${Valor:.2f}\nAluguel: R${Aluguel:.2f}\nAlugado? {Status}\n')

print(f'\nPatrimônio total: R${sum(Lista[2]):.2f}')
print(f'Empreendimentos alugados: {len(Lista[4])}')
Lista[7].sort()
print(f'Total de aluguéis desse mês: R${sum(Lista[8]):.2f}')
print(f'Imóvel mais barato: R${Lista[7][0]:.2f}')
print(f'Imóvel mais caro: R${Lista[7][len(Lista[7])-1]:.2f}')
'''
