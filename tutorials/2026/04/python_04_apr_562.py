# Greedy Interval Scheduling Algorithm

def is_overlapping(intervals1, intervals2):
    # Check if any of the events in intervals1 overlap with the events in intervals2
    for i in range(len(intervals1)):
        start_time1 = intervals1[i][0]
        end_time1 = intervals1[i][1]

        for j in range(len(intervals2)):
            start_time2 = intervals2[j][0]
            end_time2 = intervals2[j][1]

            if (start_time1 < end_time2 and start_time2 < end_time1):
                return True

    return False


def greedy_interval_scheduling(intervals):
    # Sort the events by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize a list to store the result
    result = []

    # Iterate through the sorted events
    for i in range(len(intervals)):
        start_time = intervals[i][0]
        end_time = intervals[i][1]

        # Check if there is an overlap with the last event in the result
        if not result or (start_time >= result[-1][1]):
            result.append([start_time, end_time])

    return result


# Example usage:
intervals = [(1, 3), (2, 4), (5, 7), (6, 8), (9, 11)]
print(greedy_interval_scheduling(intervals))