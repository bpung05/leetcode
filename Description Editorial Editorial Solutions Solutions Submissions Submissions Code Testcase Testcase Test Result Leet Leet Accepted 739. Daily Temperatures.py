class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while len(stack) !=0 and (temperatures[i] > temperatures[stack[-1]]):
                day_temp_index = stack.pop()
                diff = i - day_temp_index
                result[day_temp_index] = diff
            
            stack.append(i)


        while len(stack) !=0 :
            index = stack.pop()
            result[index] = 0

        return result
