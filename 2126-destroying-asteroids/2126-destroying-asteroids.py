class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # [3,5,9,19,21]
        # 10+3+9+19
        asteroids.sort()
        n=len(asteroids)
        for i in range(n):
            if mass>=asteroids[i]:
                mass+=asteroids[i]
            else:
                return False
        return True