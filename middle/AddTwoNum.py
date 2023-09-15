from typing import Optional

"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        numbers = [0, 0]
        index = 1
        while l1 or l2:
            if l1:
                numbers[0] += l1.val * 10**index
                l1 = l1.next
            if l2:
                numbers[1] += l2.val * 10**index
                l2 = l2.next
            index += 1
        numbers = sum(numbers)
        numbers = numbers // 10

        body = ListNode(val=0)
        head = body
        for i in str(numbers)[::-1]:
            head.next = ListNode()
            head = head.next
            head.val = int(i)
        return body.next
