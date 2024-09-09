from arquivo import Arquivo


def fcfs (processos):
  tempoCorrido = 0
  tempoDoProcesso = 0
  Tretorno_total = 0
  Tresposta_total = 0
  Tespera_total = 0
  for i in range(len(processos)):
    tempoDoProcesso = processos[i].duracao
    if tempoCorrido - processos[i].Tchegada < 0:
      processos[i].Tresposta = 0
    else:
      processos[i].Tresposta = tempoCorrido - processos[i].Tchegada
    while tempoDoProcesso != 0:
      tempoCorrido += 1
      tempoDoProcesso -= 1
      if tempoDoProcesso == 0:
        processos[i].Tretorno = tempoCorrido
        processos[i].Tespera = processos[i].Tresposta

  for i in range(len(processos)):
    Tretorno_total += processos[i].Tretorno 
    Tresposta_total += processos[i].Tresposta
    Tespera_total += processos[i].Tespera

  Tretorno_media = Tretorno_total / len(processos)
  Tresposta_media = Tresposta_total / len(processos)
  Tespera_media = Tespera_total / len(processos)
  return [Tretorno_media, Tresposta_media, Tespera_media]

def sjf (processos):
  tempo = 0
  finalizados = [] 
  for i in processos:
    #processos[i].duracao =- 1 
    print(processos[i].duracao)
    for j in processos :
      if processos[j].duracao < processos[i].duracao:
        aux = processos[j]
        processos[i] = processos[j]
        processos[i] = aux 
      else:
        continue
  tempo += 1

def rr(entrada):
    tempo = 0
    fila = []
    processos = entrada[:]
    quantum = 2
    finalizados = []
    Tretorno_total = 0
    Tresposta_total = 0
    Tespera_total = 0

    while processos or fila:

      if fila:
        processo_atual = fila.pop(0)

        if not processo_atual.executou:
          processo_atual.executou = True
          processo_atual.Tresposta = tempo

        tempo_em_processamento = min(quantum, processo_atual.duracao)

        tempo += tempo_em_processamento
        processo_atual.duracao -= tempo_em_processamento

        if processo_atual.duracao == 0:
          processo_atual.Tretorno = tempo - processo_atual.Tchegada
          processo_atual.Tespera = processo_atual.Tretorno - processo_atual.duracao_total
          finalizados.append(processo_atual)
        else:

          while processos and processos[0].Tchegada <= tempo:
            fila.append(processos.pop(0))


          fila.append(processo_atual)
      else:
        if processos:
          tempo = processos[0].Tchegada

        while processos and processos[0].Tchegada <= tempo:
          fila.append(processos.pop(0))
    
    for i in range(len(finalizados)):
      Tretorno_total += finalizados[i].Tretorno 
      Tresposta_total += finalizados[i].Tresposta
      Tespera_total += finalizados[i].Tespera

    Tretorno_media = Tretorno_total / len(finalizados)
    Tresposta_media = Tresposta_total / len(finalizados)
    Tespera_media = Tespera_total / len(finalizados)
    return [Tretorno_media, Tresposta_media, Tespera_media]

def main():

  arq = Arquivo()
  arq.lerArquivo("processos.txt")
  processos = arq.processos

  FCFS = fcfs(processos)
  # retorno -> resposta -> espera 
  print(" FCFS: {0} {1} {2}".format(float(FCFS[0]), float(FCFS[1]), float(FCFS[2])))

  #SJF = sjf(arq.processos)
  # retorno -> resposta -> espera 
  RR = rr(processos)
  print(" RR: {0} {1} {2}".format(float(RR[0]), float(RR[1]), float(RR[2])))
  

if __name__ == "__main__":
  main()
















