"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
#UPER
# we dont have access to head or tail - only to the node to delete

#PLAN
# set node to delte value to node to delete next value
# set node_to_delete.next.next
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node_to_delete):
    # Your code here
    node_to_delete.value = node_to_delete.next.value
    node_to_delete.next = node_to_delete.next.next


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

cur_node = x
while cur_node:
    print(cur_node.value)
    cur_node = cur_node.next

delete_node(y)

cur_node = x
while cur_node:
    print(cur_node.value)
    cur_node = cur_node.next
