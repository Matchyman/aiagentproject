import os
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