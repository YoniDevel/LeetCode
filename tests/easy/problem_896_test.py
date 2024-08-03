from src.problems.easy import problem_896

def testProblem704():
    sol = problem_896.Solution()
    isMonotonic = sol.isMonotonic
    
    assert isMonotonic([1,2,2,3])
    assert isMonotonic([6,5,4,4])
    assert not isMonotonic([1,3,2])
