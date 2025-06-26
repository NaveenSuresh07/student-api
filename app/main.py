from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, models
from app import models, database
models.Base.metadata.create_all(bind=database.engine)
from app.database import engine, SessionLocal
from pydantic import BaseModel
from datetime import date

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
    
models.Base.metadata.create_all(bind=engine)


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SCHEMAS
class StudentSchema(BaseModel):
    first_name: str
    middle_name: str = None
    last_name: str
    age: int
    city: str

class ClassSchema(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    hours: int

# STUDENT ROUTES
@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API"}

@app.post("/students/")
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    return crud.create_student(db, student.dict())

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentSchema, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student.dict())

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id)
    return {"message": "Student deleted"}

# CLASS ROUTES
@app.post("/classes/")
def create_class(cls: ClassSchema, db: Session = Depends(get_db)):
    return crud.create_class(db, cls.dict())

@app.put("/classes/{class_id}")
def update_class(class_id: int, cls: ClassSchema, db: Session = Depends(get_db)):
    return crud.update_class(db, class_id, cls.dict())

@app.delete("/classes/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    crud.delete_class(db, class_id)
    return {"message": "Class deleted"}

# REGISTRATION
@app.post("/register/")
def register(student_id: int, class_id: int, db: Session = Depends(get_db)):
    crud.register_student(db, student_id, class_id)
    return {"message": "Student registered to class"}

@app.get("/classes/{class_id}/students")
def list_students(class_id: int, db: Session = Depends(get_db)):
    return crud.get_students_in_class(db, class_id)
@app.get("/")
def read_root():
    return {"message": "Hello"}
