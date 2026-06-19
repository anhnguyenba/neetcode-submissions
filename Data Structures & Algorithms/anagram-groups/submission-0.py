class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagram_index = defaultdict(list)
        for i, s in enumerate(strs):
            anagram_index[tuple(sorted(list(s)))].append(i)

        res = []
        for key, indexes in anagram_index.items():
            sublist = []
            for i in indexes:
                sublist.append(strs[i])
            res.append(sublist)
        return res  