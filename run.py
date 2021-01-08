import uvicorn

if __name__ == "__main__":
  uvicorn.run("app.main:app", reload=True, port=3000, host='0.0.0.0')