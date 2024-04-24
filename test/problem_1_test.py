from src.problems import problem_1;

def testProblem1():
    sol = problem_1.Solution1();
    twoSum = sol.twoSum;
    betterTwoSum = sol.BetterTwoSum;
    
    assert twoSum([2, 7, 11, 15], 9) == [0, 1];
    assert twoSum([3, 2, 4], 6) == [1, 2];
    assert twoSum([3, 3], 6) == [0, 1];
    
    assert betterTwoSum([2, 7, 11, 15], 9) == [0, 1];
    assert betterTwoSum([3, 2, 4], 6) == [1, 2];
    assert betterTwoSum([3, 3], 6) == [0, 1];
