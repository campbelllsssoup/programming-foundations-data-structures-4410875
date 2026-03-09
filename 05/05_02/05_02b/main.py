from collections import deque
# queue
# queue has a beginning and end
# insert elements at the end of the queue; remove them from the beginning
# follow a FIFO (first element in the queue will be the first one out)
# "like a line at a store"
# queue#enqueue
# queue#dequeue
# queue#peek - see the first element in the queue

# deque (double ended queue)
# excels at insertion and deletion at both ends
# deque#append (add elements to the beginning of the queue)
# deque#popleft (remove elements from the front of the deque)

printer_queue = deque()
printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketNotes.docx")
printer_queue.append("Proof.png")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f'Printing {document}')