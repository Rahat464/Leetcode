class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(0, length - 1):
            result = target - nums[i]

            for j in range(i + 1, length):
                if nums[j] == result:
                    return [i, j]
