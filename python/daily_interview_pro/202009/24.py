"""
Generate All IP Addresses

This problem was recently asked by Microsoft:

An IP Address is in the format of A.B.C.D, where A, B, C, D
are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can
make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
    Input: 1592551013
    Output: ['159.255.101.3', '159.255.10.13']
"""


def ip_addresses(string, ip_parts=[]):
    if len(ip_parts) == 4:
        if string:
            return []
        else:
            return [".".join(ip_parts)]

    if not string:
        return []

    result = []
    if len(string) > 2 and 100 <= int(string[:3]) <= 255:
        result += ip_addresses(string[3:], ip_parts + [string[:3]])

    if len(string) > 1 and 10 <= int(string[:2]) <= 99:
        result += ip_addresses(string[2:], ip_parts + [string[:2]])

    result += ip_addresses(string[1:], ip_parts + [string[:1]])
    return result


if __name__ == "__main__":
    print(ip_addresses('1592551013'))
    # ['159.255.101.3', '159.255.10.13']
