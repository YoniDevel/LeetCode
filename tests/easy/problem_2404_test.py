from src.problems.easy import problem_2404

def testProblem2418():
    sol = problem_2404.Solution()
    mostFrequentEven = sol.mostFrequentEven
    
    assert mostFrequentEven([0,1,2,2,4,4,1]) == 2
    assert mostFrequentEven([4,4,4,9,2,4]) == 4
    assert mostFrequentEven([29,47,21,41,13,37,25,7]) == -1
    