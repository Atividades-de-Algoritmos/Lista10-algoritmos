#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 12/07/2022
#
# 2.	Em linguagem Python, faça um programa que efetuar o cálculo da quantidade de litros de combustível
# gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na
# viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da
# velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
# OBS: o programa de conter quatro funções:
# d.	- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# e.	- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# f.	- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# g.	- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

# funções
# a
def ler_tempo_velocidade(): # função para ler os valores (não recebe parâmetro e retorna os dois valores)
    tempo = float(input("Digite o tempo gasto na viagem: ")) # lê o tempo gasto na viagem e armazena na variável tempo
    velocidade = float(input("Digite a velocidade média durante a viagem: ")) # lê a velocidade média durante a viagem e armazena na variável velocidade
    return tempo, velocidade # retorna os dois valores lidos

# b
def calcular_distancia(tempo, velocidade): # função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
    distancia = tempo * velocidade # calcula a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE
    return distancia # retorna a distância calculada pelo tempo e a velocidade

# c
def calcular_litros(distancia): # função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
    litros = distancia / 12 # calcula a quantidade de litros utilizada na viagem com a fórmula LITROS_USADOS = DISTANCIA / 12
    return litros # retorna a quantidade de litros utilizada na viagem

# d
def apresentar_resultado(tempo, velocidade, distancia, litros): # função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
  print(f"O tempo gasto na viagem foi de {tempo} horas.") # imprime o tempo gasto na viagem
  print(f"A velocidade média durante a viagem foi de {velocidade} Km/h.") # imprime a velocidade média durante a viagem
  print(f"A distância percorrida foi de {distancia} Km.") # imprime a distância percorrida
  print(f"A quantidade de litros utilizada na viagem foi de {litros} litros.") # imprime a quantidade de litros utilizada na viagem


# chamada das funções
tempo, velocidade = ler_tempo_velocidade() # chama a função ler_tempo_velocidade para ler os valores
distancia = calcular_distancia(tempo, velocidade) # chama a função calcular_distancia para calcular a distância
litros = calcular_litros(distancia) # chama a função calcular_litros para calcular a quantidade de litros
apresentar_resultado(tempo, velocidade, distancia, litros) # chama a função apresentar_resultado para apresentar o resultado

