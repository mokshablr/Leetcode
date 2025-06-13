class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            num = abs(nums[i])
            if 1 <= num <= len(nums):
                if nums[num-1] > 0:
                    nums[num-1] = -1 * nums[num-1]
                elif nums[num-1] == 0:
                    nums[num-1] = -1 * (len(nums) + 1)

        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                return i
            else:
                continue

        return len(nums)
