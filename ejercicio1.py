def busqueda_y_ordenamiento():
    # Solicitar al usuario que ingrese 20 elementos numéricos para el arreglo
    arreglo = [int(input(f"Ingrese el elemento {i + 1}: ")) for i in range(20)]

    # Ordenar el arreglo utilizando el ordenamiento por burbuja
    n = len(arreglo)  # Obtener la longitud del arreglo
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

    # Solicitar al usuario que ingrese la clave a buscar
    clave = int(input("Ingrese la clave a buscar: "))

    # Realizar la búsqueda secuencial utilizando el método index
    try:
        indice = arreglo.index(clave)  # Intentar encontrar el índice de la clave en el arreglo
        print(f"Búsqueda secuencial: La clave {clave} se encuentra en la posición {indice}.")
    except ValueError:
        print("Clave no encontrada")

    # Realizar la búsqueda binaria
    inicio = 0  # Índice inicial del rango de búsqueda
    fin = len(arreglo) - 1  # Índice final del rango de búsqueda

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Calcular el índice medio del rango de búsqueda
        if arreglo[medio] == clave:
            # Imprimir la posición de la clave si se encuentra
            print(f"Búsqueda binaria: La clave {clave} se encuentra en la posición {medio}.")
            return  # Finalizar la función después de encontrar la clave
        elif arreglo[medio] < clave:
            inicio = medio + 1  # Establecer el nuevo inicio del rango
        else:
            fin = medio - 1  # Establecer el nuevo final del rango

    # Imprimir un mensaje si la clave no se encuentra en ninguna de las búsquedas
    print("Clave no encontrada")


busqueda_y_ordenamiento()


