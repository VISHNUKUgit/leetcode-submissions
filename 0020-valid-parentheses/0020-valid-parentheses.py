class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses ={
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []
        if len(s)%2 != 0 :
            return False 
        for par in s:
            if par in  parentheses:
                stack.append(par)
            else:
                if not stack:
                    return False
                lastPar = stack.pop()
                if parentheses[lastPar]  != par:
                    return False  
        return len(stack) == 0