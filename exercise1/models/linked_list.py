class Node:
    def __init__(self, student):
        self.student = student
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, student):
        new = Node(student)
        if not self.head:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new

    def get_list(self):
        current = self.head
        list = []
        while current:
            list.append(current.student)
            current = current.next
        return list

    def sort_by(self, attribute):
        list = self.get_list()
        list.sort(key=lambda student: getattr(student, attribute))
        new_list = LinkedList()
        for student in list:
            new_list.add(student)
        return new_list
