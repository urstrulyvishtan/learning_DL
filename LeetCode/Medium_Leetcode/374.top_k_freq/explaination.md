In this probelm we will be finding the top k frequent values in the array.

we will be using hashmap to save the frequencies. Time complexity will be O(n)

Using hashmap to get count of each element.

for this problem we will doing it in reverse in the hashmap we will be having the length of array, and will save the values corresponding to how many times they occurred.

for top K elements 
we will use the hashmap counting from reverse.

we will append the first occuring K elements to a new array and return.