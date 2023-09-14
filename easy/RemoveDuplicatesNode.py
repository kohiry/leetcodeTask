from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        body = ListNode()
        nextt = body
        correct_elem = []

        while head:
            if head.val not in correct_item:
                correct_item.append(head.val)
                nextt.val = head.val
                nextt.next = head.next
                head = head.next

        return body
