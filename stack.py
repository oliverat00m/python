class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
class ArrayStack(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class LinkedListStack(Stack):
    def __init__(self):
        super().__init__()
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.head.item
            self.head = self.head.next
            self.items.pop()
            return item

    def top(self):
        if not self.is_empty():
            return self.head.item

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

# Probar el stack con arreglo
array_stack = ArrayStack()
print(array_stack.is_empty())  # True
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)
print(array_stack.size())  # 3
print(array_stack.top())  # 3
print(array_stack.pop())  # 3
print(array_stack.pop())  # 2
print(array_stack.pop())  # 1
print(array_stack.is_empty())  # True


# Probar el stack con lista ligada
linked_list_stack = LinkedListStack()
print(linked_list_stack.is_empty())  # True
linked_list_stack.push(1)
linked_list_stack.push(2)
linked_list_stack.push(3)
print(linked_list_stack.size())  # 3
print(linked_list_stack.top())  # 3
print(linked_list_stack.pop())  # 3
print(linked_list_stack.pop())  # 2
print(linked_list_stack.pop())  # 1
print(linked_list_stack.is_empty())  # True
