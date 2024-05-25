# Link: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize a dictionary to store previously seen numbers and their indices
        prevMap = {}  # val: index

        # Iterate through the list of numbers along with their indices
        for i, n in enumerate(nums):

            # Calculate the difference needed to reach the target from the current number
            diff = target - n

            # Check if the difference exists in the previous map
            if diff in prevMap:

                # If the difference exists, return the indices of the two numbers that sum up to the target
                return [prevMap[diff], i]

            # If the difference doesn't exist, store the current number and its index in the dictionary
            prevMap[n] = i
        
        # If no solution is found, return but we were made sure in the description of the question we are guaranteed there is a solution, technically this return is not required
        return None

# End of Solution class
