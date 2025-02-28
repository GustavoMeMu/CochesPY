""" Crea una clase Coche con los siguientes atributos y métodos:

Atributos:

marca
modelo
combustible (litros, comienza en 100)
Métodos:

conducir(km): Reduce 1 litro de combustible cada 10 km.
repostar(litros): Aumenta el combustible hasta un máximo de 100 litros.
estado(): Muestra la cantidad de combustible restante.
 """
 # Definimos las constantes
COMBUSTIBLE = 100
KM_POR_LITRO = 10

# Definimos la clase Coche
class Coche:
    def __init__(self, marca='', modelo=''):
        self.marca = marca
        self.modelo = modelo
        self.combustible = COMBUSTIBLE
    
    def conducir(self, km=0):
        consumo = km / KM_POR_LITRO
        if consumo > self.combustible:
            print(f'No hay suficiente combustible para recorrer {km} km.')
        else:
            self.combustible -= consumo
            print(f'Has conducido {km} km. Combustible restante: {self.combustible} litros.')
    
    def repostar(self, litros=0):
        if litros <= 0:
            print('Cantidad de combustible inválida.')
            return
        
        nuevo_nivel = self.combustible + litros
        if nuevo_nivel > COMBUSTIBLE:
            self.combustible = COMBUSTIBLE
            print('Tanque lleno!')
        else:
            self.combustible = nuevo_nivel
            print(f'Repostaste {litros} litros. Combustible actual: {self.combustible} litros.')
    
    def estado(self):
        print(f'Combustible restante: {self.combustible} litros.')
        
# Instancia de la clase Coche
mi_coche = Coche('Toyota', 'Corolla')

def menu():
    while True:
        print(''.center(50, '^'))
        op = int(input('1) Conducir\n2) Repostar\n3) Estado\n4) Salir\nElija una opción: '))
        
        if op == 4:
            break
        elif op == 1:
            km = int(input('Ingrese la cantidad de km a conducir: '))
            mi_coche.conducir(km)
        elif op == 2:
            litros = int(input('Ingrese la cantidad de litros a repostar: '))
            mi_coche.repostar(litros)
        elif op == 3:
            mi_coche.estado()
        else:
            print('Opción no válida')
        
        print(''.center(50, '-'))
        print('\nFin de la operación. Enter para volver al menú principal')

menu()

