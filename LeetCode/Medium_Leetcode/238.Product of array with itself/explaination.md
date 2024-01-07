In this problem, we have to do the product of the numbers without including the i element, and save them in the answer[i].

we will be using hashmap, in this we will be using prefix and postfix method to find the answer array.

first the result array will be filled with 1 with length of nums array.

To solve this problem we will multiply both prefix and postfix, where prefix will multiply from the left to right while the first number will always remain 1. then with respect to that further operations done, for postfix it will start with from the reverse which will iterate through the nums array, as intial starting number will be 1 but there won't be any extra bound to save, so it will multiply with the answer array from prefix.


then prefix is assigned to 1 which is starting number, first prefix value will be saved in the first value of answer array, then prefix will update by multiplying the nums[i].

same will be going with postfix but the nums array will be iterated over backwards, as the first prefix values are stored in the answer array we will be multiplying the postfix number with that array index number, then postfix is multiplied by nums[i].