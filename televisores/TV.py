
class TV:
    num_TV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500

        TV.num_TV += 1

    @staticmethod
    def get_num_TV():
        return TV.num_TV

    @staticmethod
    def set_num_TV(num_TV):
        TV.num_TV = num_TV
        return TV.num_TV

    def turn_on(self):
        self.estado = True

    def turn_off(self):
        self.estado = False

    def canal_up(self):
        self.set_canal(self.canal + 1)

    def canal_down(self):
        self.set_canal(self.canal - 1)

    def volumen_up(self):
        self.set_volumen(self.volumen + 1)

    def volumen_down(self):
        self.set_volumen(self.volumen - 1)

    def get_marca(self):
        return self.marca

    def get_canal(self):
        return self.canal

    def get_precio(self):
        return self.precio

    def get_volumen(self):
        return self.volumen

    def get_control(self):
        return self.control

    def get_estado(self):
        return self.estado

    def set_marca(self, marca):
        self.marca = marca

    def set_canal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def set_precio(self, precio):
        self.precio = precio

    def set_volumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def set_control(self, control):
        self.control = control   