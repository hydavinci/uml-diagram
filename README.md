# C++ UML Class Diagram Generator

This tool recursively analyzes all C++ source and header files in a specified folder, extracts class, inheritance, and member information, and generates a UML class diagram in PlantUML format.

## Features
- Supports .cpp, .hpp, .h, .cc, .cxx files
- Extracts class/struct definitions, inheritance, and members
- Outputs PlantUML-compatible `.puml` file
- Filters out invalid syntax for PlantUML rendering
- **NEW**: Generate UML from file contents directly (not just directories)

## Usage

### As a script
```sh
python uml_generate.py <folder_path>
# The UML diagram will be written to 'uml_output.puml' in the current directory.
```
Example:
```sh
python uml_generate.py E:\Edge\src\components\sync\
```

### As a module (Directory-based)
```python
from uml_generate import generate_cpp_uml_from_path
uml_text = generate_cpp_uml_from_path('your_cpp_project_path')
print(uml_text)
```

### As a module (Content-based) - NEW
```python
from uml_generate import generate_cpp_uml_from_content

# Dictionary where keys are file names and values are file contents
file_contents = {
    "animal.h": """
    class Animal {
    public:
        virtual void makeSound() = 0;
    private:
        std::string name_;
    };
    """,
    "dog.h": """
    class Dog : public Animal {
    public:
        void makeSound() override;
    private:
        std::string breed_;
    };
    """
}

uml_text = generate_cpp_uml_from_content(file_contents)
print(uml_text)
```

### As an MCP Server
This tool can also be used as a Model Context Protocol (MCP) server:

1. **Directory-based generation**:
   - Tool: `generate_cpp_uml`
   - Parameter: `path` (string) - Path to directory containing C++ files

2. **Content-based generation** - NEW:
   - Tool: `generate_cpp_uml_from_content`
   - Parameter: `file_contents` (Dict[str, str]) - Dictionary mapping file names to their contents

Start the MCP server:
```sh
python server.py
```

## Requirements
- Python 3.x
- Standard library only (os, re, typing)
- For MCP server: `mcp` and `fastmcp` libraries

## Output
- The generated `uml_output.puml` can be rendered using PlantUML (VS Code extension or online)

---