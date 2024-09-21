from src.problems.easy import problem_205

def testProblem205():
    sol = problem_205.Solution()
    isIsomorphic = sol.isIsomorphic
    
    assert isIsomorphic("egg", "add")
    assert not isIsomorphic("foo", "bar")
    assert isIsomorphic("paper", "title")
