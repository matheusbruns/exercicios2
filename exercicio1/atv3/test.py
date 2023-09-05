from main import converter_massa_lunar, converter_distancia_marte
import pytest


def test_converter_massa_lunar():
  assert converter_massa_lunar(6) == 1
  assert converter_massa_lunar(12) == 2
  assert converter_massa_lunar(0) == 0


def test_converter_distancia_marte():
  assert converter_distancia_marte(10) == pytest.approx(26.48, rel=1e-2)
  assert converter_distancia_marte(20) == pytest.approx(52.96, rel=1e-2)
  assert converter_distancia_marte(0) == 0
