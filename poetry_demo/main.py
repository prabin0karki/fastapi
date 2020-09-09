import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import database
from .userapp import views
from .categoryapp import cat_views
from .productapp import pro_views

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(views.router, tags=["User"])
app.include_router(cat_views.router, tags=["Category"])
app.include_router(pro_views.router, tags=["Product"])


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, reload=True, access_log=False)
