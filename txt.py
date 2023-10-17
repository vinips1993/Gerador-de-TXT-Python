import random

def gera_placar(timeA, timeB):
    vencedor = random.randint(0, 1)
    sets_perdedor = random.randint(0, 2)

    if vencedor == 0:
        return [3, sets_perdedor]
    else:
        return [sets_perdedor, 3]

times = ["Brasil", "França", "Italia", "USA", "Cuba", "Polônia"]
i = 0
arquivo = open("resultados.txt","w", encoding="utf-8")

while i < len(times):
    j = i + 1
    while j < len(times):
        #print(times[i], " X ", times[j])
        placar = gera_placar(times[i],times[j])
        #print(f"{times[i]} {placar[0]} X {placar[1]} {times[j]}")
        arquivo.write(f"{times[i]} {placar[0]} X {placar[1]} {times[j]}\n")
        j = j + 1
    i = i + 1    
