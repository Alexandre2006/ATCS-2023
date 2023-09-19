from functools import reduce


def to_celcius():
    temps = [68, 32, 100, 87]
    print("Fahrenheit Temps: " + str(temps))

    celcius = list(map(lambda x: (x-32)*(5/9), temps))

    print("Celcius Temps: " + str(celcius))

def remove_email_domains(emails):
    print("Emails: " + str(emails))

    usernames = list(map(lambda x: x[0:x.find("@")], emails))

    print("Usernames: " + str(usernames))

def get_students(schools, students):
    print("All Students: " + str(students))
    print("Selected Schools: " + str(schools))
    return list(filter(lambda x: x["school"] in schools, students))

def avg_math_grade(grades):
    print("Grades: " + str(grades))

    math_students = list(filter(lambda x: "math" in x, grades))
    math_grades = list(map(lambda x: x["math"], math_students))
    math_avg = reduce(lambda x, y: x + y, math_grades) / len(math_grades)

    print("Average math grade: " + str(math_avg))

if __name__ == "__main__":
    while True:
        print("""
1. To Celcius
2. Remove Email Domains
3. Get Students
4. Average Math Scores
Q. Quit
""")
        selection = input("Enter a selection: ")
        if selection == "1":
            to_celcius()
        elif selection == "2":
            remove_email_domains(["me@thinkalex.dev", "exampleuser@stanford.edu", "billy.bob.jones@microsoft.com"])
        elif selection == "3":
            schools = ['Menlo', 'Sacred Heart']
            students = [{'name': 'Alice', 'grade': 9, 'school': 'Menlo'},
{'name': 'Bob', 'grade': 10, 'school': 'Sacred Heart'},
{'name': 'Charlie', 'grade': 9, 'school': 'Menlo'},
{'name': 'Delta', 'grade': 9, 'school': 'Sacred Heart'},
{'name': 'Epsilon', 'grade': 9, 'school': 'Nueva'}]
            print(get_students(schools, students))
        elif selection == "4":
            grades = [{'name': 'Alice', 'math': 85, 'science': 92},
{'name': 'Bob', 'science': 88},
{'name': 'Charlie', 'math': 90, 'science': 78},
{'name': 'Delta', 'math': 94, 'science': 78}]
            avg_math_grade(grades)
            
        elif selection.lower() == "q":
            break