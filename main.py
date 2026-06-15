from fastapi import FastAPI

from routers.sustainability import router

app = FastAPI(
    title="SustainAI API",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "message": "SustainAI API Running"
    }