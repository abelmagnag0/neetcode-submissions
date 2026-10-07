class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i, n in enumerate(nums):
            complemento = target - n 

            if complemento in vistos:
                return [vistos[complemento], i]
            else:
                vistos[n] = i