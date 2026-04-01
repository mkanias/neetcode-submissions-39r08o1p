class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anaStr = [0] * 52
            for c in s:
                if c.islower():
                    anaStr[ord(c) - ord('a')] += 1
                else:
                    anaStr[26 + ord(c) - ord('A')] += 1

            x = tuple(anaStr)

            anagrams[x].append(s)

        return list(anagrams.values())


