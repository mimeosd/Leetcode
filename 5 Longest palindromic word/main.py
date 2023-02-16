class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        n = len(s)
        start, end = 0, 0
        
        def expand_around_center(left, right):
            nonlocal start, end
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start, end = left + 1, right - 1
        
        for i in range(n):
            expand_around_center(i, i)
            expand_around_center(i, i+1)
        
        return s[start:end+1]
