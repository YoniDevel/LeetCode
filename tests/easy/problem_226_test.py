from src.problems.easy import problem_226, problem_100
from src.classes.tree_node import TreeNode

def testProblem226():
    sol = problem_226.Solution()
    invertTree = sol.invertTree
    isSameTree = problem_100.Solution().isSameTree
    
    assert isSameTree(invertTree(TreeNode(2, TreeNode(1), TreeNode(3))), TreeNode(2, TreeNode(3), TreeNode(1)))
