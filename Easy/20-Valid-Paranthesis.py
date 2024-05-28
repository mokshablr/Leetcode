class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s is the string
        stack = list()
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)

            else:
                if len(stack)==0:
                    return False
                element = stack.pop()
                if element== '(' and i==')':
                    continue
                elif element== '{' and i=='}':
                    continue
                elif element== '[' and i==']':
                    continue
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
