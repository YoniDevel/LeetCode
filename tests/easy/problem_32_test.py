from src.problems.easy import problem_32

def testProblem35():
    sol = problem_32.Solution()
    isSubsequence = sol.isSubsequence
    
    assert isSubsequence("abc", "ahbgdc")
    assert not isSubsequence("axc", "ahbgdc")
