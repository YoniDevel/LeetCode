from src.problems.easy import problem_2485

def testProblem2485():
    sol = problem_2485.Solution()
    pivotInteger = sol.pivotInteger
    
    assert pivotInteger(8) == 6
    assert pivotInteger(1) == 1
    assert pivotInteger(4) == -1
