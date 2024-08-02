from src.problems.easy import problem_35

def testProblem35():
    sol = problem_35.Solution()
    searchInsert = sol.searchInsert
    betterSearchInsert = sol.betterSearchInsert
    
    assert(searchInsert([1, 3, 5, 6], 5)) == 2
    assert(searchInsert([1, 3, 5, 6], 2)) == 1
    assert(searchInsert([1, 3, 5, 6], 7)) == 4
    
    assert(betterSearchInsert([1, 3, 5, 6], 5)) == 2
    assert(betterSearchInsert([1, 3, 5, 6], 2)) == 1
    assert(betterSearchInsert([1, 3, 5, 6], 7)) == 4