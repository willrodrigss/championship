from clube import Clube

class Jogador():
    def __init__(self, nome, num, pos, clube=Clube(" ")):
        self.nome = nome
        self.num = num
        self.pos = pos
        self.clube = clube