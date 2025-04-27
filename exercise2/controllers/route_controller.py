from models.linked_list import LinkedList

def show_list(lista):
    """Muestra la lista de estaciones disponibles."""
    stations = lista.get_list()
    if not stations:
        print("No stations in the lista.")
    else:
        print("Available stations:")
        for station in stations:
            print(station)

def calculate_time(lista):
    """Calcula el tiempo entre dos estaciones."""
    start = input("Starting station: ")
    end = input("Destination: ")
    try:
        time = lista.calculate_time(start, end)
        print(f"Estimated time from {start} to {end}: {time} minutes")
    except ValueError as e:
        print(f"Error: {e}")
