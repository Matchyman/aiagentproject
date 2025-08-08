import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    working_direct_abs_path = os.path.abspath(working_directory)
    filepath = os.path.join(working_direct_abs_path, file_path)
    file_path_abs = os.path.abspath(filepath)
    if not file_path_abs.startswith(working_direct_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(file_path_abs, "r") as file:
            content_string = file.read(MAX_CHARS)
    except Exception as e:
        return(f"Error: {e}")
    if len(content_string) == MAX_CHARS:
        content_string += f"[...File '{file_path}' truncated at '{MAX_CHARS}' characters]"
    return content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads files in the specified file constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that is to be read.",
            ),
        },
    ),
)