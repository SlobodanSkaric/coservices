from fastapi import FastAPI
from routes import main_route

app = FastAPI()

app.include_router(main_route.router)
