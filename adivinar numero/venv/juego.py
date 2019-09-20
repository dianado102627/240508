import random
class Jugador:
    def __init__ (self, nombre, tipo):
        if nombre == 'maquina' and tipo=='machine':
            self.tipo = 'machine'
            self.numero_pensado = random.randint(0,100)
            self.num_mayor = 100
            self.num_menor = 0
        else:
            self.tipo = 'human'
    def pensar(self):
        if self.tipo == 'machine':
            self.numero_pensado = random.randint(0, 100)
            print ('numero pensado: ', self.numero_pensado)
            return self.numero_pensado
        else:
            self.numero = raw_input('Introduce tu numero')
            return self.numero
    def proponer(self):
        print ('Introduce el numero propuesto entre', '[',self.num_menor,',',self.num_mayor,']')

    def comprobar(self, num):
        if num == self.numero_pensado:
            print ('has acertado')
        elif num > self.num_pensado:
            print ('menor')
            self.num_mayor = num
        else:
            print ('mayor')
            self.num_menor = num
        return num

if __name__ == '__main__':
    n = raw_input('introduce el numero de partidas a jugar: ')

    j1 = Jugador(nombre='maquina', tipo='machine')
    j2 = Jugador(nombre = 'Diana', tipo = 'human')

    i = 1
    acierto = False
    num_pen = j1.pensar()
    while i <= n:
        j1.proponer()
        num = j2.pensar()
        j1.comprobar(num)
        if num == num_pen:
            break
        i += 1

