# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        sum = 0
        newList = ListNode()
        Root = newList
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                carry = 0
                if sum > 9:
                    carry = sum//10
                    sum = sum%10
                newList.val = sum
                if l1.next or l2.next:
                    newList.next = ListNode()
                    newList = newList.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val+ carry
                carry = 0
                if sum > 9:
                    carry = sum//10
                    sum = sum%10
                newList.val = sum
                if l1.next:
                    newList.next = ListNode()
                    newList = newList.next
                l1 = l1.next
            elif l2:
                sum = l2.val+ carry
                carry = 0
                if sum > 9:
                    carry = sum//10
                    sum = sum%10
                newList.val = sum
                if l2.next:
                    newList.next = ListNode()
                    newList = newList.next
                l2 = l2.next
        if carry != 0:
            newList.next = ListNode()
            newList = newList.next
            newList.val = carry
        return Root


