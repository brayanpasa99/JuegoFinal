class Caracteristicas():

    def __init__(self):
        self.castillo = []
        self.iconos = []
        self.atacarpersonaje1 = []
        self.atacarpersonaje2 = []
        self.atacarpersonaje3 = []
        self.caminarpersonaje1 = []
        self.caminarpersonaje2 = []
        self.caminarpersonaje3 = []
        self.morirpersonaje1 = []
        self.morirpersonaje2 = []
        self.morirpersonaje3 = []

    def setSpritesCastillo(self, castillo):
        self.castillo = castillo

    def setIconos(self, iconos):
        self.iconos = iconos

    def setSpritesAtacarPersonaje1(self, atacarpersonaje1):
        self.atacarpersonaje1 = atacarpersonaje1

    def setSpritesAtacarPersonaje2(self, atacarpersonaje2):
        self.atacarpersonaje2 = atacarpersonaje2

    def setSpritesAtacarPersonaje3(self, atacarpersonaje3):
        self.atacarpersonaje3 = atacarpersonaje3

    def setSpritesCaminarPersonaje1(self, caminarpersonaje1):
        self.caminarpersonaje1 = caminarpersonaje1

    def setSpritesCaminarPersonaje2(self, caminarpersonaje2):
        self.caminarpersonaje2 = caminarpersonaje2

    def setSpritesCaminarPersonaje3(self, caminarpersonaje3):
        self.caminarpersonaje3 = caminarpersonaje3

    def setSpritesMorirPersonaje1(self, morirpersonaje1):
        self.morirpersonaje1 = morirpersonaje1

    def setSpritesMorirPersonaje2(self, morirpersonaje2):
        self.morirpersonaje2 = morirpersonaje2

    def setSpritesMorirPersonaje3(self, morirpersonaje3):
        self.morirpersonaje3 = morirpersonaje3

    def dibujar(self, ventana):
        pass

    def update(self, rectangulo):
        pass
