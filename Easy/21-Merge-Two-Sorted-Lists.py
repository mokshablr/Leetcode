# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = ListNode()
        head = output
        
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                output.next=ListNode(list1.val)
                output = output.next
                list1 = list1.next

            else:
                output.next = ListNode(list2.val)
                output = output.next
                list2 = list2.next

        if list1 != None and list2==None:
            output.next = list1
        elif list1== None and list2!=None:
            output.next = list2

        return head.next
