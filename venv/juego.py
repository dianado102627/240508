import random
class Jugador:
    def __init__ (self, nombre='maquina', tipo='machine'):
        self.numero_pensado = random.randint(0,100)
        self.num_mayor = 100
        self.num_menor = 0
    def pensar(self):
        if self.tipo == 'machine':
            self.numero_pensado = random.randint(0, 100)
            return self.numero_pensado
        else:
            self.numero = raw_input('Introduce tu numero')
            return self.numero
    def proponer(self):
        print ('Introduce el numero propuesto entre', num_menor, ' y ', num_mayor)
    def comprobar(self, num):
        if num == self.numero_pensado:
            print ('has acertado')
            return true
        elif num > self.num_pensado:
            print ('menor')
            self.num_mayor = num
            return false
        else:
            print ('mayor')
            self.num_menor = num
            return false

if __name__ == '__main__':
    n = raw_input('introduce el numero de partidas a jugar')

    j1 = Jugador()
    j2 = Jugador(nombre = 'Diana', tipo = 'human')

    i = 1
    acierto = false
    num_pen = j1.pensar()
    while i <= n | acierto == 'false':
        j1.proponer()
        num = j2.pensar()

