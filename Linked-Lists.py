import random

class llist_node_s():

    # Node for singly linked list

    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(node):

    while node is not None:

        print(node.data)
        node = node.next

def create_link_list_0_to_10():

    head = None
    current = None
    for i in range(0, 10):

        if head == None:
            head = llist_node_s(i)
            current = head

        else:
            current.next = llist_node_s(i)
            current = current.next

    return head

def create_link_list_random():

    #create a list with 10 random ints between 0 and 99

    head = None
    current = None
    # for i in random.sample(range(100), 10):
    #
    #     if head == None:
    #         head = llist_node_s(i)
    #         current = head
    #
    #     else:
    #         current.next = llist_node_s(i)
    #         current = current.next

    a = [5, 2, 3, 5, 5, 5, 7, 8, 9]

    for i in a:

        if head == None:
            head = llist_node_s(i)
            current = head

        else:
            current.next = llist_node_s(i)
            current = current.next


    return head

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list

# Function uses a dictionary to keep track of which ints we've seen

def remove_dups_buffer(head):

    if head == None:
        return None

    d = {}

    d[head.data] = True

    node = head

    while ((node is not None) and (node.next is not None)):

        if node.next.data in d:
            node.next = node.next.next
            continue

        d[node.next.data] = True
        node = node.next

    return head


# Uses two pointers to compare different nodes in the linked list
def remove_dups_no_buffer(head):

    current = head

    while current is not None:
        runner = current
        while runner.next is not None:
            if (runner.next.data == current.data):
                runner.next = runner.next.next

            else:
                runner = runner.next

        current = current.next

    return head

#2.2 Return kth to last element of a linked list

def kth_to_last(head, k):

    length = 0
    current = head

    while current is not None:

        length += 1
        current = current.next

    i = length-k-1
    current = head

    # i > 0 instead of i >=0 so that the loop stops when it reaches i = 0

    while i > 0:
        current = current.next
        i-=1

    return current.data


head = create_link_list_random()
print_linked_list(head)
print("**")
print(kth_to_last(head, 0))