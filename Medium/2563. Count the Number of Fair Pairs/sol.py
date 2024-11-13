class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the input list 'nums' to make the problem easier to solve using binary search
        nums.sort()

        # Initialize a variable to store the number of valid pairs
        answer = 0

        # Loop through each element in 'nums'
        for i in range(len(nums) - 1):
            # For the current element nums[i], we need to find indices j > i
            # where the sum nums[i] + nums[j] lies between 'lower' and 'upper'.

            # Calculate the lower bound: We want nums[i] + nums[j] >= lower, so
            # nums[j] must be >= lower - nums[i].
            # Use bisect_left to find the smallest index 'low' such that
            # nums[j] >= lower - nums[i] for j > i.
            low = bisect_left(nums, lower - nums[i], i + 1)

            # Calculate the upper bound: We want nums[i] + nums[j] <= upper, so
            # nums[j] must be <= upper - nums[i].
            # Use bisect_right to find the smallest index 'up' such that
            # nums[j] > upper - nums[i] for j > i.
            up = bisect_right(nums, upper - nums[i], i + 1)

            # The number of valid pairs for the current 'i' is the number of 'j' indices
            # such that lower - nums[i] <= nums[j] <= upper - nums[i].
            # This can be computed as 'up - low'.
            answer += up - low

        # Return the total number of valid pairs found
        return answer
