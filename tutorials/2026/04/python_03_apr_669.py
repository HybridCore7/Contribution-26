# Heap Operations in Python

import heapq

def create_heap(data):
    # Convert the list into a min-heap using heapq.heapify()
    return [-x for x in data]
    
def heap_insert(heap, value):
    # Insert an element into the heap
    return -heapq.heappush(-heap, -value)

def heap_extract(heap):
    # Remove and return the smallest element from the heap
    if len(heap) == 0:
        raise Exception("Heap is empty")
    return -heapq.heappop(heap)

def heapify(data):
    # Convert an array into a min-heap using recursion
    def _heapify(i, data):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i
        if len(data) > left_child and data[left_child] < data[smallest]:
            smallest = left_child
        if len(data) > right_child and data[right_child] < data[smallest]:
            smallest = right_child
        if smallest != i:
            # Swap elements at indices i and smallest
            data[i], data[smallest] = data[smallest], data[i]
            _heapify(smallest, data)
    for i in range(len(data) // 2 - 1, -1, -1):
        _heapify(i, data)
    
def heap_sort(data):
    # Convert the array into a min-heap and then extract elements
    heap = create_heap(data)
    sorted_data = []
    while len(heap) > 0:
        sorted_data.append(heap_extract(heap))
    return sorted_data

# Example usage:
data = [12, 11, 13, 5, 6, 7]
print("Original Data:", data)

heap_data = heapify(data)
print("Heap Data:", heap_data)

inserted_value = heap_insert(heap_data, 10)
print("Insertion Result:", inserted_value)

extracted_value = heap_extract(heap_data)
print("Extraction Result:", extracted_value)

sorted_data = heap_sort(data)
print("Sorted Data:", sorted_data)