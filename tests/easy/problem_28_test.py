from src.problems.easy import problem_28

def testProblem28():
    sol = problem_28.Solution()
    strStr = sol.strStr
    
    assert strStr("a", "a") == 0