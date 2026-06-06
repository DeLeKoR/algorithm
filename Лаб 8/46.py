class Solution:
    def permute(self, nums):
        result = []
        current = []
        used = set()

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num in used:
                    continue

                current.append(num)
                used.add(num)

                backtrack()

                current.pop()
                used.remove(num)

        backtrack()

        return result