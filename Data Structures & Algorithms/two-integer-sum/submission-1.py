class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        ans = []

        for i, n in enumerate(nums):
            if n in comp:
                ans.append(comp[n])
                ans.append(i)
                return ans
            
            compNum = target - n
            comp[compNum] = i