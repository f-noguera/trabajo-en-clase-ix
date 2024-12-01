import random
import time
import matplotlib.pyplot as plt

def measure_time(sort_function, sys_data):
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento"""
    start_time = time.time()  # Inicia el cronómetro
    sorted_data = sort_function(sys_data)  # Ejecuta la función de ordenamiento
    end_time = time.time()  # Detiene el cronómetro

    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
    return elapsed_time  # Solo devolvemos el tiempo de ejecución

def bubble_sort(sys_data):
    """Bubble sort"""
    stop = len(sys_data) - 1
    for _ in range(stop):
        for j in range(stop):
            if sys_data[j] > sys_data[j + 1]:
                sys_data[j], sys_data[j + 1] = sys_data[j + 1], sys_data[j]
    return sys_data

def selection_sort(sys_data):
    """Selection sort"""
    stop = len(sys_data) - 1
    for i in range(0, stop):
        min_index = i
        min_value = sys_data[min_index]
        for j in range(i, stop):
            if min_value > sys_data[j + 1]:
                min_value = sys_data[j + 1]
                min_index = j + 1
        if min_index != i:
            sys_data[i], sys_data[min_index] = sys_data[min_index], sys_data[i]
    return sys_data

def insertion_sort(sys_data):
    """Insertion sort"""
    for insert_index in range(1, len(sys_data)):
        insert_value = sys_data[insert_index]
        while insert_index > 0 and insert_value < sys_data[insert_index - 1]:
            sys_data[insert_index] = sys_data[insert_index - 1]
            insert_index -= 1
        sys_data[insert_index] = insert_value
    return sys_data

def merge_sort(sys_data, first_call=True):
    """Merge sort"""
    if first_call:
        print("")

    def merge(left: list, right: list) -> list:
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(sys_data) <= 1:
        return sys_data

    mid_index = len(sys_data) // 2
    left_sorted = merge_sort(sys_data[:mid_index], first_call=False)
    right_sorted = merge_sort(sys_data[mid_index:], first_call=False)

    return merge(left_sorted, right_sorted)

def quick_sort(sys_data, first_call=True):
    """Quick sort"""
    if first_call:
        print("")
    
    if len(sys_data) <= 1:
        return sys_data
    
    pivot = sys_data[-1]
    left = [x for x in sys_data[:-1] if x <= pivot]
    right = [x for x in sys_data[:-1] if x > pivot]

    return quick_sort(left, False) + [pivot] + quick_sort(right, False)

def heap_sort(sys_data):
    """Heap sort"""
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left

        if right < n and data[right] > data[largest]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            heapify(data, n, largest)

    n = len(sys_data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(sys_data, n, i)

    for i in range(n - 1, 0, -1):
        sys_data[i], sys_data[0] = sys_data[0], sys_data[i]
        heapify(sys_data, i, 0)

    return sys_data

def count_sort(sys_data):
    """Count sort"""
    stop = len(sys_data)
    max_number = max(sys_data)
    min_number = min(sys_data)

    sys_data_stop = max_number + 1 - min_number
    counting = [0] * sys_data_stop

    for number in sys_data:
        counting[number - min_number] += 1

    for i in range(1, sys_data_stop):
        counting[i] = counting[i] + counting[i - 1]

    sys_data_sorted = [0] * stop
    for i in reversed(range(stop)):
        sys_data_sorted[counting[sys_data[i] - min_number] - 1] = sys_data[i]
        counting[sys_data[i] - min_number] -= 1

    return sys_data_sorted

def random_data():
    """Generar datos aleatorios"""
    return [random.randint(-100000, 100000) for _ in range(1000)]  # Ejemplo con 1000 elementos

def execution_laps():
    sys_data = random_data()  # Datos aleatorios
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Counting Sort": count_sort
    }

    times = {name: [] for name in algorithms}
    
    for name, func in algorithms.items():
        for _ in range(500):  # Ejecutar 50 veces cada algoritmo
            elapsed_time = measure_time(func, sys_data[:])  # Usamos una copia de sys_data
            times[name].append(elapsed_time)  # Solo añadimos el tiempo de ejecución
    
    return times

def plot_times(times):
    """Genera un gráfico de los tiempos de ejecución por algoritmo"""
    plt.figure(figsize=(10, 6))
    
    for name, time_list in times.items():
        plt.plot(range(1, 501), time_list, label=name)
    
    plt.xlabel('Número de ejecución')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    times = execution_laps()  # Ejecuta los algoritmos 50 veces
    plot_times(times)  # Grafica los resultados

if __name__ == "__main__":
    main()
