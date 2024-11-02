from src.problems.easy import problem_2490

def testProblem2490():
    sol = problem_2490.Solution()
    isCircularSentence = sol.isCircularSentence
    
    assert isCircularSentence("leetcode exercises sound delightful")
    assert isCircularSentence("eetcode")
    assert not isCircularSentence("Leetcode is cool")
