import random
import time

# Genera una lista de números aleatorios sin duplicados
def generar_lista(tamano):
    return random.sample(range(1, 1000000000001), tamano)  # Rango ajustado para generar números del 1 al 1000

# Encuentra el elemento máximo en la lista
def encontrar_maximo(lista):
    return max(lista)

# Suma todos los elementos en la lista
def sumar_elementos(lista):
    return sum(lista)

# Main
if __name__ == "__main__":
    tamano_lista = 1000
    lista = generar_lista(tamano_lista)
    
    # Medición del tiempo de ejecución
    start_time = time.time()
    maximo = encontrar_maximo(lista)
    suma = sumar_elementos(lista)
    end_time = time.time()

    print(f"Lista: {lista}")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

