from src.problems.medium import problem_3

def testProblem3():
    sol = problem_3.Solution()
    lengthOfLongestSubstring = sol.lengthOfLongestSubstring
    
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring(" ") == 1