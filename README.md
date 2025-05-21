# IP Echo API

A minimal FastAPI application that displays the client's IP address (IPv4 or IPv6) with a clean, modern interface.

## Features

- Shows the client's IP address as seen by the server
- Responsive design that works on both desktop and mobile devices
- Properly handles IPv6 addresses without overflow issues
- Clean, modern dark theme interface
- JSON API endpoint for programmatic access

## Project Structure

```
ip_echo_app/
├── app/
│   ├── main.py            # FastAPI application code
│   └── templates/
│       └── index.html     # HTML template with responsive design
├── Dockerfile             # Docker configuration
└── requirements.txt       # Python dependencies
```

## Installation

### Local Development

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Open your browser and navigate to http://127.0.0.1:8000

### Using Docker

#### Build the Docker Image

```bash
docker build -t ip-echo-api .
```

#### Run the Docker Container

```bash
docker run -p 8000:8000 ip-echo-api
```

This will start the application and make it available at http://localhost:8000

#### Run with a Different Port

If you want to use a different port on your host machine:

```bash
docker run -p 3000:8000 ip-echo-api
```

This will make the application available at http://localhost:3000

## API Endpoints

### Web Interface

- `GET /`: Returns an HTML page displaying the client's IP address

### JSON API

- `GET /ip`: Returns a JSON object with the client's IP address
  ```json
  {"client_ip": "192.168.1.1"}
  ```

## Deployment

For production deployment, consider:

1. Using a reverse proxy like Nginx
2. Setting up HTTPS
3. Implementing rate limiting

## License

This project is open source and available under the MIT License.
