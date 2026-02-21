import heapq

def schedule_intervals(intervals):
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    # Create a priority queue to store the intervals
    pq = []
    for start, end in intervals:
        # Push the interval into the priority queue
        heapq.heappush(pq, (start, end))

    # Create a list to store the scheduled intervals
    scheduled_intervals = []

    while pq:
        # Get the interval with the earliest end time
        start, end = heapq.heappop(pq)

        # Check if the interval conflicts with the previously scheduled interval
        if scheduled_intervals and start < scheduled_intervals[-1][1]:
            continue

        # Add the interval to the scheduled intervals
        scheduled_intervals.append((start, end))

    return scheduled_intervals

# Example usage
intervals = [(1, 3), (2, 4), (3, 5), (6, 8)]
scheduled_intervals = schedule_intervals(intervals)
print("Scheduled Intervals:", scheduled_intervals)