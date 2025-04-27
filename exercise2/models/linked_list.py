from models.station import Node

class LinkedList:
    def __init__(self):
        self.head = None  # Cabeza de la lista enlazada

    def add(self, station, time_to_next):
        """Agrega una estación al final de la lista."""
        new_node = Node(station, time_to_next)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def calculate_time(self, start_station, end_station):
        """Calcula el tiempo estimado entre dos estaciones."""
        if start_station == end_station:
            return 0

        # Buscar el nodo de inicio
        current = self.head
        while current and current.station != start_station:
            current = current.next
        if not current:
            raise ValueError("Estación de inicio no encontrada")

        # Recorrer desde el inicio hasta el destino, sumando tiempos
        total_time = 0
        while current and current.station != end_station:
            if current.time_to_next is None:
                raise ValueError("No se puede llegar al destino desde el inicio")
            total_time += current.time_to_next
            current = current.next
        if not current:
            raise ValueError("Estación de destino no encontrada")
        
        return total_time

    def get_list(self):
        """Devuelve una lista con los nombres de las estaciones."""
        stations = []
        current = self.head
        while current:
            stations.append(current.station)
            current = current.next
        return stations
