class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            anaStr = {}
            for c in string:
                anaStr[c] = anaStr.get(c,0) + 1

            x = tuple(sorted(anaStr.items()))

            anagrams.setdefault(x, []).append(string)

        return list(anagrams.values())
        