class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return self.valor
    

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return False
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        return True

    def mostrar(self):
        canciones = []
        actual = self.cabeza
        while actual:
            canciones.append(actual.valor)
            actual = actual.siguiente
        return canciones
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mover(self, valor, nueva_posicion):
        if self.cabeza is None:
            return False
        
        # Eliminar el nodo de la posición actual
        actual = self.cabeza
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        
        if actual is None:
            return False
        
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        
        # Insertar el nodo en la nueva posición
        nuevo_nodo = Nodo(valor)
        if nueva_posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            posicion_actual = 0
            while actual and posicion_actual < nueva_posicion - 1:
                actual = actual.siguiente
                posicion_actual += 1
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        return True
    
class SistemaGestionPlaylists:
    def __init__(self):
        self.playlist = ListaEnlazada()

    def agregar_cancion(self, cancion):
        self.playlist.agregar(cancion)

    def eliminar_cancion(self, cancion):
        return self.playlist.eliminar(cancion)

    def mostrar_playlist(self):
        return self.playlist.mostrar()

    def buscar_cancion(self, cancion):
        return self.playlist.buscar(cancion)

    def mover_cancion(self, cancion, nueva_posicion):
        return self.playlist.mover(cancion, nueva_posicion)

# Inicialización del sistema de gestión de playlists
sistema = SistemaGestionPlaylists()

# Añadir canciones
sistema.agregar_cancion("Canción 1")
sistema.agregar_cancion("Canción 4")
sistema.agregar_cancion("Canción 3")

# Mostrar playlist
print("Playlist:", sistema.mostrar_playlist())

# Buscar una canción
print("Buscar 'Canción 2':", sistema.buscar_cancion("Canción 2"))
print("Buscar 'Canción 4':", sistema.buscar_cancion("Canción 4"))

# Mover una canción
sistema.mover_cancion("Canción 3", 1)

# Mostrar playlist después de mover una canción
print("Playlist después de mover 'Canción 3' a la posición 1:", sistema.mostrar_playlist())

# Eliminar una canción
sistema.eliminar_cancion("Canción 2")

# Mostrar playlist después de la eliminación
print("Playlist después de eliminar 'Canción 2':", sistema.mostrar_playlist())
