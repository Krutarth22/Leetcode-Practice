# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = slow = head #To determine the mid point
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
        #Reversing the second half
        prev = None
        while slow:
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        while prev:
            
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next
            
        return True
            