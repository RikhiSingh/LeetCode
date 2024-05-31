// Link: https://leetcode.com/problems/single-number-iii/description/

function singleNumber(nums: number[]): number[] {
    let xy = 0;
    // XOR all numbers to get the XOR of the two unique numbers
    for (let n of nums) {
        xy ^= n;
    }

    // Get the rightmost set bit of xy
    xy &= -xy;

    // Initialize the result array to store the two unique numbers
    const result = [0, 0];

    // Divide the numbers into two groups and XOR within each group
    for (let n of nums) {
        if ((xy & n) === 0) {
            result[0] ^= n;
        } else {
            result[1] ^= n;
        }
    }

    return result;
}
