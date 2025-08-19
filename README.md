# C++ UML Class Diagram Generator

This tool recursively analyzes all C++ source and header files in a specified folder, extracts class, inheritance, and member information, and generates a UML class diagram in PlantUML format.

## Features
- Supports .cpp, .hpp, .h, .cc, .cxx files
- Extracts class/struct definitions, inheritance, and members
- Outputs PlantUML-compatible `.puml` file
- Filters out invalid syntax for PlantUML rendering

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

### As a module
```python
from uml_generate import generate_cpp_uml_from_path
uml_text = generate_cpp_uml_from_path('your_cpp_project_path')
print(uml_text)
```

## Requirements
- Python 3.x
- Standard library only (os, re)

## Output
- The generated `uml_output.puml` can be rendered using PlantUML (VS Code extension or online)

---