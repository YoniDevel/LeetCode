from src.problems.easy import problem_217

def testProblem217():
    sol = problem_217.Solution()
    containsNearbyDuplicate = sol.containsDuplicate
    
    assert containsNearbyDuplicate([1,2,3,1])
    assert not containsNearbyDuplicate([1,2,3,4])
    assert containsNearbyDuplicate([1,1,1,3,3,4,3,2,4,2])