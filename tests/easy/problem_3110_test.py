from src.problems.easy import problem_3110

def testProblem3110():
    sol = problem_3110.Solution()
    scoreOfString = sol.scoreOfString
    
    assert scoreOfString("hello") == 13
    assert scoreOfString("zaz") == 50
