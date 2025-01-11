from functions import *
import networkx as nx
import matplotlib.pyplot as plt
from data import data


class Node:
    """Represents a single node in a decision tree."""

    def __init__(self, val: int = 0):
        self.val: int = val
        self.index: list['Node' | None] = []

    def add_i(self, i: int, node: 'Node') -> None:
        """Adds or updates a child node at the specified index."""
        while i >= len(self.index):
            self.index.append(None)
        self.index[i] = node


def build_decision_tree(array, node=None):
    if len(array) <= 1:
        return node  
    result = findNODE(array)
    node_val, index = result[0], result[1]

 
    if index is None:
        return Node(node_val)

    
    node = Node(node_val)

   
    for i, branch in enumerate(list_branches(array, index)):
        branch_array = changeTable(array, index, branch)
        child_node = build_decision_tree(branch_array)  
        node.add_i(i, child_node)

    return node


node=build_decision_tree(data)

print(node.index[0].val)