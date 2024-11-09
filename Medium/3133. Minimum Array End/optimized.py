# this one has time complexity of (o(log2n)) instead the original one being (o(n))
# so previous if we had 63 bit long it was goint to be 2^63 but this one will be only 63

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        i_x = 1
        i_n = 1 # for n - 1 as we are already setting the first element as x
        
        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n-1):
                    result = result | i_x
                i_n = i_n << 1
                
            i_x = i_x << 1
        
        return result