from fastapi import FastAPI

app=FastAPI()

app.get("/")
def hello():
    return {
        "message" : "Hello your site is live"
    }

@app.get("/about")
def about():
    return {
        'mesage' : 'this is the about page for the web app'
    }

