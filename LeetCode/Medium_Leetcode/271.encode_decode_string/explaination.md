This problem passes string that has to be encoded and decoded by our own means. The encoding is to combine the strings together and decode to seperate them.

so for encoding we should assign a rule to act as a seperating identifier say in this case #/ but before that we should know how many characters are there in that string so we will add the length of that string infront of #/.

Decoding will be finding the number followed by #/ then the number of times the loop will iterate to retrive the string.

In encoding the result is saved as string and returned.

In Decoding the result will be saved in a list, then while iterating by the length of encoded string. Then one copy is saved to other variable i.e j = i where until the string of Jth position is #/ it will iterate through. once it is found then the length of the J will be saved from i(still it is not updated.). Finally will append the string value to the result. Finally i will be updated by adding 2 positions and the length as the string is found and appended.

Time Complexity is O(n).