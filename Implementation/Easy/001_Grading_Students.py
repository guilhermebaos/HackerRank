def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades += [grade]
        else:
            closest_mult_5 = 5 * (grade // 5 + 1)
            delta = closest_mult_5 - grade
            if delta < 3:
                grade = closest_mult_5
            new_grades += [grade]
    return new_grades
