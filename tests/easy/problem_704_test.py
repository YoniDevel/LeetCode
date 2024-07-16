from src.problems.easy import problem_704

def testProblem1():
    sol = problem_704.Solution()
    search = sol.search
    
    assert (search([-1,0,3,5,9,12], 9) == 4)
    assert (search([-1,0,3,5,9,12], 2) == -1)