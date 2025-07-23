class Solution:
    def dutch_sort(self, nums: list[int]):

        start = 0
        current = 0
        mid = 1
        end = len(nums) - 1

        while current <= end:
            if nums[current] < mid:
                nums[start], nums[current] = nums[current], nums[start]
                start += 1
                current += 1
            elif nums[current] > mid:
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
            else:
                current += 1

        return nums


solution = Solution()

test1 = [2,0,1,0,0,2,2,1,1,2,1,0]
test2 = [2, 0, 2, 1, 1, 0]
test3 = [2, 0, 1]
test4 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
test5 = [2, 2, 2, 1, 1, 1, 0, 0, 0]
test6 = [1, 1, 1, 1, 1]
test7 = [0, 0, 0, 0]
test8 = [2, 2, 2, 2]
test9 = [1, 0, 2, 1, 0, 2, 1, 0, 2]
test10 = [2, 1, 0]
test11 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
test12 = [0,0,0,2,2,2,1,1,1,1]

print(test1)
print(solution.dutch_sort(test1))