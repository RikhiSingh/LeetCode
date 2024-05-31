// Link: https://leetcode.com/problems/find-the-maximum-divisibility-score/description/

function maxDivScore(nums: number[], divisors: number[]): number {
    // Initialize the result variable 'res' to store the divisor with the maximum score
    let res = 0;
    // Initialize 'curr' to keep track of the highest score found so far
    let curr = -1;

    // Loop through each divisor in the divisors array
    for (let d of divisors) {
        // Initialize score for the current divisor 'd'
        let score = 0;
        // Loop through each number in the nums array
        for (let it of nums) {
            // If the number is divisible by the current divisor, increment the score
            if (it % d === 0) {
                score++;
            }
        }
        // If the current score is greater than or equal to the highest score found so far
        if (score >= curr) {
            // If the current score is equal to the highest score, choose the smaller divisor
            if (score === curr) {
                res = Math.min(res, d);
            } else {
                // Otherwise, update the result with the current divisor
                res = d;
            }
            // Update the highest score found so far
            curr = score;
        }
    }

    // Return the divisor with the maximum score
    return res;
}
