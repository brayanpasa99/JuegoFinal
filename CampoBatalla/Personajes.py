import random

PERSONAJES = [['Orco1.png', 'Orco2.png', 'Orco3.png'], ['Elfo1.png', 'Elfo2.png', 'Elfo3.png'], ['Guerrero1.png', 'Guerrero2.png', 'Guerrero3.png']]


class Personaje():

    def figuras(self):
        return PERSONAJES[random.randrange(2)]
