class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_case = s.lower()
        
        res = []
        for char in low_case:
            if char.isalnum():
                res.append(char)
        res_str = "".join(res)
        
        if res_str == res_str[::-1]:
            return True
        


sample = "A man, a plan, a canal: Panama"
s1 = Solution()
print(s1.isPalindrome(sample))