from fastapi import FastAPI, HTTPException

app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/open")
def read_root():
    print("Manuka")
    return {"Hello": "Manuka"}