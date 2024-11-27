import random
import time

# prueba de libreria time para medir los tiempos
def time_tester():
    start_time = time.time()
    time.sleep() # se debe dejar sin argumentos para medir el tiempo real
    end_time = time.time()
    sorting_time = end_time - start_time
    return sorting_time

# paso 2: implementar y probar los algoritmos de ordenamiento
def bubble_sort(sys_data):
    """bubble data sorting"""
    stop = len(sys_data) - 1 # define el limite del recorrido

    # controla las veces que recorre la lista
    for _ in range(stop):
        # compara los elementos y los intercambia
        for j in range(stop):
            if sys_data[j] > sys_data[j + 1]:
                sys_data[j], sys_data[j + 1] = sys_data[j + 1], sys_data[j]
    
    print("Ordenamiento burbuja")
    print("Tiempo de ordenamiento: ") # TODO: añadir la función de tiempo

    return sys_data

def selection_sort():
    """selection data sorting"""
    pass

def insertion_sort():
    """insertion data sorting"""
    pass

def merge_sort():
    """merge data sorting"""
    pass

def quick_sort():
    """quick data sorting"""
    pass

def heap_sort():
    """heap data sorting"""
    pass

def count_sort():
    """count data sorting"""
    pass

# paso 1: generar datos aleatotios para probar los algoritmos
def random_data():
    """Generar datos aleatorios"""
    # data generator
    print("Lista de datos")
    sys_data = [random.randint(-100000, 100000) for _ in range(10)] # se trabajará con 10 datos para verificar el ordenamiento, luego se ampliará a 10 000
    return sys_data

def execution_laps():
    """Define la cantidad de veces que se debe ejecutar cada aloritmo"""
    # se debe implementar la funciónde ejecutar el código 500 veces, empezar con 3 veces primero.
    pass

def main():
    print("")
    sys_data = random_data()
    print(sys_data)
    print("")
    bubble_sort(sys_data)
    print(sys_data)

if __name__ == "__main__":
    main()