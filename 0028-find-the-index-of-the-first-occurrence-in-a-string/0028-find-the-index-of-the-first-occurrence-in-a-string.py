class Solution(object):
    def strStr(self, haystack, needle):
        lenOfHaystack = len(haystack)
        lenofNeedle = len(needle)

        if lenofNeedle == 0:
            return 0

        if lenOfHaystack < lenofNeedle:
            return -1

        for x in range(lenOfHaystack - lenofNeedle + 1):
            if haystack[x:x+lenofNeedle] == needle:
                return x

        return -1