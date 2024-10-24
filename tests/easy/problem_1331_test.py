from src.problems.easy import problem_1331

def testProblem1331():
    sol = problem_1331.Solution()
    arrayRankTransform = sol.arrayRankTransform
    
    assert arrayRankTransform([40,10,20,30]) == [4, 1, 2, 3]
    assert arrayRankTransform([100,100,100]) == [1, 1, 1]
    assert arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3]
