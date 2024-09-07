from src.problems.easy import problem_101
from src.classes.tree_node import TreeNode

def testProblem101():
    sol = problem_101.Solution()
    isSymmetric = sol.isSymmetric
    
    assert isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
    assert not isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))))
