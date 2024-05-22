from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        "Agrega un elemento al final de la cola."
        self.items.append(item)

    def dequeue(self):
        "Quita y devuelve el primer elemento de la cola."
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("La cola está vacía")

    def is_empty(self):
        "Retorna True si la cola está vacía, sino False."
        return len(self.items) == 0

    def size(self):
        "Devuelve cuántos elementos hay en la cola."
        return len(self.items)

class TaskManager:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        "Añade una nueva tarea a la cola."
        self.queue.enqueue(task)
        print(f"Se ha añadido la tarea: '{task}'.")

    def process_task(self):
        "Procesa la tarea en el frente de la cola."
        if not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Procesando la tarea: {task}")
        else:
            print("No hay tareas pendientes para procesar.")

    def show_tasks(self):
        "Muestra todas las tareas en la cola."
        if self.queue.is_empty():
            print("No hay tareas en la cola.")
        else:
            print("Tareas en la cola:")
            for task in self.queue.items:
                print(f"- {task}")

# Pruebas del TaskManager
task_manager = TaskManager()
task_manager.add_task("Tarea 1")
task_manager.add_task("Tarea 2")
task_manager.show_tasks()
task_manager.process_task()
task_manager.show_tasks()
task_manager.process_task()
task_manager.process_task()

# Pruebas unitarias
def test_task_manager():
    tm = TaskManager()
    tm.add_task("Tarea 1")
    tm.add_task("Tarea 2")
    assert tm.queue.size() == 2
    tm.process_task()
    assert tm.queue.size() == 1
    tm.process_task()
    assert tm.queue.is_empty()
    print("Todas las pruebas pasaron.")

test_task_manager()
