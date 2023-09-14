# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next_num = -1
        under_link = ListNode()
        answer = ListNode()
        next_link = 0

        while l1.next:
            num = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            if num >= 10:
                next_num = num // 10
            else:
                next_num = 0

            if answer.next is None:
                ansewr.val = num % 10
                answer.next = ListNode()
                under_link = answer.next
            else:
                undex_link.val = num % 10
                under_link.next = ListNode()
                under_link = under_link.next
        return answer
