from src.problems.easy import problem_476

def testProblem476():
    sol = problem_476.Solution()
    findComplement = sol.findComplement
    
    assert findComplement(5) == 2
    assert findComplement(1) == 0
