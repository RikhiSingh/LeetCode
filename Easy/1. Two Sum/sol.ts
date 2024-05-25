function twoSum(nums: number[], target: number): number[] {
    // Iterate through each number in the array
    for (let i = 0; i < nums.length; i++) {

        // Iterate through the remaining numbers in the array
        for (let j = i + 1; j < nums.length; j++) {

            // Check if the sum of the current number and any other number equals the target
            if (nums[i] + nums[j] === target) {
                
                // Return the indices of the two numbers that sum up to the target
                return [i, j];
            }
        }
    }
    
    // No solution found
    return [-1, -1];
}