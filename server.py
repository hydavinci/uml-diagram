from mcp.server.fastmcp import FastMCP
from weather_fetcher import get_weather_internal

mcp = FastMCP("Region Weather")

@mcp.tool("get_weather")
async def get_weather(region_name: str):
    """
    MCP handler to get weather information for a specified region
    
    Args:
        region_name (str): Name of the region to get weather for
        
    Returns:
        dict: Weather information for the specified region
    """
    return get_weather_internal(region_name)

if __name__ == "__main__":
    mcp.run()
