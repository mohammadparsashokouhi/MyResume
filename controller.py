from model import Student, parsa
from sqlalchemy.exc import SQLAlchemyError  

class Manager:
    def add_student(self, name, last_name, score):
        try:
            student = Student(Name=name, Last_name=last_name, Score=float(score))
            parsa.add(student)
            parsa.commit()
            return True
        except SQLAlchemyError:
            parsa.rollback()
            return False

    def show_students(self):
        return parsa.query(Student).all()

    def update_student(self, key_, name, last_name, score):
        try:
            student = parsa.query(Student).filter(Student.id == key_).first()
            if student:
                student.Name = name
                student.Last_name = last_name
                student.Score = float(score)
                parsa.commit()
                return True
            else:
                return False
        except SQLAlchemyError:
            parsa.rollback()
            return False

    def remove_student(self, key_):
        try:
            student = parsa.query(Student).filter(Student.id == key_).first()
            if student:
                parsa.delete(student)   
                parsa.commit()
                return True
            else:
                return False
        except SQLAlchemyError:
            parsa.rollback()
            return False