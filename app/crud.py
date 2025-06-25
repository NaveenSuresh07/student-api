from sqlalchemy.orm import Session
from . import models

# STUDENTS

def create_student(db: Session, data):
    student = models.Student(**data)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student(db: Session, student_id: int, data):
    student = db.query(models.Student).get(student_id)
    for key, value in data.items():
        setattr(student, key, value)
    db.commit()
    return student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).get(student_id)
    db.delete(student)
    db.commit()

# CLASSES

def create_class(db: Session, data):
    cls = models.Class(**data)
    db.add(cls)
    db.commit()
    db.refresh(cls)
    return cls

def update_class(db: Session, class_id: int, data):
    cls = db.query(models.Class).get(class_id)
    for key, value in data.items():
        setattr(cls, key, value)
    db.commit()
    return cls

def delete_class(db: Session, class_id: int):
    cls = db.query(models.Class).get(class_id)
    db.delete(cls)
    db.commit()

# REGISTRATION

def register_student(db: Session, student_id: int, class_id: int):
    student = db.query(models.Student).get(student_id)
    cls = db.query(models.Class).get(class_id)
    cls.students.append(student)
    db.commit()

def get_students_in_class(db: Session, class_id: int):
    cls = db.query(models.Class).get(class_id)
    return cls.students
