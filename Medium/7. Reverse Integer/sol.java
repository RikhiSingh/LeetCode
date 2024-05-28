// Link: https://leetcode.com/problems/reverse-integer/

class Solution {
    public int reverse(int x) {
        // Flag to check if the number is negative
        boolean negative = false;

        // If the number is negative, make it positive and set the flag
        if(x < 0){
            negative = true;
            x *= -1;
        }

        // Use a long variable to handle potential overflow during reversal
        long reversed = 0;

        // Loop to reverse the digits of the number
        while(x > 0){
            // Add the last digit of x to the reversed number
            reversed = (reversed * 10) + (x % 10);
            // Remove the last digit from x
            x /= 10;
        }

        // Check for overflow: if reversed number exceeds the max value of int, return 0
        if(reversed > Integer.MAX_VALUE){
            return 0;
        }

        // If the original number was negative, convert the reversed number back to negative
        // Otherwise, return the reversed number as is
        return negative ? (int)(-1 * reversed) : (int)reversed;
    }
}
