# TASK 1 - Linked List

Implement a linked list class. The class should be able to:

- Append data to the tail of the list and prepend to the head
- Search the linked list for a value and return the node
- Remove a node
- Pop, which means to return the first node's value and delete the node from the list
- Insert data at some position in the list
- Return the size (length) of the linked list

# TASK 2 - Max Sum Subarray

You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

**Example:**
* `arr= [1, 2, 3, -4, 6]`
* The largest sum is `8`, which is the sum of all elements of the array.

# TASK 3 - Pascal's Triangle

Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
**Exmaple:**
if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html

# TASK 4 - Balanced parantheses

Take a string as an input and return `True` if it's parentheses are balanced or `False` if it is not. 

# TASK 5 - Reverse Polish Notation

Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.
When making mathematical expressions, we typically put arithmetic operators `(like +, -, *, and /)` between operands. 
**Example**: `5 + 7 - 3 * 8`

However, in Reverse Polish Notation, the operators come after the operands.
**Example**: `3 1 + 4 *` would be evaluated as `(3 + 1) * 4 = 16`

The goal of this exercise is to create a function that given a postfix expression as input, evaluate and return the correct final answer.

# TASK 8 - Binary Tree Traversals
Implement depth-first tree traversal with recursion for all three types:
- pre-order
- in-order
- post-order

# TASK 9 - Breadth-first search
Implement breadth-first search on a tree

# TASK 10 - String Key Hash Table

In this quiz, you'll write your own hash table and hash function that uses string keys. Your table will store strings in buckets by their first two letters, according to the formula below:

`Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter`

You can assume that the string will have at least two letters, and the first two characters are uppercase letters (ASCII values from 65 to 90). You can use the Python function ord() to get the ASCII value of a letter, and chr() to get the letter associated with an ASCII value.


# TASK 11 - Pair-Sum-to-target

Given an `input_list` and a `target`, return the indices of pair of integers in the list that sum to the target. The best solution takes O(n) time. You can assume that the list does not have any duplicates.

**Exmaple:** `input_list = [1, 5, 9, 7]` and `target = 8`, the answer would be `[0, 3]`.

# TASK 12 - First and Last Index

Given a sorted array that may have duplicate values, use *binary search* to find the **first** and **last** indexes of a given value.

For example, if you have the array `[0, 1, 2, 2, 3, 3, 3, 4, 5, 6]` and the given value is `3`, the answer will be `[4, 6]` (because the value `3` occurs first at index `4` and last at index `6` in the array).

The expected complexity of the problem is $O(log(n))$.

# TASK 14 - Trie

Implement a Trie class in Python and a function that allows adding a word to the Trie.
Also, create a method `exists` to return True if the word exist in the Trie and False if the word doesn't exist.


# TASK 14 - Minimum Platforms

Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.
Time hh:mm would be written as integer e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345

# TASK 15 - Minimum Operations

Starting from the number 0, find the minimum number of operations required to reach a given positive target number. You can only use the following two operations:

1. Add 1
2. Double the number

```
For Target = 18, output = 6, because it takes at least 6 steps shown below to reach the target

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 + 1 = 9
step 6 ==> 9 * 2 = 18
```

# TASK 16 - Graph Depth First Search Implementation

Create a Graph class in Python, then implement the `dfs_search` method to return the GraphNode with the value `search_value` starting at the `root_node`.

# TASK 17 - Graph Breadth First Search Implementation

# TASK 18 - Dijkstra's Shortest Path Algorithm

# TASK 19 - Connecting Islands

# TASK 20 - Knapsack

*"The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible."*

Cited from https://en.wikipedia.org/wiki/Knapsack_problem

Implement the function `max_value` to return the maximum value given the items and the maximum weight of the knapsack. The items variable is the type `Item`, which is a named tuple.

# TASK 21 - Longest Common Subsequence

In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text). In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence or LCS.

*"The Longest Common Subsequence is the longest string of letters that are the same between to strings."*

A short example:

```
For two input strings, A and B
A = 'ABCD'
B = 'BD'
The LCS is 'BD', which has a length of 2 characters
```

The recommended method for implementing an efficient LCS algorithm is using a matrix and dynamic programming. Dynamic programming is all about breaking a larger problem into a smaller set of subproblems, and building up a complete result without having to repeat any subproblems.