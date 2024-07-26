from src.problems.easy import problem_136

def testProblem1():
    sol = problem_136.Solution()
    singleNumber = sol.singleNumber
    
    assert singleNumber([2, 2, 1]) == 1
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    assert singleNumber([1]) == 1
