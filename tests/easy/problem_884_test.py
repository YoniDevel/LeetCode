from src.problems.easy import problem_884

def testProblem884():
    sol = problem_884.Solution()
    uncommonFromSentences = sol.uncommonFromSentences
    
    assert uncommonFromSentences("this apple is sweet", "this apple is sour") in (
        ["sour", "sweet"],
        ["sweet", "sour"]
    )
    assert uncommonFromSentences("apple apple", "banana") == ['banana']
    