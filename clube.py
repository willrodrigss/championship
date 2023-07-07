class Clube():
    def __init__(self, nome, pts=0, vit=0, emp=0, der=0, gp=0, gc=0, sg=0):
        self.nome = nome
        self.pts = pts
        self.vit = vit
        self.emp = emp
        self.der = der
        self.gp = gp
        self.gc = gc
        self.sg = sg
    
    def ganhou(self):
        self.vit += 1
        self.pts += 3
    
    def empatou(self):
        self.emp += 1
        self.pts += 1

    def perdeu(self):
        self.der += 1
    