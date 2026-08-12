#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=[]
        current=head
        while current:
            node.append(current)
            current=current.next
        removed_node=len(node)-n
        if removed_node==0:
            return head.next
        node[removed_node-1].next=node[removed_node].next
        return head

        