union & intersection of the two linked list is the problem statement. I have used a set inorder to store the result of union and intersection. Then I created a new linked list from the set.
Insertions and deletions (deletes not done in this example) have average and worst case Big O(1).
searching a particular element requires O(n) in order to find an element as it may have to iterate the entire list.
if there are m elements in one linked list and n elements in second linked list, then space complexity is addition of two lengths of the linked list

Union: Time complexity: O(n) , Space complexity: O(m+n)



The intersection function (intersect)  - goes through one list element by element, O(n) and I have taken advantage of the fast lookup time of the second set here , hence it is a linear lookup since I am using a set : O(1) and also in the intersect list before it adds it

The space complexity worst case would be if all the elements in both the sets are same: O(m+m), if m is the length of linked list

intersection: Time complexity: O(n + 1) = O(n) , Space complexity: O(2m)

