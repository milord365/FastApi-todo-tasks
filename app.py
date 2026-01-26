from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Привет, {name}!"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)