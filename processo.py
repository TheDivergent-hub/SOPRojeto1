class Processo:
  idProcesso = 0
  Tchegada = 0 
  duracao = 0
  Tespera = 0
  Tretorno = 0
  Tresposta = 0
  executou = False
  duracao_total = 0
  
  
  def __init__(self, idProcesso, Tchegada, duracao):
    self.idProcesso = idProcesso
    self.Tchegada = Tchegada
    self.duracao = duracao
    self.setDuracao_total(duracao)

  def setDuracao_total(self, duracao):
    self.duracao_total = duracao

  