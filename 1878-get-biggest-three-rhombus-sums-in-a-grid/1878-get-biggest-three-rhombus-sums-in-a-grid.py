class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # def getBiggestThree(grid):
        m = len(grid)
        n = len(grid[0])
        st = set()

        def addToSet(val):
            st.add(val)
            if len(st) > 3:
                st.remove(min(st))

        for r in range(m):
            for c in range(n):

                # every cell is valid for rhombus of side = 0
                addToSet(grid[r][c])

                side = 1
                while r - side >= 0 and r + side < m and c - side >= 0 and c + side < n:
                    total = 0

                    for k in range(side):
                        total += grid[r - side + k][c + k]     # top -> right
                        total += grid[r + k][c + side - k]     # right -> bottom
                        total += grid[r + side - k][c - k]     # bottom -> left
                        total += grid[r - k][c - side + k]     # left -> top

                    addToSet(total)
                    side += 1

        return sorted(st, reverse=True)    
            