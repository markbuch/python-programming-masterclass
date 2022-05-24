morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternooon = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = morning ^ afternooon
print(possible_courses)

possible_courses = set(afternooon).symmetric_difference(morning)

