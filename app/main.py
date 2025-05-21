from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional

# Setup app and templates
app = FastAPI(title="IP Echo API")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

def get_client_ip_from_request(request: Request) -> str:
    """
    Extract client IP address from request with the following priority:
    1. First IP from X-Forwarded-For header chain
    2. X-Real-IP header value
    3. request.client.host as fallback
    
    Args:
        request: FastAPI Request object
    
    Returns:
        str: The detected client IP address
    """
    # Check for X-Forwarded-For header (priority 1)
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        # Get the first IP in the chain (client IP)
        return x_forwarded_for.split(",")[0].strip()
    
    # Check for X-Real-IP header (priority 2)
    x_real_ip = request.headers.get("X-Real-IP")
    if x_real_ip:
        return x_real_ip.strip()
    
    # Fallback to request.client.host (priority 3)
    return request.client.host

@app.get("/ip")
async def get_client_ip(request: Request):
    client_ip = get_client_ip_from_request(request)
    return {"client_ip": client_ip}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    client_ip = get_client_ip_from_request(request)
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "client_ip": client_ip}
    )

@app.get("/debug", response_class=HTMLResponse)
async def debug_headers(request: Request):
    """
    Debug endpoint to show all request headers and the detected IP
    """
    client_ip = get_client_ip_from_request(request)
    headers = dict(request.headers.items())
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request, 
            "client_ip": f"{client_ip}\n\nHeaders:\n{headers}"
        }
    )
