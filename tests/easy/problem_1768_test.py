from src.problems.easy import problem_1768

def testProblem1544():
    sol = problem_1768.Solution()
    mergeAlternately = sol.mergeAlternately
    
    assert mergeAlternately('abc', 'pqr') == 'apbqcr'
    assert mergeAlternately("ab", "pqrs") == 'apbqrs'
    assert mergeAlternately("abcd", "pq") == 'apbqcd'
