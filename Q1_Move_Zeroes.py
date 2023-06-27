"""Q1) Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1"""

Solution:
def moveZeroes(nums):
    """
    Moves all zeros to the end of the input list while maintaining the order of non-zero elements.
    """
    left = 0  # pointer to track the position of the next non-zero element

    # Traverse the list and move non-zero elements to the left side
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1

    # Fill the remaining positions with zeros
    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums


input_str = input("Enter the array elements separated by spaces: ")
nums1 = list(map(int, input_str.split()))
print(moveZeroes(nums1)) 
