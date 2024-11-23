using System;

class Program
{
    static void Main()
    {
        int[] originalArray = { 10, 20, 30, 40, 50, 60 };  // Example array
        int i = 0;  // Starting index
        int k = 3;  // Ending index (exclusive)

        // Loop until k reaches the length of the array
        while (k <= originalArray.Length)
        {
            // Calculate the length of the new array based on i and k
            int length = k - i;

            // Create a new array to hold the elements from i to k
            int[] newArray = new int[length];

            // Populate the new array with elements from original array
            for (int index = 0; index < length; index++)
            {
                newArray[index] = originalArray[i + index];
            }

            // Print the new array
            Console.WriteLine("New Array:");
            foreach (var item in newArray)
            {
                Console.WriteLine(item);
            }

            // Increment both i and k for the next iteration
            i++;
            k++;
        }
    }
}
