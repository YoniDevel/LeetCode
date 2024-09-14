from src.problems.easy import problem_2418

def testProblem2418():
    sol = problem_2418.Solution()
    sortPeople = sol.sortPeople
    
    assert sortPeople(["Mary","John","Emma"], [180,165,170]) == ["Mary","Emma","John"]
    assert sortPeople(["Alice","Bob","Bob"], [155,185,150]) == ["Bob","Alice","Bob"]
