class Solution:
    def trap(self, height: List[int]) -> int:
        down = -1
        up = -1
        i = 0
        sets = []
        temp = []
        total = 0
        while i < len(height):
            try:
                print(height[i])
                if i == len(height) - 1:
                    if down != -1 and (height[i] >= height[down] or height[i] > height[i -1]):
                        temp.append(height[i])
                        sets.append(temp)
                        temp = []
                        i += 1
                    else:
                        break
                elif height[i + 1] < height[i] and down == -1:
                    print(height[i], "1st")
                    down = i
                    temp.append(height[i])
                    i += 1
                elif down != -1 and height[i] >= height[down]:
                    print(height[i], "2nd")
                    down = -1
                    temp.append(height[i])
                    sets.append(temp)
                    temp = []
                elif down != -1:
                    print(height[i], "3rd")
                    temp.append(height[i])
                    i += 1
                else:
                    print(height[i], "4th")
                    i+=1
                
            except:
                break
        if temp != []:
            sets.append(temp)

        print(sets)
        for group in sets:
            for i in range(len(group)):
                if i == 0 or i == len(group)-1:
                    continue
                elif min(group[0], group[len(group)-1]) - group[i] >= 0:
                    total += min(group[0], group[len(group)-1]) - group[i]
        return total

            



                    
                

