#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(LL1, LL2):
    my_set = set()
    current = LL1.head
    while current:
        my_set.add(current.value)
        current = current.next
    current = LL2.head
    while current:
        my_set.add(current.value)
        current = current.next

    result = LinkedList()
    for element in my_set:
        result.append(element)
    if result.size():
        return result
    return None

def intersection(LL1, LL2):
    if LL1 is None or LL2 is None:
        return None
    my_set1 = set()
    current = LL1.head
    while current:
        my_set1.add(current.value)
        current = current.next
    my_set2 = set()
    current = LL2.head
    while current:
        my_set2.add(current.value)
        current = current.next
        
    result = LinkedList()
    for element1 in my_set1:
        if element1 in my_set2:
            result.append(element1)

    if result.size():
        return result
    return None

    

# Test case 1
print("\n\t\tTest case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
print("\n\t\tTest case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
print("\n\t\tTest case 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2, 4, 6, 8, 10]
element_2 = [1,3,5,7,9,11,13]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5, linked_list_6))
print (intersection(linked_list_5, linked_list_6))


# Test case 4
print("\n\t\tTest case 4")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7, linked_list_8))
print (intersection(linked_list_7, linked_list_8))


# In[ ]:




