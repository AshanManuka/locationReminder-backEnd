from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, condecimal
from typing import List, Tuple
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import requests


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

class PlaceBase(BaseModel):
    placename:str
    latitude: condecimal(ge=-90, le=90, decimal_places=6)
    longitude: condecimal(ge=-180, le=180, decimal_places=6)
    
class PlaceResponse(BaseModel):
    placename: str
    latitude: float
    longitude: float
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      
db_dependency = Annotated[Session, Depends(get_db)]

def save_place_to_database(db: Session, place_info: dict):
    db_place = models.Place(**place_info)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

@app.get("/hopePlaces/")
async def get_police_stations(keyword: str, latitude: float, longitude: float, db: db_dependency):
    api_key = "fuck"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=+{keyword}+near+{latitude},{longitude}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        places_info = []
        for place in data.get("results", []):
            
            place_info = {
                "placename": place.get("name", ""),
                "latitude": place.get("geometry", {}).get("location", {}).get("lat", 0),
                "longitude": place.get("geometry", {}).get("location", {}).get("lng", 0),
            }
            places_info.append(place_info)
            print(f"Place: {place_info['placename']}, Latitude: {place_info['latitude']}, Longitude: {place_info['longitude']}")
            
            save_place_to_database(db, place_info)
        return {"message": "Places information saved to the database."}

    except requests.RequestException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            

@app.post("/place/", status_code=status.HTTP_201_CREATED)
async def create_place(place:PlaceBase, db: db_dependency):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    return {db_place.placename,"Successfully Save..!"}
    

#should modify for get latitude and logitude from 
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/open")
def read_root():
    print("Manuka")
    return {"Hello": "Manuka"}

