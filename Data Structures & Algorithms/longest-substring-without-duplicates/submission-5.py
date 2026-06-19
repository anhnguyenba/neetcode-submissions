class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        start = 0
        imap = {}
        for end in range(len(s)):
            if s[end] in imap and imap[s[end]] >= start:
                maxLength = max(maxLength, end - start)
                start = imap[s[end]] + 1
            imap[s[end]] = end

        maxLength = max(maxLength, end - start + 1)
        return maxLength