from src.problems.easy import problem_121

def testProblem136():
    sol = problem_121.Solution()
    maxProfit = sol.maxProfit
    
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0
