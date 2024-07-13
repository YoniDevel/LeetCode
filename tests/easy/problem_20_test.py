from src.problems.easy import problem_20

def testProblem1():
    sol = problem_20.Solution()
    isValid = sol.isValid
    
    assert isValid("()")
    assert not isValid("(]")