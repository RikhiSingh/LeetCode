// Link: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor

function countTriplets(arr: number[]): number {
    // Get the length of the input array
    const n = arr.length;
    // Initialize the prefix array with zeros, having length n + 1
    const prefix = new Array(n + 1).fill(0);

    // Fill the prefix array with cumulative XOR values
    for (let i = 0; i < n; i++) {
        // prefix[i + 1] holds the XOR of all elements from arr[0] to arr[i]
        prefix[i + 1] = prefix[i] ^ arr[i];
    }

    let count = 0;
    // Iterate over each possible starting index i
    for (let i = 0; i < n; i++) {
        // Iterate over each possible ending index j
        for (let j = i + 1; j < n; j++) {
            // Check if the XOR from arr[0] to arr[i-1] is equal to the XOR from arr[0] to arr[j]
            if (prefix[i] === prefix[j + 1]) {
                // If true, increment the count by the number of elements between i and j
                count += j - i;
            }
        }
    }

    // Return the total count of such triplets
    return count;
}
