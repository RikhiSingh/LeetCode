// https://leetcode.com/problems/find-if-array-can-be-sorted?envType=daily-question&envId=2024-11-06

function canSortArray(nums: number[]): boolean {
    // maximum number in the previous bit count group
    let previousMax = 0;
    // min number in the current bit count group sahring same number of 1s
    let currentMin = Infinity;
    // max number in the current bit count group sahring same number of 1s
    let currentMax = -Infinity;
    // track the bit count of previous group
    let previousBitCount = 0;

    // iterate through the each number in nums
    for (let num of nums) {
        // cal how many 1 in binary of current number
        // then count how many 1 in binary
        // python have an inbuilt function to do this num.bit_count()
        const currentBitCount = num.toString(2).split('1').length - 1;
        
        // if the current bit count is same as previous bit count
        if (previousBitCount === currentBitCount) {
            // Update to the smallest number in the current group
            currentMin = Math.min(currentMin, num);
            // Update to the largest number in the current group
            currentMax = Math.max(currentMax, num);

            // if the bit count is different
        } else {
            // if the current min is less than the previous max
            if (currentMin < previousMax) {
                return false;
            }
            // The maximum value of the previous group becomes the currentMax (largest number in the current group).
            previousMax = currentMax;
            // Both are set to the current number ( num ), as the new group starts with this number.
            currentMin = currentMax = num;
            // Update to the currentBitCount for the new group
            previousBitCount = currentBitCount;
        }
    }
    // After the loop finishes, we return true if the last group (the one that was processed last) is valid
    return currentMin >= previousMax;
}
