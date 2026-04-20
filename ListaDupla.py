from NoListaDupla import NoListaDupla

class ListaDupla:
    def __init__(self):
        self._head = None

    def insere(self, v):
        novo = NoListaDupla(v)
        novo.set_prox(self._head)
        if self._head is not None:
            self._head.set_ant(novo)
        self._head = novo

    def imprime(self):
        atual = self._head
        while atual is not None:
            print(atual.get_info())
            atual = atual.get_prox()

    def vazia(self):
        return self._head is None

    def busca(self, v):
        atual = self._head
        while atual is not None:
            if atual.get_info() == v:
                return atual
            atual = atual.get_prox()
        return None

    def comprimento(self):
        cont = 0
        atual = self._head
        while atual is not None:
            cont += 1
            atual = atual.get_prox()
        return cont

    def ultimo(self):
        if self.vazia():
            return None
        atual = self._head
        while atual.get_prox() is not None:
            atual = atual.get_prox()
        return atual

    def retira(self, v):
        alvo = self.busca(v)
        if alvo is None:
            return

        if alvo == self._head:
            self._head = alvo.get_prox()
        else:
            alvo.get_ant().set_prox(alvo.get_prox())

        if alvo.get_prox() is not None:
            alvo.get_prox().set_ant(alvo.get_ant())

    def libera(self):
        self._head = None

    def insereFim(self, v):
        if self.vazia():
            self.insere(v)
            return
        ult = self.ultimo()
        novo = NoListaDupla(v)
        ult.set_prox(novo)
        novo.set_ant(ult)

    def inserePosicao(self, v, pos):
        if pos < 1:
            return
        if pos == 1:
            self.insere(v)
            return

        atual = self._head
        contador = 1
        while atual is not None and contador < pos - 1:
            atual = atual.get_prox()
            contador += 1

        if atual is None:
            return

        novo = NoListaDupla(v)
        novo.set_prox(atual.get_prox())
        novo.set_ant(atual)
        
        if atual.get_prox() is not None:
            atual.get_prox().set_ant(novo)
        atual.set_prox(novo)

    def retiraPosicao(self, pos):
        if pos < 1 or self.vazia():
            return
        atual = self._head
        contador = 1

        while atual is not None and contador < pos:
            atual = atual.get_prox()
            contador += 1

        if atual is None:
            return

        if atual == self._head:
            self._head = atual.get_prox()
        else:
            atual.get_ant().set_prox(atual.get_prox())

        if atual.get_prox() is not None:
            atual.get_prox().set_ant(atual.get_ant())

    def _get_info_posicao(self, pos):
        atual = self._head
        contador = 1
        while atual is not None and contador < pos:
            atual = atual.get_prox()
            contador += 1
        return atual.get_info() if atual is not None else None

    def move(self, posAtual, novaPos):
        titulo = self._get_info_posicao(posAtual)
        if titulo is None or posAtual == novaPos:
            return
        self.retiraPosicao(posAtual)
        self.inserePosicao(titulo, novaPos)

    def imprimeNumerada(self):
        atual = self._head
        pos = 1
        while atual is not None:
            print(f"{pos}. {atual.get_info()}")
            atual = atual.get_prox()
            pos += 1