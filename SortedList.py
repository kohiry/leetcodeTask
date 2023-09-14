from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_node = ListNode(0)
        curr = new_node

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return new_node.next


FirstNode = ListNode(val=0, next=None)
N2ode = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
N3ode = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
print(Solution().mergeTwoLists(None, None))
