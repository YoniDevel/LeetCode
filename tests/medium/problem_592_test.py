from src.problems.medium import problem_592

def testProblem592():
    sol = problem_592.Solution()
    fractionAddition = sol.fractionAddition
    
    assert fractionAddition("-1/2+1/2") == "0/1"
    assert fractionAddition("-1/2+1/2+1/3") == "1/3"
    assert fractionAddition("1/3-1/2") == "-1/6"
    