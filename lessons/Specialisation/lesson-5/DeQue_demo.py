# --- Real-life Scenario ---
# Imagine you are managing a ticket queue for a theme park. Customers can join the queue either at
# the front (VIP customers) or at the back (regular customers).
# Additionally, customers can be served from the front
# of the queue. This scenario is perfect for demonstrating the use of deque.
#
# Example
# Let's create an example where we use deque to manage the ticket queue for a theme park.

from collections import deque

ticket_queue = deque()

ticket_queue.append('Customer 1')
ticket_queue.append('Customer 2')

ticket_queue.appendleft('VIP customer 1')
ticket_queue.appendleft('VIP customer 2')

print("Current queue: ", list(ticket_queue))

served_customer = ticket_queue.popleft()
print(served_customer)
print("Current queue: ", list(ticket_queue))
served_customer = ticket_queue.pop()
print(served_customer)
print("Current queue: ", list(ticket_queue))

