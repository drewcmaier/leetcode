class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif len(stack) > 0:
                top = stack[-1]
                if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0



solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("]"))
print(solution.isValid("(])"))
