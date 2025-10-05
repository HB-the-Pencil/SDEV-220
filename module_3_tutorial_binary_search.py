# My best attempt at a binary search algorithm (on my own) using recursion. I'm not good at recursive functions.
# Also, what does this have to do with functional vs. object-oriented programming?
class Solution:
    def binarysearch(self, arr, k):
        index = len(arr) // 2
        
        if arr[index] == k:
            return index
        elif arr[index] > k:
            return self.binarysearch(arr[:index], k)
        elif arr[index] < k:
            return self.binarysearch(arr[index:], k) + index
        elif index == 0 and arr[index] != k:
            return -1

# Note that this does not work.

# Following the editorial, I got this and annotated every line:
class Solution:
    def binarysearch(self, arr, k):
        # Base index of the list.
        low_i = 0
        # Max index of the list (subtract 1).
        high_i = len(arr) - 1
        
        # Wasn't sure if a while loop would be efficient. I guess recursion is no better.
        while low_i <= high_i:
            
            # The middle is equal to the lowest index plus half of the total range.
            mid = low_i + (high_i - low_i) // 2
            
            # If the item is at the middle index, we can stop searching.
            if arr[mid] == k:
                return mid
            # Else if the middle item is less than x, look at the right side.
            elif arr[mid] < k:
                # Add one so that you don't repeat the middle value.
                low_i = mid + 1
            # Else if the middle item is greater than x, look at the left side.
            elif arr[mid] > k:
                # Subtract one because of zero indexing.
                high_i = mid - 1
            # If it reaches this else clause the user has bent the laws of spacetime.
            else:
                return 3.14159265
        
        # If it goes through the ENTIRE while loop, checking every index until
        # the slice is flat, then the item must not be there.
        return -1

# However, this STILL doesn't work because it does not return the *first* index of a number
# in a list. It only returns the first time it matches.

# Finally, I came up with this, increasing the time slightly:
class Solution:
    def binarysearch(self, arr, k):
        # Base index of the list.
        low_i = 0
        # Max index of the list (subtract 1).
        high_i = len(arr) - 1
        
        # Wasn't sure if a while loop would be efficient. I guess recursion is no better.
        while low_i <= high_i:
            
            # The middle is equal to the lowest index plus half of the total range.
            mid = low_i + (high_i - low_i) // 2
            
            # If the item is at the middle index, we can stop searching.
            if arr[mid] == k:
                #         vvv NEW CODE HERE vvv
                
                # Check if this is the first instance of the item.
                while arr[mid-1] == k:
                    mid -= 1
                
                #         ^^^ NEW CODE HERE ^^^
                return mid
            # Else if the middle item is less than x, look at the right side.
            elif arr[mid] < k:
                # Add one so that you don't repeat the middle value.
                low_i = mid + 1
            # Else if the middle item is greater than x, look at the left side.
            elif arr[mid] > k:
                # Subtract one because of zero indexing.
                high_i = mid - 1
            # If it reaches this else clause the user has bent the laws of spacetime.
            else:
                return 3.14159265
        
        # If it goes through the ENTIRE while loop, checking every index until
        # the slice is flat, then the item must not be there.
        return -1
