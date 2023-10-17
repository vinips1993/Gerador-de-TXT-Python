import json

times = {}

with open("resultados.txt", "r", encoding="utf-8") as arq:
    for linha in arq:
        dado = linha.split(" ")
        sets_pri = int (dado[1])
        sets_seg = int (dado[3])
        if sets_pri < sets_seg:
            #segundo time venceu
            pts = sets_seg - sets_pri
            time = dado[4].replace('\n','')
        else:
            #primeiro time venceu
            pts = sets_pri = sets_seg
            time = dado [0]

        if time in times: 
            times[time] += pts       
        else:
            times [time] = pts 


with open("campeonato.txt", "w", encoding="utf-8") as camp:
    camp.write(json.dumps(times))

#print(times)