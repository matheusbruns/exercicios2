from main import BibliotecaVirtual


def test_adicionar_livro():
  biblioteca = BibliotecaVirtual()
  biblioteca.adicionar_livro("Duna")
  assert "Duna" in biblioteca.listar_livros()


def test_remover_livro():
  biblioteca = BibliotecaVirtual()
  biblioteca.adicionar_livro("Neuromancer")
  biblioteca.remover_livro("Neuromancer")
  assert "Neuromancer" not in biblioteca.listar_livros()


def test_listar_livros():
  biblioteca = BibliotecaVirtual()
  biblioteca.adicionar_livro("Fundação")
  biblioteca.adicionar_livro("Solaris")
  biblioteca.adicionar_livro("Blade Runner")
  assert biblioteca.listar_livros() == ["Fundação", "Solaris", "Blade Runner"]
