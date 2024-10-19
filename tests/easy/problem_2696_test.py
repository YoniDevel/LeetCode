from src.problems.easy import problem_2696

def testProblem2540():
    sol = problem_2696.Solution()
    minLength = sol.minLength
    
    assert minLength('ABFCACDB') == 2
    assert minLength('ACBBD') == 5
