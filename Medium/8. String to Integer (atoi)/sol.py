class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading and trailing whitespace
        s = s.strip()
        minus = 0

        # Check if the string is empty
        if s == "":
            return 0

        # Check if the string has only one character and it's not a digit
        if len(s) == 1 and not s[0].isdigit():
            return 0

        # Check if the first character is a minus or plus sign
        if s[0] == "-" or s[0] == "+":
            minus = 1

        # Find the end index for the number part of the string
        end = len(s)

        # If the string starting with minus sign or plus sign is not followed by a digit,
        # set the end index to the index of the first non-digit character after the sign
        if not s[minus:].isdigit():
            end = [not x.isdigit() for x in s[minus:]].index(True)

        # Convert the substring representing the number into an integer
        if not s[minus].isdigit():
            res = 0
        else:
            res = int(s[minus:end + minus])

        # If the first character is a minus sign, multiply the result by -1
        if s[0] == "-":
            res *= -1

        # Check for overflow and underflow
        if res > 2**31 - 1:
            res = 2**31 - 1
        elif res < -2**31:
            res = -2**31

        return res
