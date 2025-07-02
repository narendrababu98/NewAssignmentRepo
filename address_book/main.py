from fastapi import FastAPI
from database import engine
from routes.address_book import book
import models
import uvicorn

app = FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(book)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
