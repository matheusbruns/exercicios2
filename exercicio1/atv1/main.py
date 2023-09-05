import random


def gerar_array_aleatorio(tamanho):
  return [random.randint(-999999, 999999) for _ in range(tamanho)]


def verificar_valores_no_intervalo(array):
  return all(-999999 <= valor <= 999999 for valor in array)
