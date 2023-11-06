class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)
 
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'
        
    def grades_avg(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
            grades_average = grades_sum / grades_count
            return grades_average
        
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_avg() > other.grades_avg()
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_avg() < other.grades_avg()
    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_avg() == other.grades_avg()
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {round(self.grades_avg(), 0)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    lecturer_list =[]
    grades_lec = {}

    def grades_average_lec(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lec:
            grades_count += len(self.grades_lec[grade])
            grades_sum += sum(self.grades_lec[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0
        
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_lec() > other.grades_average_lec()
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_lec() < other.grades_average_lec()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_lec() == other.grades_average_lec()

    def __str__(self):
        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {round(self.grades_average_lec(), 0)}')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}')
    

def courses_average_students(student_list, course):
    for student in student_list:
        for cours_name, average in Student.grades():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Студент: {student.name} {student.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")

def courses_average_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for cours_name, average in Lecturer.grades_lec.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за лекции: {round(sum_average, 0)}\n")

 
student_1 = Student('Ivan', 'Ivanov', 'man')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Mary', 'Petrova', 'woman')
student_2.courses_in_progress += ['Python', 'Django']
student_2.finished_courses += ['Введение в программирование']

mentor_reviewer_1 = Reviewer('Alexander', 'Alexandrov')
mentor_reviewer_1.courses_attached += ['Python', 'Git', 'Django']

mentor_reviewer_2 = Reviewer('Irina', 'Sidorova')
mentor_reviewer_2.courses_attached += ['Python', 'Git']

mentor_lecturer_1 = Lecturer('Anton', 'Popov')
mentor_lecturer_1.courses_attached += ['Python', 'Git', 'Django']

mentor_lecturer_2 = Lecturer('Pavel', 'Sokolov')
mentor_lecturer_2.courses_attached += ['Python', 'Git', 'Django']

mentor_reviewer_2.rate_hw(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw(student_1, 'Python', 8)
mentor_reviewer_1.rate_hw(student_1, 'Git', 8)
mentor_reviewer_1.rate_hw(student_1, 'Git', 10)

mentor_reviewer_1.rate_hw(student_2, 'Python', 10)
mentor_reviewer_1.rate_hw(student_2, 'Python', 9)
mentor_reviewer_2.rate_hw(student_2, 'Django', 7)
mentor_reviewer_2.rate_hw(student_2, 'Django', 9)

student_1.rate_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_lecturer(mentor_lecturer_1, 'Python', 9)
student_1.rate_lecturer(mentor_lecturer_1, 'Python', 7)
student_1.rate_lecturer(mentor_lecturer_1, 'Git', 10)

student_2.rate_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_lecturer(mentor_lecturer_2, 'Python', 8)
student_2.rate_lecturer(mentor_lecturer_2, 'Django', 9)

print(mentor_reviewer_1)
print(mentor_reviewer_2)
print(mentor_lecturer_1)
print(mentor_lecturer_2)
print(student_1)
print(student_2)

if student_1 > student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}')
elif student_1 < student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}')
else:
    print(f'Средняя оценка {student_1.name} {student_1.surname}  равна средней оценке {student_2.name} {student_2.surname}')

if mentor_lecturer_1 > mentor_lecturer_1:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} больше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
elif mentor_lecturer_1 < mentor_lecturer_1:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} меньше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
else:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname}  равна средней оценке {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')




