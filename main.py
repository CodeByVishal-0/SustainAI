from fastapi import FastAPI

from routers.sustainability import router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SustainAI API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
@app.get("/health")
def health():

    return {
        "status": "healthy"
    }