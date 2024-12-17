from src.problems.easy import problem_3264

def testProblem3264():
    sol = problem_3264.Solution()
    getFinalState, betterGetFinalState = sol.getFinalState, sol.betterGetFinalState
    
    assert getFinalState([2,1,3,5,6], 5, 2) == [8,4,6,5,6]
    assert getFinalState([1,2], 3, 4) == [16, 8]
    
    assert betterGetFinalState([2,1,3,5,6], 5, 2) == [8,4,6,5,6]
    assert betterGetFinalState([1,2], 3, 4) == [16, 8]
