class Solution:
    def shuffle(self, arr: List[int], n: int) -> List[int]:
        # n = len(arr) // 2
        M = max(arr) + 1  # M should be larger than any number in arr

        # Step 1: Encode both old and new values at each index
        for i in range(2*n):
            # Determine from where the new value should come
            if i % 2 == 0:
                new_val = arr[i // 2]
            else:
                new_val = arr[n + i // 2]
            arr[i] += (new_val % M) * M

        # Step 2: Decode the new values
        for i in range(2*n):
            arr[i] = arr[i] // M
        return arr
