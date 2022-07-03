import test

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}


@app.get("/bus")
async def bus():
    bus = test.Bus()
    bus.get_bus_info()
    return bus.return_bus_info()


def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
