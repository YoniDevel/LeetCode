from src.problems.easy import problem_26;
import pytest;

@pytest.fixture
def testArray(inputArray: list[int], expectedArray: list[int], removeDuplicates):
    nums: list[int] = inputArray;
    expectedNums: list[int] = expectedArray; 

    k: int = removeDuplicates(nums); 

    assert k == len(expectedNums);
    for i in range(k):
        assert nums[i] == expectedNums[i];

@pytest.fixture(name='testArray')
def testProblem26():
    sol = problem_26.Solution();
    removeDuplicates = sol.removeDuplicates;
    
    testArray([1, 1, 2], [1, 2], removeDuplicates);
    testArray([0,0,1,1,1,2,2,3,3,4], [0, 1, 2, 3, 4], removeDuplicates);
    
