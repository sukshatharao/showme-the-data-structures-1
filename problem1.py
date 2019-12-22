#!/usr/bin/env python
# coding: utf-8

# In[7]:


class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next= None

        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_capacity = capacity
        self.hash = {}
        self.current_size = 0
        self.head = None
        self.end = None
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key is None or key not in self.hash:
            return -1
        node = self.hash[key]
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.hash and self.cache_capacity >0:
            if self.current_size >= self.cache_capacity :
                element = self.remove(self.end)
                if element is not None:
                    del self.hash[element.value]
                    print("Iam inside when the current size is greater or equal to capacity of LRU")
                    print("Deleting old element to make space")
            node= DoubleNode(value)
            self.set_head(node)
            self.hash[key]= node
        elif key in self.hash:
                node = self.hash[key]
                node.value = value
                if self.head != node:
                    self.remove(node)
                    self.set_head(node)
        self.current_size +=1                    #increasing the current_size
        pass
    
    def remove(self, node):
        if self.head is None:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == self.end:
            self.head = self.end= None
        if self.end == node:
            self.end.prev.next = None
            self.end = self.end.prev
        self.current_size -=1
        return node
    
    def set_head(self, node):
        if self.head == None:
            self.head = self.end = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        

#Test case 1 - LRU of size 5
print("Test case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(7, 7)

#Test case 2 to check when current size is >= capacity
print("Test case 2")
our_cache.set(8, 8)

#Test case 3: to get elements not in cache
print("Test case 3")
print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(''))    # returns -1

#Test case 4: to overwrite the value for the same key
print("Test case 4")
our_cache.set(1,1);
our_cache.set(1,9);
print(our_cache.get(1))     # returns 9 , which is recently "set"

#Test case 5: get and set tested for LRU cache is zero
print("Test case 5")
our_cache1 = LRU_Cache(0)
our_cache1.set(1,1);
our_cache1.set(1,9);
print(our_cache1.get(1))    # returns -1 since LRU cache size is 0


# In[ ]:




