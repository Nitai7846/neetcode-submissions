class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)
            elif i == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif i == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            elif i == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(i))
        return stack[0]

            


