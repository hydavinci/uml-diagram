from mcp.server.fastmcp import FastMCP
from uml_generate import generate_cpp_uml_from_path

mcp = FastMCP("UML Generator")

@mcp.tool("generate_cpp_uml")
async def generate_cpp_uml(path: str):
    """
    MCP handler to generate UML diagrams from C++ source files

    Args:
        path (str): Path to the directory containing C++ source files

    Returns:
        str: PlantUML diagram as a string
    """
    return generate_cpp_uml_from_path(path)

if __name__ == "__main__":
    mcp.run()
