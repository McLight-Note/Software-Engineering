# 2025.03.22
# Mavzu: Student grading
# Muallif: Muhammadsodiq

students = [
    {'name': "Yusuf", "grades": [85, 90, 78]},
    {'name': "Ali", "grades": [85, 90, 78]},
    {'name': "Salohiddin", "grades": [85, 90, 78]},
    {'name': "Siroj", "grades": [85, 90, 78]},
    {'name': "Oyatullo", "grades": [85, 90, 78]}
]

def avarage_grade(grades):
    return sum(grades)/ len(grades)

def final_grade(avarage):
    if avarage >= 90:
        return 'A'
    elif avarage >= 80:
        return 'B'
    elif avarage >= 70:
        return 'C'
    elif avarage >= 60:
        return 'D'
    else:
        return 'F'

def resluts():
    print("Grades of the students:\n")
    for  student in students:
        avarage = avarage_grade(student['grades'])
        grade = final_grade(avarage)
        print(f"Name: {student['name']}\n")
        print(f"Avaarage score: {avarage}\n")
        print(f"Grade: {grade}\n")
        
resluts()