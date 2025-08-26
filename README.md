# Instant Mock API

Instant Mock API: This initial prototype provides a lightweight, config-driven server powered by FastAPI, designed to accelerate development and testing.

## Getting Started

### 1. Clone the repository
```
git clone <your-repo-url>
cd instant-mock-api
```

### 2. Create a virtual environment (Windows)
```
python -m venv mock
```

### 3. Activate the virtual environment
```
mock\Scripts\activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```


### 5. Run the server
You can run the server using the CLI with options:

```
python main.py <config_file> [--host <host>] [--port <port>]
```

#### Example
```
python main.py api.yaml --host 0.0.0.0 --port 8080
```

#### Show help
```
python main.py --help
```

#### Options
- `<config_file>`: Path to your API configuration file (e.g., api.yaml)
- `--host`, `-h`: Host address to run the server (default: 127.0.0.1)
- `--port`, `-p`: Port to run the server (default: 8000)

## Project Structure
- `main.py`: Entry point for the FastAPI server
- `api.yaml`: API specification
- `requirements.txt`: Python dependencies
- `mock_server/`: Core server logic
