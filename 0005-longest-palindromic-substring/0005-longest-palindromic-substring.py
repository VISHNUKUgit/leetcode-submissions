class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        slen = len(s)
        
        def expand(left: int, right: int) -> None:
            nonlocal start, end
            while left >= 0 and right < slen and s[left] == s[right]:
                left -= 1
                right += 1
            # palindrome is s[left+1 : right]
            if right - left - 1 > end - start:
                start, end = left + 1, right
        
        for i in range(slen):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length
        
        return s[start:end]