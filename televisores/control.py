from televisores.tv import TV

class Control:
    def __init__(self):
        self.__tv = None

    def enlazar(self, tv):
        self.__tv = tv
        tv.set_control(self)

    def turn_on(self):
        self.__tv.set_estado(True)

    def turn_off(self):
        self.__tv.set_estado(False)

    def canal_up(self):
        self.__tv.set_canal(self.__tv.get_canal() + 1)

    def canal_down(self):
        self.__tv.set_canal(self.__tv.get_canal() - 1)

    def volumen_up(self):
        self.__tv.set_volumen(self.__tv.get_volumen() + 1)

    def volumen_down(self):
        self.__tv.set_volumen(self.__tv.get_volumen() - 1)

    def set_volumen(self, volumen):
        self.__tv.set_volumen(volumen)

    def set_canal(self, canal):
        self.__tv.set_canal(canal)

    def get_tv(self):
        return self.__tv
