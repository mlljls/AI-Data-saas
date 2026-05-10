from fastapi import FastAPI

app = FastAPI(title="AI Data SaaS")

@app.get("/")
def home():
    return {"message": "AI SaaS is running 🚀"}
