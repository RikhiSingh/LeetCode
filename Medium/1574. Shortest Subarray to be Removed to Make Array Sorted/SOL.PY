from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        l = 0

        while l + 1 < n and arr[l] <= arr[l+1]:
            l += 1

        if l == n-1:
            return 0

        r = n-1
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1

        result = min(n-l-1, r)

        i,j =0, r
        while i <=l and j<n:
            if arr[i] <= arr[j]:
                result = min(result, j-i-1)
                i +=1
            else:
                j+=1
        return result
        
                
                
            


# Test case
solution = Solution()
s = [1,2,3,10,4,2,3,5]
# s = [1,2,3]
print(solution.findLengthOfShortestSubarray(s))