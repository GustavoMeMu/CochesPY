# Definimos las constantes
COMBUSTIBLE = 100
KM_POR_LITRO = 10

# Definimos la clase Coche
class Coche:
    def __init__(self, marca='', modelo=''):
        self.__marca = marca  
        self.__modelo = modelo  
        self.__combustible = COMBUSTIBLE  
    
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
    
    
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    

    def get_combustible(self):
        return self.__combustible
    
    def set_combustible(self, combustible):
        if combustible < 0:
            self.__combustible = 0
        elif combustible > COMBUSTIBLE:
            self.__combustible = COMBUSTIBLE
        else:
            self.__combustible = combustible
    
    def conducir(self, km=0):
        consumo = km / KM_POR_LITRO
        if consumo > self.__combustible:
            print(f'No hay suficiente combustible para recorrer {km} km.')
        else:
            self.__combustible -= consumo
            print(f'Has conducido {km} km. Combustible restante: {self.__combustible} litros.')
    
    def repostar(self, litros=0):
        if litros <= 0:
            print('Cantidad de combustible inválida.')
            return
        
        nuevo_nivel = self.__combustible + litros
        if nuevo_nivel > COMBUSTIBLE:
            self.__combustible = COMBUSTIBLE
            print('Tanque lleno!')
        else:
            self.__combustible = nuevo_nivel
            print(f'Repostaste {litros} litros. Combustible actual: {self.__combustible} litros.')
    
    def estado(self):
        print(f'Combustible restante: {self.__combustible} litros.')


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
        print('\nFin de la operación.')

menu()
