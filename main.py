import random
import time

# prueba de libreria time para medir los tiempos
def time_tester():
    pass

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
    # empieza recorrido desde el segundo elemento
    for insert_index in range(1, len(sys_data)):

        # obtiene el valor actual que se va a insertar
        insert_value = sys_data[insert_index]

        # desplaza elementos mayores hacia la derecha
        while insert_index > 0 and insert_value < sys_data[insert_index - 1]:
            sys_data[insert_index] = sys_data[insert_index - 1]
            insert_index -= 1

            # coloca el valor en la posición correcta
        sys_data[insert_index] = insert_value

    print("Algoritmo: Inserción")
    print("Tiempo: ")

    return sys_data

def merge_sort(sys_data, first_call=True):
    """merge data sorting"""
    if first_call:
        print("")
        print("Algoritmo: Merge Sort")
        print("Tiempo: ")

    def merge(left: list, right: list) -> list:

        """Combina dos listas ordenadas"""
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(sys_data) <= 1:
        return sys_data

    mid_index = len(sys_data) // 2

    # Aseguramos que `first_call` no se propague a las llamadas recursivas
    left_sorted = merge_sort(sys_data[:mid_index], first_call=False)
    right_sorted = merge_sort(sys_data[mid_index:], first_call=False)

    return merge(left_sorted, right_sorted)

def quick_sort():
    """quick data sorting"""
    print("")

    print("Algoritmo: Quick Sort")
    print("Tiempo: ") # TODO: añadir la función de tiempo

def heap_sort():
    """heap data sorting"""
    print("")

    print("Algoritmo: Quick Sort")
    print("Tiempo: ") # TODO: añadir la función de tiempo

def count_sort(sys_data):
    """count data sorting"""
    print("")
    # obtener información sobre la lista
    stop = len(sys_data)
    max_number = max(sys_data)
    min_number = min(sys_data)

    # control de conteo
    sys_data_stop = max_number + 1 - min_number
    counting = [0] * sys_data_stop

    # control de repetición del número
    for number in sys_data:
        counting[number - min_number] += 1

    # suma cada posición con sus predecesores. Ahora, counting_arr[i] nos dice 
    # cuántos elementos <= i hay en sys_data
    for i in range(1, sys_data_stop):
        counting[i] = counting[i] + counting[i - 1]

    # lista ordenada
    sys_data_sorted = [0] * stop

    # coloca los elementos en la salida, respetando el orden original (ordenamiento 
    # estable) de final a inicio, actualizando counting_arr
    for i in reversed(range(stop)):
        sys_data_sorted[counting[sys_data[i] - min_number] - 1] = sys_data[i]
        counting[sys_data[i] - min_number] -= 1

    print("Algoritmo: Conteo")
    print("Tiempo: ") #TODO: añadir la función de tiempo
    return sys_data_sorted

def random_data():
    """Generar datos aleatorios"""
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

    # ordenamiento merge sort
    merge_sorted = merge_sort(sys_data[:])
    print(merge_sorted)

    # ordenamiento quick sort

    # ordenamiento heap sort

    # ordenamiento por conteo
    count_sorted = count_sort(sys_data[:])
    print(count_sorted)

if __name__ == "__main__":
    main()