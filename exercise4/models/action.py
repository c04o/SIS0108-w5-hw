class Action:
    def __init__(self, action):
        self.action = action  # Name
        self.prev = None  # Undo
        self.next = None  # Redo
