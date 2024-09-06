from src.problems.easy import problem_1544

def testProblem1544():
    sol = problem_1544.Solution()
    makeGood = sol.makeGood
    
    assert makeGood("leEeetcode") == "leetcode"
    assert makeGood("abBAcC") == ''
    assert makeGood("s") == "s"
