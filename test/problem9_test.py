from problems import problem9

def testProblem2():
    sol = problem9.Solution();
    isPalindrome = sol.isPalindrome;
    isPalindromeWithoutString = sol.isPalindromeWithoutString;
    
    assert isPalindrome(121);
    assert not isPalindrome(-121);
    assert not isPalindrome(10);
    
    print(121 == 121);
    assert isPalindromeWithoutString(121);
    assert not isPalindromeWithoutString(-121);
    assert not isPalindromeWithoutString(10);