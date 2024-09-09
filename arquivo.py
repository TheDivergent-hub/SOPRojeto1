from processo import Processo


class Arquivo:
  processos = []


  def lerArquivo(self, nomeArq):
    try:
      with open(nomeArq, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            self.extrairProcessos(linhas)
    except FileNotFoundError:
      print(f"Erro: Arquivo '{nomeArq}' não encontrado.")
      exit(1)
    except Exception as e:
      print(f"Erro ao abrir arquivo '{nomeArq}': {e}")
      exit(1)

  def extrairProcessos(self, linhas):

    idProcesso = 0
    for linha in linhas:
      
      tempo_chegada, duracao = linha.strip().split()
      self.processos.append(Processo(int(idProcesso), int(tempo_chegada),int(duracao)))
      idProcesso += 1 
      #print("id {0} chegada {1} duração {2}".format(idProcesso, tempo_chegada, duracao))
      


#arq = Arquivo()
#arq.lerArquivo("processos.txt")
