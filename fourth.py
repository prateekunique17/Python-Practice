class Solution:
    def isValid(self, s: str) -> bool:
        if "(" in s and ")" in s:
            return True
        elif "[" in s and "]" in s:
            return True
        elif "{" in s and "}" in s:
            return True
        else:
            return False


sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True