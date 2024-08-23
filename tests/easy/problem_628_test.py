from src.problems.easy import problem_628

def testProblem628():
    sol = problem_628.Solution()
    maximumProduct = sol.maximumProduct
    
    assert maximumProduct([1,2,3]) == 6
    assert maximumProduct([1,2,3,4]) == 24
    assert maximumProduct([-1,-2,-3]) == -6
