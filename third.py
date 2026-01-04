class Solution:
    
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        
        result = ""
        
        # Loop through characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character in all strings
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return result
            
            result += char
        
        return result


# Create object of Solution
sol = Solution()

# Input
strs = ["flower", "flow", "flight"]

# Call function and print result
print(sol.longestCommonPrefix(strs))
