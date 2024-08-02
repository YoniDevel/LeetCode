from src.problems.easy import problem_66

def testProblem66():
    sol = problem_66.Solution()
    plusOne = sol.plusOne
    
    assert (plusOne([1,2,3]) == [1, 2, 4])
    assert (plusOne([4,3,2,1]) == [4,3,2,2])
    assert (plusOne([9]) == [1, 0])
