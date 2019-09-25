import random
class Jugador:
    def __init__(self, nombre, tipo):
        if nombre == 'maquina' and tipo == 'machine':
            self.nombre = nombre
            self.tipo = tipo
            self.numero_pensado = random.randint(0,100)
            self.num_mayor = 100
            self.num_menor = 0
        else:
            self.nombre = input('Introduce tu nombre: ')
            self.tipo = tipo
    def pensar(self):
        if self.tipo == 'machine':
            self.num_mayor = 100
            self.num_menor = 0
            self.numero_pensado = random.randint(0, 100)
            print ('numero pensado: ', self.numero_pensado)
            return self.numero_pensado
        else:
            self.numero = int(input('Introduce tu numero: '))
            return self.numero
    def proponer(self):
        print('Introduce el numero propuesto entre', '[', self.num_menor, ',', self.num_mayor, ']')

    def comprobar(self, num, iteracion, totalIntentos):
        if num == self.numero_pensado:
            print('Has acertado en ', iteracion, 'intentos')
        elif num > self.numero_pensado:
            print('Vuelve a intentarlo con un numero menor')
            print('Te quedan ', totalIntentos-iteracion, 'intentos')
            self.num_mayor = num
        else:
            print('Vuelve a intentarlo con un numero mayor')
            print('Te quedan ', totalIntentos - iteracion, 'intentos')
            self.num_menor = num
        return num

if __name__ == '__main__':
    n = int(input('Introduce el numero de partidas a jugar: '))

    j1 = Jugador(nombre='maquina', tipo='machine')
    j2 = Jugador(nombre='', tipo='human')

    acabar = True
    while acabar:
        i = 1
        num_pen = j1.pensar()
        while i <= n:
            j1.proponer()
            num = j2.pensar()
            j1.comprobar(num, i, n)
            if num == num_pen:
                break
            i += 1
        opcion = input('¿Deseas seguir jugando? S/N: ')
        if opcion == 'N':
            acabar = False
    print('No quedan mas tiradas!!')

