from src.problems.easy import problem_94
from src.classes.tree_node import TreeNode

def testProblem70():
    sol = problem_94.Solution()
    inorderTraversal = sol.inorderTraversal
    
    assert inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))) == [1, 3, 2]
    assert inorderTraversal(None) == []
    assert inorderTraversal(TreeNode(1)) == [1]
