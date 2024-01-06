Using HashMap:

Time Complexity O(N)

dont ask about space complexity :P

In the array we have to find target number which should be sum of two elements from the array

for this using a dictionary where we can save visited values

start from the array

[11, 15, 2, 8, 10, 7] and target is 9
answer should be [2, 5]

will use a difference of the target and values that are iterated.

difference = target - n(in for loop first variable will iterate with incremental values and next variable will enumeratethrough array)

if the difference is found in hashmap then it'll return the hasmap[difference], i

