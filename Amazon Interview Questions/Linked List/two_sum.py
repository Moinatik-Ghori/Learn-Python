'''
Two Sum

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class ListNodes:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

def add_two_numbers(l1,l2):
    dummy_node = ListNodes()
    current = dummy_node
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        total_sum = val1 + val2 + carry
        carry = total_sum // 10

        current.next = ListNodes(total_sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    current = dummy_node.next
    result_list = []
    while current:
        result_list.append(current.data)
        current = current.next
    return result_list

l1=ListNodes(2, ListNodes(4, ListNodes(3)))
l2=ListNodes(5, ListNodes(6, ListNodes(4)))
print(add_two_numbers(l1,l2))
