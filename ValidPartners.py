class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif c in [")", "]", "}"]:
                if not stack:
                    return False
                last = stack.pop()
                if (
                    (c == ")" and last != "(")
                    or (c == "]" and last != "[")
                    or (c == "}" and last != "{")
                ):
                    return False

        if stack:
            return False
        else:
            return True


test_case = ["()", "()[]{}", "{]", "([)]", "{[()]}", "[", "[[[]", "(([]{})"]
for test in test_case:
    print(Solution().isValid(test))
    # Solution().longestCommonPrefix(test)
