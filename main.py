from fastapi import FastAPI
from router import main_route,user

app = FastAPI()

# defaut
app.include_router(main_route.router)

# user
app.include_router(user.router)
