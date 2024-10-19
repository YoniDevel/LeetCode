from src.problems.medium import problem_1545

def testProblem1():
    sol = problem_1545.Solution()
    findKthBit = sol.findKthBit
    
    assert findKthBit(3, 1) == '0'
    assert findKthBit(4, 11) == '1'
    