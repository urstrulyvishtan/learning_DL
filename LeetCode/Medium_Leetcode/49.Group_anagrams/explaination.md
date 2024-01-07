In the group anagrams we will be using hashmaps for better complexity.

we will be using the ord function to convert strings to ASCII values in order to compare.

First we will use counter variable which has [0] in a array multiplied by 26 times because every time different strings have to check with others.

for the character the counter will increase by 1 with respect to the difference of character's ASCII and ASCII of "a".

then with respect to the counter value that is increased the string will be then saved to the hashmap on the counter value.

by making this all the strings will be groupped and returned all the dictionary values.
