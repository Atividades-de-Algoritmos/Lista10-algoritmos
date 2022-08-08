#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 06/08/2022
#
# 4. Crie um programa que permita o usuário escolher entre fazer a conversão cambial de real para dólar ou de dólar para real. O usuário deve informar o valor e taxa de câmbio para 1U$.

# OBS: o programa de conter quatro funções:

# a - Função para ler e retorna o valor (recebe como parâmetro a opção)
# b - Função para ler e retorna a taxa de câmbio (não recebe parâmetro)
# c - Função para fazer o cálculo do valor em dólar (recebe como parâmetro o valor e a taxa de câmbio)
# d - Função para fazer o cálculo do valor em real (recebe como parâmetro o valor e a taxa de câmbio)

# -- Funções(a, b, c, d) --

# 1. função a
def ler_valor(opcao): # Função para ler e retorna o valor
    if opcao.lower() in "d": # Condição para selecionar a opção de conversão de dólar para real
        valor = float(input("\nDigite o valor em dólar: ")) # Solicita um valor flutuante do usuário
        return valor # Retorna o valor
    
    elif opcao.lower() in "r": # Condição para selecionar a opção de conversão de real para dólar
        valor = float(input("\nDigite o valor em real: ")) # Solicita um valor flutuante do usuário
        return valor # Retorna o valor
    
    else: # Caso contrário
        print("\nOpção inválida!") # Imprime uma mensagem de erro
        return ler_valor(opcao) # Retorna uma chamada da função

# 2. função b
def ler_taxa(): # Função para ler e retorna a taxa de câmbio (não recebe parâmetro)
    taxa = float(input("\nDigite a taxa de câmbio: ")) # Lê a taxa de câmbio e armazena na variável taxa
    return taxa # Retorna a taxa de câmbio

# 3. função c
def calcular_valor_dolar(valor, taxa): # Função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_dolar = valor / taxa # Faz o cálculo do valor em dólar e armazena na variável valor_dolar
    return valor_dolar # Retorna o valor em dólar

# 4. função d
def calcular_valor_real(valor, taxa): # Função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_real = valor * taxa # Faz o cálculo do valor em real e armazena na variável valor_real
    return valor_real # Retorna o valor em real

# -- Chamada das funções --

opcoes = {'R': "Real para Dólar", 'D': "Dólar para Real"} # Cria um dicionário com as opções de conversão

for i in opcoes: # Percorre o dicionário
    print(f"{i} - {opcoes[i]}") # Faz a impressão das opções de conversão

opcao_escolhida = input("\nEscolha a opção de conversão: ") # Lê a opção de conversão e armazena na variável opcao_escolhida

valor = ler_valor(opcao_escolhida) # Chama a função ler_valor para ler e retorna o valor (recebe como parâmetro a opção de conversão)

taxa = ler_taxa() # Chama a função ler_taxa para ler e retorna a taxa de câmbio (não recebe parâmetro)

if opcao_escolhida in "Rr": # Condição para selecionar a opção de conversão de real para dólar
    print(f"\nO valor em dólar é: {calcular_valor_dolar(valor, taxa):.2f}") # Faz a impressão do valor em dólar

elif opcao_escolhida in "Dd": # Condição para selecionar a opção de conversão de dólar para real
    print(f"\nO valor em real é: {calcular_valor_real(valor, taxa):.2f}") # Faz a impressão do valor em real

else:
    print("\nOpção inválida!") # Imprime que a opção está inválida
