from src.problems.easy import problem_2239

def testProblem2022():
    sol = problem_2239.Solution()
    findClosestNumber = sol.findClosestNumber
    
    assert findClosestNumber([-4,-2,1,4,8]) == 1
    assert findClosestNumber([2,-1,1]) == 1
