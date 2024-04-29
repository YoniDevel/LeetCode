from src.problems.easy import problem_9;

def testProblem2():
    sol = problem_9.Solution();
    isPalindrome = sol.isPalindrome;
    isPalindromeWithoutString = sol.isPalindromeWithoutString;
    
    assert isPalindrome(121);
    assert not isPalindrome(-121);
    assert not isPalindrome(10);
    
    assert isPalindromeWithoutString(121);
    assert not isPalindromeWithoutString(-121);
    assert not isPalindromeWithoutString(10);