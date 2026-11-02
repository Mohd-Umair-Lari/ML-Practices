from fastapi import FastAPI
import asyncio

app = FastAPI()

async def get_burger(n:int):
    await asyncio.sleep(n)
    return n;

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/wait={n},{m}")
async def wait(n:int):
    result=await get_burger(n)
    return {
        "Time served" : result,
    }