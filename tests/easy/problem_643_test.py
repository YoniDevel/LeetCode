from src.problems.easy import problem_643

def testProblem643():
    sol = problem_643.Solution()
    findMaxAverage = sol.findMaxAverage
    
    assert findMaxAverage([1,12,-5,-6,50,3], 4) == 12.7500
    assert findMaxAverage([5], 1) == 5
