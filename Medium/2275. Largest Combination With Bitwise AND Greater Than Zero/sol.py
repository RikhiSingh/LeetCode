# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero

#  to find if whether the bit is set for both number(s) at the position 
#  and we are suppposed to return the maximum of the count

# so they must have the same bit at that position set
# Count how many numbers have the first bit (bit 0) set to 1, how many have the second bit (bit 1) set to 1, and so on, for all 32 bits (since integers are at most 32-bit).
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # we create an array of size 32
        count = [0] * 32
        
        # Loop over all candidates
        for c in candidates:
            # we initialize i to 0
            # which handles the 32 bits of the integer
            i = 0
            
            # Loop over all numbers
            while c > 0:                
                #  if the bit is set to 1 we add to the count current [i]
                count[i] += 1 & c
                
                i += 1 # we move to the next index in the array
                c = c >> 1 # we move to the next bit by right shofting all the bits so if while c> 0 was 16 here it changed to 8
                
        # Return the maximum count of any bit position
        return max(count)
