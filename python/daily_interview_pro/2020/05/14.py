"""
This problem was recently asked by Microsoft:

An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']

"""


def solution(s, ip_parts=None):
    if ip_parts is None:
        ip_parts = []

    if len(ip_parts) == 4:
        if s:
            return []
        else:
            return [".".join(ip_parts)]

    if not s:
        return []

    result = []
    if len(s) > 2 and 100 <= int(s[:3]) <= 255:
        result += solution(s[3:], ip_parts + [s[:3]])
    if len(s) > 1 and 10 <= int(s[:2]) <= 99:
        result += solution(s[2:], ip_parts + [s[:2]])

    result += solution(s[1:], ip_parts + [s[:1]])
    return result


if __name__ == "__main__":
    assert solution("0000") == ["0.0.0.0"]
    print(solution("1592551013"))
    assert solution("1592551013") == ["159.255.101.3", "159.255.10.13"]
