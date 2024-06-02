// Link: https://leetcode.com/problems/reverse-string/description/

/**
 Do not return anything, modify s in-place instead.
 */
 function reverseString(s: string[]): void {
    // Initialize two pointers, left starting at the beginning and right starting at the end of the array
    let left = 0;
    let right = s.length - 1;

    // Loop until the two pointers meet in the middle
    while (left < right) {
        // Swap the elements at the left and right pointers
        [s[left], s[right]] = [s[right], s[left]];
        // Move the left pointer one step to the right
        left++;
        // Move the right pointer one step to the left
        right--;
    }
}
