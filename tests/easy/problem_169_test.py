from src.problems.easy import problem_169

def testProblem1():
    sol = problem_169.Solution()
    majorityElement = sol.majorityElement
    
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([2,2,1,1,1,2,2]) == 2
