from fastapi import FastAPI
# from .routers import module

app = FastAPI()

# app.include_router(module.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}