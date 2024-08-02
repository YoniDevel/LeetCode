from src.problems.easy import problem_70

def testProblem70():
    sol = problem_70.Solution()
    climbStairs = sol.climbStairs
    
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
