# SECTION A 
# 1.B -INHERITENCC
# 2 .C a
# 3.b [1,4,9] 
# 4.c map()
# 5.b with
# 6.c ROW_NUMBER()
# 7 .C CROSS
# 8.A left pointer 
# 9 .B dictionary
# 10.A right pointer

#SECTION B
#11
class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)


# Creating object
s1 = Student("Mahboob", 85)

# Display details
s1.display()

# Updating marks
s1.set_marks(90)

print("Updated Marks:", s1.get_marks())


#12try:

try:
    with open("students.txt", "r") as file:

        data = file.read()

        lines = data.splitlines()
        words = data.split()

        print("Total Lines:", len(lines))
        print("Total Words:", len(words))

except FileNotFoundError:
    print("Error: students.txt file not found.")


#13

SELECT
    s.student_name,
    s.city,
    c.course_name,
    r.subject,
    r.marks
FROM students s
INNER JOIN courses c
    ON s.course_id = c.course_id
LEFT JOIN results r
    ON s.student_id = r.student_id;


#14

SELECT
    c.course_name,
    COUNT(DISTINCT s.student_id) AS total_students,
    AVG(r.marks) AS average_marks
FROM courses c
INNER JOIN students s
    ON c.course_id = s.course_id
INNER JOIN results r
    ON s.student_id = r.student_id
GROUP BY c.course_id, c.course_name
HAVING AVG(r.marks) > 70;


#15
WITH StudentAverage AS
(
    SELECT
        s.student_id,
        s.student_name,
        s.course_id,
        AVG(r.marks) AS average_marks
    FROM students s
    INNER JOIN results r
        ON s.student_id = r.student_id
    GROUP BY
        s.student_id,
        s.student_name,
        s.course_id
)

SELECT
    student_name,
    average_marks,
    RANK() OVER (
        PARTITION BY course_id
        ORDER BY average_marks DESC
    ) AS student_rank
FROM StudentAverage;

#16
def check_pattern(arr):
    if len(arr) < 2:
        return True

    difference = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != difference:
            return False

    return True


numbers = [2, 4, 6, 8, 10, 12]

print(check_pattern(numbers))

#17

arr = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0

for i in range(len(arr) - k + 1):
    window_sum = sum(arr[i:i+k])

    print(arr[i:i+k], "=", window_sum)

    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)

#18

def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return arr[left], arr[right]

        elif total < target:
            left += 1

        else:
            right -= 1

    return None


arr = [1, 2, 4, 6, 8, 9]

print(find_pair(arr, 10))

#19

def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return arr[left], arr[right]

        elif total < target:
            left += 1

        else:
            right -= 1

    return None


arr = [1, 2, 4, 6, 8, 9]

print(find_pair(arr, 10))



