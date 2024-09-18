from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def hello_world() -> str :
    return "Let's get Subqueue Started !"


if __name__ == "__main__":
    uvicorn.run("app:app", port=1337, log_level="debug")

