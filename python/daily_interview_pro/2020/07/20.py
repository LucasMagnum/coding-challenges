"""
Number of Meeting Rooms

This problem was recently asked by Facebook:

Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all meetings.

Each meeting will be represented by a tuple of (start_time, end_time),
where both start_time and end_time will be represented by an integer to indicate the time.
start_time will be inclusive, and end_time will be exclusive, meaning a meeting of (0, 10) and (10, 20)
will only require 1 meeting room.

"""
import heapq


def meeting_rooms(meetings):
    meetings.sort()

    max_rooms = 0
    meeting_end = []

    for meeting in meetings:
        # pop all meetings that end before the current meeting starts
        while meeting_end and meeting_end[0] <= meeting[0]:
            heapq.heappop(meeting_end)

        heapq.heappush(meeting_end, meeting[1])

        max_rooms = max(max_rooms, len(meeting_end))

    return max_rooms


if __name__ == "__main__":
    # print 1
    print(meeting_rooms([(0, 10), (10, 20)]))
    # 1

    print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
    # 3 (all meetings overlap at time 20)