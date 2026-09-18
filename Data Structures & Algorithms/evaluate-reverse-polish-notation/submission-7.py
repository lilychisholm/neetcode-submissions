class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                int1 = stack.pop()
                int2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(int1 + int2)
                elif tokens[i] == "-":
                    stack.append(int2 - int1)
                elif tokens[i] == "*":
                    stack.append(int1 * int2)
                else:
                    stack.append(int(float(int2) / int1))

        final = stack.pop()
        return final

        