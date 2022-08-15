# 1. Two Sum
# https://leetcode.com/problems/two-sum/
nums = [3,2,3]
target = 6

def twoSum():
    length = len(nums)
    for i in range(0, length - 1):
        result = target - nums[i]

        for j in range(i+1, length):
            if nums[j] == result:
                answer = [nums[i], nums[j]]
                return answer

print(twoSum())
