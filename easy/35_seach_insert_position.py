############################################################
# 35. Search Insert Position
# O(log n)なので二分探索を使用する
############################################################
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        # leftとrightは実際の数値ではなくインデックスを指している

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        
        return left