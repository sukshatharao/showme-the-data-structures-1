## Design:
I built a huffmann tree using priority queue. This tree stores the letters in the sentence and their frequency of occurence. 

## Time Complexity

Encoding:
Trees  have O(log(n)) time for retrieving, inserting and removing on an average. worst case is O(nlogn) - n being the number of nodes in the tree.

Decoding:
Other structures for solving the problem:
I have used a dictionary (which stores unique elements) to store letters and frequency - O(1) best case, O(n) worst case when the dictionary should be iterated over to create a list of tuples (with freq, letters).

priority queue: O(n) worst case for retrieving and searching, O(1) inserting. Keeping track of minimum value is easier in priority queue. Elements with highest priority are dequeued before those with lower priorities. Elements with same priority are served according to the order they are pushed in the queue. This takes care of some of the work managing the nodes of the tree.

## Space Complexity
Encoding:
During encoding, every iteration of a node in the tree inserts one element to the dictionary. So it grows by number (n) of items being encoded plus the size of the encoding string which is related to the depth or number of levels (d) in the tree: O(n+d). 

Decoding:
Decoding requires rebuilding the output string to the same size (n) as the original data provided: O(n).
