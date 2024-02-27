from .marca import Marca
from .control import Control

class TV:
    def __init__(self, marca=None, estado=False):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = Control(self)

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_canal(self):
        return self._canal

    def set_canal(self, canal):
        self._canal = canal

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def get_volumen(self):
        return self._volumen

    def set_volumen(self, volumen):
        self._volumen = volumen

    def get_control(self):
        return self._control