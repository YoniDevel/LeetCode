from src.problems.easy import problem_2022

def testProblem2022():
    sol = problem_2022.Solution()
    construct2DArray = sol.construct2DArray
    
    assert construct2DArray([1,2,3,4], 2, 2) == [[1, 2], [3, 4]]
    assert construct2DArray([1,2,3], 1, 3) == [[1, 2, 3]]
    assert construct2DArray([1, 2], 1, 1) == []
