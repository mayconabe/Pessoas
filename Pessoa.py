class Pessoa:
  
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def get_nome(self):
    return self.nome

  def set_nome(self, nome):
    self.nome = nome
    return self