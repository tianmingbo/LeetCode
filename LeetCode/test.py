class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.search([6, 7, 0, 1, 2, 4, 5], 5))
