import random
import time

# prueba de libreria time para medir los tiempos
def time_tester():
    start_time = time.time()
    time.sleep() # se debe dejar sin argumentos para medir el tiempo real
    end_time = time.time()
    sorting_time = end_time - start_time
    return sorting_time

def bubble_sort(sys_data):
    """bubble data sorting"""
    print("")
    stop = len(sys_data) - 1 # define el limite del recorrido

    # controla las veces que recorre la lista
    for _ in range(stop):

        # compara los elementos y los intercambia
        for j in range(stop):
            if sys_data[j] > sys_data[j + 1]:
                sys_data[j], sys_data[j + 1] = sys_data[j + 1], sys_data[j]
    
    print("Algoritmo: Burbuja")
    print("Tiempo: ") # TODO: añadir la función de tiempo

    return sys_data

def selection_sort(sys_data):
    """selection data sorting"""
    print("")
    stop = len(sys_data) - 1
    # control de recorrido
    for i in range(0, stop):
        min_index = i
        min_value = sys_data[min_index]

        # compara los datos
        for j in range(i, stop):
            if min_value > sys_data[j + 1]:
                min_value = sys_data[j + 1]
                min_index = j + 1

        # intercambia los valores
        if min_index != i:
           sys_data[i], sys_data[min_index] = sys_data[min_index], sys_data[i]

    print("Algoritmo: Selección")
    print("Tiempo: ") #TODO: añadir la función de tiempo

    return sys_data

def insertion_sort(sys_data):
    """insertion data sorting"""
    print("")

    print("Algoritmo: Inserción")
    print("Tiempo: ")

    return sys_data

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
    print("")
    print("Lista de datos")
    sys_data = [random.randint(-100000, 100000) for _ in range(5)] # se trabajará con 10 datos para verificar el ordenamiento, luego se ampliará a 10 000
    return sys_data

def execution_laps():
    """Define la cantidad de veces que se debe ejecutar cada aloritmo"""
    # se debe implementar la funciónde ejecutar el código 500 veces, empezar con 3 veces primero.
    pass

def main():
    """
    OJO: Para pasar la lista (sys_data) que genera la función (random_data)
    se debe pasar por argumento de la siguiente forma: sys_data[:] para que
    sea una copia de la lista original
    """
    # lista generada aleatoriamente
    sys_data = random_data()
    print(sys_data)

    # ordenamiento por bubuja
    bubble_sorted = bubble_sort(sys_data[:])
    print(bubble_sorted)

    # ordenamiento por selección
    selection_sorted = selection_sort(sys_data[:])
    print(selection_sorted)

    # ordenamiento por inserción
    insertion_sorted = insertion_sort(sys_data[:])
    print(insertion_sorted)

if __name__ == "__main__":
    main()