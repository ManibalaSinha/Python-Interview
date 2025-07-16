class Node:
    def __init__(self, data):#constructor method, data stored in node
        self.data = data #stores data in node
        self.next = None #not pointing to anything

def reverse_linked_list(head):#head as input 1st node
    prev = None        # Will point to the previous node (initially None)
    current = head     # Start from the head

    while current is not None: #loop thru list until end(current==None) ie last node
        next_node = current.next   # Save the next node
        current.next = prev        # Reverse the link
        prev = current             # Move prev to current
        current = next_node        # Move to next node

    return prev  # New head of the reversed list

# Create a list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Reverse the list
reversed_head = reverse_linked_list(head)

# Print the reversed list: 3 -> 2 -> 1 -> None
current = reversed_head
while current:
    print(current.data, end=" -> ")
    current = current.next
