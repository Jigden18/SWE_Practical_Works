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

# Exercises
# Implement a method to find the middle element of the linked list.
# Create a method to detect if the linked list has a cycle.
# Implement a method to remove duplicates from an unsorted linked list.
# Add a method to merge two sorted linked lists into a single sorted linked list.


 # Step 9: implementing a function to find middle element
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    

    # Step 10: Implement the Has Cycle Method
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
     # Step 11: Implement the Remove Duplicates Method
    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()  # This set will store the unique values we encounter

        while current:
            if current.data in seen:
                # Duplicate found, remove it by skipping the current node
                prev.next = current.next
            else:
                # Not a duplicate, add to seen set
                seen.add(current.data)
                prev = current
            current = current.next
    
    # Step 12: implementing merge sorted linked list
    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head

        # dummy node to help with appending nodes to the merged list
        dummy = Node(0)
        tail = dummy

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # append the remaining nodes of either list
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        # set the head of the merged linked list
        merged_list.head = dummy.next
        return merged_list


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


# test to find midddle element
print("Middle element:", ll.find_middle()) 


# test to check linked list has cycle
print("Has cycle:", ll.has_cycle())  

# making the next of the last node point to the second node to have a cycle
ll.head.next.next.next.next.next = ll.head.next
print("Has cycle:", ll.has_cycle()) 

# Test the remove_duplicates function
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(3)

print("Before removing duplicates:")
ll.display()  

ll.remove_duplicates()

print("After removing duplicates:")
ll.display() 

# create first sorted linked list
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

# create second sorted linked list
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

# merge the two sorted linked lists
merged_ll = LinkedList.merge_sorted(ll1, ll2)

print("Merged sorted linked list:")
merged_ll.display()  