from mcp.server.fastmcp import FastMCP
from uml_generate import generate_cpp_uml_from_path, generate_cpp_uml_from_content
from typing import Dict

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
    try:
        result = generate_cpp_uml_from_path(path)
        # 如果结果为空，返回带有诊断信息的 UML
        if result.strip() == "@startuml\n@enduml":
            return f"@startuml\nnote top : No C++ classes found in {path}\n@enduml"
        return result
    except Exception as e:
        return f"@startuml\nnote top : Error: {str(e)}\n@enduml"

@mcp.tool("generate_cpp_uml_from_content")
async def generate_cpp_uml_from_file_contents(file_contents: Dict[str, str]):
    """
    MCP handler to generate UML diagrams from C++ source file contents

    Args:
        file_contents (Dict[str, str]): Dictionary where keys are file names and values are file contents

    Returns:
        str: PlantUML diagram as a string
    """
    try:
        result = generate_cpp_uml_from_content(file_contents)
        # 如果结果为空，返回带有诊断信息的 UML
        if result.strip() == "@startuml\n@enduml":
            return f"@startuml\nnote top : No C++ classes found in provided file contents\n@enduml"
        return result
    except Exception as e:
        return f"@startuml\nnote top : Error: {str(e)}\n@enduml"

if __name__ == "__main__":
    mcp.run()
