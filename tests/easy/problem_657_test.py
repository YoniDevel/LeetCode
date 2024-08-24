from src.problems.easy import problem_657

def testProblem657():
    sol = problem_657.Solution()
    judgeCircle = sol.judgeCircle
    
    assert judgeCircle("UD")
    assert not judgeCircle("LL")
