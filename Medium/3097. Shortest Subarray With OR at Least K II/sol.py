# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        index = 0
        out = float('inf')
        while index < len(nums):
            size = 0
            while index < len(nums) - 1 and nums[index+1] == nums[index]:
                index += 1
            j = index
            result = 0
            while j < len(nums) and result < k:
                result = result | nums[j]
                size += 1
                j += 1
            if result >= k:
                out = min(out,size)
            else:
                #full array iterated
                break
            index += 1
        if out == float('inf'):
            return -1
        return out


# Example usage:
solution = Solution()
nums = [1, 2, 3]
k = 2
print(solution.minimumSubarrayLength(nums, k))  # Output: 1
