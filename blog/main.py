import uvicorn
from fastapi import FastAPI
from routers import authentication, blog, user


app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
