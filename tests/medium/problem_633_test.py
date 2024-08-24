from src.problems.medium import problem_633

def testProblem1():
    sol = problem_633.Solution()
    judgeSquareSum = sol.judgeSquareSum
    
    assert judgeSquareSum(5)
    assert not judgeSquareSum(3)
