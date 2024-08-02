from src.problems.easy import problem_14

def testProblem14():
    sol = problem_14.Solution()
    longestCommonPrefix = sol.longestCommonPrefix
    
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert longestCommonPrefix(["dog","racecar","car"]) == ""