class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyxzyz
        # z: 0, x: 1, y: 2
        # start = index(z) + 1 = 1
        # Only consider if index(c) >= start
        cmap = {}
        start = 0
        res = 0
        for end, c in enumerate(s):
            if c in cmap and cmap[c] >= start:
                start = cmap[c] + 1
            cmap[c] = end
            res = max(res, end - start + 1)
        return res
