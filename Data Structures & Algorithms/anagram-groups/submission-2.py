class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act", "pots", "tops", "cat", "stop", "hat"]
        anagram_dict = defaultdict(list)
        for s in strs:
            key = "".join(sorted(list(s)))
            anagram_dict[key].append(s)

        return [anagrams for _, anagrams in anagram_dict.items()]