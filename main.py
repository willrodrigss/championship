from clube import Clube
from partida import Partida
from jogador import Jogador

fla = Clube("Flamengo")
vas = Clube("Vasco")

j1 = Jogador("Gabi", 10, "Atacante", fla)
j2 = Jogador("Puma", 21, "Lateral", vas)
j3 = Jogador("Arrascaeta", 14, "Meia", fla)
j4 = Jogador("Capasso", 2, "Zagueiro", vas)

r1 = Partida(1, fla, vas, "Maracana")

r1.golC(j1)
r1.golC(j1)
r1.golC(j2)
r1.golC(j4)
r1.golF(j2)

r1.placar()

r1.fimdeJogo()

fla.estatisticas()


        