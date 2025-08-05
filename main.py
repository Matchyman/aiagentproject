import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()


def main(arg):
    print("Hello from aiagentproject!")
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)  
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
    
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        arg = args[1]
    else:
        print("No prompt entered, please enter prompt into CLI when running programme")
        sys.exit(1)
    main(arg)
