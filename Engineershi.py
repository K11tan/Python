import os
import openai

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

def convert_to_instructions(text):
    """
    Converts the given text to simple, easily understandable instructions using OpenAI's GPT model.
    """
    response = openai.Completion.create(
        engine="gpt-4-turbo-2024-04-09",
        prompt=f"Convert the following text to simple, easily understandable instructions: {text}",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    converted_text = response.choices[0].text.strip()
    return converted_text

# Example usage
input_text = "Write a Python script that sends a GET request to a web server and prints the response content."
instructions = convert_to_instructions(input_text)
print(instructions)