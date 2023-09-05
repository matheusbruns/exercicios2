from main import gerar_array_aleatorio, verificar_valores_no_intervalo


def test_tamanho_do_array():
  array_aleatorio = gerar_array_aleatorio(20000)
  print(array_aleatorio)
  assert len(array_aleatorio) == 20000


def test_valores_no_intervalo():
  array_aleatorio = gerar_array_aleatorio(20000)
  assert verificar_valores_no_intervalo(array_aleatorio)


test_tamanho_do_array()
