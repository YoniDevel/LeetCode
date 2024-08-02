from src.problems.easy import problem_2540

def testProblem2540():
    sol = problem_2540.Solution()
    getCommon = sol.getCommon
    
    assert getCommon([1, 2, 3], [2, 4]) == 2
    assert getCommon([1, 2, 3, 6], [2, 3, 4, 5]) == 2
