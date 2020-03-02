"""
Course Prerequisites

This problem was recently asked by Google:

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']

"""
from collections import defaultdict


def solution(courses):
    # Transform list in a set to make it faster
    # to compare items inside it
    courses = {c: set(p) for c, p in courses.items()}

    # Used to find courses D which have C as a prerequisite
    prereq_to_course = defaultdict(list)
    for course, prereqs in courses.items():
        for prereq in prereqs:
            prereq_to_course[prereq].append(course)

    result = []
    courses_without_prereq = [c for c, p in courses.items() if not p]

    while courses_without_prereq:
        prereq = courses_without_prereq.pop()
        result.append(prereq)

        # Find courses that are now free to take
        for course in prereq_to_course.get(prereq, []):
            courses[course].remove(prereq)
            if not courses[course]:
                courses_without_prereq.append(course)

    # Circular dependency
    if len(result) < len(courses):
        return None

    return result


if __name__ == "__main__":
    courses = {"CSC300": ["CSC100", "CSC200"], "CSC200": ["CSC100"], "CSC100": []}
    print(f"Solution({courses}) ->", solution(courses))
