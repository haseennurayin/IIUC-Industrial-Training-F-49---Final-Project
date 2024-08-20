from fastapi import FastAPI
import uvicorn
from app.routers import news, summary

app = FastAPI(
    title="AI-based News Summary API",
    version="0.2",
    description="API Documentation for Generating News Summaries Using AI.",
    contact={
        "name": "Haseen Nurayin",
        "email": "haseennurayin@outlook.com",
    },
    redoc_url="/documentation",
    docs_url="/endpoints",
)

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8011, reload=True)
