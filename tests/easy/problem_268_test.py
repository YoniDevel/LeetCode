from src.problems.easy import problem_268

def testProblem219():
    sol = problem_268.Solution()
    missingNumber = sol.missingNumber
    
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8
