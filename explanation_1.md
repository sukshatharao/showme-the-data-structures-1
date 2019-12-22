Design Least Recently Used (LRU) cache with O(1) operations. 
Dictionary in python stores the key value pairs and stores single value of keys as key:value pairs.  I have used doubly linked list to keep track of values most used and least recently used. 
The methods "remove" (to remove the oldest element) and "set_head" (to set the head of the doubly linked list with recent fetch) approximately has O(1) performance in either direction

Get Time complexity: O(1) 
Set Time complexity: O(1)

Space complexity of the LRU: O(m); [it is O(capacity); capacity defined by udacity is 5; m=5]
If m is the size of the data stored in the cache then each set operation will cause it to grow by m up to the maximum size of the cache capacity