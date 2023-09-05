from main import gerar_array_aleatorio, verificar_valores_no_intervalo, bubble_sort


def test_tamanho_do_array():
  array_aleatorio = gerar_array_aleatorio(20000)
  assert len(array_aleatorio) == 20000


def test_valores_no_intervalo():
  array_aleatorio = gerar_array_aleatorio(20000)
  assert verificar_valores_no_intervalo(array_aleatorio)


def test_ordenacao_do_array():
  array_aleatorio = gerar_array_aleatorio(20000)
  bubble_sort(array_aleatorio)
  print(array_aleatorio)
  assert all(array_aleatorio[i] <= array_aleatorio[i + 1]
             for i in range(len(array_aleatorio) - 1))
