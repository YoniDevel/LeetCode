from typing import Optional
from collections import deque

from classes.tree_node import TreeNode


# Recursive Pre Order Traversal (DFS). Time: O(n), Space: O(n)
def pre_order(node: Optional[TreeNode]) -> None:
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursive In Order Traversal (DFS). Time: O(n), Space: O(n)
def in_order(node: Optional[TreeNode]) -> None:
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
    
# Iterative Post Order Traversal (DFS). Time: O(n), Space: O(n)
def post_order(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        
# Iterative Pre Order Traversal (DFS). Time: O(n), Space: O(n)
def pre_order_iterative(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        print(node)

# Level Order Traversal (BFS). Time: O(n), Space: O(n)
def level_order(node):
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# Check If Value Exists (DFS). Time: O(n), Space: O(n)
def search(node: Optional[TreeNode], target: int) -> bool:
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

# Check If Value Exists in BST. Time: O(log2(n)), Space: O(log2(n))
def search_bst(node: Optional[TreeNode], target: int) -> bool:
    if not node: 
        return False
    
    if node.val == target:
        return True
    
    if target < node.val:
        return search_bst(node.left, target)
    
    return search_bst(node.right, target)
