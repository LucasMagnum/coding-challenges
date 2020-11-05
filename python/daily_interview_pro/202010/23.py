"""
Number of Meeting Rooms

his problem was recently asked by Facebook:

Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all meetings.

Each meeting will be represented by a tuple of (start_time, end_time),
where both start_time and end_time will be represented by an integer to indicate the time.
start_time will be inclusive, and end_time will be exclusive, meaning a meeting of (0, 10)
and (10, 20) will only require 1 meeting room.
"""


def meeting_rooms(meetings):
    if not meetings:
        return 0

    used_rooms = 0

    starts = sorted([m[0] for m in meetings])
    ends = sorted([m[1] for m in meetings])

    start_index = end_index = 0

    while start_index < len(meetings):
        if starts[start_index] >= ends[end_index]:
            used_rooms -= 1
            end_index += 1

        used_rooms += 1
        start_index += 1

    return used_rooms


if __name__ == "__main__":
    print(meeting_rooms([(0, 10), (10, 20)]))
    # 1

    print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
    # 3 (all meetings overlap at time 20)