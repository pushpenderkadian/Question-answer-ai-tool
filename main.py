from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.api import router as api_router
from app.routes.socket import router as socket_router
import  uvicorn


app = FastAPI()


# Static files and templates 
templates = Jinja2Templates(directory="templates")

# Routers
app.include_router(api_router)
app.include_router(socket_router)

# Routes for the web app
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})





if __name__ == "__main__" :


    uvicorn.run(app, host="0.0.0.0", port=8000)
