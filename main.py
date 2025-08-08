import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

load_dotenv()
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def main(arg, verbose):
    print("Hello from aiagentproject!")

    messages = [
    types.Content(role="user", parts=[types.Part(text=arg)]),
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)  
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
    tools = [available_functions]
    )
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(response.text)
    if verbose:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    args = sys.argv
    verbose = False
    if len(args) > 1:
        arg = args[1]
        if len(args) > 2:
            verbose = "--verbose" in args[2]
    else:
        print("No prompt entered, please enter prompt into CLI when running programme")
        sys.exit(1)
    main(arg, verbose)
