I have created linked list inorder to create blocks. I have initialized the linked list with head and tail and Head points to the starting of the chain. tail points to the end of linked list. Appending the new block to the linked list is done at the end of the tail in O(1) complexity. 
There is a previous pointer within the blocks  themselves so traversal backwards through the block chain is possible.
Insertions have average and worst case Big O(1) while searching requires O(n).

Time complexity: O(1) - for appending a node/block

Space complexity: O(n*m) - total space occupied by the blockchain 

If there are n nodes in the list (blockchain) and each node takes up m amount of memory the space complexity would be O(n*m).
Data is the string that we pass into the function. Hence length of the string also matters while calculating m