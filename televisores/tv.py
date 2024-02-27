class TV:
    __numTV = 0
    def __init__ (self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1

        TV.__numTV += 1

    def getMarca(self):
        return self.__marca
    
    def getCanal(self):
        return self.__canal

    def getPrecio(self):
        return self.__precio
    
    def getVolumen(self):
        return self.__volumen

    def getControl(self):
        return self.__control

    def setMarca(self, marca):
        self.__marca = marca
    
    def setCanal(self, canal):
        if self.__estado and canal>=1 and canal<=120:
            self.__canal = canal

    def setPrecio(self, precio):
        self.__precio = precio
    
    def setVolumen(self, volumen):
        if self.__estado and volumen>=0 and volumen<=7:
            self.__volumen = volumen

    def setControl(self, control):
        self.__control = control

    @classmethod
    def getNumTV(cls):
        return cls.__numTV

    @classmethod
    def setNumTV(cls, num):
        cls.__numTV = num
    
    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def getEstado(self):
        return self.__estado

    def canalUp(self):
        self.setCanal(self.__canal +1)

    def canalDown(self):
        self.setCanal(self.__canal -1)

    def volumenUp(self):
        self.setVolumen(self.__volumen +1)

    def volumenDown(self):
        self.setVolumen(self.__volumen -1)
