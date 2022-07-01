import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}


def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
