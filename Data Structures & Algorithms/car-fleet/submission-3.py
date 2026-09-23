class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i], (target-position[i])/speed[i]])
        
        cars.sort(key=lambda x: x[0])
        
        stack = [cars.pop()]
        fleets = 1



        while cars != []:
            new_car = cars.pop()
            if new_car[2] > stack[-1][2]:
                fleets += 1
                stack.append(new_car)
            
        return fleets
            


        