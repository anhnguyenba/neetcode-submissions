class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        imap = { s[0]: 0 }
        l = 0
        res = 1
        for r in range(1, len(s)):
            if s[r] in imap and imap[s[r]] >= l:
                l = imap[s[r]] + 1
            imap[s[r]] = r
            res = max(res, r - l + 1)
        return res

        
