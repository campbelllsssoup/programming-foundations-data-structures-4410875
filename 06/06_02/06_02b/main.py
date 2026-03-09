# stacks
# ordered series of objects that pushes objects onto the stack
# and pops objects off of the stack
# best for LIFO (last in first out tasks)
# think, call stack used when calling functions (must use other functions
# and the order is managed by using a stack)

# stack#push add an element to the stack
# stack#pop remove an element from the stack
# (think of a stack like a deck of cards that only allows you to access
# the top of the deck)

# you cannot access anything but the top element, and you can only
# use the methods pop and push to remove or add elements to a stack

# stack - ordered list with a specific way of adding and removing items
# we can use a list that acts as a stack to implement a stack

card_stack = []

card_stack.append("Jack of Hearts")
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")

# front(bottom) ---- back(top)
# only use push and pop!!
# last item is the most recent item in the stack
# first item is the first item added to the stack

top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)

# card_stack.pop()
# card_stack.pop()
if not card_stack:
    print("Card stack is empty")
else:
    print(len(card_stack))