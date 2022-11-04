file = open('dist.csv')
primeira_linha = file.readline().strip()
csv = file.read()
file.close()

cidades = primeira_linha.split(',')
distancias = csv.split(',')

matriz = []

# for i in range(len(cidades)):  
#   matriz.append(cidades[i] + distancias[i])

# print(matriz)


escolha = '0'
custo_por_km = '0'

def menu():
    print('\n..:: Escolha sua opção ::..\n')
    print('1 - Custo por km rodado')
    print('2 - Consultar trecho')
    print('3 - Melhor rota')
    print('4 - Rota completa')
    print('5 - Sair\n')
    item = input('Escolha uma opção: ')
    return item

def escolha_um():
    custo_por_km = input("Informe o custo por km rodado: ")
    if custo_por_km <= '0' or not custo_por_km.replace('.','',1).isdigit():
        print('O valor informado é inválido!')
        custo_por_km = '0'
    return custo_por_km

def escolha_dois():
    print('z')

while escolha != '6':
    escolha = menu()
    if escolha == '1':
        custo_por_km = escolha_um()
        
    elif escolha == '2':
        if custo_por_km == '0':
            print('Não foi informado o custo por km rodado!')
            continue 
        escolha_dois()

    elif escolha == '3':
        if custo_por_km == '0':
            print('Não foi informado o custo por km rodado!')
            continue  
        print('Sistema !')

    elif escolha == '4':
        if custo_por_km == '0':
            print('Não foi informado o custo por km rodado!') 
            continue 
        print('Sistema !') 
        
    elif escolha == '5':
        print('Sistema finalizado!') 
        break
        
    else:
        print('\nOpção desconhecida!\n')
        input('\n\nPressione ENTER para continuar   ')

        