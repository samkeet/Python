# python-stuff
a showcase of python codes
Trees

Notes
________________________________________
1. 3 types of traversals: preorder, inorder and postorder
2. preorder - root, left, right
3. inorder - left, root, right
4. postorder - left, right, root
5. binary heap: can enqueue and dequeue items in O(logn) for a priority queue
6. two types - max heap(largest key value in front) and min heap (smallest key value in front)
7. The method that we will use to store items in a heap relies on maintaining the heap order property. The heap order property is as follows: In a heap, for every node x with parent pp, the key in pp is smaller than or equal to the key in x.
8. Height of binary tree = log2(n) if elements are added randomly
9. Number of notes at any height is 2^d where d is the depth of tree
10. The total number of nodes in a binary bst are 2^(h+1) - 1 where h is the height of tree
11. The worst case performance of insertion is O(log2(n)) where n is the number of nodes.
12. for balanced bst: balance factor = height(left subtree) - height(right subtree)

This derivation shows us that at any time the height of our AVL tree is equal to a constant(1.44) times the log of the number of nodes in the tree. This is great news for searching our AVL tree because it limits the search to O(logN)


Hashing 
___
Notes
________________________________________
1. Search time O(1)
2.load factor (lambda) = number of items/total size of array
3. Given a collection of items, if a hash function is able to map each item uniquely ot a slot in the memory, 
the such a hash function is called perfect hash function 
4. anagrams can be used with each digit multiplied by its ASCII value (123 and 321)
5.	As before, we will have a result for both a successful and an unsuccessful search. 
For a successful search using open addressing with linear probing, the average number of comparisons is approximately 1/2(1+1/1−λ)12(1+11−λ) and an unsuccessful search gives 1/2(1+(11−λ)2)12(1+(1/1−λ)^2) If we are using chaining, the average number of comparisons is 1+λ21+λ2 for the successful case, and simply λλ comparisons if the search is unsuccessful.

Graphs
1.	in an undirected graph with n nodes, total edges are n(n-1)/2
2.	hence an n vertices graph with n(n-1)/2 edges is said to be complete, where there is an edge between every pair of vertices
3.	use adj. matrix if number of vertices are less else use adj. list
4.	Prim’s is a greedy algorithm. uses Mimimum spanning tree
5.	Minimum spanning tree is the smallest directed acyclic graph that connects all nodes 
