class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = [ [False for i in range(len(s))] for j in range(len(s)) ]
        lps = (0,0)
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ( (j-i+1) <= 2 or cache[i+1][j-1] == True ):
                    cache[i][j] = True
                    if j-i+1 >= lps[1] - lps[0] + 1:
                        lps = (i, j)
        return s[lps[0]:lps[1]+1]
