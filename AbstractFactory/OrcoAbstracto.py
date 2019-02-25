import abc

class OrcoAbstracto():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def Atacar(self):
        pass

    @abc.abstractmethod
    def Caminar(self):
        pass

    @abc.abstractmethod
    def Muerte(self):
        pass
