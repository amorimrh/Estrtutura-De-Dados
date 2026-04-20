class NoListaDupla:
    def __init__(self, info):
        self._info = info
        self._ant = None
        self._prox = None

    def get_info(self):
        return self._info

    def set_info(self, info):
        self._info = info

    def get_ant(self):
        return self._ant

    def set_ant(self, ant):
        self._ant = ant

    def get_prox(self):
        return self._prox

    def set_prox(self, prox):
        self._prox = prox