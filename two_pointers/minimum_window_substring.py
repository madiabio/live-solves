class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = dict()
        for ch in t:
            tCounts[ch] = tCounts.get(ch, 0) + 1
        need = len(tCounts.keys())
        have = 0
        l = 0
        res = [-1, -1]
        resLen = float("infinity")
        sCounts = dict()
        for r in range(len(s)):
            sCounts[s[r]] = sCounts.get(s[r], 0) + 1
            if s[r] in tCounts:
                if sCounts[s[r]] == tCounts[s[r]]:
                    have += 1
                    
                while have == need:
                    if (r - l  + 1) < resLen:
                        res = [l,r]
                        resLen = r - l + 1
                    sCounts[s[l]] -= 1
                    if s[l] in tCounts and sCounts[s[l]] == tCounts.get(s[l], 0) - 1:
                        have -= 1
                    l+=1
        l, r  = res
        return s[l:r+1] if resLen != float("infinity") else ""
                    
