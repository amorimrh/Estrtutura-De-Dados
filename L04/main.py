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


if __name__ == "__main__":
    playlist = ListaDupla()

    playlist.insereFim("Seek and Destroy")
    playlist.insereFim("Rock and Roll Ain't Noise Pollution")
    playlist.insereFim("Good Times Bad Times")

    playlist.inserePosicao("Sabbath Bloody Sabbath", 3)
    
    print("Playlist Inicial:")
    playlist.imprimeNumerada()
    print(f"\nTotal de musicas: {playlist.comprimento()}\n")

    playlist.move(3, 1)
    print("Apos mover a musica da posicao 3 para 1:")
    playlist.imprimeNumerada()
    print()

    playlist.retira("Seek and Destroy")
    print("Apos remover 'Seek and Destroy':")
    playlist.imprimeNumerada()
    print()

    playlist.retiraPosicao(2)
    print("Apos remover a musica da posicao 2:")
    playlist.imprimeNumerada()
    print()
    
    playlist.libera()
    if playlist.vazia():
        print("A playlist foi limpa com sucesso.")
