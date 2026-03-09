from collections import deque

def check_matching_parentheses(s):
    stack = deque()
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))

# great for programs where we must keep track of state
# appending, peeking, and popping take constant time O(1)
# indexing, and searching are not ideal - involves removing many elements
# use for LIFO tasks

# useful for reversing a list
