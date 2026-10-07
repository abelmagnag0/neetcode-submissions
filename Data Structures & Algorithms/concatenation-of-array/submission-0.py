class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)

        ans = [0] * (2 * lenNums)
        
        for i in range(lenNums):
            ans[i] = nums[i]
            ans[i + lenNums] = nums[i]

        return ans