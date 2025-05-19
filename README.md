# Weather MCP Server

A Model Context Protocol (MCP) server that provides weather information for different regions around the world.

## Overview

This MCP server uses the [wttr.in](https://wttr.in/) API to fetch weather data and serves it through a standardized MCP interface. It allows AI models and other clients to request weather information for any region by name.

## Features

- Fetch weather information for any city or region worldwide
- Uses the free wttr.in API (no API key required)
- Implemented as a FastMCP server for easy integration with AI models
- Docker support for easy deployment

## Requirements

- Python 3.10+
- Required packages (see requirements.txt):
  - requests
  - beautifulsoup4
  - fastapi
  - uvicorn
  - pydantic
  - fastmcp

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd weather_mcp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the server locally

```bash
python server.py
```

The MCP server will start on port 8000 by default (as specified in smithery.yaml).

### Using Docker

Build the Docker image:
```bash
docker build -t weather-mcp-server .
```

Run the container:
```bash
docker run -p 8000:8000 weather-mcp-server
```

## API Usage

The server exposes a single MCP handler:

### `get_weather`

Fetches weather information for the specified region.

**Parameters:**
- `region_name` (string, required): The name of the city or region to get weather for.

**Returns:**
- JSON object with weather information from wttr.in

**Example:**
```python
# Example client code
from mcp.client import MCPClient

async with MCPClient("http://localhost:8000") as client:
    weather_data = await client.get_weather(region_name="London")
    print(weather_data)
```

## Testing

You can test the weather functionality directly by running:

```bash
python weather_fetcher.py
```

This will fetch and display weather information for Suzhou (default city).

## License

See the [LICENSE](LICENSE) file for details.