class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    res = nums[i] + nums[j]

                    if res == target:
                        return (i,j)
