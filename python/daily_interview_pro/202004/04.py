"""
Angles of a Clock

This problem was recently asked by Microsoft:

Given a time in the format of hour and minute,
calculate the angle of the hour and minute hand on a clock.

"""

def solution(hour, minutes):
    if hour < 0 or minutes < 0 or hour > 12 or minutes > 60:
        print("Wrong input")

    if hour == 12:
        hour = 0
    
    if minutes == 60:
        minutes = 0

    hour_angle = (360 / (12 * 60)) * (hour * 60 + minutes)
    minutes_angle = (360 / 60) * minutes

    angle = abs(hour_angle - minutes_angle)
    return min(360 - angle, angle)


if __name__ == "__main__":
    print(solution(3, 30))
    print(solution(12, 30))