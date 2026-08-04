# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        value1 = []
        value2 = []
        current1 = l1
        while current1:
            value1.append(current1.val)
            current1=current1.next
        current2 = l2  
        while current2:
            value2.append(current2.val)
            current2=current2.next 
        value1.reverse()  
        value2.reverse()
        sum =  int("".join(map(str, value1))) +  int("".join(map(str, value2)))
        if sum == 0:
            return ListNode(0)
        dummy = ListNode(0)
        current = dummy
        
        while sum > 0:
            digit = sum % 10  # Get last digit
            current.next = ListNode(digit)
            current = current.next
            sum //= 10
        
        return dummy.next
        