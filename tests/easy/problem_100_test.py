from src.problems.easy import problem_100
from src.classes.tree_node import TreeNode

def testProblem100():
    sol = problem_100.Solution()
    isSameTree = sol.isSameTree
    
    assert isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
    assert not isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
    assert not isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2)))