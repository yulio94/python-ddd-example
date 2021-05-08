import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


def entrypoint():
    uvicorn.run("src.apps.backoffice.backend.start:app", host="0.0.0.0", port=8000, reload=True)
