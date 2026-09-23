class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i], (target-position[i])/speed[i]])
        
        cars.sort(key=lambda x: x[0])
        
        prev = cars.pop()
        fleets = 1

        while cars != []:
            new_car = cars.pop()
            if new_car[2] > prev[2]:
                fleets += 1
                prev = new_car
            
        return fleets
            


        