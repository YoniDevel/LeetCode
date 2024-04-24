from src.problems import problem_13;

def testProblem2():
    sol = problem_13.Solution();
    romanToInt = sol.romanToInt;
    
    assert romanToInt('III') == 3;
    assert romanToInt('LVIII') == 58;
    assert romanToInt('MCMXCIV') == 1994;