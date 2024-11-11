# https://leetcode.com/problems/prime-subtraction-operation
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        # Helper function to check if a number n is prime
        def isPrime(n):
            # Check divisibility by numbers from 2 to sqrt(n)
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False # n is divisible by f, so it's not prime
            return True # n is prime if we didn't find any divisors            

        previousNumber = 0 # This variable tracks the value after subtracting primes in each iteration

        # Iterate through each number in the input list `nums`
        for n in nums:
            # Calculate the upper bound for the prime subtraction operation
            # This is the maximum value we can subtract from n to not violate the condition
            upperBound = n - previousNumber

            largestPrime = 0 # Variable to store the largest prime we can subtract
            
            # Loop through possible prime candidates starting from just below `upperBound`
            # `reversed(range(2, upperBound))` goes from `upperBound-1` down to 2
            for i in reversed(range(2, upperBound)):
                if isPrime(i): # Check if i is prime
                    largestPrime = i # If prime, set it as the largest prime we can use
                    break # Found the largest prime, exit the loop
              
            # If the prime subtraction results in a value that is less than or equal to the previous number
            # we return False because we are violating the condition
            if n - largestPrime <= previousNumber:
                return False
            
            # Update previousNumber to be the new number after the prime subtraction
            previousNumber = n - largestPrime

        # If we successfully process all the numbers without returning False, return True
        return True
