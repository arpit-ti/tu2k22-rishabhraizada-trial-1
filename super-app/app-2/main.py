from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome")
async def root(name: str = "Rishabh"):
    return {"message": "Welcome " + str(name)}

@app.post("/sum")
async def root(request: Request):
    req = await request.json()
    return {"sum":req["a"] + req["b"]}