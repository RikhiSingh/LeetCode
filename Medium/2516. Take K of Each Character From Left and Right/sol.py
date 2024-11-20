class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        ans = n
        a, b, c = 0, 0, 0

        # Count total occurrences of 'a', 'b', and 'c'
        totalA = s.count('a')
        totalB = s.count('b')
        totalC = s.count('c')

        # If there are not enough 'a', 'b', or 'c', return -1
        if totalA < k or totalB < k or totalC < k:
            return -1

        # Reset counters and start sliding window
        while r < n:
            if s[r] == 'a': a += 1
            if s[r] == 'b': b += 1
            if s[r] == 'c': c += 1
            r += 1

            # Shrink window if it exceeds the limits
            while a > totalA - k or b > totalB - k or c > totalC - k:
                if s[l] == 'a': a -= 1
                if s[l] == 'b': b -= 1
                if s[l] == 'c': c -= 1
                l += 1

            # Update the answer with the minimum number of characters to remove
            ans = min(ans, n - (r - l))

        return ans