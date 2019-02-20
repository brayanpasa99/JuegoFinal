class Jugador():

    def __init__(self, vidaCastillo, cantDinero, raza):
        self._vidaCastillo = vidaCastillo
        self._canDinerocanDinero = cantDinero
        self._raza = raza

    def escogerUnidad(self):
        return self._raza
