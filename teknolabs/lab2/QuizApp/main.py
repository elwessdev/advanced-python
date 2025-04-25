from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from models import Choices, Questions
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Models
class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Routes
@app.get("/")
def root():
    return "Server works fine!!"

@app.post('/questions')
def create_questions(question: QuestionBase, db: db_dependency):
    db_question = Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = Choices(
            choice_text=choice.choice_text, 
            is_correct=choice.is_correct, 
            question_id=db_question.id
        )
        db.add(db_choice)
    db.commit()

@app.get('/all_questions')
def get_questions(db: db_dependency):
    questions = db.query(Questions).all()
    result = []
    for question in questions:
        choices = db.query(Choices).filter(Choices.question_id == question.id).all()
        question_data = {
            "id": question.id,
            "question_text": question.question_text,
            "choices": [
                {
                    "id": choice.id, 
                    "choice_text": choice.choice_text, 
                    "is_correct": choice.is_correct
                } 
                for choice in choices
            ]
        }
        result.append(question_data)
    return result

@app.get('/questions/{id}')
def get_question(id: int, db: db_dependency):
    qus = db.query(Questions).filter(Questions.id==id).first()
    if not qus:
        raise HTTPException(status_code=404, detail="Question not found")
    return qus