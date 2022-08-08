#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 06/08/2022
#
# 2 - Em linguagem Python, faça um programa que efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# . Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# . Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# . Após basta calcular a quantidade de litros de combustível na fórmula: LITROS_USADOS = DISTANCIA / 12. O.
# . O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

# OBS: o programa de conter quatro funções:
# a.	- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# b.	- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# c.	- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# d.	- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

# -- Funções(a, b, c, d) --

# 1. função a
def ler_tempo_velocidade(): # Função para ler os valores (não recebe parâmetro e retorna os dois valores)
    tempo = float(input("Digite o tempo gasto na viagem (horas): ")) # Lê o tempo gasto na viagem e armazena na variável tempo
    velocidade = float(input("Digite a velocidade média durante a viagem (km/h): ")) # Lê a velocidade média durante a viagem e armazena na variável velocidade
    return tempo, velocidade # Retorna os dois valores lidos

# 2. função b
def calcular_distancia(tempo, velocidade): # Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
    distancia = tempo * velocidade # Calcula a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE
    return distancia # Retorna a distância calculada pelo tempo e a velocidade

# 3. função c
def calcular_litros(distancia): # Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
    litros = distancia / 12 # Calcula a quantidade de litros utilizada na viagem com a fórmula LITROS_USADOS = DISTANCIA / 12
    return litros # Retorna a quantidade de litros utilizada na viagem

# 4. função d
def apresentar_resultado(tempo, velocidade, distancia, litros): # Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
  print(f"\nO tempo gasto na viagem foi de {tempo} horas.") # Imprime o tempo gasto na viagem
  print(f"A velocidade média durante a viagem foi de {velocidade} Km/h.") # Imprime a velocidade média durante a viagem
  print(f"A distância percorrida foi de {distancia} Km.") # Imprime a distância percorrida
  print(f"A quantidade de litros utilizada na viagem foi de {litros} litros.") # Imprime a quantidade de litros utilizada na viagem

# -- Chamada das funções --

tempo, velocidade = ler_tempo_velocidade() # Chama a função ler_tempo_velocidade para ler os valores

distancia = calcular_distancia(tempo, velocidade) # Chama a função calcular_distancia para calcular a distância

litros = calcular_litros(distancia) # Chama a função calcular_litros para calcular a quantidade de litros

apresentar_resultado(tempo, velocidade, distancia, litros) # Chama a função apresentar_resultado para imprimir as informações
