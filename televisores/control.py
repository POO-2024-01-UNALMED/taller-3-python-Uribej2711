class Control:
    def __init__(self, tv):
        self._tv = tv

    def enlazar(self, tv):
        self._tv = tv

    def get_tv(self):
        return self._tv
