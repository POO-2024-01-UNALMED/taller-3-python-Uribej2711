from.tv import TV

class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv

    def get_tv(self):
        return self._tv
