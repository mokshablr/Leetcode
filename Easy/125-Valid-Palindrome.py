class Solution(object):
    def isPalindrome(self,s):
            """
            :type s: str
            :rtype: bool
            """
            l = 0
            length = len(s)
            r = length-1
            low = s.lower()

            while l<r:
                while l<length and not (low[l].isalnum()) :
                    l+=1
                while r>0 and not (low[r].isalnum()):
                    r-=1

                if l<length and r>0 and low[l]!=low[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
