from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome")
async def root(name: str = "Rishabh"):
    return {"message": "Welcome " + str(name)}