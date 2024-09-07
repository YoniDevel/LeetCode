from typing import Optional

from src.classes.tree_node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
