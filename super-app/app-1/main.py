from fastapi import FastAPI, Request
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome")
async def root(name: str = "Rishabh"):
    return {"message": "Welcome " + str(name)}

@app.post("/sum")
async def proxy(request: Request):
    body = await request.json()
    resp = requests.post("http://server-2:8081/sum", json=body)
    return resp.json()
    # return resp.json()