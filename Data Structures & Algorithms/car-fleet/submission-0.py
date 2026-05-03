from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and time to reach target
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        
        # Sort by position (closest to target first)
        cars.sort(reverse=True)
        
        fleets = 0
        max_time = 0
        
        for pos, time in cars:
            # If this car takes longer than current fleet → new fleet
            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets