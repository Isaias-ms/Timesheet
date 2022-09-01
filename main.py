from datetime import time

#TIMESHEET

with open("horario.txt", "r", encoding="utf-8") as horas:    #lendo um arquivo txt e se referindo ele como "HORAS".
    horario = horas.readlines()

lista_monitoramento = list()               #Aqui vou usar uma lista para pegar o horario.
separar = list()                           #vai ser para eu separar as frases em palavras.
for linha in horario:
    separar = linha.split()
    lista_monitoramento.append(separar)

#print(lista_monitoramento)
prelista = list()
caractere = list()
lista = list()
if len(lista_monitoramento) == 4:
    for c in range(1, len(lista_monitoramento)+1):
        prelista.append(lista_monitoramento[c-1][-1]) #Para botar cada hórario, só pegando o último dado dentro de cada lista.

    #print(prelista)
    #Fiz para tirar os ( ":" ).
    for c in prelista:
        caractere.append(c.split(":"))  #del caractere[contador][-1] #Excluir os minutos-#contador += 1

    for c in range(2, len(caractere) + 1, 2):  # A ideia foi agrupar 2 grupos de horários mais próximos para fazer o calc d horas
        lista.append([caractere[c - 2], caractere[c - 1]])

elif len(lista_monitoramento) > 5:
    for c in range(1, len(lista_monitoramento) + 1):
        prelista.append(lista_monitoramento[c - 1][-1])

    #print(prelista)
    for c in prelista:
        caractere.append(c.split(":"))
    #print(prelista)
    #print(caractere)
    for c in range(2, len(caractere)+1, 2):
        lista.append([caractere[c - 2], caractere[c - 1]])
    #print(lista)



#Tempo trabalhado.
#t_dtrb = []#Criei mais uma lista para resolver o calculo das horas/minutos.
#for cont in range(0, len(lista)):
    #tempo_dtrabalho.append([horas, minutos]) #adicionando eles à lista.
    #t_dtrb.append     #  time = tempo, vou tentar solucionar as horas
    #print(t_dtrb)
#print(t_dtrb)

#print(lista)
def cal():
        hora = list()
        minutos = list()
        soma = clc = dif = calhora = 0
        for tm in range(0, len(lista)):  # tm = 0 /
            hora.append([lista[tm][0][0], lista[tm][1][0]])  # Pegar as horas
            minutos.append([lista[tm][0][1], lista[tm][1][1]])  # Pegar os minutos
        #print(hora)
        #print(minutos)

        for c in range(0, len(hora)):
            h1 = int(hora[c][0])
            h2 = int(hora[c][1])
            dif = h2 - h1
            calhora += dif
        #print(calhora)

        for c in range(0, len(minutos)):
            min1 = int(minutos[c][0])
            min2 = int(minutos[c][1])
            clc = min1 + min2
            soma += clc
            #print(min1, min2)
        #print(soma)

        # Equilabrando os 60m para +1h.
        if soma >= 60:
            div = soma // 60
            calhora = calhora + div  # adicionando ás horas
            soma = soma % 60  # minutos que sobrar
            #print(div, calhora, soma)

        if soma == 0:
            return print(f"Horas Trabalhadas -> {calhora} horas.")
        else:
            return print(f"Horas Trabalhadas -> {calhora} horas e {soma} minutos.")

with open("horario.txt", "r", encoding="utf-8") as arquivo:
    timesheet = arquivo.read()
    print(timesheet)
    cal() #Em seguida abrir a função dos cálculos das horas trabalhadas


