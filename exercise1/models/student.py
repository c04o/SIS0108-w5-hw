class Student:
    def __init__(self, id, name, last_name, weight, height, sex, average):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.weight = weight
        self.height = height
        self.sex = sex
        self.average = average

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Last name: {self.last_name}, Weight: {self.weight}, Height: {self.height}, Sex: {self.sex}, Average: {self.average}")
