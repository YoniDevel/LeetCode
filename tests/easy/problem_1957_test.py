from src.problems.easy import problem_1957

def testProblem1957():
    sol = problem_1957.Solution()
    makeFancyString = sol.makeFancyString
    
    assert makeFancyString('leeetcode') == 'leetcode'
    assert makeFancyString('aaabaaaa') == 'aabaa'
    assert makeFancyString('aab') == 'aab'
