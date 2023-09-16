from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


print(
    Solution().middleNode(
        ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
    )
)
