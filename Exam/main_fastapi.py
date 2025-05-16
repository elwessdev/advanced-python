from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from typing import List
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import models
import schemas
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie API")

groq_api_key = "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"
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

# Create Movie Route
@app.post("/movies/", response_model=schemas.MoviePublic)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = models.Movies(
        title=movie.title,
        year=movie.year,
        director=movie.director
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    for actor in movie.actors:
        db_actor = models.Actors(
            actor_name=actor.actor_name,
            movie_id=db_movie.id
        )
        db.add(db_actor)
    db.commit()
    db.refresh(db_movie)
    
    return db_movie

# Get Random Movie Route
@app.get("/movies/random/", response_model=schemas.MoviePublic)
def get_random_movie(db: Session = Depends(get_db)):
    random_movie = db.query(models.Movies)\
        .options(joinedload(models.Movies.actors))\
        .order_by(func.random())\
        .first()
    if not random_movie:
        raise HTTPException(status_code=404, detail="No movies found in the database")
    
    return random_movie

# Generate Summary Route
@app.post("/generate_summary/", response_model=schemas.SummaryResponse)
def generate_movie_summary(request: schemas.SummaryRequest, db: Session = Depends(get_db)):
    movie = db.query(models.Movies)\
        .options(joinedload(models.Movies.actors))\
        .filter(models.Movies.id == request.movie_id)\
        .first()
    
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with ID {request.movie_id} not found")
    
    actor_names = [actor.actor_name for actor in movie.actors]
    if len(actor_names) > 1:
        actor_list = ", ".join(actor_names[:-1]) + f", and {actor_names[-1]}"
    else:
        actor_list = actor_names[0] if actor_names else "unknown cast"
    
    prompt_template = PromptTemplate.from_template(
        "Generate a short, engaging summary (around 150 words) for the movie '{title}' "
        "({year}), directed by {director} and starring {actor_list}. "
        "The summary should capture the essence of the film and make someone want to watch it. "
        "Do not make up plot details if you don't know them."
    )

    chain = prompt_template | llm | StrOutputParser()
    
    summary = chain.invoke({
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "actor_list": actor_list
    })
    
    return schemas.SummaryResponse(
        movie_id=movie.id,
        title=movie.title,
        summary_text=summary
    )

# Get Movies Route
@app.get("/movies/", response_model=List[schemas.MoviePublic])
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.query(models.Movies)\
        .options(joinedload(models.Movies.actors))\
        .all()
    
    return movies


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session, joinedload
# from sqlalchemy import func
# from typing import List

# import models
# import schemas
# from database import engine, get_db

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Movie API")


# @app.post("/movies/", response_model=schemas.MoviePublic)
# def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
#     db_movie = models.Movies(
#         title=movie.title,
#         year=movie.year,
#         director=movie.director
#     )
    
#     db.add(db_movie)
#     db.commit()
#     db.refresh(db_movie)
    
#     for actor in movie.actors:
#         db_actor = models.Actors(
#             actor_name=actor.actor_name,
#             movie_id=db_movie.id
#         )
#         db.add(db_actor)
    
#     db.commit()
    
#     db.refresh(db_movie)
    
#     return db_movie


# @app.get("/movies/random/", response_model=schemas.MoviePublic)
# def get_random_movie(db: Session = Depends(get_db)):
#     random_movie = db.query(models.Movies)\
#         .options(joinedload(models.Movies.actors))\
#         .order_by(func.random())\
#         .first()
    
#     if not random_movie:
#         raise HTTPException(status_code=404, detail="No movies found in the database")
    
#     return random_movie


# @app.get("/movies/", response_model=List[schemas.MoviePublic])
# def get_all_movies(db: Session = Depends(get_db)):
#     movies = db.query(models.Movies)\
#         .options(joinedload(models.Movies.actors))\
#         .all()
    
#     return movies


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)