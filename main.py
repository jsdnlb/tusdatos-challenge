from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import user, auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(auth.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to this amazing API"}


""" @app.exception_handler(404)
def not_found(request, exc):
    return JSONResponse(status_code=404, content={"message": "Not Found"}) """


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
