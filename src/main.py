from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello"}


@app.get("/details")
def details():
    return {"name": "FastAPI Demo app", "language": "python", "hosted_on": "k8s"}
