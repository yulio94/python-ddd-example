import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


def entrypoint():
    uvicorn.run("src.apps.uvcp.backend.start:app", host="0.0.0.0", port=8001, reload=True)
