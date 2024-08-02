from src.problems.easy import problem_3005

def testProblem3005():
    sol = problem_3005.Solution()
    maxFrequencyElements = sol.maxFrequencyElements
    
    assert maxFrequencyElements([1,2,2,3,1,4]) == 4
    assert maxFrequencyElements([1,2,3,4,5]) == 5
