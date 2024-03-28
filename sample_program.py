from toolz import pipe, curry, filter, valfilter

# Define a list of student grades
grades = {
    'Alice': {'math': 85, 'science': 90, 'history': 75},
    'Bob': {'math': 70, 'science': 80, 'history': 65},
    'Charlie': {'math': 60, 'science': 75, 'history': 80},
    'David': {'math': 80, 'science': 85, 'history': 90},
    'Eve': {'math': 55, 'science': 60, 'history': 70}
}

# Calculate average grade for each student
average_grades = pipe(
    grades.values(),
    map(lambda x: sum(x.values()) / len(x)),
    list
)

# Find highest and lowest grades
all_subject_grades = pipe(
    grades.values(),
    map(lambda x: list(x.values())),
    sum,
    list
)
highest_grade = max(all_subject_grades)
lowest_grade = min(all_subject_grades)

# Filter out failing grades (below 60)
failing_grades = pipe(
    grades.items(),
    valfilter(lambda x: all(subject_grade >= 60 for subject_grade in x.values())),
    list
)

# Print results
print("Average grades:", average_grades)
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)
print("Students with passing grades:", failing_grades)

