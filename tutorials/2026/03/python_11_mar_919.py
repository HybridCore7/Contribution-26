# Greedy Interval Scheduling
#================================

# A greedy algorithm for scheduling intervals. This algorithm sorts the intervals by their end time
# and then schedules them one by one. If the current interval does not overlap with the last scheduled
# interval, it is scheduled.

def greedy_interval_scheduling(intervals):
    # Sort the intervals by their end time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the list to store the scheduled intervals
    scheduled_intervals = []
    
    # Iterate through the sorted intervals
    for interval in intervals:
        # If the current interval does not overlap with the last scheduled interval, schedule it
        if not scheduled_intervals or interval[0] >= scheduled_intervals[-1][1]:
            scheduled_intervals.append(interval)
    
    return scheduled_intervals

# Example usage
intervals = [(1, 3), (2, 4), (3, 5), (6, 8), (7, 9), (8, 10)]
scheduled_intervals = greedy_interval_scheduling(intervals)

# Print the scheduled intervals
for i, interval in enumerate(scheduled_intervals):
    print(f"Interval {i+1}: {interval[0]} - {interval[1]}")