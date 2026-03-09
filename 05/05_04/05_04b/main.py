from collections import deque
# take a number n as input (n=5)
# print out the first n binary numbers (1,2,3,4,5)
# if the input is less than or equal to 0, print nothing

def print_binary_numbers(n):
    if n <= 0:
        return []
    
    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)

print_binary_numbers(5)

# best performance when you use queues for FIFO functions
# used for task or event processing (sequential processing)
# don't use a queue if you find yourself pulling from the middle consistently