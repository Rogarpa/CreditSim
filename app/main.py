from fastapi import FastAPI

app = FastAPI(title="CreditSim")


@app.get("/health")
def health():
    return {"status": "ok"}

