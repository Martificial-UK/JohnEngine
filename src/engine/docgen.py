import inspect
import os

def generate_docs(module, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) or inspect.isclass(obj):
                f.write(f"{name}: {inspect.getdoc(obj)}\n\n")
