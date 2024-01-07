We will be finding duplicates in the given list

if one duplicate number is found then the function should return True

Sorting:
Time Complexity O(nlogn)
Space Complexity O(1)

first we will sort the array and check if nearby number is same or not so that we don't have to iterate the loop completely

HashSet:
Time Complexity O(n)
Space Complexity O(n)

we will check the len(nums) != len(set(nums))

In simple terms every visited element will be saved by the set and compared whether the element exist.
