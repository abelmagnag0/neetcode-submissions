class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if n1 + n2 == target and i != j:
                    return [i, j]