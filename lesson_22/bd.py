from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from tabulate import tabulate
import random

Base = declarative_base()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=student_course, back_populates='courses')

engine = create_engine('sqlite:///students.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if not session.query(Course).count():
    course_titles = ["Math", "History", "Physics", "Programming", "Art"]
    courses = [Course(title=title) for title in course_titles]
    session.add_all(courses)
    session.commit()

    courses = session.query(Course).all()
    for i in range(1, 21):
        student = Student(name=f"Student {i}")
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)
    session.commit()

def show_courses():
    courses = session.query(Course).all()
    table = [(c.id, c.title) for c in courses]
    print("\nСписок курсів:")
    print(tabulate(table, headers=["ID", "Назва курсу"], tablefmt="grid"))

def show_students():
    students = session.query(Student).all()
    table = [(s.id, s.name, ", ".join(c.title for c in s.courses)) for s in students]
    print("\nСписок студентів:")
    print(tabulate(table, headers=["ID", "Ім'я", "Курси"], tablefmt="grid"))

def add_student():
    name = input("Введіть ім'я нового студента: ")
    show_courses()
    course_id = int(input("ID курсу для запису: "))
    course = session.get(Course, course_id)
    if course:
        new_student = Student(name=name, courses=[course])
        session.add(new_student)
        session.commit()
        print(f"✅ Додано {name} на курс {course.title}")
    else:
        print("❌ Курс не знайдено")

def students_by_course():
    show_courses()
    course_id = int(input("Введіть ID курсу: "))
    course = session.get(Course, course_id)
    if course:
        table = [(s.id, s.name) for s in course.students]
        print(f"\nСтуденти на курсі {course.title}:")
        print(tabulate(table, headers=["ID", "Ім'я"], tablefmt="grid"))
    else:
        print("Курс не знайдено")

def courses_by_student():
    show_students()
    student_id = int(input("Введіть ID студента: "))
    student = session.get(Student, student_id)
    if student:
        table = [(c.id, c.title) for c in student.courses]
        print(f"\nКурси, на які записаний {student.name}:")
        print(tabulate(table, headers=["ID", "Назва курсу"], tablefmt="grid"))
    else:
        print("Студента не знайдено")

def update_student():
    show_students()
    student_id = int(input("ID студента для оновлення: "))
    student = session.get(Student, student_id)
    if student:
        new_name = input("Введіть нове ім'я: ")
        student.name = new_name
        session.commit()
        print(f"✅ Ім'я оновлено: {student.name}")
    else:
        print("Студента не знайдено")

def delete_student():
    show_students()
    student_id = int(input("ID студента для видалення: "))
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"🗑 Видалено студента ID={student_id}")
    else:
        print("Студента не знайдено")

# --- МЕНЮ ---
def menu():
    while True:
        print("\n=== Система управління студентами ===")
        print("1. Додати студента")
        print("2. Показати всі курси")
        print("3. Показати всіх студентів")
        print("4. Студенти за курсом")
        print("5. Курси за студентом")
        print("6. Оновити студента")
        print("7. Видалити студента")
        print("0. Вийти")

        choice = input("Виберіть дію: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_courses()
        elif choice == "3":
            show_students()
        elif choice == "4":
            students_by_course()
        elif choice == "5":
            courses_by_student()
        elif choice == "6":
            update_student()
        elif choice == "7":
            delete_student()
        elif choice == "0":
            break
        else:
            print("❌ Невірний вибір!")

if __name__ == "__main__":
    menu()
