"""
C++ UML Class Diagram Generator
==============================

Description:
    Recursively analyzes all C++ source and header files in the specified folder, extracts class, inheritance, and member information, and generates a UML class diagram in PlantUML format.

Usage (as a script):
    python uml_generate.py <folder_path>
    - The UML diagram will be written to 'uml_output.puml' in the current directory.
    - Example:
        python uml_generate.py E:\Edge\src\components\sync\

Usage (as a module):
    from uml_generate import generate_cpp_uml_from_path
    uml_text = generate_cpp_uml_from_path('your_cpp_project_path')
    print(uml_text)

Dependencies:
    Python standard library: os, re
"""

import os
import re
from typing import List, Dict, Any

def find_cpp_files(path: str) -> List[str]:
    """Recursively find all C++ source and header files in the given path."""
    cpp_exts = ('.cpp', '.hpp', '.h', '.cc', '.cxx')
    files = []
    for root, _, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith(cpp_exts):
                files.append(os.path.join(root, fname))
    return files

def parse_cpp_classes(file_content: str) -> List[Dict[str, Any]]:
    """Extract class/struct definitions, inheritance, and members from C++ code."""
    class_pattern = re.compile(r'(class|struct)\s+(\w+)(\s*:\s*([^{]+))?\s*{', re.MULTILINE)
    member_pattern = re.compile(r'(public|private|protected):|([\w:<>,~]+\s+[\w:]+\s*(\([^)]*\))?;)', re.MULTILINE)
    classes = []
    for class_match in class_pattern.finditer(file_content):
        kind = class_match.group(1)
        name = class_match.group(2)
        inherit = class_match.group(4)
        start = class_match.end()
        end = file_content.find('};', start)
        body = file_content[start:end] if end != -1 else ''
        members = []
        access = 'private' if kind == 'class' else 'public'
        for m in member_pattern.finditer(body):
            if m.group(1):
                access = m.group(1)
            elif m.group(2):
                members.append((access, m.group(2).strip()))
        classes.append({
            'kind': kind,
            'name': name,
            'inherit': inherit,
            'members': members
        })
    return classes

def strip_template(name: str) -> str:
    """Remove generic type parameters, e.g. Foo<Bar> -> Foo."""
    return re.sub(r'<.*?>', '', name)

def is_valid_identifier(name: str) -> bool:
    """Check if a string is a valid C++ identifier for PlantUML."""
    if not name:
        return False
    if any(c in name for c in '()[]*&=,'): 
        return False
    if name.startswith('std::') and '<' in name:
        return False
    if re.search(r'[^\w:]', name):
        return False
    return True

def is_valid_member(member: str) -> bool:
    """Check if a member string is a valid PlantUML field/method declaration."""
    if not member:
        return False
    if any(c in member for c in '()[]*&=,'): 
        return False
    if '<' in member or '>' in member:
        return False
    if re.search(r'[^\w:; ]', member):
        return False
    return True

def generate_plantuml(classes: List[Dict[str, Any]]) -> str:
    """Generate PlantUML class diagram from parsed class info."""
    lines = ['@startuml']
    for cls in classes:
        class_name = strip_template(cls["name"])
        if not is_valid_identifier(class_name):
            continue
        kind = 'class' if cls['kind'] == 'class' else 'class'
        inherit = cls['inherit']
        lines.append(f'{kind} {class_name} {{')
        for access, member in cls['members']:
            if not is_valid_member(member):
                continue
            prefix = '+' if access == 'public' else '-' if access == 'private' else '#'
            lines.append(f'    {prefix} {member}')
        lines.append('}')
        if inherit:
            for base in re.split(r',', inherit):
                base = base.strip().split(' ')[-1]
                base = strip_template(base)
                if is_valid_identifier(base):
                    lines.append(f'{base} <|-- {class_name}')
    lines.append('@enduml')
    return '\n'.join(lines)

def generate_cpp_uml_from_path(path: str) -> str:
    """Main entry: generate PlantUML diagram from all C++ files in a folder."""
    cpp_files = find_cpp_files(path)
    all_classes = []
    for f in cpp_files:
        try:
            with open(f, encoding='utf-8', errors='ignore') as file:
                content = file.read()
            classes = parse_cpp_classes(content)
            all_classes.extend(classes)
        except Exception as e:
            print(f'Error reading {f}: {e}')
    return generate_plantuml(all_classes)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python uml_generate.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    uml_text = generate_cpp_uml_from_path(folder_path)
    output_file = "uml_output.puml"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(uml_text)
    print(f"UML diagram written to {output_file}")
