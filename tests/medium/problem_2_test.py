from src.problems.medium import problem_2
ListNode = problem_2.ListNode

def testProblem2():
    sol = problem_2.Solution()
    addTwoNumbers = sol.addTwoNumbers
    
    assert addTwoNumbers(
        ListNode(1, ListNode(2, ListNode(3))),
        ListNode(1, ListNode(2))
    ).toString() == "2->4->3->"    
    assert addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))
    ).toString() == "7->0->8->"