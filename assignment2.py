
# You're building a system to manage student data for a university. Each student is identified by a unique student ID and has the following details:

# - Name
# - Major
# - Enrolled Courses (each course has a course name and a dictionary of assessment scores like midterm, final, and project)



#  Sample Data (Nested Dictionary):


# university_data = {
#     "S101": {
#         "name": "Alice Johnson",
#         "major": "Computer Science",
#         "courses": {
#             "Python101": {"midterm": 88, "final": 92, "project": 94},
#             "Math201": {"midterm": 78, "final": 85, "project": 80}
#         }
#     },
#     "S102": {
#         "name": "Bob Smith",
#         "major": "Mathematics",
#         "courses": {
#             "Math201": {"midterm": 90, "final": 93, "project": 88},
#             "Stats101": {"midterm": 84, "final": 80, "project": 85}
#         }
#     },
#     "S103": {
#         "name": "Clara Lopez",
#         "major": "Physics",
#         "courses": {
#             "Physics101": {"midterm": 75, "final": 82, "project": 78},
#             "Math201": {"midterm": 70, "final": 72, "project": 68}
#         }
#     }
# }
# # Q1: Print all student names and their majors
# Q2: Average score per course per student
# Q3: Find students who scored >90 in final of Python101
# Q4: Add new course AI101 for student S101
# Q5: Print average for each course

university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

# Q1: Print all student names and their majors
print("Q1: Student Names and Majors")
for name, info in university_data.items():
    print(f"{info['name']} - {info['major']}")
print()

# Q2: Average score per course per student
print("Q2: Average score per course per student")
for sid, info in university_data.items():
    print(f"{info['name']}:")
    for course, scores in info['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course} - Average Score: {avg:.2f}")
print()

# Q3: Find students who scored >90 in final of Python101
print("Q3: Students who scored >90 in final of Python101")
for sid, info in university_data.items():
    python_course = info['courses'].get("Python101")
    if python_course and python_course["final"] > 90:
        print(f"{info['name']} scored {python_course['final']} in Python101 final")
print()

# Q4: Add new course AI101 for student S101
print("Q4: Adding AI101 for S101")
university_data["S101"]["courses"]["AI101"] = {"midterm": 91, "final": 89, "project": 95}
print(f"S101 courses after adding AI101: {university_data['S101']['courses']}")
print()

# Q5: Print average for each course (all students)
print("Q5: Average score for each course (across all students)")
from collections import defaultdict

course_scores = defaultdict(list)
for student in university_data.values():
    for course, assessments in student["courses"].items():
        avg = sum(assessments.values()) / len(assessments)
        course_scores[course].append(avg)

for course, scores in course_scores.items():
    overall_avg = sum(scores) / len(scores)
    print(f"{course}: {overall_avg:.2f}")
