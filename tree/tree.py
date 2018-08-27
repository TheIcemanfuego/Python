# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Tree():
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right


    def __str__(self):
        return str(self.cargo)

#Function
def total(tree):
    if tree == None: 
        return 0

    return total(tree.left) + total(tree.right) + tree.cargo

#Function
def print_tree(tree):
    if tree == None: return
    print (tree.cargo),
    print_tree(tree.left)
    print_tree(tree.right)




if __name__ == "__main__":
    z = Tree(1)
    x = Tree(2, Tree(4), Tree(5))
    y = Tree(3, Tree(6), Tree(7))
    z.left = x
    z.right = y
    
    #print(z)
    #print("total: "+str(total(z)))
    #print_tree(z)
    
    tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
    print_tree(tree)
    

