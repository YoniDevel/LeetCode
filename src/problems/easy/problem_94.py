from typing import List, Optional

from src.classes.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
