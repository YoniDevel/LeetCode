from src.problems import problem_14;

def testProblem2():
    sol = problem_14.Solution();
    longestCommonPrefix = sol.longestCommonPrefix;
    
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl";
    assert longestCommonPrefix(["dog","racecar","car"]) == "";