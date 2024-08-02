from src.problems.easy import problem_20

def testProblem20():
    sol = problem_20.Solution()
    isValid = sol.isValid
    
    assert isValid("()")
    assert not isValid("(]")