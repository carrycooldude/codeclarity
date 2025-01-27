import ast
from vertexai_utils import generate_docstring

def extract_functions_classes(code):
    tree = ast.parse(code)
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return functions, classes

def generate_docs(code):
    functions, classes = extract_functions_classes(code)
    docs = {}
    for func in functions:
        func_code = ast.unparse(func)
        docs[func.name] = generate_docstring(func_code)
    for cls in classes:
        cls_code = ast.unparse(cls)
        docs[cls.name] = generate_docstring(cls_code)
    return docs