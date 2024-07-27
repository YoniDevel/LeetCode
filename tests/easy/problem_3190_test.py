from src.problems.easy import problem_3190

def testProblem1():
    sol = problem_3190.Solution()
    minimumOperations = sol.minimumOperations
    
    assert minimumOperations([1, 2, 3, 4]) == 3
    assert minimumOperations([3, 6, 9]) == 0
