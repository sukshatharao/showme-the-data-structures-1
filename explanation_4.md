I have used recursion to solve the problem. Initial check is to find if the given user is in the list of users in the particular group. 
Else then I recursively check if the user in the group of users, if found I return true 
Else false
I have implemented this using the concept of recursion. So the time taken depends on the user group structure. So for any given string, I will have to recursively check the node and then return if there is a match or not. In worst case, I will have to traverse through all nodes n.

Run time complexity: O(n); n = number of nodes

Space Complexity : O(m + u) ; m is the space occupied by the node(user/group) and u being the space required for each stack frame.

however recursion does use additional overhead as it requires additional stack space for the functions arguments, rewinding the stack, passing control back to where the function was called, etc. Also, requires some additional time to complete these steps. The memory or space used is based on the number of recursive calls, which determines the number of stack frames times the space required for each stack frame. 
