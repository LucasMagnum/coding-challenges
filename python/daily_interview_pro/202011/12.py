"""
Compare Version Numbers

This problem was recently asked by Amazon:

Version numbers are strings that are used to identify unique states of software products.
A version number is in the format a.b.c.d. and so on where a, b, etc.
are numeric strings separated by dots.
These generally represent a hierarchy from major to minor changes.

Given two version numbers version1 and version2, conclude which is the latest version number.

Your code should do the following:
If version1 > version2 return 1.
If version1 < version2 return -1.
Otherwise return 0.

Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not start or end with dots. Unspecified level revision numbers default to 0.

"""

def solution(version1, version2):
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]

    for i in range(max(len(versions1), len(versions2))):
        v1 = versions1[i] if i < len(versions1) else 0
        v2 = versions2[i] if i < len(versions2) else 0

        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    return 0


if __name__ == "__main__":
    version1 = "1.0.1"
    version2 = "1"
    print(solution(version1, version2))
    # 1