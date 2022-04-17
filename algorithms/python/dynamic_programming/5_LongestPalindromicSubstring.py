class Solution:
    """Palindrome is a string that reads the same from left to right and right to left
    """
    def longestPalindrome(self, s: str) -> str:
        """Returns the longest palindrome
        
        Args:
            s (str): input string
            
        Returns:
            res (str): longest palindrome string
        """
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length - initialise the left and right character pointer to the centre
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return res