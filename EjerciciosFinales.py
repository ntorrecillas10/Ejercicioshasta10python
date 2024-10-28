from random import randint

jugadaEscrita = randint(1,3)
jugadaMaquina = randint(1,3)

#1-papel-2-piedra-3-tijera

if jugadaEscrita - 1 == jugadaMaquina or jugadaEscrita +2 == jugadaMaquina:
    print("Gana Maquina")
elif jugadaEscrita + 1 == jugadaMaquina or jugadaEscrita - 2 == jugadaMaquina:
    print("Gana Escrito")
else:
    print("Empate")
