class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0

        for i in range(n-k+1):
            subarray = nums[i:i+k]
            
            if len(set(subarray)) == k:
                max_sum = max(max_sum, sum(subarray))
        return max_sum