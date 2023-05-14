import random


class JuegoAhorcado:
    ESTADOS = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    SALVADO = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    categorias = 'FRUTAS ANIMALES VIDEOJUEGOS'.split()
    frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
             'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    animales = 'MONO GORILA COCODRILO ELEFANTE GATO PERRO'.split()
    videojuegos = 'ZELDA MARIO CSGO KIRBY DOOM WOLFESTEIN CASTLEVANIA'.split()

    escoger = {'FRUTAS': frutas, 'ANIMALES': animales, 'VIDEOJUEGOS': videojuegos}
    categoria = ''
    nombre_jugador = ''

    def get_intentos(self, fallos):
        return len(self.ESTADOS) - fallos - 1

    def jugar(self):

        self.nombre_jugador = str(input("Cual es tu nombre? "))

        let_incorrectas = []
        let_correctas = []
        self.categoria = random.choice(self.categorias)
        secreto = random.choice(self.escoger[self.categoria])

        while True:
            self.dibujar(let_incorrectas, let_correctas, secreto)

            letra_actual = self.dime_letra(let_incorrectas + let_correctas)

            if letra_actual == "TERMINAR":
                print(self.ESTADOS[-1])
                print('La palabra era "{}"'.format(secreto))
                break

            if letra_actual in secreto:

                let_correctas.append(letra_actual)

                g = True
                for sl in secreto:
                    if sl not in let_correctas:
                        g = False
                        break
                if g:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado, {}!'.format(self.nombre_jugador))
                    break

            else:
                let_incorrectas.append(letra_actual)
                if len(let_incorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(let_incorrectas, let_correctas, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break
                print("Te quedan {} intentos".format(self.get_intentos(len(let_incorrectas))))

    def dibujar(self, incorrectas, correctas, secreto):
        print(self.ESTADOS[len(incorrectas)])
        print('La categoría es: ', self.categoria)
        print()

        print('Letras incorrectas: ', end='')
        for letras in incorrectas:
            print(letras, end=' ')

        long_li = len(incorrectas)
        if long_li == 0:
            print('No hay letras incorrectas.')
        if long_li == long_li + 1:
            print('Letras diferentes.')
        if long_li == long_li + 2:
            print('No coinciden.')

        print()

        espacios = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in correctas:
                espacios[i] = secreto[i]

        print(' '.join(espacios))

    def dime_letra(self, ya_adivinadas):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()

            if len(adivina) != 1 and adivina.upper() != "TERMINAR":
                print('Introduce una única letra.')
            elif adivina in ya_adivinadas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    juego1 = JuegoAhorcado()
    juego1.jugar()
