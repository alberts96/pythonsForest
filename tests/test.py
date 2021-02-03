# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:55:37 2020

@author: carlo
"""

## Define some function useful for testing
import random

## generate an array of n random integers up to b
def get_random_array(n, b = 50):
    return [random.randint(0, b) for _ in range(n)]


import BST
# Test your implementation here
a = get_random_array(30)


bst = BST.BinarySearchTree()

for x in a: 
    bst.insert(x)
    
print(bst)
print([x for x in bst.root][:10])
    




print(bst.max())
print(bst.min())

print(bst.successor(bst.root.getVal()))
print(bst.successor(43))
print(bst.root.val)
print(bst.predecessor(bst.max()))
print(bst.successor(bst.min()))