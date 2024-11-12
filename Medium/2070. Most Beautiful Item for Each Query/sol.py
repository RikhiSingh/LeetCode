import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Sort the 'items' list based on the price (first element of each pair)
        items.sort()
        # print(items)
        
        beautyMax = 0  # This will store the maximum beauty encountered so far
        result = []    # This will store the final results for each query
        dictionary = dict()  # This will store the maximum beauty for each price


        # Step 2: Loop through sorted items and track the maximum beauty for each price
        for price, beauty in items:
            # Update the beautyMax if the current beauty is greater
            beautyMax = max(beauty, beautyMax)
            # print(beautyMax)
            # Map the price to the maximum beauty encountered up to that price
            dictionary[price] = beautyMax
        # print(dictionary)
        
        
        # Step 3: Sort the keys (prices) in the dictionary to facilitate binary search
        keys = sorted(dictionary.keys())
        
        # Step 4: Process each query and find the corresponding maximum beauty
        for q in queries:
            # Use binary search to find the index of the first price greater than or equal to the query price
            index = bisect.bisect_left(keys, q)
            
            # If the query price exists exactly in the list of prices, return the corresponding beauty
            if index < len(keys) and keys[index] == q:
                result.append(dictionary[q])
            # If the query price is smaller than all available prices, return 0
            elif index == 0:
                result.append(0)
            # If the query price is not found, return the maximum beauty for the largest price less than the query
            else:
                result.append(dictionary[keys[index-1]])
                
        return result


# Test case
solution = Solution()
word1 = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]  # List of [price, beauty]
word2 = [1, 2, 3, 4, 5, 6]  # List of query prices
print(solution.maximumBeauty(word1, word2))  # Should print the results for each query
