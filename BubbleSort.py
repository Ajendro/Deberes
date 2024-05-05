def bubble_sort():
    # Solicitar al usuario que ingrese los números separados por comas
    entrada = input("Ingrese los 5 números separados por comas: ")

    # Convertir la entrada del usuario en una lista de números enteros
    numeros = entrada.split(',')
    arreglo = []
    
    # Verificar si se ingresaron exactamente 5 números
    if len(numeros) != 5:
        print("¡Error! Debe ingresar exactamente 5 números separados por comas.")
        return

    # Convertir los elementos a enteros y agregarlos al arreglo
    for num in numeros:
        try:
            num_entero = int(num)
            arreglo.append(num_entero)
        except ValueError:
            print("¡Error! Ingrese solo números separados por comas.")
            return

    n = len(arreglo)  # Obtener la longitud del arreglo
    intercambio = True  # Variable para rastrear si se realizan intercambios en una pasada

    # Continuar el bucle hasta que no se realicen intercambios en una pasada
    while intercambio:
        intercambio = False  # Reiniciar la variable de intercambio para esta pasada

        # Bucle para comparar elementos adyacentes
        for i in range(n - 1):
            # Si el elemento actual es mayor que el siguiente
            if arreglo[i] > arreglo[i + 1]:
                # Intercambiar los elementos
                arreglo[i], arreglo[i + 1] = arreglo[i + 1], arreglo[i]
                intercambio = True  # Se ha realizado un intercambio en esta pasada

        # Reducir el tamaño del rango para la siguiente pasada,
        # ya que el elemento más grande ya está en su lugar
        n -= 1

    # Imprimir el arreglo ordenado
    print("Arreglo ordenado:", arreglo)

# Llamar a la función para ordenar los 5 números ingresados por el usuario
bubble_sort()

