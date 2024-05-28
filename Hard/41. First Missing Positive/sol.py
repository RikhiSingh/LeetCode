class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        
        # Rearrange the elements in the list
        for i in range(n):
            # Continue swapping until the current element is either out of range or in its correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the elements to their correct positions
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # After rearrangement, find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:  # If the element is not in its correct position
                return i + 1  # Return the first missing positive integer
        
        # If all elements are in their correct positions, the first missing positive is n + 1
        return n + 1
