from clube import Clube

class Partida():
    def __init__(self, rodada, casa=Clube(" "), fora=Clube(" "), estadio=" ", golCasa=0, golFora=0):
        self.rodada = rodada
        self.casa = casa
        self.fora = fora
        self.estadio = estadio
        self.golCasa = golCasa
        self.golFora = golFora
    
    def golC(self):
        self.golCasa += 1
        self.casa.gp += 1
        self.fora.gc += 1
        self.casa.sg += 1
        self.fora.sg -= 1
        self.atualizaVED()

    def golF(self):
        self.golFora += 1
        self.casa.gc += 1
        self.fora.gp += 1
        self.casa.sg -= 1
        self.fora.sg += 1
        self.atualizaVED()
    
    def atualizaVED(self):
        if(self.golCasa > self.golFora):
            self.casa.vit += 1
            self.fora.der += 1
        
        if(self.golCasa < self.golFora):
            self.casa.der += 1
            self.fora.vit += 1

        if(self.golCasa == self.golFora):
            self.casa.emp += 1
            self.fora.emp += 1
    
    def placar(self):
        print(self.casa.nome, " ", self.golCasa, " x " , self.golFora, " ",self.fora.nome)

 
    
