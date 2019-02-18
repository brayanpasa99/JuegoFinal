import random

PERSONAJES = [['Orcos/Orco1.png', 'Orcos/Orco2.png', 'Orcos/Orco3.png'],
              ['Elfos/Elfo1.png', 'Elfos/Elfo2.png', 'Elfos/Elfo3.png'],
              ['Guerreros/Guerrero1.png', 'Guerreros/Guerrero2.png', 'Guerreros/Guerrero3.png']]


class Personaje():

    def figuras(self):
        return PERSONAJES[random.randrange(3)]
