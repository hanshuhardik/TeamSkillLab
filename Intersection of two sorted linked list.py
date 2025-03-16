class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the intersection of two sorted linked lists
def find_intersection(head1, head2):
    head = None
    curr = None

    while head1 and head2:
        if head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            if head is None:
                head = Node(head1.data)
                curr = head
            else:
                curr.next = Node(head1.data)
                curr = curr.next
            head1 = head1.next
            head2 = head2.next

    return head

