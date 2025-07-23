class Solution:
    def dutch_sort(self, nums: list[int]):
        if not nums:
            return None

        end = len(nums) - 1
        start = 0
        index = 0

        while start < end and index <= end:
            if nums[index] == 0:
                if index < start:
                    index += 1
                    continue
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                continue
            if nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
                continue

            index += 1

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

print(test9)
print(solution.dutch_sort(test9))