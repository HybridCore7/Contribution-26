# Greedy Interval Scheduling
#=====================================

## Problem Statement

Given a set of intervals, select the maximum number of non-overlapping intervals.

## Algorithm

The greedy algorithm works by sorting the intervals by their end time and then selecting the intervals one by one. If the current interval does not overlap with the previously selected interval, we select it.

## Code

```python
def greedy_interval_scheduling(intervals):
    # Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the list of selected intervals
    selected_intervals = []

    # Iterate over the sorted intervals
    for interval in intervals:
        # Check if the current interval does not overlap with the previously selected interval
        if not selected_intervals or interval[0] >= selected_intervals[-1][1]:
            # Select the current interval
            selected_intervals.append(interval)

    return selected_intervals

# Example usage
intervals = [(1, 3), (2, 4), (3, 5), (6, 8), (7, 9)]
selected_intervals = greedy_interval_scheduling(intervals)
print("Selected Intervals:", selected_intervals)
print("Number of Selected Intervals:", len(selected_intervals))
```

## Explanation

1.  The `greedy_interval_scheduling` function takes a list of intervals as input, where each interval is represented as a tuple of `(start, end)`.
2.  The function sorts the intervals by their end time using the `sort` method and a lambda function as the key.
3.  It initializes an empty list `selected_intervals` to store the selected intervals.
4.  The function then iterates over the sorted intervals.
5.  For each interval, it checks if the current interval does not overlap with the previously selected interval by comparing the start time of the current interval with the end time of the last selected interval.
6.  If the current interval does not overlap, it is selected and added to the `selected_intervals` list.
7.  Finally, the function returns the list of selected intervals and prints the number of selected intervals.

## Output

```
Selected Intervals: [(1, 3), (3, 5), (6, 8)]
Number of Selected Intervals: 3