from src.problems.easy import problem_796

def testProblem704():
    sol = problem_796.Solution()
    rotateString = sol.rotateString
    
    assert rotateString("abcde", "cdeab")
    assert not rotateString("abcde", "abced")
