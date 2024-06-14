#
# Trabajo de Investigación
#
# Alumnos: José Fernando Usui
#

import random
import timeit
from typing import List

def ordenación_por_insercion_directa_insert_sort(v: List[int]):
    tam_v: int = len(v)
    for i in range(1, tam_v):
        aux = v[i]
        j = i
        while (aux < v[j - 1]) and (j > 0):
            v[j] = v[j - 1]
            j = j - 1
        v[j] = aux

def main():
    v: List[int] = [random.randint(1, 1000) for _ in range(100)]
    print("SIN ORDENAR:\n")
    print(v)
    print("\n\nAPLICACIÓN DEL MÉTODO DE ORDENACIÓN POR INSERCIÓN DIRECTA (INSERT SORT):\n")
    start = timeit.default_timer()
    print("Tiempo Inicial (Antes de invocar el procedimiento): 0.00 ms")
    ordenación_por_insercion_directa_insert_sort(v)
    print(f'Tiempo Final (Después de invocar el procedimiento): {((timeit.default_timer() - start) * 1000):.2f} ms')
    print(v)

if __name__ == "__main__":
    main()