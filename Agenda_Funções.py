Agenda = {}
Telefone = []
menu = '''
////////// Agenda //////////
[1] - Adicionar novo Contato
[2] - Adicionar um Número
[3] - Excluir um Número
[4] - Excluir um Contato
[5] - Consultar um Contato
[6] - Encerrar Menu
'''

def Novo_Contato():
	Nome = input('Digite o Nome do contato que deseja adicionar: ')
	if Nome in Agenda:
		print('O nome já está na agenda.')
	else:
		Continuar = 1
		while Continuar == 1:
			Numero = input('Digite o Número que deseja adicionar: ')
			if Numero in Telefone:
				print('Número já anexado a esse contato')
			else:
				Telefone.append(Numero)
				print('Número adicionado com sucesso!')
			Continuar = int(input('Deseja adicionar outro?\n[1] - Sim\n[2] - Não\n'))
	Agenda[Nome] = Telefone
def Adicionar_Telefone():
	Nome = input('Digite o contato ao qual deseja adicionar um novo número: ')
	if Nome in Agenda:
		Telefone = Agenda[Nome]
		Numero = input(f'Digite o Número que deseja adicionar ao contato de {Nome}: ')
		if Numero in Telefone:
			print('Número já anexado ao contato.')
		else:
			Telefone.append(Numero)
			print('Número adicionado com sucesso!')
			Agenda[Nome] = Telefone
	else:
		print('Este contato não está na sua lista, vamos adicionar')
		Novo_Contato()
def Excluir_Numero():
	Nome = input('Quem é a pessoa que você deseja deletar um número: ')
	if Nome in Agenda:
		Telefone = Agenda[Nome]
		if len(Telefone) == 1:
			print(f'O contato de {Nome} só tem um número anexado, contato excluído com sucesso!')
			del Agenda[Nome]
		else:
			print(f'Telefones anexados ao contato de {Nome}')
			Contador = 0
			for i in Telefone:
				Contador += 1 
				print(f'[{Contador}] - {i}')
			Opcao = int(input('Qual desses contatos você deseja excluir: '))
			Opcao -= 1
			del Telefone[Opcao]
			print('Telefone excluido comn Sucesso!')
			Agenda[Nome] = Telefone
def Excluir_Contato():
	Nome = input('Digite o contato que deseja excluir:')
	if Nome in Agenda:
		print(f'Contato de {Nome} deletado!')
		del Agenda[Nome]
	else:
		print('Não há nenhum contato com esse nome.')
def Consultar_Telefone():
	Nome = input('Digite o contato que você deseja consultar: ')
	if Nome in Agenda:
		Telefone = Agenda[Nome]
		print(f'Telefones anexados ao contato de {Nome}: ')
		for i in Telefone:
			print(i)
	else:
		print(f'{Nome} não consta na agenda.')
while True:
	print(menu)
	Opcao = input('Selecione sua opção: ')
	match Opcao:
		case '1': Novo_Contato()
		case '2': Adicionar_Telefone()
		case '3': Excluir_Numero()
		case '4': Excluir_Contato()
		case '5': Consultar_Telefone()
		case '6': break
		case _:	print('Entrada inválida, tente novamente.')
	Telefone = []
