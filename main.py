from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

# Deta Space looks for a variable called `app` or `application`
application = app  # For Deta compatibility
