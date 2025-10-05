# This is my code. It works perfectly. But for some reason, the website won't accept my answer.
# I have tried printing it, reassigning arr, returning it, and a combination of the three. Nothing works.
class Solution:
    def sort012(self, arr):
        # No built-in sort function, eh?
        # Didn't say anything about count...
        zeroes, ones, twos = arr.count(0), arr.count(1), arr.count(2)
        arr = [0] * zeroes + [1] * ones + [2] * twos
        return arr

# My code is perfectly correct, but it won't accept it. I give up trying and am going to use the editorial.

# This site is stupid. For whatever reason, it wanted the EXACT address in memory (presumably), so when I tried:
class Solution:
    def sort012(self, arr):
        # No built-in sort function, eh?
        # Didn't say anything about count...
        zeroes, ones, twos = arr.count(0), arr.count(1), arr.count(2)
        arr[:] = [0] * zeroes + [1] * ones + [2] * twos # note the full-list slice

# it worked fine. At the cost of my points. The editorial told me nothing.
