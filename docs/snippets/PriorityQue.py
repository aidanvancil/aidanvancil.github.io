import heapq

# Creating an empty priority queue
priority_queue = []

# Adding elements to the priority queue
heapq.heappush(priority_queue, 5)
heapq.heappush(priority_queue, 3)
heapq.heappush(priority_queue, 8)
heapq.heappush(priority_queue, 2)

# Removing and returning the smallest element from the priority queue
smallest = heapq.heappop(priority_queue)
print(smallest)  # Output: 2

# Retrieving the smallest element from the priority queue without removing it
smallest = priority_queue[0]
print(smallest)  # Output: 3

# Converting a list to a heap (in-place transformation)
my_list = [9, 1, 6, 4, 3]
heapq.heapify(my_list)
print(my_list)  # Output: [1, 3, 6, 4, 9]

# Combining multiple heaps into a single heap
heap1 = [1, 3, 5]
heap2 = [2, 4, 6]
merged_heap = heapq.merge(heap1, heap2)
print(list(merged_heap))  # Output: [1, 2, 3, 4, 5, 6]

# Finding the n smallest elements from a list
my_list = [9, 1, 6, 4, 3]
smallest_elements = heapq.nsmallest(3, my_list)
print(smallest_elements)  # Output: [1, 3, 4]

# Finding the n largest elements from a list
my_list = [9, 1, 6, 4, 3]
largest_elements = heapq.nlargest(2, my_list)
print(largest_elements)  # Output: [9, 6]
