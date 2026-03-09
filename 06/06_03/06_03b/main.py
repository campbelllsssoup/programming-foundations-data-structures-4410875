from collections import deque
# you can use a deque to implement a stack data structure

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")

print(history_stack[-1]) # peek at what element is on the top of the stack
print(history_stack.pop()) # pop the item off of the stack