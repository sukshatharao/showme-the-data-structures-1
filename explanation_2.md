my function takes input of suffix, path until that point in time. I am using a list which is used to store the list of file collection. Each time I try to find a file ending with suffix will be appended to this list. Appending to the list is O(1) and for f files with "suffix", it is O(f)
We can think of this as working with a tree structure here where files act as leaves and directories act as internal nodes. I have implemented this using the concept of recursion. This traverses the entire tree to find matches given a query string.
Then estimate the number of nodes in the tree which will be = number of files + directories; since we have to visit every node once.

Run time complexity: O(n); n = number of nodes

Space Complexity : O(m + u*d) ; m is the space occuppied by every node
constant stack space of u and multiplied by d- which is the depth

however recursion does use additional overhead as it requires additional stack space for the functions arguments, rewinding the stack, passing control back to where the function was called, etc. Also, requires some additional time to complete these steps. The memory or space used is based on the number of recursive calls, which determines the number of stack frames times the space required for each stack frame. 

In the worst case, all the nested directories are traversed, in which case the stack occupied while recuresively calling the function will depend on the depth of the tree. In this case, it will traverse until the leaf node inorder to find the file.
Stack will occupies constant space but is dependent on the depth of the tree.
Hence I have added the constant stack space of u and multiplied by d- which is the depth.