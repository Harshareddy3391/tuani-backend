from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware





app=FastAPI()

#cors implemations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_methods=["*"]
)




@app.get("/")
def home():
    return{
        "home":"home page"
    }