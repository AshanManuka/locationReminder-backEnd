from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class PlaceBase(BaseModel):
    placename:str
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
        

@app.post("/place/", status_code=status.HTTP_201_CREATED)
async def create_place(place:PlaceBase, db: db_dependency):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    return {db_place.placename,"Successfully Save..!"}
    


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/open")
def read_root():
    print("Manuka")
    return {"Hello": "Manuka"}