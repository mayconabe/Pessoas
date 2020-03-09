class Pessoa:
  
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def set_idade(self, idade):
		self.idade = idade
		return self

	def get_idade(self):
		return self.idade
