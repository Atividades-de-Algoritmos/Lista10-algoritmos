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

# a
def ler_valor(): # função para ler e retorna o valor (não recebe parâmetro)
    valor = float(input("Digite o valor: ")) # lê o valor e armazena na variável valor
    return valor # retorna o valor

# b
def ler_taxa(): # função para ler e retorna a taxa de câmbio (não recebe parâmetro)
    taxa = float(input("Digite a taxa de câmbio: ")) # lê a taxa de câmbio e armazena na variável taxa
    return taxa # retorna a taxa de câmbio

# c
def calcular_valor_dolar(valor, taxa): # função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_dolar = valor * taxa # faz o cálculo do valor em dólar e armazena na variável valor_dolar
    return valor_dolar # retorna o valor em dólar

# d
def calcular_valor_real(valor, taxa): # função para fazer o cálculo (recebe como parâmetro o valor e a taxa de câmbio)
    valor_real = valor / taxa # faz o cálculo do valor em real e armazena na variável valor_real
    return valor_real # retorna o valor em real

# programa principal
opcao = {1: "Real para Dólar", 2: "Dólar para Real"} # cria um dicionário com as opções de conversão
for i in opcao: # percorre o dicionário
  print(f"{i} -> {opcao[i]}") # faz a impressão das opções de conversão

opcao_escolhida = int(input("Escolha a opção de conversão: ")) # lê a opção de conversão e armazena na variável opcao_escolhida
valor = ler_valor() # chama a função ler_valor para ler e retorna o valor (não recebe parâmetro)
taxa = ler_taxa() # chama a função ler_taxa para ler e retorna a taxa de câmbio (não recebe parâmetro)

if opcao_escolhida == 1: # se a opção escolhida for 1
    print(f"O valor em dólar é: {calcular_valor_dolar(valor, taxa)}") # chama a função calcular_valor_dolar para fazer o cálculo e faz a impressão do valor em dólar
elif opcao_escolhida == 2: # se a opção escolhida for 2
    print(f"O valor em real é: {calcular_valor_real(valor, taxa)}") # chama a função calcular_valor_real para fazer o cálculo e faz a impressão do valor em real
else: # se não for nenhuma das opções
    print("Opção inválida!") # faz a impressão de que a opção é inválida
    print("Tente novamente!") # faz a impressão de que o usuário deve tentar novamente
    print("") # faz a impressão de um espaço em branco


