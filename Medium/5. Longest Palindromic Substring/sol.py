# Link: https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check if the string length is less than or equal to 1
        if len(s) <= 1:
            return s

        # Function to expand around the center
        def expand_around_center(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            # Return the palindrome substring
            return s[left+1:right]

        # Initialize the maximum palindrome substring as the first character
        max_str = s[0]

        # Loop through the string characters
        for i in range(len(s) - 1):
            # Expand around the center for both odd and even length palindromes
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i+1)

            # Update the maximum palindrome substring if the length of the odd palindrome is greater
            if len(odd) > len(max_str):
                max_str = odd

            # Update the maximum palindrome substring if the length of the even palindrome is greater
            if len(even) > len(max_str):
                max_str = even

        # Return the maximum palindrome substring found
        return max_str
