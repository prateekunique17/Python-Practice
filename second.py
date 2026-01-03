class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        while n==n[::-1]:
            return True
        else:
            return False
        
obj=Solution()
x=454
print(obj.isPalindrome(x))    
