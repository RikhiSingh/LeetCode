// Link: https://leetcode.com/problems/excel-sheet-column-title/description/

public class Solution {
    public string ConvertToTitle(int columnNumber) {
        // Create a StringBuilder to build the resulting column title string
        StringBuilder sb = new StringBuilder();
        
        // Loop until the column number is greater than 0
        while (columnNumber > 0) {
            // Decrement the column number by 1 to make it 0-based
            columnNumber--;
            
            // Calculate the remainder (modValue) when columnNumber is divided by 26
            int modValue = columnNumber % 26;
            
            // Convert the remainder to a character ('A' + modValue gives the corresponding letter)
            char ch = (char)('A' + modValue);
            
            // Insert the character at the beginning of the StringBuilder
            sb.Insert(0, ch);
            
            // Divide the column number by 26 to continue the conversion process for the next digit
            columnNumber /= 26;
        }
        
        // Convert the StringBuilder to a string and return it
        return sb.ToString();
    }
}