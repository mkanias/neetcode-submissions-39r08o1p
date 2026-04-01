class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            anaStr = {}
            for c in string:
                anaStr[c] = anaStr.get(c,0) + 1

            x = tuple(sorted(anaStr.items()))

            if not x in anagrams.keys():
                anagrams[x] = [string]
            else:
                anagrams[x].append(string)

        return list(anagrams.values())
        