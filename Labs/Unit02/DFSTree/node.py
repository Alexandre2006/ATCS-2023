"""
A single node of a tree
which contains information on the 
parent, children, and data within 
the node.

@author: Ms. Namasivayam
@version: ATCS 2023-2024
"""

class Node:
    def __init__(self, value=0, parent=None):
        self.value = value
        self.children = []
        self.parent = parent
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, children):
        self.children.extend(children)
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        return str(self.value)