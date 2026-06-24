from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI"
    }


@app.get("/about")
def about():
    return {
        "application": "Location Price",
        "version": "1.0"
    }
