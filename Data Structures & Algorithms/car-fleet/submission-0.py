class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for position, speed in sorted(zip(position, speed), reverse=True):
            time = (target - position) / speed
            times.append(time)

        stack = []
        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        