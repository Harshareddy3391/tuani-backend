from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware





app=FastAPI()

#cors implemations




@app.get("/")
def home():
    return{
        "home":"home page"
    }