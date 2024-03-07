# Pascal's Triangle

## Overview

This project involves creating a Python function to generate Pascal's Triangle. Pascal's Triangle is a mathematical structure that consists of a triangular array of binomial coefficients. Each number in the triangle is the sum of the two directly above it.

## Algorithm

<h3>The algorithm involves generating each row of Pascal's Triangle based on the values of the previous row. This can be achieved using nested loops or recursion.<h3>

## Resources

- [What is Pascal’s triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=0sPqClOWSMs)
- [What are Python Algorithms](https://www.programiz.com/python-programming/algorithms)

### Additional Resources

- Mock Technical Interview[ https://youtu.be/1qw5ITr3k9E ]

## Prerequisites

To successfully complete this project, it's important to be familiar with the following Python concepts:

- Lists and List Comprehensions
- Functions
- Loops
- Conditional Statements
- Recursion (Optional)
- Arithmetic Operations
- Indexing and Slicing
- Memory Management
- Error and Exception Handling (Optional)
- Efficiency and Optimization

## Tasks

### 0. Pascal's Triangle

Create a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

### 1. Inverting a 2D Matrix

Create a function `def rotate_2d_matrix(matrix)` that rotates a 2D matrix 90 degrees clockwise:

- You can assume the matrix is square and will have at least one element
- The matrix can be modified in-place

### 2. School Chocolates

Create a function `def distribute_chocolates(students, m)` that distributes chocolates to students:

- Each student gets exactly one chocolate
- Distribute the chocolates in order of age (from the oldest to the youngest)
- Return a list containing the number of chocolates each student will receive

### 3. Singly Linked List

Create a class `Node` representing a node of a singly linked list:

- Each node should contain an integer value and a reference to the next node in the sequence
- Implement methods to retrieve and set the value of a node, as well as to retrieve the next node

### 4. LRU Caching

Create a class `LRUCache` that represents a Least Recently Used (LRU) cache:

- The cache should have a maximum capacity specified when it is created
- Implement methods to get a value from the cache and set a value in the cache
- The cache should evict the least recently used item when it reaches maximum capacity and a new item is added

## Repository Information

- GitHub repository: alx-interview
- Directory: 0x00-pascal_triangle
- Files: 
  - 0-pascal_triangle.py
  - 1-rotate_2d_matrix.py
  - 2-distribute_chocolates.py
  - 3-node.py
  - 4-lru_cache.py
