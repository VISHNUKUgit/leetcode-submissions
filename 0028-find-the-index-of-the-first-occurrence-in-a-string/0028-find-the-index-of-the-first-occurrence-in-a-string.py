class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenOfHaystack = len(haystack)
        lenofNeedle   = len(needle)
        if lenOfHaystack < lenofNeedle:
            return -1
        
        for x in range(lenOfHaystack):
            slicevalue = haystack[x:x+lenofNeedle]
            if  len(slicevalue) > lenofNeedle :
                return -1
            elif slicevalue == needle:
                return x
            
        return -1    