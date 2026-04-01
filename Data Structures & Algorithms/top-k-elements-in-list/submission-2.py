class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for n in nums:
            numCount[n] += 1

        sortedDict = sorted(numCount.items(), key=lambda x: x[1], reverse=True)
        print(numCount)
        print(sortedDict)

        ans = []
        for tup in sortedDict:
            ans.append(tup[0])

        return ans[:k]

