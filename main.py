import api.bus as bus

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/oit-nagao")
async def oit_to_nagao():
    return bus.oit_to_nagao()


@app.get("/nagao-oit")
async def nagao_to_oit():
    return bus.nagao_to_oit()


@app.get("/oit-kuzuha")
async def oit_to_kuzuha():
    return bus.oit_to_kuzuha()


@app.get("/kuzuha-oit")
async def kuzuha_to_oit():
    return bus.kuzuha_to_oit()


def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
