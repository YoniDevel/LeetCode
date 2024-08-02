from src.problems.medium import problem_7

def testProblem7():
    sol = problem_7.Solution()
    reverse = sol.reverse
    
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
