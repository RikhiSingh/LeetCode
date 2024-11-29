def finddigitIndex(target):
    initial = 1
    index = 0
    
    while True:
        num_str = str(initial) # Convert the current number to a string
        num_len = len(num_str) # Get the number of digits in the current number
        
        # Check if the target index x is within the range of digits for this number
        if index + num_len > target:
            # If so, return the specific digit in the current number
            return num_str[target - index]
        
        else:
            # Otherwise, move to the next number and update the index
            index += num_len
            initial += 1

print(finddigitIndex(100))