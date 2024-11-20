class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0

        for i in range(n-k+1):
            subarray = nums[i:i+k]
            
            if len(set(subarray)) == k:
                max_sum = max(max_sum, sum(subarray))
        return max_sum

# sliding window
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        ws = 0
        max_sum = 0

        for i in range(n):
            # Add the current element to the window
            mp[nums[i]] += 1
            ws += nums[i]

            # If the window size exceeds 'k', slide the window
            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            # Check if the window has exactly 'k' distinct elements
            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum