import pytest


def converter_massa_lunar(massa_terrestre):
  return massa_terrestre / 6


def converter_distancia_marte(metros):
  gravidade_terra = 9.81
  gravidade_marte = 3.71
  return (gravidade_terra / gravidade_marte) * metros
