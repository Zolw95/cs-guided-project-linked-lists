"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # UPER

    # PLAN
    # Reverse all the pointers
    # Loop (while) we go while.. we still have nodes to process
    # On each iteration of the loop
        # We have a current node
        # next node
            # next node = current node . next
        # We need a reference to previous node
            # when we start, prev is none
        # set current node.next to previous
        # set prev node to cur node
        # 
        # Update current node to point to next_node

    

    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node
    return previous_node
    # X Y Z

print(LinkedListNode.reverse())



num_open = 0

for c in s:
    if c == "(":
        num_open = num_open + 1
    elif c == ")":
        num_open = num_open - 1
    if num_open < 0:
        return False
return num_open == 0










    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node
    # return previous_node


















def insertValueIntoSortedLinkedList(l, value):

    # Set prev to the node head
    prev = l
    # Set current node to the node head
    current_node = l
    # If l node is None
    # create a new node and return it
    if l is None:
        new_node = ListNode(value)
        return new_node
    # if the input value is less than the value of l node
    if value < l.value:
        # Create a new node
        new_node = ListNode(value)
        # Insert the new node in the beginning
        # By setting a pointer to the next value (l node) which is
        # the first node before we set the new node
        new_node.next = l
        # return the new node
        return new_node
    
    # Loop over the current node which is l
    while current_node:
        # If the current node value is less than the input value
        if current_node.value < value:
            # save the current node in the previous var
            prev = current_node
            # change current node to the next node
            current_node = current_node.next
            # Continue Checking for the right value
            continue
            # Else if the current node is not less than the value
        else:
            # Create a new node
            new_node = ListNode(value)
            # set the prev_node next to the new node
            prev.next = new_node
            # set new_node next to the current node
            new_node.next = current_node
            # return the l node
            return l
    
    # create a new node
    new_node = ListNode(value)
    # set prev node.next to the new node in line
    prev.next = new_node
    # return the l node
    return l










