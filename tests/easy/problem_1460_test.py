from src.problems.easy import problem_1460

def testProblem1460():
    sol = problem_1460.Solution()
    canBeEqual = sol.canBeEqual
    
    assert canBeEqual([1,2,3,4], [2,4,1,3])
    assert canBeEqual([7], [7])
    assert not canBeEqual([3,7,9], [3,7,11])
