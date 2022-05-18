class Solution:
    def squareAll(self, nums: List[int]) -> None:
        for i, num in enumerate(nums):
            nums[i] = num * num
    # return lhs^2 > rhs^2
    def cmp_sqr(self, lhs, rhs):
        return lhs*lhs > rhs*rhs
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # edge cases
        # only  negative
        # only positive
        # empty list

        # general case : negative and positive

        # initial approach -> square all numbers then sort
        # alternative 1: bucket sort with magnitudes
        # alternative 2: two pointers, one to negative numbers and one to positive
        # merge the negative list with the positive list ignoring the sign
        # implement alternative 2

        # start both pointers at lowest magnitude positive and negative values
        # compare the values at both pointers, and move into new array as needed
        #

        if not nums:
            return nums
        len_nums = len(nums)
        n_ptr = None
        p_ptr = None

        for i, x in enumerate(nums):
            if x < 0:
                n_ptr = i
            else:
                p_ptr = i
                break

        new_nums = [0 for num in nums]
        nums_ptr = 0

        if n_ptr is None:
            self.squareAll(nums)
            return nums
        if p_ptr is None:
            nums.reverse()
            self.squareAll(nums)
            return nums


        while n_ptr >= 0 or p_ptr < len_nums:
            if p_ptr >= len_nums:
                new_nums[nums_ptr] = nums[n_ptr]
                nums_ptr += 1
                n_ptr -= 1
            elif n_ptr < 0:
                new_nums[nums_ptr] = nums[p_ptr]
                nums_ptr += 1
                p_ptr += 1

            elif self.cmp_sqr(nums[n_ptr], nums[p_ptr]):
                new_nums[nums_ptr] = nums[p_ptr]
                nums_ptr += 1
                p_ptr += 1
            else:
                new_nums[nums_ptr] = nums[n_ptr]
                nums_ptr += 1
                n_ptr -= 1

        self.squareAll(new_nums)
        print(new_nums)
        return new_nums

# extension:

# how to do in-place and in one pass?
