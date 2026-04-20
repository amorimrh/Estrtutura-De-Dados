from ListaDupla import ListaDupla

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
