import problems

def testProblem2():
    sol = problems.problem_9.Solution();
    isPalindrome = sol.isPalindrome;
    isPalindromeWithoutString = sol.isPalindromeWithoutString;
    
    assert isPalindrome(121);
    assert not isPalindrome(-121);
    assert not isPalindrome(10);
    
    assert isPalindromeWithoutString(121);
    assert not isPalindromeWithoutString(-121);
    assert not isPalindromeWithoutString(10);