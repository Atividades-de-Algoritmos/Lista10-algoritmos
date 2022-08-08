#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 06/08/2022
#
# 1 - Em linguagem Python, faça um programa que lê uma temperatura em graus Celsius e apresentá-la convertida em
# graus Fahrenheit.
# . A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius.

# OBS: o programa de conter três funções:
# a - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# b - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# c - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

# -- Funções(a, b, c) --

# 1. função a
def ler_temperaturaC():  # Função para ler e retorna o valor da temperatura (não recebe parâmetro)
    temperaturaC = float(input("Digite a temperatura em graus Celsius: ")) # Lê a temperatura em graus Celsius e armazena na variável temperaturaC
    return temperaturaC # Retorna o valor da temperatura em graus Celsius

# 2. função b
def calcular_temperaturaF(temperaturaC): # Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
    temperaturaF = (9 * temperaturaC + 160) / 5 # Faz o cálculo da temperatura em graus Fahrenheit e armazena na variável temperaturaF
    return temperaturaF # retorna o valor da temperatura em graus Fahrenheit

# 3. função c
def mostrar_temperaturaF(temperaturaF): # Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão (recebe como parâmetro a temperatura em graus Fahrenheit)
    print(f"\nA temperatura em graus Fahrenheit é:  {temperaturaF}") # Faz a impressão da temperatura em graus Fahrenheit

# -- Chamada das funções --

temperaturaC = ler_temperaturaC() # Chama a função ler_temperaturaC para ler e retorna o valor da temperatura em graus Celsius e armazena na variável temperaturaC

temperaturaF = calcular_temperaturaF(temperaturaC) # Chama a função calcular_temperaturaF para fazer o cálculo da temperatura em graus Fahrenheit e armazena na variável temperaturaF

mostrar_temperaturaF(temperaturaF) # Chama a função mostrar_temperaturaF para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão da temperatura em graus Fahrenheit

print('\nFim do programa') # Informando ao usuário que o script chegou ao fim