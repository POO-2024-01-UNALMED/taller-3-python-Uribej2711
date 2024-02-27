
from televisores.marca import Marca
from televisores.control import Control

class TV:
    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = Control()

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_canal(self):
        return self.__canal

    def set_canal(self, canal):
        self.__canal = canal

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_volumen(self):
        return self.__volumen

    def set_volumen(self, volumen):
        self.__volumen = volumen

    def get_control(self):
        return self.__control