# Step 1: Define the Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Step 3: Implement the Append Method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Step 4: Implement the Display Method    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
    
    # Step 5: Implement the Insert Method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    # Step 6: Implement the Delete Method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    # Step 7: Implement the Search Method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # Step 8: Implement the Reverse Method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3


# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3


# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3


# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1


# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1


