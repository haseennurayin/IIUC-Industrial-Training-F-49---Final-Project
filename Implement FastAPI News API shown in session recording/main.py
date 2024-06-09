from fastapi import FastAPI
import uvicorn
from app.routers import news

app = FastAPI(
    title="AI based News Summary API",
    version="0.2",
    description="This is the API documentation for News Summary generating by AI.",
    contact={
        "name": "Haseen Nurayin",
        "email": "nurayinabdurrahman@gmail.com",
    },
    redoc_url="/documentation",
    docs_url="/try-out",
)

app.include_router(news.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the News Summary API"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8011,
        reload=True
    )
