from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Setup app and templates
app = FastAPI(title="IP Echo API")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

@app.get("/ip")
async def get_client_ip(request: Request):
    client_host = request.client.host
    return {"client_ip": client_host}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    client_ip = request.client.host
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "client_ip": client_ip}
    )
