class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anaStr = [0] * 26
            for c in s:
                anaStr[ord(c) - ord('a')] += 1

            x = tuple(anaStr)

            anagrams[x].append(s)

        return list(anagrams.values())


