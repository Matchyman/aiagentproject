import os
from google.genai import types
def write_file(working_directory, file_path, content):
    working_direct_abs_path = os.path.abspath(working_directory)
    filepath = os.path.join(working_direct_abs_path, file_path)
    file_path_abs = os.path.abspath(filepath)
    if not file_path_abs.startswith(working_direct_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        with open(file_path_abs, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file"
            )
        },
        required=["file_path", "content"]
    ),
)