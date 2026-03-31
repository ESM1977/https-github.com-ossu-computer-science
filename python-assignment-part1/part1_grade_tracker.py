# part1_grade_tracker.py
# Student Grade Tracker that manages student data, compute results and provides a summary report 

# -------------------- Task 1 --------------------
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    name = student["name"].strip().title()                             # clean the name
    roll = int(student["roll"])                                        # convert rollno into integer
    marks = [int(mark) for mark in student["marks_str"].split(", ")]   # convert marks into list of integers

    valid = all(word.isalpha() for word in name.split())                # validate data
    #print(f"{name} {'✓ Valid name' if valid else '✗ Invalid name'}")

    cleaned_student = {
        "name": name, 
        "roll": roll, 
        "marks": marks}
    cleaned_students.append(cleaned_student)

    vdata = all(word.isalpha() for word in name.split())
    datavalid = "✓ Valid name" if vdata else "✗ Invalid name"

    # print formatted profile card
    print("="*32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print(datavalid)
    print("="*32)

# Print in lowercase and uppercase with rollno.

for student in cleaned_students:
    if student["roll"] == 103:
        print("\nStudent with Roll No. 103:")
        print("Upper Case:", student["name"].upper())
        print("Lower Case:",student["name"].lower())


# -------------------- Task 2 --------------------
print("\n--- Task 2 : Marks Analysis Using Loops & Conditionals Output ---")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nStudent Name: {student_name}\n")

# Print each subject with marks and grade

for i in range(len(subjects)):
    score = marks[i]
    if 90 <= score <= 100:
        grade = "A+"
    elif 80 <= score <= 89:
        grade = "A"
    elif 70 <= score <= 79:
        grade = "B"
    elif 60 <= score <= 69:
        grade = "C"
    else:
        grade = "F"
    print(f"{subjects[i]} : {score} → Grade {grade}")

# Calculate total, average, Higj=hest and lowest

total = sum(marks)
avg = round(total / len(marks), 2)


max_marks = max(marks)
min_marks = min(marks)

print("\n-----------Analysis-----------")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")
print(f"Highest scoring subject: {subjects[marks.index(max_marks)]}, {max_marks}")
print(f"Lowest scoring subject: {subjects[marks.index(min_marks)]}, {min_marks}")

# While looop for adding new subject

new_subjects = 0

while True:
    sub = input("\nEnter subject name (or type 'done' to stop): ")
    if sub.lower() == "done":
        break

    marks_input = input(f"Enter marks for {sub} (0-100): ")

    # validation of data

    if not marks_input.isdigit():
        print("Warning: Invalid input!")
        continue

    m = int(marks_input)
    if m < 0 or m > 100:
        print("Warning: Marks must be between 0–100")
        continue

    subjects.append(sub)
    marks.append(m)
    new_subjects += 1

print("\nNew subjects added:", new_subjects)
print("Updated Average:", round(sum(marks)/len(marks), 2))


# -------------------- Task 3 --------------------
print("\n--- Task 3 : Class Performance Summary Output ---")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Display of data in the given format

print("\n Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []

for name, marks in class_data:
    avg = round(sum(marks)/len(marks), 2)
    averages.append(avg)

    status = "Pass" if avg >= 60 else "Fail"

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    print(f"{name:<18} | {avg:^7} | {status}")

print("\nNumber of students passed:", pass_count)
print("\nNumber of students failed:", fail_count)

top_avg = max(averages)
top_index = averages.index(top_avg)

print(f"Class Topper:", class_data[top_index][0], top_avg)

class_avg = round(sum(averages)/len(averages), 2)
print("Class Average:", class_avg)


# -------------------- Task 4 --------------------
print("\n--- Task 4: String Manipulation Utility Output ---")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print("\n1. Stripped Essay:\n", clean_essay)

print("\n2. Title Case:\n", clean_essay.title())

print("\n3. Count of python\n:", clean_essay.count("python"))

replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Essay:\n", replaced)

sentences = clean_essay.split(". ")
print("\n5. List of Sentences:\n", sentences)

print("\n6. Numbered Sentences:")
for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")
