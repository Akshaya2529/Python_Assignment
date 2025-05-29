#Assignment
#Data
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

print(university_data)
#1
for i in university_data.values():
    print(f"{i['name']} , {i['major']}")

#2
for sid, i in university_data.items():
    name = i["name"]
    print(f"\n{name} ({sid}):")

    for course_name, marks in i["courses"].items():
        total = marks["midterm"] + marks["final"] + marks["project"]
        average = total / 3
        print(f"  {course_name}: Average = {average:.2f}")

#3
for sid, i in university_data.items():
    courses = i["courses"]
    if "Python101" in courses and courses["Python101"]["final"] > 90:
        print(f"{i['name']} ")

#4
university_data["S101"]["courses"]["AI101"] = {"midterm": 89, "final": 94, "project": 90}
print(f"{list(university_data['S101']['courses'].keys())}")

#5
course_totals = {}
for student in university_data.values():
    for course, scores in student["courses"].items():
        if course not in course_totals:
            course_totals[course] = {"midterm": 0, "final": 0, "project": 0, "count": 0}
        
        course_totals[course]["midterm"] += scores["midterm"]
        course_totals[course]["final"] += scores["final"]
        course_totals[course]["project"] += scores["project"]
        course_totals[course]["count"] += 1
for course, totals in course_totals.items():
    count = totals["count"]
    avg_mid = totals["midterm"] / count
    avg_final = totals["final"] / count
    avg_proj = totals["project"] / count
    overall = (avg_mid + avg_final + avg_proj) / 3

    print(f"{course}: Avg Midterm = {avg_mid:.2f}, Avg Final = {avg_final:.2f}, Avg Project = {avg_proj:.2f}, Overall Avg = {overall:.2f}")
