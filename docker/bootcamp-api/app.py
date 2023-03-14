from fastapi import FastAPI

from routes.producers import router as producers

app = FastAPI()

app.include_router(producers)


@app.get("/")
async def root():
    return {"message": "Hello World"}
