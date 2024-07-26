from src.problems.easy import problem_219

def testProblem1():
    sol = problem_219.Solution()
    containsNearbyDuplicate = sol.containsNearbyDuplicate
    
    assert containsNearbyDuplicate([1,2,3,1], 3)
    assert containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
