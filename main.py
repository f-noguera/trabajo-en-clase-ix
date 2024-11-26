import random
import time

# prueba de libreria time para medir los tiempos
def time_tester():
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()

    print(f"Tiempo en generar los datos: {end_time - start_time} milisegundos")

# paso 2: implementar y probar los algoritmos de ordenamiento
def bubble_sort():
    """bubble data sorting"""
    pass

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
    sys_data = [random.randint(-100000, 100000) for _ in range(10000)]
    return sys_data
    
def main():
    print("")
    sys_data = random_data()
    print(sys_data)
    print("")
    time_tester() #borrar ya que es una prueba

if __name__ == "__main__":
    main()