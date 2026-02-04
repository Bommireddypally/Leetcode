class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_amount = 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            if i == 2:
                dp[i] = max(nums[0]+nums[2], nums[1])
            else:
                dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i], dp[i-1])
        return dp[n-1]
