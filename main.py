from fastapi import FastAPI
from router import main_route,user,coffe

app = FastAPI()

# defaut
app.include_router(main_route.router)

# user
app.include_router(user.router)

# coffe
app.include_router(coffe.router)
