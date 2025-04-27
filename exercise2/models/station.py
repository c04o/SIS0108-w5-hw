class Node:
    def __init__(self, station, time_to_next):
        self.station = station
        self.time_to_next = time_to_next
        self.next = None
