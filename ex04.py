#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 12/07/2022
#
# 4. Crie um programa que permita o usuário escolher entre fazer a conversão cambial de real para dólar ou de
# dólar para real. O usuário deve informar o valor e taxa de câmbio para 1U$.
# OBS: o programa de conter quatro funções:
# a - Função para ler e retorna o valor (recebe como parâmetro a opção)
# b - Função para ler e retorna a taxa de câmbio (não recebe parâmetro)
# c - Função para fazer o cálculo do valor em dólar (recebe como parâmetro o valor e a taxa de câmbio)
# d - Função para fazer o cálculo do valor em real (recebe como parâmetro o valor e a taxa de câmbio)


# a
def ler_valor(opcao): # função para ler e retorna o valor
    if opcao in "Dd": # condição para selecionar a opção de conversão de dólar para real
        valor = float(input("Digite o valor em dólar: "))
        return valor
    elif opcao in "Rr": # condição para selecionar a opção de conversão de real para dólar
        valor = float(input("Digite o valor em real: "))
        return valor
    else:
        print("Opção inválida!")
        return ler_valor(opcao)

# b
def ler_taxa(): # função para ler e retorna a taxa de câmbio (não recebe parâmetro)
    taxa = float(input("Digite a taxa de câmbio: ")) # lê a taxa de câmbio e armazena na variável taxa
    return taxa # retorna a taxa de câmbio

# c
def calcular_valor_dolar(valor, taxa): # função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_dolar = valor / taxa # faz o cálculo do valor em dólar e armazena na variável valor_dolar
    return valor_dolar # retorna o valor em dólar

# d
def calcular_valor_real(valor, taxa): # função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_real = valor * taxa # faz o cálculo do valor em real e armazena na variável valor_real
    return valor_real # retorna o valor em real



# programa principal
opcoes = {'R': "Real para Dólar", 'D': "Dólar para Real"} # cria um dicionário com as opções de conversão
for i in opcoes: # percorre o dicionário
    print(f"{i} - {opcoes[i]}") # faz a impressão das opções de conversão


opcao_escolhida = input("Escolha a opção de conversão: ") # lê a opção de conversão e armazena na variável opcao_escolhida
valor = ler_valor(opcao_escolhida) # chama a função ler_valor para ler e retorna o valor (recebe como parâmetro a opção de conversão)
taxa = ler_taxa() # chama a função ler_taxa para ler e retorna a taxa de câmbio (não recebe parâmetro)

if opcao_escolhida in "Rr": # condição para selecionar a opção de conversão de real para dólar
    print(f"O valor em dólar é: {calcular_valor_dolar(valor, taxa)}") # faz a impressão do valor em dólar
elif opcao_escolhida in "Dd": # condição para selecionar a opção de conversão de dólar para real
    print(f"O valor em real é: {calcular_valor_real(valor, taxa)}") # faz a impressão do valor em real
else:
    print("Opção inválida!")




