from typing import Optional

from src.classes.tree_node import TreeNode

# using problems 100 and 226
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val: 
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        if not p and not q:
            return True
        
        return False
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root, self.invertTree(root))
