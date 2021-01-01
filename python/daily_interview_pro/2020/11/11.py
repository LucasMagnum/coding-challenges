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


def courses_to_take(course_to_prereqs):
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

    # Used to find courses which have some other course as pre req
    prereq_to_course = {}
    for course in course_to_prereqs:
        for prereq in course_to_prereqs[course]:
            if prereq not in prereq_to_course:
                prereq_to_course[prereq] = []
            prereq_to_course[prereq].append(course)

    result = []
    todo = [c for c, p in course_to_prereqs.items() if not p]

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        for c in prereq_to_course.get(prereq, []):
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs[c]:
                todo.append(c)

    if len(result) < len(course_to_prereqs):
        return None

    return result


if __name__ == "__main__":
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    print(courses_to_take(courses))
    # ['CSC100', 'CSC200', 'CSC300']