import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def main(arg, verbose):
    print("Hello from aiagentproject!")
    messages = [
    types.Content(role="user", parts=[types.Part(text=arg)]),
]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)  
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
    )
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
