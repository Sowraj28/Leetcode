class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        a = len(arr)
        i = 0
        while i < a - 1:
            if arr[i] == 0:
                for j in range(a - 1, i, -1):
                    arr[j] = arr[j - 1]
                arr[i + 1] = 0
                i += 1
            i += 1
