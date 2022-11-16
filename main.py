# variaveis
escolha = '0'
custo_por_km = '0'
cidade_origem = None
cidade_destino = None
tres_cidades = []

# abre csv e cria matriz
file = open('dist.csv')
csv = file.readlines()
file.close()
 
matriz = []

for linha in csv:
    campos = linha.replace("\n", "").split(",")
    matriz.append(campos)

# funçoes de validação
def custo_por_km_is_valid_or_default(custo_por_km):
    if custo_por_km <= '0' or not custo_por_km.replace('.','',1).isdigit():
        print('O valor informado é inválido!')
        custo_por_km = '0'
    return custo_por_km

def custo_por_km_is_valid(custo_por_km):
    if custo_por_km == '0':
        print('\nNão foi informado o custo por km rodado!') 
        return False
    else: return True

def cidades_are_valid(cidade_origem, cidade_destino):
    if cidade_origem == cidade_destino or cidade_origem not in matriz[0] or cidade_destino not in matriz[0]:
        print("\nCidades não existem no cadastro ou são iguais! \nDigite novamente\n")
        cidade_destino = None
        cidade_origem = None
    return cidade_origem, cidade_destino

def tres_cidades_are_valid(cidades, tres_cidades):
    array_cidades = cidades.replace(", ", ",").split(",")
    for i, cidade in enumerate(array_cidades):
        if cidade not in matriz[0] or cidade in array_cidades[i+1:]:
            print("\nCidades não existem no cadastro ou são iguais!\n")
            return tres_cidades
    return array_cidades

# funçao para salvar no historico.csv
def salva_historico(historico):
    log = open('historico.csv', 'a')
    log.write('\n')
    for i in historico:
        log.write(i) if i == historico[-1] else log.write(i + ',')
    log.flush()
    log.close()

# funçao de calculo menu escolha 2
def calcula_distancia_custo_total(cidade_origem, cidade_destino, custo_por_km):
    posicao_cidade_origem = matriz[0].index(cidade_origem)
    posicao_cidade_destino = matriz[0].index(cidade_destino)
    valor_distancia_destino = matriz[posicao_cidade_origem + 1][posicao_cidade_destino]
    custo_total_trecho = int(valor_distancia_destino) * float(custo_por_km)
    return valor_distancia_destino, custo_total_trecho

# funçao escolha um
def escolha_um():
    custo_por_km = input("Informe o custo por km rodado: ")
    custo_por_km = custo_por_km_is_valid_or_default(custo_por_km)
    return custo_por_km

# funçao escolha dois
def escolha_dois(cidade_origem, cidade_destino, custo_por_km):
    while cidade_origem == None and cidade_destino == None:
        cidade_origem = input("Informe a cidade de origem: ").upper()
        cidade_destino = input("Informe a cidade de destino: ").upper()
        cidade_origem, cidade_destino = cidades_are_valid(cidade_origem, cidade_destino)
    
    valor_distancia_destino, custo_total_trecho = calcula_distancia_custo_total(cidade_origem, cidade_destino, custo_por_km)
    
    print("\nDistância rodoviária entre {} e {}: {} Km".format(cidade_origem.capitalize(), cidade_destino.capitalize(), valor_distancia_destino))
    print("Custo total do trecho: R$ {:.2f}".format(custo_total_trecho))

    historico = [cidade_origem, cidade_destino, valor_distancia_destino, custo_por_km, str(custo_total_trecho)]
    salva_historico(historico)

# funçao escolha tres
def escolha_tres(tres_cidades):
    cidades = input("Informe as três cidades: ").upper()
    tres_cidades = tres_cidades_are_valid(cidades, tres_cidades)
    if not tres_cidades:
        return
    # TO-DO    

def menu():
    print('\n..:: Escolha sua opção ::..\n')
    print('1 - Custo por km rodado')
    print('2 - Consultar trecho')
    print('3 - Melhor rota')
    print('4 - Rota completa')
    print('5 - Sair\n')
    item = input('Escolha uma opção: ')
    return item      

while escolha != '5':
    escolha = menu()
    if escolha == '1':
        custo_por_km = escolha_um()
        
    elif escolha == '2':
        if custo_por_km_is_valid(custo_por_km): 
            escolha_dois(cidade_origem, cidade_destino, custo_por_km)

    elif escolha == '3':
        if custo_por_km_is_valid(custo_por_km): 
            escolha_tres(tres_cidades)

    elif escolha == '4':
        if custo_por_km_is_valid(custo_por_km): 
            print('Sis!')

    elif escolha == '5':
        print('Sistema finalizado!') 
        break
        
    else:
        print('\nOpção desconhecida!\n')
        input('\n\nPressione ENTER para continuar   ')
        