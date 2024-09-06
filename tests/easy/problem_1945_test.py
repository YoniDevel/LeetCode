from src.problems.easy import problem_1945

def testProblem1945():
    sol = problem_1945.Solution()
    getLucky = sol.getLucky
    
    assert getLucky("iiii", 1) == 36
    assert getLucky("leetcode", 2) == 6
    assert getLucky("zbax", 2) == 8
