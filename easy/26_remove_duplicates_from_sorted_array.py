######
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#   
# Example
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and
# 2 respectively.
# It doesn't matter what you leave beyond the returned length.
# Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # iは重複していない要素のインデックスを指す
        i = 0

        # まずjを使って配列を走査する
        for j in range(1, len(nums)):
            # 今jで見ている要素がiに入っている要素と違う場合はiをインクリメントしてiにjの要素を入れる
            # もしjとiが同じ要素を指している場合はiはインクリメントされず、jはインクリメントされる
            if nums[j] != nums[i]
                i += 1 # iの書き込む先を一個ずらす
                nums[i] = nums[j] # iの書き込む先にjを入れる

        return i + 1 # iは0から始まるので+1すると今求めたい配列の長さになる
