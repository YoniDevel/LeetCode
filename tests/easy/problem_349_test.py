from src.problems.easy import problem_349

def testProblem349():
    sol = problem_349.Solution()
    intersection = sol.intersection
    
    assert intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert intersection([4,9,5], [9,4,9,8,4]) == [4, 9] or [9, 4]
