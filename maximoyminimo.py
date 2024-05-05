# Definición de la función que encuentra el máximo y mínimo
def encontrar_maximo_y_minimo():
    # Solicitar al usuario que ingrese la cantidad de números
    cant_numeros = int(input("Ingrese la cantidad de números: "))
    
    # Verificar si la cantidad de números es válida
    if cant_numeros < 1:
        return None, None  # Si no es válida, devolver None para ambos valores
    
    # Inicializar el máximo y el mínimo con valores extremos
    max_numero = float('-inf')
    min_numero = float('inf')

    # Bucle para iterar sobre la cantidad de números ingresados
    for cont in range(cant_numeros):
        # Solicitar al usuario que ingrese un número específico
        num = int(input(f"Ingrese número {cont + 1}: "))
        
        # Actualizar el máximo si es necesario
        if num > max_numero:
            max_numero = num
        # Actualizar el mínimo si es necesario
        elif num < min_numero:
            min_numero = num

    # Devolver el máximo y el mínimo encontrados
    return max_numero, min_numero

# Ejemplo de uso de la función
maximo, minimo = encontrar_maximo_y_minimo()
# Imprimir los resultados
print("Max =", maximo, ", Min =", minimo)


