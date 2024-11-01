from src.problems.hard import problem_1106

def testProblem1106():
    sol = problem_1106.Solution()
    parseBoolExpr = sol.parseBoolExpr
    
    assert not parseBoolExpr("&(|(f))")
    assert parseBoolExpr("|(f,f,f,t)")
    assert parseBoolExpr("!(&(f,t))")
